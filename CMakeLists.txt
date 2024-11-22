cmake_minimum_required(VERSION 3.30)
project(gkls)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "-fPIC -O3")

if($ENV{CIBUILDWHEEL})
  message(STATUS "Building wheel")
  find_package(Python COMPONENTS Development.Module REQUIRED)
  set(Python_LIBRARIES ${PYTHON_LIB_PATH})
else()
  find_package(Python COMPONENTS REQUIRED Development)
endif()

file(GLOB_RECURSE SRC_FILES src/*.cc)

include_directories(include ${Python_INCLUDE_DIRS})

message(STATUS "Python_INCLUDE_DIRS: ${Python_INCLUDE_DIRS}")
message(STATUS "Python_LIBRARIES: ${Python_LIBRARIES}")

add_library(${EXT_NAME} SHARED ${SRC_FILES} ${CYTHON_CPP_FILE})

# link_libraries(${EXT_NAME} ${Python_LIBRARIES})

# add_executable(example src/example.cc)