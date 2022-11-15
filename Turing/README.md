#    Explanation:

This beautiful piece of code I learned it on the internet. but with no comments so, here we go.  
There is another solution using itertools powerset function, but has no fun.  

The problem consist in based on a number list and a number n lower than len(list)  
returns all the posible subsets of the first n items of the list  
This is named **POWERSET**  
## Example:

    Input:
        n = 2
        arr = [1,2,3,4,5,6]

    Output:
        [[],[1],[2],[1,2]]
        length = 4

as n = 2, we only get the first and second items from the list, in this case 1 and 2  
the output consists on a list of four lists:
 * the first one is the empty list, the first of possibles list  
 * the second and third, are **[1]** and **[2]** being the lists with only one value.  
*if n were **4**, we would have four of this ([1],[2],[3],[4])*  
 * the fourth element is **[1,2]** the combination of 2 items, in this case all of the items:  
*if n were **3** we would have more of this **([1,2],[1,3][2,3])***

**The ordering is not important in this problem.*  

## Other Example:

    Input:
        n = 3
        arr = [1,2,3,4,5,6]
    Output:
        [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
        length = 8

Once we understood this i will create a new similar function but not oneliner, so we can understand what's happening.  
Check subsets.py  
***HINT:** Binary operations is all we need*