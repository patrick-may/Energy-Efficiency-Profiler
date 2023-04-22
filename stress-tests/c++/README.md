# C++ CowProf Usage

As part of this investigation to energy consumption, I wanted to observe at least one compiled programming language, even
if python was drastically easier to implement. 

This C++ folder is a proof-of-concept that the energy profiler can be extended to be used in other programming languages relatively easily. 

Within this subdirectory are various self-contained c++ programs to try analysis on, as well as a `wrapper.hpp` file, which is important to keep as is.

---

## Pinpointing Profiling Spots
Within every C++ file that is part of a project you want to have CowProf analyze, the steps required of the developer are as follows:

- add `#include "wrapper.hpp"` to the top of files you are going to observe
- At the beginning of each function (or code segment of interest) add a line: 
```cpp
CowProf {varname}("{function identifier}");
```
- Before a function returns or at the end of a specific code block of interest, add the line 
```cpp
{varname}.finish();
```

That is all the injective code required! Look at `mixed.cpp` for some examples of implementing **CowProf**.

---

## Running on a C++ Project
After code injection is complete, pass a compilation command of your c++ project to the **CowProf** script. Currently, the script assumes code will be compiled to a single `./a.out` object file after compilation.

