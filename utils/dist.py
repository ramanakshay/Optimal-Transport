import numpy as np 

# Distances

# -----------------------------------------------------------------------------

def ln_metric(x,y,n):
  return pow(np.sum(pow(abs(x-y),n),axis = len(x.shape)-1),1/n)

def euclidean(x,y):
  return pow(np.sum(pow(abs(x-y),2),axis = len(x.shape)-1),1/2)

def euclidean_sq(x,y):
  return np.sum(pow(abs(x-y),2),axis = len(x.shape)-1)

def coulomb(x,y,shift = 1e-5):
  x = x.astype(float)
  y = y.astype(float)
  return pow(shift + euclidean(x,y),-2)

# -----------------------------------------------------------------------------

metrics = { 'euclidean':euclidean,\
            'euclidean_sq':euclidean_sq,\
            'ln_metric':ln_metric,\
            'coulomb': coulomb }

def calculate_distance(x,y,dist):
  return eval(dist[0]+'(x,y,'+str(dist[1:])[1:],metrics,{'x':x,'y':y})

# Cost Matrix

def find_cost_matrix_old(xa,xb,p,dist = ("euclidean",)):
  if isinstance(dist,str):
    dist = (dist,)
  d = xa.shape[1]
  C = []
  for pa in xa:
    row = []
    for pb in xb:
      row.append(pow(calculate_distance(pa,pb,dist),p))
    C.append(row)
  C = np.array(C)
  return C

def find_cost_matrix(xa,xb,p,dist = ("euclidean",)):
  if isinstance(dist,str):
    dist = (dist,)
  xa_ = np.tile(xa, (1,xa.shape[0])).reshape(xa.shape[0],xb.shape[0],xa.shape[1])
  xb_ = np.tile(xb, (xb.shape[0],1)).reshape(xa.shape[0],xb.shape[0],xb.shape[1])
  return pow(calculate_distance(xa_,xb_,dist),p)