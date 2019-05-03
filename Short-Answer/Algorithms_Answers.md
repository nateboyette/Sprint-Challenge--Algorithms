Add your answers to the Algorithms exercises here.

## Exercise I

a) O(1) - A function with this while loop will only run one time.
b) O(n^2) - For the size of n, the function would have to perform 4 operations before it adds 1 to sum.
c) O(nlogn) - This is a recursive function that will look at each item of n and perform a function on it.

## Exercise II

for i in range(building):
if egg breaks when dropped from building[i]:
Do not go up any further, eggs will break
return f == building[i]

This would be O(n). We would have to go to each floor starting from either the top or bottom. The number of times it takes to figure this out could be at best O(c) and at worst O(n).
