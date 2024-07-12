import invoke
import os

# Get the include path for the python3 interpreter
python_include = os.popen("python -m pybind11 --includes").read().strip()

# check if macos
lib_name = "libpygkls.so"
linker_flag = os.popen("python3-config --ldflags").read().strip()
if os.uname().sysname == "Darwin":
    lib_name = "libpygkls.dylib"
    python_version  = ".".join(
        os.popen("python --version").read().strip().split(" ")[-1].split(".")[:-1]
    )
    linker_flag += f" -shared -lpython{python_version}"

def print_banner(msg):
    print("==================================================")
    print("= {} ".format(msg))


@invoke.task()
def build_pygkls_lib(c):
    print_banner("Building C++ Library")
    os.system(f"mkdir -p build && cd build && cmake .. && make -j && cp {lib_name} ..")
    print("* Complete")


def compile_python_module(cpp_name, extension_name):
    invoke.run(
        "g++ -O3 -Wall -Werror -shared -std=c++20 -fPIC "
        f"{python_include} "
        f"{cpp_name} "
        f"-o {extension_name}`python3-config --extension-suffix` "
        f"{linker_flag} "
        "-L. -lpygkls -Wl,-rpath,."
    )


@invoke.task(build_pygkls_lib)
def build_pygkls(c):
    print_banner("Building pyGKLS Module")
    invoke.run("cython --cplus -3 pygkls.pyx -o pygkls.cc")
    compile_python_module("pygkls.cc", "pygkls")
    print("* Complete")


@invoke.task(build_pygkls)
def test_pygkls(c):
    print_banner("Testing pyGKLS Module")
    invoke.run("python tests.py", pty=True)
