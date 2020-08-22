
cmake_minimum_required(VERSION 3.5)

set(CMAKE_CXX_STANDARD 17)

if(APPLE)
    set(CMAKE_OSX_DEPLOYMENT_TARGET "10.13" CACHE STRING "macOS deployment target")
endif()

project(echodict VERSION 0.0.1)

include(GNUInstallDirs)

set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_BUILD_TYPE Debug)
set(CMAKE_VERBOSE_MAKEFILE ON)

find_package(Qt5 COMPONENTS LinguistTools Multimedia Network WebEngine WebEngineWidgets Widgets REQUIRED)


add_executable(qolibri MACOSX_BUNDLE WIN32
   src/main.cpp
)

