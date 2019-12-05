
# xbsuite (Scott's XBeach Suite)

**xbsuite** is a set of Python tools (and bash scripts) related to XBeach simulations. They may be useful for certain stages of creating and analyzing the simulations.

This suite consists of Python code written by Scott Feister. Some of the code is translations of MATLAB tools written by other XBeach authors.

The primary use case has been personal, but I'm sharing these tools in case others find them useful.

## Setup

### Dependencies
This module requires **Python 3.6+**. Installation requires **git**.

**OS X users:** Prior to installing dependencies, ensure an adequate Python installation by following [this guide](https://matplotlib.org/faq/installing_faq.html#osx-notes). The Python that ships with OS X may not work well with some required dependencies.

* [`numpy`](http://www.numpy.org/)
* [`scipy`](https://www.scipy.org/)
* [`matplotlib`](https://matplotlib.org/)
* [`h5py`](https://www.h5py.org/)

The dependencies may be installed according to the directions on 
their webpages, or with any Python
package manager that supports them. For example, one could use `pip` to install
them as
 ```bash
pip install numpy scipy matplotlib h5py
```

**NOTE**: If you are on a cluster where you do not have write permissions to the python installation directory, you may need to add "--user" to your pip and setup calls here and below. E.g.
```bash
pip install --user numpy scipy matplotlib h5py
```

As an alternate to pip, one could also use [Anaconda Python](https://anaconda.org/anaconda/python) to
install the dependencies
```bash
conda install numpy scipy matplotlib h5py
```

### Installation
After installing the required packages, we may install **xbsuite**.

One way to install **xbsuite** is via
```bash
pip install git+https://github.com/phyzicist/xbsuite.git
```

To update **xbsuite** at a later date
```bash
pip install --upgrade git+https://github.com/phyzicist/xbsuite.git
```

An alternative way to install **xbsuite** is via
```bash
git clone https://github.com/phyzicist/xbsuite.git
cd xbsuite/
python setup.py install
```

If you installed with the "--user" flag and "\~/.local/bin" is not on your system path, add it to your path (e.g. by appending the line "PATH=$PATH:$HOME/.local/bin" to "\~/.bashrc"). This will allow you to use any command-line tools from this repository (if any exist yet!).

## Usage
You will need to read through the source code for descriptions of the functions of this package. There is unfortunately no formal documentation.

### General usage
```python
import xbsuite as xb
```

## Uninstalling

To uninstall **xbsuite**
```shell
pip uninstall xbsuite
```
