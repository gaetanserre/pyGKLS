# Create a setup.py file to install the optimizers module using invoke.

from setuptools import setup, Extension
from extensions import *

setup(
    version="0.1.0",
    ext_modules=[GKLSBuildExtension("gkls", "0.1.0")],
    cmdclass={"build_ext": GKLSBuild},
    zip_safe=False,
)
