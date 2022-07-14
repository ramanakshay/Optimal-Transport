import numpy as np 
import matplotlib.pyplot as plt # plotting


#Plot any matrix
def plot_matrix(M,rlabel = [],clabel = [],cmap = 'viridis',textcolor = 'white',title = "",size = (1.5,1.5)):

  fig = plt.figure()
  ax = fig.add_axes([0.1,0.1,]+list(size)) # main axes

  r,c = M.shape

  if (r <= 10 or c <= 10):
    for i in range(r):
      for j in range(c):
          m = round(M[i][j],3)
          ax.text(i, j, str(m), va='center', ha='center', color = textcolor,fontsize = 66*size[0]/r)


    rlabel = np.round_(rlabel,2)
    clabel = np.round_(clabel,2)

    if (len(rlabel) > 0 and len(clabel) > 0):
      ax.set_xticks(np.arange(0,len(clabel),1))
      ax.set_xticklabels(list(map(str,clabel)))

      ax.set_yticks(np.arange(0,len(rlabel),1))
      ax.set_yticklabels(list(map(str,rlabel)))
     

  ax.xaxis.tick_top()
  ax.xaxis.set_tick_params(labeltop=True)
  ax.xaxis.set_tick_params(labelbottom=False)
  
  ax.set_xlabel(title,fontsize='xx-large')
  M = M.T # MATLAB reads column-wise 
  plt.imshow(M,cmap)
  plt.show()

# 2D Discrete Point Clouds
def plot_2d_map(xa,xb,P,limit = 0,title =""):
  for i in range(len(xa)):
    for j in range(len(xb)):
      if P[i][j] > limit:
        if (tuple(xa[i]) != tuple(xb[j])):
          plt.arrow(xa[i][0],xa[i][1],xb[j][0]-xa[i][0],xb[j][1]-xa[i][1],width = 0.0001,color = "black", alpha = 0.5*P[i][j]/P.max())
  plt.plot(xa[:, 0], xa[:, 1], '+b', label='Source samples')
  plt.plot(xb[:, 0], xb[:, 1], 'xr', label='Target samples')
  plt.legend(loc=0)

# For 2D Grids
def plot_grid(grid,n,title = ""):
  plt.imshow(abs(1-grid),cmap=plt.cm.gray)

  ax = plt.gca()
  ax.set_xticks(np.arange(-0.5, n, 1))
  ax.set_yticks(np.arange(-0.5, n, 1))
  ax.grid(which = 'major',color='grey')

  plt.tick_params(
      axis='x',        
      which='both',    
      bottom=False,  
      top=False,
      labelbottom=False)

  plt.tick_params(
      axis='y',         
      which='both',    
      left=False,     
      right=False,       
      labelleft=False) 

  plt.title(title)