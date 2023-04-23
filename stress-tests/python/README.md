# Python CowProf Usage

Python is a very high level and multi-paradigm language that can be used to do multiple things. 
However, a lot of research has found python to definetly be energy inefficient compared to other programming languages

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

