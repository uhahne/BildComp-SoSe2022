# BildComp-SoSe2022
Exercises for course "Bildverarbeitung und Computergrafik" in summer term 2022 at HS Furtwangen University. Please note that all content here is tentative and will be adopted to the students' needs during the course.

## Prerequisites
- Download and install Python 3 from [python.org](https://www.python.org/downloads/)
  - Version 3.10.2 is recommended
  - Test which version is installed on your machine with `python --version` in the terminal
    - Ensure that the correct version is used in the terminal as well as the selected interpreter.
- Install pip from https://pip.pypa.io/en/stable/installation/
  - Ensure that a version newer than 19.3 is installed (pip --version)

## Further Python ressources
If you are not familiar with Python, check out the following tutorials:
- https://www.python.org/about/gettingstarted/ 
- https://docs.python.org/3/tutorial/
- https://code.visualstudio.com/docs/python/python-tutorial

## VS Code
The code is all developed using VS Code. You can use any IDE, but VS Code will be used in the lecture.
- Install VS Code from https://code.visualstudio.com/

## VS Code extensions
In order to get supported in coding it is helpful to install some extensions in VS Code.

### Python
Python extension for Visual Studio Code

#### Pylance
Fast, feature-rich language support for Python

### Python Image Preview
You can quickly check your Python image data during debugging.

### Rather optional extensions

#### Todo Tree
Provides an overview about all code lines marked with "TODO".

#### Python-autopep8
This is a vscode-extension that applies autopep8 to your current file.

## Installing OpenCV
- Install opencv as pip module opencv-python as explained on https://pypi.org/project/opencv-python/ (Main modules should be enough for the beginning)

| Windows         | MacOS     | Linux |
|--------------|-----------|------------|
|pip install opencv-python|python -m pip install opencv-python|python -m pip install opencv-python|

⚠ Note that there is no need to install OpenCV from opencv.org

⚠ Ensure that Python 3.10.2 is used as mentioned above.

See https://docs.opencv.org/master/d0/de3/tutorial_py_intro.html for further help on other systems.

You can check the installed version with pip show opencv-python. It should be "Version: 4.5.5.62" or newer.

## Start coding
Now you are ready to start coding the tutorials that are described further below. The idea is to start with the "BC_tutorial_XX_empty.py" files and try to fulfill the TODOs. That's how it is done during the course. The "BC_tutorial_XX.py" files contain the solution.

---
## Helpful ressources

### Python
You can use https://docs.python.org/3/ as a starting point and the [Library Reference](https://docs.python.org/3/library/index.html) or the [Language Reference](https://docs.python.org/3/reference/index.html) should contain all the needed information.

### OpenCV reference
See https://docs.opencv.org/4.5.5/ for the OpenCV code reference. Here, all OpenCV methods are explained. If you want to know about parameters and flags, this is the page to look them up. 

### NumPy
OpenCV uses NumPy ndarrays as the common format for data exchange. It can create, operate on, and work with NumPy arrays. For some operations it makes sense to import the NumPy module and use special functions provided by NumPy. Other libraries like TensorFlow and SciPy also use NumPy. See https://numpy.org/doc/stable/reference/index.html for the API reference.

### Python style guide
All these tutorials are written according to the [PEP8 Python Code Style Guide](https://www.python.org/dev/peps/pep-0008/). This is realized using the Python tools [pycodestyle (pep8)](https://code.visualstudio.com/docs/python/linting#_pycodestyle-pep8) and [autopep8](https://pypi.org/project/autopep8/).

### Other learning sources for OpenCV
- [LearnOpenCV](https://learnopencv.com/) is a website that hosts some complete courses in Computer Vision and also some very good and [introductive tutorials](https://learnopencv.com/getting-started-with-opencv/).


### Other video tutorials
- [Tech with Tim: OpenCV Python Tutorials](https://www.youtube.com/watch?v=qCR2Weh64h4&list=PLzMcBGfZo4-lUA8uGjeXhBUUzPYc6vZRn)
- [freeCodeCamp.org -OpenCV Course - Full Tutorial with Python](https://www.youtube.com/watch?v=oXlwWbU8l2o) (not yet watched)

---
## Tutorials

### Tutorial #1
Load, resize and rotate an image. And display it to the screen.
- [empty code](./BC_tutorial_01_empty.py)
- [complete code](./BC_tutorial_01.py)

### Tutorial #2
Direct pixel access and manipulation. Set some pixels to black, copy some part of the image to some other place, count the used colors in the image
- [empty code](./BC_tutorial_02_empty.py)
- [complete code](./BC_tutorial_02.py)

### Tutorial #3
Show camera video and mirror it.
- [empty code](./BC_tutorial_03_empty.py)
- [complete code](./BC_tutorial_03.py)

### Tutorial #4
Loading a video file and mirror it.
- [empty code](./BC_tutorial_04_empty.py)
- [complete code](./BC_tutorial_04.py)

### Tutorial #5
Use the webcam image stream and draw something on it. Animate one of the drawings.
- [empty code](./BC_tutorial_05_empty.py)
- [complete code](./BC_tutorial_05.py)

### Tutorial #6
Analyze the webcam image stream and draw points at the mouse position on the image
- [empty code](./BC_tutorial_06_empty.py)
- [complete code](./BC_tutorial_06.py)

### Tutorial #7
Geometric transformations a.k.a. image warping.
- [empty code](./BC_tutorial_07_empty.py)
- [complete code](./BC_tutorial_07.py)

### Tutorial #8
Clicking points to define lines and compute intersection points
- [empty code](./BC_tutorial_08_empty.py)
- [complete code](./BC_tutorial_08.py)

### Tutorial #9
Computing vanishing points and lines 
- [empty code](./BC_tutorial_09_empty.py)
- [complete code](./BC_tutorial_09.py)

### Tutorial #10
Computing depth map from a pair of rectified stereo images 
- [empty code](./BC_tutorial_10_empty.py)
- [complete code](./BC_tutorial_10.py)

### Tutorial #11
Extracting the intrinsic camera parameters from an image
- [empty code](./BC_tutorial_11_empty.py)
- [complete code](./BC_tutorial_11.py)

### Tutorial #12
Computing the fundamental matrix from point correspondencies which are found with SIFT
- [empty code](./BC_tutorial_12_empty.py)
- [complete code](./BC_tutorial_12.py)

### Tutorial #13
Seam carving as example for dynamic programming
- [empty code](./BC_tutorial_13_empty.py)
- [complete code](./BC_tutorial_13.py)
