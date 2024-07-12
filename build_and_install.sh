#!/usr/bin/env bash

Purple="\033[0;35m"
Red="\033[0;31m"
Green="\033[0;92m"
NC="\033[0m"

platform=$(python -c "import platform; print(platform.processor())")
echo -e "${Purple}Running on ${platform} platform${NC}"

unameOut="$(uname -s)"
case "${unameOut}" in
    Linux*)     lib_ext=so; lib_path=LD_LIBRARY_PATH;;
    Darwin*)    lib_ext=dylib; lib_path=DYLD_LIBRARY_PATH;;
    *)          echo -e "${Red}Unsupported OS!${NC}"; exit 1;;
esac

# Install dependencies
echo -e "${Purple}Installing dependencies...${NC}"
pip install -r requirements.txt

# Build pyGKLS
echo -e "${Purple}Building pyGKLS...${NC}"
cd pygkls && invoke build-pygkls

pkg_path=$(python -c "import os; import invoke; \
print('/'.join(os.path.dirname(invoke.__file__).split('/')[:-1]))")

# Copy shared libraries to package path
echo -e "${Purple}Copying shared libraries to package path...${NC}"
cp pygkls*.so $pkg_path
mkdir -p $HOME/.local/lib
cp libpygkls.${lib_ext} $HOME/.local/lib

# Test pyGKLS
echo -e "${Purple}Testing pyGKLS...${NC}"
cd
if python -c "import pygkls; pygkls.init()"; then
    echo -e "${Green}pyGKLS is working correctly!${NC}"
else
    echo -e "${Red}pyGKLS is not working correctly!${NC}"
    echo -e "${Red}Please make sure that $HOME/.local/lib is in ${lib_path}!${NC}"
    exit 1
fi
