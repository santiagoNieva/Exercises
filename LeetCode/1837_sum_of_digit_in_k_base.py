"""
    1837 Sum of Digit in K base

    Given an integer n (in base 10) and a base k, 
    return the sum of the digits of n 
    after converting n from base 10 to base k.

    After converting, each digit should be 
    interpreted as a base 10 number, 
    and the sum should be returned in base 10.

    Start Time = 11/11/22 22:44
    End Time = 11/11/22 23:37

"""
class Solution:
    acumulador = 0
    def sumBase(self, n: int, k: int) -> int:
        if n >= k:
            self.acumulador += n % k
            _n = n//k
            return self.sumBase(_n,k)
        else:
            self.acumulador += n
            return self.acumulador
            

if __name__ == "__main__":
    description = """
Given an integer n (in base 10) and a base k, 
return the sum of the digits of n 
after converting n from base 10 to base k.

After converting, each digit should be 
interpreted as a base 10 number, 
and the sum should be returned in base 10.

Example:
python 1837_sum_of_digit_in_k_base.py 4 8 
>>>> 9
"""

    import sys
    args = sys.argv[1:]
    if not args or args[0] in ['--help','-h'] or len(args)>2:
        print(description)
    else:
        try:
            n = int(args[0])
            k = int(args[1])
            hola = Solution()
            results = hola.sumBase(n,k)
        except Exception as e:
            print(f"""Exception: {e}
You should send 2 INTEGERS, number 'n' and base 'k'.
Exception: {e}

Example:
python 1837_sum_of_digit_in_k_base.py 4 8 
>>>> 9""")
        else:
            print(results)