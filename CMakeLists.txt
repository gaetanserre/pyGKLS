cmake_minimum_required(VERSION 3.28)
project(gkls)

set(Python_EXECUTABLE "python" CACHE STRING "Path to the Python executable")

execute_process(
  COMMAND
  ${Python_EXECUTABLE} -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())"
  OUTPUT_VARIABLE
  Python_INCLUDE_DIRS
  OUTPUT_STRIP_TRAILING_WHITESPACE
)

set(Python_INCLUDE_DIRS ${Python_INCLUDE_DIRS} CACHE STRING "" FORCE)
message(STATUS "Python_EXECUTABLE: ${Python_EXECUTABLE}")

# Detect platform
if(UNIX AND NOT APPLE)
  set(LINUX TRUE)
elseif(UNIX)
  set(DARWIN TRUE)
else()
  set(WINDOWS TRUE)
endif()

# Find Python
message(STATUS "Python_INCLUDE_DIRS: ${Python_INCLUDE_DIRS}")

# Source files
file(GLOB_RECURSE SRC_FILES src/*.cc)

# Include directories
include_directories(include ${Python_INCLUDE_DIRS})

# Add the shared library
if(WINDOWS)
  set(CMAKE_CXX_STANDARD 17)
  set(CMAKE_CXX_FLAGS_RELEASE "/O2")

  # Find Python library
  find_package(Python COMPONENTS Development.Module REQUIRED)
  message(STATUS "Python_LIBRARIES: ${Python_LIBRARIES}")
  add_library(${EXT_NAME} SHARED ${SRC_FILES} ${CYTHON_CPP_FILE})
  target_link_libraries(${EXT_NAME} ${Python_LIBRARIES})
else()
  set(CMAKE_CXX_STANDARD 23)
  set(CMAKE_CXX_FLAGS "-fPIC -O3")
  add_library(${EXT_NAME} SHARED ${SRC_FILES} ${CYTHON_CPP_FILE})
endif()

# Set macOS-specific linker flags
if(APPLE)
  set_target_properties(
    ${EXT_NAME}
    PROPERTIES
    LINK_FLAGS "-undefined dynamic_lookup"
  )
endif()
