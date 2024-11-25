cmake_minimum_required(VERSION 3.30)
project(gkls)
set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_FLAGS "-fPIC -O3")

# Detect platform
if(UNIX AND NOT APPLE)
  set(LINUX TRUE)
elseif(UNIX)
  set(DARWIN TRUE)
else()
  set(WINDOWS TRUE)
endif()

# Find Python
if(APPLE)
  find_package(Python COMPONENTS Development.Module REQUIRED)
else()
  find_package(Python COMPONENTS Development.Module REQUIRED)
endif()

message(STATUS "Python_INCLUDE_DIRS: ${Python_INCLUDE_DIRS}")

# Source files
file(GLOB_RECURSE SRC_FILES src/*.cc)

# Include directories
include_directories(include ${Python_INCLUDE_DIRS})

# Add the shared library
add_library(${EXT_NAME} SHARED ${SRC_FILES} ${CYTHON_CPP_FILE})

# Set macOS-specific linker flags
if(APPLE)
  set_target_properties(
    ${EXT_NAME}
    PROPERTIES
    LINK_FLAGS "-undefined dynamic_lookup"
  )
endif()
