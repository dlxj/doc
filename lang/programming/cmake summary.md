





```
cmake . -Bbuild && cmake --build build --
```

./zero-epwing  --pretty "/Users/vvw/Documents/dic/NHK"



## Debug  Flag



```cmake
set(CMAKE_BUILD_TYPE Debug)
```



## Verbose output



```cmake
set(CMAKE_VERBOSE_MAKEFILE ON)
```



GCC/Clang：使用-I开关指定附加包含路径即可，和cl相似，每个附加包含目录都要分开用-I指定。也可以设置环境变量C_INCLUDE_PATH（编译C时的默认包含路径）、CPLUS_INCLUDE_PATH（编译C++时的默认包含路径）或者CPATH（同时对C/C++起作用）



```
cmake_minimum_required(VERSION 3.5)
project(zero-epwing)

set(CMAKE_BUILD_TYPE Debug)

include(ExternalProject)
ExternalProject_Add(
	eb
	SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR}/eb
	CONFIGURE_COMMAND ${CMAKE_CURRENT_SOURCE_DIR}/eb/configure --disable-shared --disable-ebnet --disable-nls
	PREFIX ${CMAKE_CURRENT_SOURCE_DIR}/eb
	BUILD_COMMAND make
	BUILD_IN_SOURCE 1
	INSTALL_COMMAND ""
	)
include_directories(eb ${CMAKE_BINARY_DIR})
option(JANSSON_EXAMPLES "" OFF)
option(JANSSON_BUILD_DOCS "" OFF)
option(JANSSON_WITHOUT_TESTS "" ON)
add_subdirectory(jansson)
link_directories(eb/eb/.libs ${CMAKE_BINARY_DIR}/jansson/lib)
add_executable(zero-epwing main.c book.c convert.c hooks.c)
add_dependencies(zero-epwing eb jansson)
target_link_libraries(zero-epwing libeb.a libz.a libjansson.a)
if (WIN32 OR APPLE)
    target_link_libraries(zero-epwing libiconv.a)
endif (WIN32 OR APPLE)
target_link_libraries(zero-epwing)

```





```

```





