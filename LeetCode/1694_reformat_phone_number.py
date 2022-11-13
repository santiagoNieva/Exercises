"""
You are given a phone number as a string number. number consists of digits, spaces ' ', and/or dashes '-'.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

    2 digits: A single block of length 2.
    3 digits: A single block of length 3.
    4 digits: Two blocks of length 2 each.

The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce at most two blocks of length 2.

Return the phone number after formatting.

Example 1:

Input: number = "1-23-45 6"
Output: "123-456"
Explanation: The digits are "123456".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 3 digits remaining, so put them in a single block of length 3. The 2nd block is "456".
Joining the blocks gives "123-456".

Example 2:

Input: number = "123 4-567"
Output: "123-45-67"
Explanation: The digits are "1234567".
Step 1: There are more than 4 digits, so group the next 3 digits. The 1st block is "123".
Step 2: There are 4 digits left, so split them into two blocks of length 2. The blocks are "45" and "67".
Joining the blocks gives "123-45-67".

Example 3:

Input: number = "123 4-5678"
Output: "123-456-78"
Explanation: The digits are "12345678".

---!SECTION TIMING
    Start Time = 11/11/22 23:44
    End Time = 12/11/22 00:25

"""
class Solution:
    def reformatNumber(self, number: str) -> str:

        number = ''.join(c for c in number if c.isdigit())
        response = []
        length = len(number)
        index = 0
        while length > 0:
            if length > 4:
                response.append(number[index:index+3])
                length -= 3
                index += 3

            elif length == 4:
                response.append(number[index:index+2])
                response.append(number[index+2:])
                length = 0
                
            elif length == 3:
                response.append(number[index:])
                length = 0

            elif length == 2:
                response.append(number[index:])
                length = 0

        return "-".join(response)

if __name__ == "__main__":
    description = """
Input a phone number and will be reformatted

Example 1:

Input: number = "1-23-45 6"
Output: "123-456"
"""

    import sys
    args = sys.argv[1:]
    if not args or args[0] in ['--help','-h'] or len(args) > 1:
        print(description)
    else:
        try:
            number = args[0]
            hola = Solution()
            results = hola.reformatNumber(number)
        except Exception as e:
            print(f"""Exception: {e}
You should enter a phone nomber as a string with quotes.
Exception: {e}

Example:
python 1694_reformat_phone_number.py "1-23-45 6"
>>>> "123-456"
""")

        else:
            print(results)