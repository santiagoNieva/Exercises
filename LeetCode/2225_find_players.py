"""
You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

Return a list answer of size 2 where:

    answer[0] is a list of all players that have not lost any matches.
    answer[1] is a list of all players that have lost exactly one match.

The values in the two lists should be returned in increasing order.

Note:

    You should only consider the players that have played at least one match.
    The testcases will be generated such that no two matches will have the same outcome.

 

Example 1:

Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
Output: [[1,2,10],[4,5,7,8]]
Explanation:
Players 1, 2, and 10 have not lost any matches.
Players 4, 5, 7, and 8 each have lost one match.
Players 3, 6, and 9 each have lost two matches.
Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].

Example 2:

Input: matches = [[2,3],[1,3],[5,4],[6,4]]
Output: [[1,2,5,6],[]]
Explanation:
Players 1, 2, 5, and 6 have not lost any matches.
Players 3 and 4 each have lost two matches.
Thus, answer[0] = [1,2,5,6] and answer[1] = [].

 

Constraints:

    1 <= matches.length <= 10 to the 5th
    matches[i].length == 2
    1 <= winneri, loseri <= 10 to the 5th
    winneri != loseri
    All matches[i] are unique.



---!SECTION TIMING
    Start Time = 28/11/22 11:55
    End Time = 28/11/22 12:32

"""


class Solution:
    def findWinners(self,matches):
        winners = [matches[0][0]]
        losers = [matches[0][1]]
        deleted = []
        index_w = 0
        index_l = 0
        index_d = 0
        for winner, loser in matches[1:]:
            print(f"\Probando set {winner} - {loser}\n\twinners: {winners}")
            # Winner section
            if winners:
                while not winners[index_w] == winner:
                    print(f"\t\tPrincipio de while:   - index_w:{index_w} -- winner: {winner}")
                    if winners[index_w] > winner:
                        print("\t\t\t\tEntra al mayor que >>>>>>>")
                        if index_w == 0:
                            if not winners[0] == winner:
                                winners.insert(0,winner)
                            break
                        else:
                            index_w -= 1
                            print(f"\t\t\t\t\t\t\t{winners[index_w]}[{index_w}] < {winner}")
                            if winners[index_w] < winner:
                                winners.insert(index_w+1,winner)
                                index_w += 1
                                break
                    else:
                        print("\t\t\t\tEntra al menor que <<<<<<<")
                        if index_w == len(winners) -1:
                            if not winners[index_w] == winner:
                                winners.append(winner)
                                index_w += 1
                            break
                        else:
                            index_w += 1
                            if winners[index_w] > winner:
                                winners.insert(index_w,winner)
                                break
            else:
                index_w = 0
                winners.append(winner)     

            # losers
            while not losers[index_l] == loser:
                pass
            else:
                del losers[index_l]
                index_l = index_l -1 if index_l > 0 else 0
                deleted.append(loser)

        print(f"\nwinners: {winners}\n\nlosers:{losers}")


if __name__ == '__main__':
    matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    solution = Solution()
    solution.findWinners(matches)
                    
            


