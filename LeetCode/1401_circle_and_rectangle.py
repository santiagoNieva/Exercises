"""
1401. Circle and Rectangle Overlapping

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.


Example 1:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false

Example 3:

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true

Constraints:

    1 <= radius <= 2000
    -104 <= xCenter, yCenter <= 104
    -104 <= x1 < x2 <= 104
    -104 <= y1 < y2 <= 104

---!SECTION TIMES
    Start Time = 12/11/22 00:27
    Pause = 01:30
    UnPause = 12:58
    End Time = 12/11/22 13:02
"""

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        """ 00.37"""

        # get nearest distance from center of the circle to any point of rectangle
        if xCenter <= x1:
            x_dist = x1-xCenter
        elif xCenter >= x2:
            x_dist = xCenter-x2
        else:
            x_dist = 0
                
        if yCenter <= y1:
            y_dist = y1-yCenter
        elif yCenter >= y2:
            y_dist = yCenter-y2
        else:
            y_dist = 0
                
        # Check if vertice is inside circle
        return x_dist**2 + y_dist**2 <= radius**2

if __name__ == "__main__":
    description = """
Enter circle represented as (radius, xCenter, yCenter)
and an axis-aligned rectangle represented as (x1, y1, x2, y2),
where (x1, y1) are the coordinates of the bottom-left corner, 
and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. 
In other words, check if there is any point (xi, yi)
that belongs to the circle and the rectangle at the same time.

Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).

"""

    import sys
    args = sys.argv[1:]
    if not args or args[0] in ['--help','-h'] or len(args)>7:
        print(description)
    else:
        try:
            radius = int(args[0])
            xCenter = int(args[1])
            yCenter = int(args[2])
            x1 = int(args[3])
            y1 = int(args[4])
            x2 = int(args[5])
            y2 = int(args[6])
            solution = Solution()
            results = solution.checkOverlap(radius, xCenter, yCenter, x1, y1, x2, y2)
        except Exception as e:
            print(f"""Exception: {e}
You should enter circle represented as (radius, xCenter, yCenter)
and an axis-aligned rectangle represented as (x1, y1, x2, y2),
where (x1, y1) are the coordinates of the bottom-left corner, 
and (x2, y2) are the coordinates of the top-right corner of the rectangle.
Exception: {e}

Example:
python 1401_circle_and_rectangle.py 1 0 1 2 3 4 5
>>>> 9""")
        else:
            print(results)