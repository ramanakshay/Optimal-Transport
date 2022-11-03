# Optimal-Transport

## About 

This repository contains the work done during my summer internship at uOttawa under the supervision of Prof. Augusto Gerolin. We have implemented various algorithms in Python to solve the optimal transport problem for the multi-marginal case. These algorithms are also used to study the dissociation of atoms which is of interest in Density Functional Theory.

## Visualising Optimal Transport using the POT Library

The emd.ipynb notebook demonstrates how to use functions from the Python Optimal Transport (POT) library to solve the primal problem. Different kinds of data tested include:
1. 1D Probability Distributions
2. 2D Probability Distributions
3. 2D Binary Grids
4. 2D Discrete Point Clouds

We also look at how wasserstien distance can be used as a valid distance measure to compare two distributions. Matplotlib is used to plot matrices and transport mappings.

## Entropic Regularisation of Optimal Transport: Sinkhorn Algorithm

Sinkhorn algorithm is used to find solutions of entropy-regularised optimal transport problems. The sinkhorn.ipynb notebook contains two versions of sinkhorn based on the stopping time - no. of iterations or marginal condition. The sinkhorn algorithm is tested on different kinds of data along with different values of epsilon and size of data. The performance of sinkhorn is compared with the emd function from the POT library and the results are tabulated.

## Multi-Marginal Optimal Transport

This notebook expands from the previous sinkhorn algorithm to work for the multi-marginal case. The SinkhornSolver class contains the previous implementations of sinkhorn and a new implementation which updates scaling vectors at random. Tensors are stored as numpy arrays and brodcasting is used to perform multiplication of scaling vectors and n-dimensional tensors. The running time vs. the number of marginals are tabulated. It shows that the running time increases exponentially as the number of marginals are increased.

## Dispersion Simulation

The multi-marginal sinkhorn algorithm is used to study qualitatively the dissasociation of two atoms. To model the dissociation of the electrons we choose the one-body density as a superpostion of two Gaussian with their center separated a distance R. The coulomb distance is chosen as the cost function since we are dealing with electron-electron repulsion. The scaling vectors which are the Kantorovich potentials are plotted using matplotlib. We also plot the total potential energy (wasserstien distance) as a function of R. Finally, other densities like Lorentzian, and Uniform density are also tested.


## Solving Optimal Transport Using Neural Networks (Gradient Descent)

The gradient_descent.ipynb notebook includes a preliminary implementation of solving optimal transport using neural networks. The neural network is trained and built using Tensorflow. The input of the neural network is the marginal vector and the output is the potential from which we can generate the coupling matrix. The projection of the coupling matrix (for the multi-marginal case) is plotted after every training iteration to visualise the evolution of the coupling matrix. 

## utils Package

The utils folder is a package within the repository to share various helper functions between notebooks. Functions in data.py can be used to get different types of densities/marginals. The dist.py includes functions to get cost matrices and tensors for various distance measures like euclidean, euclidean-squared, coulomb, ln-metric. The plot.py contains functions that use matplotlib to plot various matrices and mappings.
