import math
n=int(input("Number of teams\n"))
top_three_ordered=1/(n*(n-1)*(n-2))
top_three_unordered=math.factorial(3)*top_three_ordered
print(f"probability that A, B and C finish first, second and third,respectively {top_three_ordered}.")
print(f"probability that A, B and C are first three to finish (in any order) {top_three_unordered}.")