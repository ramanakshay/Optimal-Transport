import numpy as np

def gaussian_mix(size,mu,std,scale = None):
  assert len(mu) == len(std)
  if scale == None:
    scale = [1]*len(mu)
  x = np.arange(size, dtype = np.float64)
  h = 0
  for i in range(len(mu)):
    h += np.exp(-(x - mu[i]) ** 2 / (2 * std[i] ** 2))*scale[i]
  return h / h.sum()

def dispersion_density(size,R):
  assert R <= 10*size/16 and R >= 0
  return gaussian_mix(size,[size//2 + R/2,size//2 - R/2],[size/16,size/16],[1,1])

def uniform_density(size):
  return 1/size * np.ones((size,))

def lorentzian(size):
  x = np.arange(size, dtype = np.float64)
  h = 2/(np.pi*(1+pow((x-size/2)*0.05,2)))
  return h / h.sum()
  