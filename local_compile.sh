# /bin/bash

pkg_name=gkls
ext_suffix=$(python3-config --extension-suffix)

lib_name=${pkg_name}${ext_suffix}

cython --cplus -3 $pkg_name.pyx -o $pkg_name.cc

mkdir -p build
cd build
cmake -DEXT_NAME=$lib_name -DCYTHON_CPP_FILE=$pkg_name.cc ..
make -j
mv lib$lib_name.so ../$lib_name