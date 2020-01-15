# CS498 IR, Spring 2020

## Kris Hauser
## Yifan Zhu

Assignments for CS498IR, Spring 2020

## Installation

Open a Jupyterhub terminal, and run the following lines

```
git clone https://github.com/krishauser/cs489ir_s2020.git
cs489ir_s2020/setup.sh
```

To test that your installation is working:

1. Refresh the Jupyterhub main window.  
2. Try to create a new notebook with the "cs489ir-virtualenv" kernel.  If you don't see this, something has gone wrong.
3. Open up one of the notebooks in Klampt-examples/Jupyter/ (such as BasicKlamptDemo.ipynb).  Use the Kernel menu to change the kernel to the cs489ir-virtualenv kernel.  Start running the cells.  If you get an error, then something has gone wrong.
4. Open up RoboticSystemsBook/Book.ipynb.  Follow the instructions under "The first time you install..." in the Jupyterhub main window.
5. Open up another chapter of the book (such as 3DRotations.ipynb).  You should see a table of contents, and all the math should be formatted without stray \V symbols.

If all of these tests pass, you're ready to go!


## Updating assignments

Open a Jupyterhub terminal, and run

```
cs489ir_s2020/update.sh
```
