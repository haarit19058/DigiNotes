
# CMakeLists.txt
cmake_minimum required(VERSION 3.16) - sets the minimum required version for cmake

project(KIO VERSION $(KF_VERSION)) - declares the project name and version

set(KF_VERSION "6.17.0") - sets the variable KF_VERSION
set(KF_DEP_VERSION)


find_package(ECM 6.16.0 NO_MODULE)
	ECM(Extra CMake Modules) is KDE's CMake helper module library. It provides custom macros, logging, build settings, etc.

set(CMAKE_MODULE_PATH  ${ECM_MODULE_PATH} ${CMAKE_CURRENT_SOURCE_DIR}/cmake)



