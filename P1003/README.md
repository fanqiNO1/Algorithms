# P1002 Soldier who Crossed the River

It's Chinese name is "过河卒". The translation is not very proper.

This problem is a typical dynamic-programming problem. Namely, dp-problem.

The initialization conditions are $dp[0][0] = 1 \text{ else } 0$ and the transfer equation is $dp[i][j] = dp[i-1][j] + dp[i][j-1]$. Because the soldier can only take one step down or to the right at a time.

Meanwhile, due to the existence of some restrictions, not all the value in board is computed by the transfer equation.

Attention:
1. How to build multidimensional arrays in python.
2. The restrictions includes the horse itself.
3. The index of board is begin from 0.
