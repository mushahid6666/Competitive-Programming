'''
Your music player contains N different songs and she wants to listen to L (not necessarily different)
songs during your trip.  You create a playlist so that:

Every song is played at least once
A song can only be played again only if K other songs have been played
Return the number of possible playlists.  As the answer can be very large, return it modulo 10^9 + 7.



Example 1:

Input: N = 3, L = 3, K = 1
Output: 6
Explanation: There are 6 possible playlists. [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1].
Example 2:

Input: N = 2, L = 3, K = 0
Output: 6
Explanation: There are 6 possible playlists. [1, 1, 2], [1, 2, 1], [2, 1, 1], [2, 2, 1], [2, 1, 2], [1, 2, 2]
Example 3:

Input: N = 2, L = 3, K = 1
Output: 2
Explanation: There are 2 possible playlists. [1, 2, 1], [2, 1, 2]


Note:

0 <= K < N <= L <= 100
'''
import math
class Solution(object):
    """
    Intuition

    Let dp[i][j] be the number of playlists of length i that have exactly j unique songs.
    We want dp[L][N], and it seems likely we can develop a recurrence for dp.
    Algorithm
    Consider dp[i][j]. Last song, we either played a song for the first time or we didn't.
    If we did, then we had dp[i-1][j-1] * (N-j) ways to choose it. If we didn't, then we repeated
    a previous song in dp[i-1][j] * max(j-K, 0) ways (j of them, except the last K ones played are banned.)


    """

    def numMusicPlaylists(self, N, L, K):
        """
        :type N: int
        :type L: int
        :type K: int
        :rtype: int
        """
        mod = math.pow(10,9) + 7
        dp = [[long(0) for _ in range(N + 1)] for _ in range(L +1 )]
        dp[0][0] = 1
        for i in range(1, L +1):
            for j in range(1, N +1):
                dp[i][j] = dp[i-1][j-1] * (N-(j-1)) % mod
                if j > K :
                    dp[i][j] = (dp[i][j] + ((dp[i-1][j] * (j-K))% mod) ) % mod

        return int(dp[L][N])

obj = Solution()
# N = 3
# L = 3
# K = 1
# print obj.numMusicPlaylists(N, L,  K)
# N = 2
# L = 3
# K = 0
# print obj.numMusicPlaylists(N, L,  K)
# N = 2
# L = 3
# K = 1
# print obj.numMusicPlaylists(N, L,  K)
N = 16
L = 16
K = 4
print obj.numMusicPlaylists(N, L,  K), "Exp: 789741546"