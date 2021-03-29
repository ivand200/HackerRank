# The included code stub will read an integer, n, from STDIN.
# Without using any string methods, try to print the following: 123...n
# Note that "..." represents the consecutive values in between.
# Example n = 5
# Print the string 12345.

n = int(input())
    n = n + 1
    lst = list()
    for i in range(0, n):
        i = str(i)
        lst.append(i)

    n = ""
    str_join = n.join(lst)
    num = int(str_join)
    print(num)
# print(*range(1, int(input())+1), sep='')


# Let's learn about list comprehensions! You are given three integers x,y and
# representing the dimensions of a cuboid along with an integer .
# Print a list of all possible coordinates given by (i,j,k) on a 3D grid
# where the sum of i+j+k is not equal to n.Please use list comprehensions rather
# than multiple loops, as a learning exercise.
x = int(input())
y = int(input())
z = int(input())
n = int(input())

print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if     a + b + c != n ])

# Given the participants' score sheet for your University Sports Day,
# you are required to find the runner-up score. You are given  scores.
# Store them in a list and find the score of the runner-up.
x = [2, 3, 6, 6, 5]  # [6, 6, 5, 3, 2]
n = int(input())
    arr = map(int, input().split())
    lst = list(arr)
    lst.sort(reverse=True)
    maximum = max(lst)
    round = list()
    for num in lst:
        if num == maximum: continue
        else:
            round.append(num)
    print(round[0])

x = [2, 3, 6, 6, 5]  # [6, 6, 5, 3, 2]
run = 5
x = sorted(x, reverse=True)
m = max(x)
lst = list()
run_up = None
for num in x:
    if num == run:
        run_up = num
    else:
        continue
print(run_up)
# Ver2
i = int(input())
lis = list(map(int,raw_input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print max(lis)
