def findSubsets(arr,n):
    # Short version
    ans = []
    for i in range(1 << n):
        ans.append([arr[j] for j in range(n) if (i & (1 << j))])
        
    return ans

def findSubsetsExplained(arr, n):
    # Long version
    # We declare an empty array were we'll append subsets.
    ans = []

    # The length of the power set is 2 to the power of n
    # The << notations is for bit shift operator. it works directly on bits
    # It adds n times 0 to the right of the number in binary. So, if we have
    # 1 << 3 it will get 1000 which translated to decimal is 8
    # which results on 2 to the power of 3. Try it out in your shell
    for i in range(1 << n):
        # we create an empty array to store the values.
        nuevo = []

        # we loop n times
        for j in range(n):
            # this is where the magic happens
            # & operator works with binary numbers too
            # it will compare every bit of both binaries, and will return a 1 if both are 1, else 0
            # Example:
            #     a  =  1 0 0 1 1 1 0 0           ->    156
            #     b  =  0 1 0 1 1 0 0 0           ->    88
            # --------------------------
            # a & b  =  0 0 0 1 1 0 0 0           ->    24

            # in this case, we will go thru every item of the array (to the nth value actually)
            # and append it only if the subset is a 1

            if (i & (1 << j)):
                nuevo.append(arr[j])

        # Let's re-check this
        # the binary progresion from 1 to n will be this. Let's take n = 3
        # range(1<<3) -> will loop 8 times from 0 to 7
        # i will take then this numbers (binary mode)

        # i = 0  ->   0 0 0
        # i = 1  ->   0 0 1
        # i = 2  ->   0 1 0
        # i = 3  ->   0 1 1
        # i = 4  ->   1 0 0
        # i = 5  ->   1 0 1
        # i = 6  ->   1 1 0
        # i = 7  ->   1 1 1

        # If you take a look, in this progresion we can observe the complete powerset.
        # we have the null subset when i = 0
        # the single value subsets when i = 1,2 and 4
        # the double value subset when i = 3, 5, 6
        # and finally the triple value subset when i = 7

        # Then with the & operator, we just add the value if it has a 1, and none if its 0

        ans.append(nuevo)
    return ans


def findSubsetsPrintedStepByStep(arr, n):
    # We declare an empty array were we'll append subsets.
    ans = []
    print(arr, " len: ", n)
    print("powerset len: ", 1 << n)
    for i in range(1 << n):
        print("i: ", i)
        nuevo = []
        for j in range(n):
            print("\tj: ", j, " ----> magic: (i & (1 << j)):")
            print("\t\t\t\t\t",bin(i))
            print("\t\t\t\t\t",bin(1<<j))
            print("\t\t\t\t\t\t: Result: ", i & (1<<j))
            if (i & (1 << j)):
                print("\t\tElement: ",arr[j])
                nuevo.append(arr[j])
        print("\tNew: ", nuevo)
        ans.append(nuevo)
        print()
    return ans