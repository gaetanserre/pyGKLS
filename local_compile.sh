# /bin/bash

pkg_name=gkls
ext_suffix=$(python -c "from importlib.machinery import EXTENSION_SUFFIXES; print(EXTENSION_SUFFIXES[0])")

lib_name=${pkg_name}${ext_suffix}
shared_library_header=lib

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  shared_library_ext=.so
elif [[ "$OSTYPE" == "darwin"* ]]; then
  shared_library_ext=.dylib
else
  shared_library_ext=.dll
  shared_library_header=Release/
fi

build() {
  if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    cmake -DEXT_NAME=$lib_name -DCYTHON_CPP_FILE=$pkg_name.cc ..
    make -j
  else
    cmake -DEXT_NAME=$lib_name -DCYTHON_CPP_FILE=$pkg_name.cc -G "Visual Studio 17 2022" -A x64 ..
    cmake --build . --config Release
  fi
}

cython --cplus -3 $pkg_name.pyx -o $pkg_name.cc

mkdir -p build
cd build
build
mv $shared_library_header$lib_name$shared_library_ext ../$lib_name