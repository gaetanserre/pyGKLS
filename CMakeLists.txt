cmake_minimum_required(VERSION 3.30)
project(gkls)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "-fPIC -O3")

if(UNIX AND NOT APPLE)
  set(LINUX TRUE)
elseif(UNIX)
  set(DARWIN TRUE)
else()
  set(WINDOWS TRUE)
endif()

if(APPLE)
  find_package(Python COMPONENTS Development REQUIRED)
  link_libraries(${Python_LIBRARIES})
else()
  find_package(Python COMPONENTS Development.Module REQUIRED)
endif()

file(GLOB_RECURSE SRC_FILES src/*.cc)

include_directories(include ${Python_INCLUDE_DIRS})

add_library(${EXT_NAME} SHARED ${SRC_FILES} ${CYTHON_CPP_FILE})

# link_libraries(${EXT_NAME} ${Python_LIBRARIES})

# add_executable(example src/example.cc)