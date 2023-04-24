# Python CowProf Usage

Python is a very high level and multi-paradigm language that can be used to do multiple things. 
However, a lot of research has found python to definetly be energy inefficient compared to other programming languages

---

## Pinpointing Profiling Spots
Within every Python file that is part of a project you want to have CowProf analyze, the steps required of the developer are as follows:

- add `from wrapper include measure_time` to the top of files you are going to observe
- At the beginning of each function, decorate the function header with `@measure_time`


That is all the injective code required! Look at `mixed.py` for some examples of implementing **CowProf**.

---

## Running on a C++ Project
After code injection is complete, pass a compilation command of your python project to the **CowProf** script.

