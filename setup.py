# Create a setup.py file to install the optimizers module using invoke.

import sys
from setuptools import setup, Extension
from toml import load
import os
import platform
import shutil
from pathlib import Path
from subprocess import check_call
from setuptools.command.build_ext import build_ext
from importlib.machinery import EXTENSION_SUFFIXES


def create_directory(path: Path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(exist_ok=True, parents=True)
    return path


def get_shared_lib_ext():
    if sys.platform.startswith("linux"):
        return ".so"
    elif sys.platform.startswith("darwin"):
        return ".dylib"
    else:
        return ".dll"


class GKLSBuildExtension(Extension):
    def __init__(self, name: str, version: str):
        super().__init__(name, sources=[])
        # Source dir should be at the root directory
        self.source_dir = Path(__file__).parent.absolute()
        self.version = version


class GKLSBuild(build_ext):
    def run(self):
        try:
            check_call(["cmake", "--version"])
        except OSError:
            raise RuntimeError("CMake must be installed")

        if platform.system() not in ("Windows", "Linux", "Darwin"):
            raise RuntimeError(f"Unsupported os: {platform.system()}")

        for ext in self.extensions:
            if isinstance(ext, GKLSBuildExtension):
                self.build_extension(ext)

    @property
    def config(self):
        return "Debug" if self.debug else "Release"

    def cmake_command(self, python_path, lib_name, pkg_name):
        if platform.system() == "Windows":
            return f'cmake -G "Visual Studio 17 2022" -A x64 -DPython_EXECUTABLE={python_path} -DEXT_NAME={lib_name} -DCYTHON_CPP_FILE={pkg_name}.cc ..'
        else:
            return f"cmake -DPython_EXECUTABLE={python_path} -DEXT_NAME={lib_name} -DCYTHON_CPP_FILE={pkg_name}.cc .."

    def build_command(self):
        if platform.system() == "Windows":
            return "cmake --build . --config Release"
        else:
            return "make -j"

    def shared_lib_path(self, lib_name):
        if platform.system() == "Windows":
            return f"Release/{lib_name}{get_shared_lib_ext()}"
        else:
            return f"lib{lib_name}{get_shared_lib_ext()}"

    def build_extension(self, ext: Extension):
        python_path = Path(sys.executable).absolute()

        ext_dir = Path(self.get_ext_fullpath(ext.name)).parent.absolute()
        create_directory(ext_dir)

        pkg_name = "gkls"
        ext_suffix = EXTENSION_SUFFIXES[0]
        lib_name = ".".join((pkg_name + ext_suffix).split(".")[:-1])
        pkg_ext = ".pyd" if platform.system() == "Windows" else ".so"

        # Compile the Cython file
        os.system(f"cython --cplus -3 {pkg_name}.pyx -o {pkg_name}.cc")

        # Compile the C++ files
        os.system(
            "cd build "
            f"&& {self.cmake_command(python_path, lib_name, pkg_name)} "
            f"&& {self.build_command()} "
            f"&& mv {self.shared_lib_path(lib_name)} {ext_dir / (lib_name + pkg_ext)} "
        )


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

name = load("pyproject.toml")["project"]["name"]
version = load("pyproject.toml")["project"]["version"]

setup(
    name=name,
    version=version,
    ext_modules=[GKLSBuildExtension("gkls", "0.1.0")],
    cmdclass={"build_ext": GKLSBuild},
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown",
)
