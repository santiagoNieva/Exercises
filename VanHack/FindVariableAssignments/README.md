# FIND VARIABLE ASSIGNMENTS

This exercise consists on creating a script that will take as input python (3.8) code and detect any dangerous re-definitions of python's builtins functions.

I copy the tests that comes with the challenges and you can add more if you want to.

For this task i had to checkout any form of variable definition that python may accept, and gets me into a better understanding of the language.

**This solution is not a good one. It should be done with ast module. It was a nice try**

14/11/2022 I found a way to bypass this warngins with f-strings

Example:
hi = 2
f"the variable hi is {hi} but now {'' if exec('hi=3') else ''}has changed for {hi}"

Output:
'the variable hi is 2 but now has changed for 3'

as the real execution begins as a string. I will set a specific warning for this.