cmake_minimum_required(VERSION 3.28)
project(pygkls)
set(CMAKE_CXX_STANDARD 20)
set (CMAKE_CXX_FLAGS "-fPIC -O3")

file (GLOB_RECURSE SRC_FILES src/*.cc)

include_directories(include)

add_library(pygkls SHARED ${SRC_FILES})

link_libraries(pygkls)
add_executable(example src/example.cc)