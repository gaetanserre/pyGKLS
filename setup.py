# Create a setup.py file to install the optimizers module using invoke.

from setuptools import setup, Extension
from extensions import *

# Get version from toml file
from toml import load

version = load("pyproject.toml")["project"]["version"]

setup(
    version=version,
    ext_modules=[GKLSBuildExtension("gkls", "0.1.0")],
    cmdclass={"build_ext": GKLSBuild},
    zip_safe=False,
)
