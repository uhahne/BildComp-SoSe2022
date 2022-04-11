# BildComp SoSe 2022 - Assignment #02 - Height measurement

## Task
Implement a script with Python and OpenCV that calculates the height of an object given a reference object placed on the same plane. Given three exemplary images (images\table_bottle_\*.jpg) of a table showing two objects - a bottle and a mug. The bottle has a height of 26 cm*. Calculate the height of the mug in cm. Write a readme file that explains what you have done and how to run the script and what the script does.

\* measured by hand as no official source found for the bottle dimensions.

## Hints
Check the script [BildComp-05-Perspektiven.pdf](https://felix.hs-furtwangen.de/url/RepositoryEntry/4072407268/CourseNode/105308879908340/path%3D~~BildComp%2D05%2DPerspektiven%2Epdf/0) slide 58 in order to get the formulas how to compute the height of an object.

You can use any of the three given images: images\table_bottle_\*.jpg

Check out [this project](https://github.com/othneildrew/Best-README-Template) to get an impression about a good readme file.

## Rating
- Write a script that allows manually selecting the needed image points for the calculation. (2 points)
- Write a script that computes the vanishing line for the table plane and visualizes it. (2 points)
- Write a script that computes the height of the mug. (2 points)
- BONUS: Most precise solution among all submissions. (1 point)
- BONUS: Write a script that finds the plane and hence the vanishing line automatically from the edges in the image. (1 point)
- Code is well readable, structured and documented. And it can be well explained in the consultation. (up to 2 points)
- Code fullfils the [PEP8 styleguide](https://peps.python.org/pep-0008/). (1 point)
- Readme is well written and helpful. It contains all used modules and their version. (1 point)

## Acceptance criteria
- Hand in code (.py files), accompanying images or videos and short explanation (readme.md file) either as one zip file or as a link to a public github respository via FELIX. If you use a Github link, please create a tag of the final version before the deadline.
- The reamde file should be no longer than 600 words, it can be German or English.
- The code is written mainly on your own and any other source is mentioned in the code. If two groups hand in the same or extremely similar solution, both groups do not pass the assignment.

## Pass criteria
- The assignment is passed, if 5 or more points are reached.