# ImHex

## Main Cmake.txt

### Breakdown of Functions and Underlying Concepts in the CMake Configuration

#### 1. `cmake_minimum_required(VERSION 3.20)`
This function specifies the minimum version of CMake required to build the project. In this case, CMake version 3.20 or newer is required. This ensures compatibility between the project's configuration and the CMake version on the user’s system.

#### 2. `option(<option_variable> "Description of the option" <default_value>)`
The `option()` function defines a build-time configuration setting. The `<option_variable>` can be toggled by the user (ON/OFF), allowing them to customize various aspects of the build process. The description helps users understand the option, and the default value (ON or OFF) specifies the default behavior if the user doesn't override it.

### Detailed Explanation of the Options:

#### `IMHEX_PLUGINS_IN_SHARE`
- **Purpose:** Decides where plugins should be installed. If this option is ON, plugins will be placed in the `share/imhex/plugins` directory. Otherwise, they will be installed in the system's default `lib` directory (for Linux).
- **Use Case:** This option is helpful for Linux users who may want to isolate plugins from system libraries for easier management.

#### `IMHEX_STRIP_RELEASE`
- **Purpose:** Removes unneeded symbols from release builds, reducing binary size.
- **Use Case:** Stripping is often used in production environments to minimize the size of executable files, as debugging symbols and metadata are not necessary in most production scenarios.

#### `IMHEX_OFFLINE_BUILD`
- **Purpose:** When enabled, the project will not download dependencies or additional files from the internet.
- **Use Case:** This is useful for environments without internet access or if the user wants to ensure reproducible builds without external dependencies.

#### `IMHEX_IGNORE_BAD_CLONE`
- **Purpose:** Skips checks for corrupted or improperly cloned Git repositories.
- **Use Case:** Some projects enforce checks to prevent users from building incomplete or corrupted source trees. This option disables that check.

#### `IMHEX_PATTERNS_PULL_MASTER`
- **Purpose:** Automatically fetches the latest files from the master branch of the "ImHex-Patterns" repository.
- **Use Case:** This is useful for users who want the most up-to-date pattern files during the build process. It’s usually disabled in offline or reproducible builds.

#### `IMHEX_IGNORE_BAD_COMPILER`
- **Purpose:** Allows building with unsupported compilers.
- **Use Case:** The project might have restrictions on which compilers are allowed. This option lets users bypass those restrictions, which might result in non-optimal or unsupported builds.

#### `IMHEX_USE_GTK_FILE_PICKER`
- **Purpose:** On Linux systems, this enables using the GTK file picker rather than `xdg-desktop-portals`.
- **Use Case:** Some users may prefer the GTK file picker for better compatibility or functionality on their system.

#### `IMHEX_DISABLE_STACKTRACE`
- **Purpose:** Disables stack trace printing when errors occur in the program.
- **Use Case:** This is often disabled in production environments where security or performance considerations outweigh the usefulness of detailed error information.

#### `IMHEX_BUNDLE_DOTNET`
- **Purpose:** Bundles the .NET runtime with the application.
- **Use Case:** If your application relies on .NET and you want to ensure that it will run without needing users to install .NET separately, this option bundles the runtime.

#### `IMHEX_ENABLE_LTO`
- **Purpose:** Enables Link-Time Optimization (LTO), which optimizes the entire program during the final linking stage.
- **Use Case:** LTO can greatly reduce binary size and improve runtime performance by optimizing across object files. However, it increases build time, so it’s usually optional.

#### `IMHEX_USE_DEFAULT_BUILD_SETTINGS`
- **Purpose:** Uses default build settings instead of custom or user-specified ones.
- **Use Case:** This can enforce consistent behavior across all builds by overriding any user-specific configurations with the project's default settings.

#### `IMHEX_STRICT_WARNINGS`
- **Purpose:** Enables most available compiler warnings and treats warnings as errors, preventing the build from succeeding if there are any warnings.
- **Use Case:** This is commonly used to enforce code quality by ensuring that no code with potential issues (e.g., risky or non-portable code) is allowed in the project.

#### `IMHEX_STATIC_LINK_PLUGINS`
- **Purpose:** Statically links all plugins into the main executable rather than building them as separate dynamic libraries.
- **Use Case:** Static linking can make distribution easier since all necessary code is included in the executable, avoiding potential issues with missing libraries.

#### `IMHEX_GENERATE_PACKAGE`
- **Purpose:** Specifies whether a native package (e.g., installer or package file) should be built for Windows and MacOS.
- **Use Case:** If enabled, the build process will create an installation package, which is useful for distributing the software on these platforms.

#### `IMHEX_ENABLE_UNITY_BUILD`
- **Purpose:** Enables Unity builds, where multiple source files are compiled together to reduce build times.
- **Use Case:** Unity builds can greatly speed up large projects by reducing the overhead of multiple compilation units.

#### `IMHEX_GENERATE_PDBS`
- **Purpose:** Enables the generation of Program Database (PDB) files for debugging on non-debug builds, applicable only on Windows.
- **Use Case:** PDB files are useful for debugging Windows applications, even in release mode, as they contain debugging information.

#### `IMHEX_REPLACE_DWARF_WITH_PDB`
- **Purpose:** Removes DWARF debugging information and replaces it with PDB files when generating PDB files on Windows.
- **Use Case:** DWARF is a debugging standard typically used on Unix-like systems, but on Windows, PDB files are preferred.

#### `IMHEX_ENABLE_STD_ASSERTS`
- **Purpose:** Enables C++ standard library asserts, which can break the Application Binary Interface (ABI) for plugins.
- **Use Case:** Standard library asserts are useful for debugging but may cause incompatibilities with external plugins.

#### `IMHEX_ENABLE_UNIT_TESTS`
- **Purpose:** Enables building unit tests for the project.
- **Concept:** Unit tests are small, isolated tests that check the functionality of individual components or functions in the codebase. Enabling this option allows the project to include unit tests in the build, ensuring the code works as expected.
- **Use Case:** Useful in development environments to verify code correctness.

#### `IMHEX_ENABLE_PRECOMPILED_HEADERS`
- **Purpose:** Enables precompiled headers to speed up compilation times.
- **Concept:** Precompiled headers store commonly used headers in a precompiled form, reducing the need to recompile them every time a new file is compiled.
- **Use Case:** Precompiled headers are a standard optimization for large projects with many source files.

#### `IMHEX_COMPRESS_DEBUG_INFO`
- **Purpose:** Compresses debugging information to reduce the size of the generated binary.
- **Use Case:** This option is useful when you want to include debug symbols (for use in debugging or profiling) but still want to minimize binary size.

### Underlying Concepts

- **CMake:** A cross-platform build system that automates the creation of build environments. It is used to generate platform-specific makefiles or project files, based on the given configuration files (`CMakeLists.txt`).
  
- **Link-Time Optimization (LTO):** A compiler optimization that occurs at the linking stage, allowing the compiler to optimize across different compilation units, improving performance and reducing binary size.

- **Precompiled Headers:** A mechanism used to reduce compilation times by precompiling commonly included header files and using the precompiled version in multiple source files.

- **Static vs. Dynamic Linking:** Static linking includes all the code from the libraries directly into the executable, while dynamic linking keeps the library separate and loads it at runtime. Static linking can simplify distribution, but dynamic linking can save memory if the same library is used by multiple programs.

- **Unity Build:** A technique where multiple source files are compiled together as a single unit, reducing the overhead of managing many individual compilation units, thus speeding up the build process.

- **Unit Tests:** Small tests that verify the behavior of individual functions or modules in isolation, ensuring that each part of the code works correctly.

- **PDB (Program Database) Files:** Files used in Windows development to store debugging information for an application, enabling debuggers to map the executable code back to the source code.

- **DWARF:** A debugging standard used on Unix-like systems to store debugging information in a binary. This information is used to map executable code back to the source code during debugging.

## ide-helper.cmake
This code is part of a CMake build system configuration that enhances IDE support, particularly for Xcode and projects using folder hierarchies in IDEs. The configuration includes several functions and options aimed at tweaking how targets (like libraries and executables) are handled in IDEs. Here’s a detailed breakdown of each section:

### 1. **Options**

```cmake
option(IMHEX_IDE_HELPERS_OVERRIDE_XCODE_COMPILER "Enable choice of compiler for Xcode builds, despite CMake's best efforts" OFF)
option(IMHEX_IDE_HELPERS_INTRUSIVE_IDE_TWEAKS    "Enable intrusive CMake tweaks to better support IDEs with folder support" OFF)
```

- **IMHEX_IDE_HELPERS_OVERRIDE_XCODE_COMPILER**: This option allows overriding the default compiler in Xcode builds, which CMake typically controls. Setting this to `ON` lets you choose your compiler in Xcode, although it’s described as hacky and potentially fragile.
  
- **IMHEX_IDE_HELPERS_INTRUSIVE_IDE_TWEAKS**: When enabled (`ON`), this option applies additional tweaks for better folder support in IDEs, such as organizing source files and handling headers better.

### 2. **Xcode Compiler Override**

```cmake
if (IMHEX_IDE_HELPERS_OVERRIDE_XCODE_COMPILER AND CMAKE_GENERATOR STREQUAL "Xcode")
    set(CMAKE_GENERATOR "Unknown")
    enable_language(C CXX)
    
    set(CMAKE_GENERATOR "Xcode")
    ...
endif()
```

- This block handles overriding the compiler when using Xcode as the build generator. Normally, CMake ignores custom compilers with Xcode, but this snippet tricks CMake by temporarily changing the generator and setting the compiler explicitly.
  
- **Key Concept**: This is a workaround to force CMake to use a specific compiler in Xcode, even though Xcode has its own internal compiler settings.

### 3. **Utility Functions**

#### **`macro(returnIfTargetIsNonTweakable target)`**

```cmake
macro(returnIfTargetIsNonTweakable target)
    get_target_property(targetIsAliased ${target} ALIASED_TARGET)
    get_target_property(targetIsImported ${target} IMPORTED)
    ...
endmacro()
```

- This function checks if a target is "non-tweakable," meaning it should be excluded from further modifications. For instance, aliased and imported targets are skipped since they are usually external libraries or custom target types.

#### **`function(tweakTargetForIDESupport target)`**

```cmake
function(tweakTargetForIDESupport target)
    returnIfTargetIsNonTweakable(${target})
    ...
endfunction()
```

- **Purpose**: This function organizes target sources into a directory tree within IDEs and adds private headers to the project. It attempts to improve how source files are displayed in IDEs with folder support (like Visual Studio or Xcode).
  
- **Key Concept**: IDEs may not group files well by default, so this function helps to structure them, especially when dealing with private headers or third-party libraries.

### 4. **Functions for Adding Libraries and Executables**

```cmake
function(add_library target)
    _add_library(${target} ${ARGN})
    tweakTargetForIDESupport(${target})
endfunction()

function(add_executable target)
    _add_executable(${target} ${ARGN})
    tweakTargetForIDESupport(${target})
endfunction()
```

- These functions override CMake’s default `add_library` and `add_executable` to automatically apply the `tweakTargetForIDESupport` function whenever a new library or executable is created. This ensures that all targets benefit from IDE support improvements.

### 5. **Folder Tweaking Functions**

#### **`function(_tweakTarget target path)`**

```cmake
function(_tweakTarget target path)
    get_target_property(targetType ${target} TYPE)
    ...
endfunction()
```

- **Purpose**: This function assigns each target (libraries, executables, etc.) to a specific folder in the IDE. Folders are purely an IDE feature and have no effect on the build system, but they help developers organize their project visually within the IDE.

#### **`macro(_tweakTargetsRecursive dir)`**

```cmake
macro(_tweakTargetsRecursive dir)
    get_property(subdirectories DIRECTORY ${dir} PROPERTY SUBDIRECTORIES)
    foreach(subdir IN LISTS subdirectories)
        _tweakTargetsRecursive("${subdir}")
    endforeach()
    ...
endmacro()
```

- This macro recursively applies folder tweaks to all subdirectories in the project. It ensures that every target in the project is placed into the correct folder based on its path.

#### **`function(tweakTargetsForIDESupport)`**

```cmake
function(tweakTargetsForIDESupport)
    set_property(GLOBAL PROPERTY USE_FOLDERS ON)
    _tweakTargetsRecursive("${CMAKE_SOURCE_DIR}")
endfunction()
```

- **Purpose**: This function is the entry point for tweaking all targets in the project for IDE support. It turns on folder support globally and then recursively applies folder tweaks to all subdirectories and targets.

### **Key Concepts and Underlying Ideas**

- **Xcode Compiler Override**: Xcode has built-in mechanisms for choosing compilers, and CMake usually respects this. The snippet shown overrides this behavior, allowing developers to explicitly set which compiler to use for Xcode builds.

- **IDE Folder Support**: IDEs like Visual Studio and Xcode can organize project files into folders for easier navigation. The functions in this CMake script are designed to enhance how targets and source files are grouped into folders to make the project structure clearer in IDEs.

- **Intrusive Tweaks**: The "intrusive tweaks" option modifies how CMake handles certain things, like adding private headers to targets, which normally CMake doesn't manage well in IDEs. This helps developers using IDEs by making file organization more intuitive.

- **Target Tweaks**: Functions like `tweakTargetForIDESupport` apply improvements to each target, such as grouping files and adding headers, making it easier to work with projects that involve many files and directories.

This configuration is especially useful for developers working with large CMake-based projects who use IDEs like Xcode or Visual Studio and want better control over how their project appears and is managed in the IDE environment.