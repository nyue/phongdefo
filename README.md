# phongdefo

### 1. About

This is a C++ Houdini SOP implementing [phong deformation](https://graphics.pixar.com/library/PhongDefo/paper.pdf).

![screenshot](twist.png)

Under extreme deformation, the method gives noticeably smoother, more accurate results compared to standard linear deformation, and also houdini's builtin point deform node, which can require tweaking radius/samples to achieve smoothness while being prone to pushing geometry outside the deformed cage. Generally useful when using tetrahedral meshes to drive high detail embedded geometry. 

### 2. Installation

```bash 
git clone https://github.com/rituals/phongdefo.git
cd phongdefo/src
make install
```

[source the Houdini environment](https://www.sidefx.com/docs/hdk/_h_d_k__intro__compiling.html) in your shell beforehand. The SOP depends on two header-only libraries, [eigen](https://gitlab.com/libeigen/eigen) for linear algebra operations and [nanoflann](https://github.com/jlblancoc/nanoflann) for its kdtree implementation. This has only been tested on a 64-bit linux machine, running the free version of houdini v19.5. Tinkering is probably needed for compiling and installing on different systems.

