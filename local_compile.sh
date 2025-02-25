# /bin/bash

pkg_name=gkls
ext_suffix=$(python -c "from importlib.machinery import EXTENSION_SUFFIXES; print(EXTENSION_SUFFIXES[0])")

lib_name=${pkg_name}${ext_suffix}

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  shared_library_ext=.so
  shared_library_header=lib
elif [[ "$OSTYPE" == "darwin"* ]]; then
  shared_library_ext=.dylib
  shared_library_header=lib
else
  shared_library_ext=.lib
  shared_library_header=
fi

build() {
  if [[ "$OSTYPE" == "linux-gnu"* ]] || [[ "$OSTYPE" == "darwin"* ]]; then
    make -j
  else
    cmake --build . --config Release
  fi
}

cython --cplus -3 $pkg_name.pyx -o $pkg_name.cc

mkdir -p build
cd build
cmake -DEXT_NAME=$lib_name -DCYTHON_CPP_FILE=$pkg_name.cc ..
build
mv $shared_library_header$lib_name$shared_library_ext ../$lib_name