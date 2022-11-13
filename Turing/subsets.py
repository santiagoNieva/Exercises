

def findSubsets(arr,n):
    ans = []
    for i in range(1 << n):
        ans.append([arr[j] for j in range(n) if (i & (1 << j))])
        
    return ans
