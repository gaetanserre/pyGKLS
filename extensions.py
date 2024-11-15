import os
import platform
import shutil
from pathlib import Path
from subprocess import check_call

from setuptools import Extension
from setuptools.command.build_ext import build_ext


def create_directory(path: Path):
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(exist_ok=True, parents=True)
    return path


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

    def build_extension(self, ext: Extension):
        ext_dir = Path(self.get_ext_fullpath(ext.name)).parent.absolute()
        create_directory(ext_dir)

        pkg_name = "gkls"
        ext_suffix = os.popen("python3-config --extension-suffix").read().strip()
        lib_name = pkg_name + ext_suffix
        ext_name = ".".join((lib_name).split(".")[:-1])
        lib_ext_dir = Path(f"{ext_dir}/{lib_name}")

        # Compile the Cython file
        os.system(f"cython --cplus -3 {pkg_name}.pyx -o {pkg_name}.cc")

        # Compile the C++ files
        os.system(
            "cd build "
            f"&& cmake -DEXT_NAME={ext_name} -DCYTHON_CPP_FILE={pkg_name}.cc .. "
            "&& make -j "
            f"&& mv lib{lib_name} {lib_ext_dir} "
        )
