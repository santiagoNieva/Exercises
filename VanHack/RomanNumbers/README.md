# ROMAN TO DECIMAL

This exercise gets a roman number as string and returns it value as a decimal number.

## Solution Explanation

The first thing to do was mapping avery Roman Character into his decimal counterpart. So i did this in a simple dicctionary.

The next thing to do was to read the entire string one by one. I use to extra variables, one for the final result, and other to store the previous roman number. Every time I read a character I checkout if there is a previous one and if it is smaller i just simply add it to the results, but if it is bigger than previous one, then i have to add the new number, and subustract the previous, but, as the previous number was already added, i have to substract it again.
The original challenge doesn't ask for validation but I will add them for good practice (I will obviously use internet for this because is not the actual problem here).