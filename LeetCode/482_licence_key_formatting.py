"""
You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

 

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

 

Constraints:

    1 <= s.length <= 105
    s consists of English letters, digits, and dashes '-'.
    1 <= k <= 104


"""

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        upper_no_dash = s.replace("-","").upper()
        length = len(upper_no_dash)
        first = length % k
        result = []
        index = 0
        while length > 0:
            if not first:
                first = k
            result.append(upper_no_dash[index:index+first])
            index += first
            length -= first
            first = k
        return "-".join(result)
                

if __name__ == "__main__":
    description = """
Input a license key composed by number letters and dashes '-'
Example 1:

Input: number = ""2-5g-3-J""
Output: "25-G3J"
"""

    import sys
    args = sys.argv[1:]
    if not args or args[0] in ['--help','-h'] or len(args) > 2:
        print(description)
    else:
        try:
            license = args[0]
            group_number = int(args[1])
            solution = Solution()
            results = solution.licenseKeyFormatting(license,group_number)
        except Exception as e:
            print(f"""Exception: {e}
You should enter a license key composed by numbers letters and dashes '-'
Exception: {e}

Example:
python 482_license_key_formatting.py "2-5g-3-J" 3
>>>> "25-G3J"
""")

        else:
            print(results)