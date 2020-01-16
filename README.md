# CS498 IR, Spring 2020

## Assignments and programming environment for CS498IR, Spring 2020

Kris Hauser (kkhauser@illinois.edu)
Yifan Zhu (yifan16@illinois.edu)


## Installation

Open a Jupyterhub terminal, and run the following lines

```
git clone https://github.com/krishauser/cs498ir_s2020.git
cs498ir_s2020/setup.sh
```

To test that your installation is working:

1. Refresh the Jupyterhub main window.  
2. Try to create a new notebook with the "cs498ir-virtualenv" kernel.  If you don't see this, something has gone wrong.  
3. Open up one of the notebooks in Klampt-examples/Jupyter/ (such as BasicKlamptDemo.ipynb).  Use the Kernel menu to change the kernel to the cs498ir-virtualenv kernel.  Start running the cells.  If you get an error, then something has gone wrong.

If all of these tests pass, you're ready to go!

**If some test fails**, try logging out of the Jupyterhub environment and logging back in.  If it fails again, please contact the instructors.


## Updating assignments

Open a Jupyterhub terminal, and run

```
cs498ir_s2020/update.sh
```

