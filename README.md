# Project Statement
It’s Christmas time and project MANAS is getting ready to open their presents. Unfortunately, Shivansh is a bit clumsy and falls over the presents by mistake. The presents are actually gift hampers so their contents get spread on the floor by mistake. Thankfully, the damage is not much and one can understand which item belongs to which hamper. In addition to being clumsy, Shivansh is very lazy so he wants you to do that. You are given the floor dimensions and the number of presents and your goal is to identify the centre of the fallen items of each present. The fallen items are represented as 1s and the empty spots as 0s. Output the centers.

Note: Make sure to handle the input in the same order as given. (consider the bottom left as the origin)

Input Format

m rows
n columns
k hampers
m * n matrix
Constraints

1 <= m <= 100
1 <= n <= 100
1 <= k < 15
Output Format

Sorted K points of the center (sorted primarily with respect to x and secondarily with respect to y in ascending order) in the format x y. The centers can be in float, rounded down, or truncated- the checker will handle all the cases quite well.
