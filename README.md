#  PyMFEM (MFEM Python wrapper)

This package (PyMFEM) is Python wrapper for MFEM, which is a high performance finite
element metod library.(http://mfem.org/).

Installer downloads a couple of external libraries and build them.
By default, "pip install mfem" downloads and builds the serial version of MFEM and PyMFEM.
See more detail below for other configurations

## Install
```
pip install mfem --no-binary mfem   # install serial MFEM + wrapper
```
For other configuration such as parallel version, one has to donwload
the package and run setup script. For example, this below download
MFEM, Metis and Hypre and install under <prefix>/mfem
```
$ pip3 download mfem
(expand tar.gz file and move to the downloaded directory)
$ python setup.py install --with-parallel # build metis/hypre/mfem and PyMFEM in parallel
```
For other configurations, see docs/install.txt or help
```
$ python setup.py install --help
```

## Usage
Here is an example to solve div(grad(f)) = 1 in squre and to plot the result
with matplotlib
```
import mfem.ser as mfem

# create sample mesh for squre shape
mesh = mfem.Mesh(10, 10, "TRIANGLE")

# create finite element function space
fec = mfem.H1_FECollection(1, mesh.Dimension())   # H1 order=1
fespace = mfem.FiniteElementSpace(mesh, fec)      

# 
ess_tdof_list = mfem.intArray()
ess_bdr = mfem.intArray([1]*mesh.bdr_attributes.Size())
fespace.GetEssentialTrueDofs(ess_bdr, ess_tdof_list)

# constant coefficient 
one = mfem.ConstantCoefficient(1.0)

# define Bilinear and Linear operator
a = mfem.BilinearForm(fespace)
a.AddDomainIntegrator(mfem.DiffusionIntegrator(one))
a.Assemble()
b = mfem.LinearForm(fespace)
b.AddDomainIntegrator(mfem.DomainLFIntegrator(one))
b.Assemble()

# create gridfuction, which is where the solution vector is stored
x = mfem.GridFunction(fespace);
x.Assign(0.0)

# form linear equation (AX=B)
A = mfem.OperatorPtr()
B = mfem.Vector()
X = mfem.Vector()
a.FormLinearSystem(ess_tdof_list, x, b, A, X, B);
print("Size of linear system: " + str(A.Height()))

# solve it using PCG solver and store the solution to x
AA = mfem.OperatorHandle2SparseMatrix(A)
M = mfem.GSSmoother(AA)
mfem.PCG(AA, M, B, X, 1, 200, 1e-12, 0.0)
a.RecoverFEMSolution(X, b, x)

# extract vertices and solution as numpy array
verts = mesh.GetVertexArray()
sol = x.GetDataArray()

# plot solution using Matplotlib

import matplotlib.pyplot as plt
import matplotlib.tri as tri

triang = tri.Triangulation(verts[:,0], verts[:,1])

fig1, ax1 = plt.subplots()
ax1.set_aspect('equal')
tpc = ax1.tripcolor(triang, sol, shading='gouraud')
fig1.colorbar(tpc)
plt.show()
```
![](docs/example_image.png)


## License
PyMFEM is licesed under BSD-3.
Please referre the developers web sites for the external libraries
MFEM: https://mfem.org/
Hypre: https://computing.llnl.gov/projects/hypre-scalable-linear-solvers-multigrid-methods
METIS: http://glaros.dtc.umn.edu/gkhome/metis/metis/overview