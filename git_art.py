import os
from pprint import pprint
import itertools

# Number of days you want to make commits
# for i in range(1, 365*2 + 1):
for i in range(1, 30+1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('bot.txt', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add bot.txt')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "github Art"')

## push the commit to github
# os.system('git push -u origin master')


######
# Pprint canvas built
# canvas_built = [["0" for i in range(7)] for n in range(25) ]
# pprint(canvas_built)
canvas = [
 ['B', '0', 'x', '0', '0', '0', 'A'],
 ['D', '0', 'x', 'x', '0', '0', 'C'],
 ['0', '0', 'x', '0', '0', '0', '0'],
 ['0', '0', 'x', '0', 'x', '0', '0'],
 ['0', '0', 'x', '0', '0', 'x', '0'],
 ['x', 'x', 'x', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', 'x'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
 ['0', '0', '0', 'x', '0', '0', '0'],
 ['0', '0', '0', 'x', '0', '0', '0'],
 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['x', 'x', 'x', 'x', 'x', '0', 'x'],
 ['x', 'x', 'x', 'x', 'x', '0', 'x'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
 ['0', '0', '0', 'x', '0', '0', 'x'],
 ['0', '0', 'x', 'x', '0', '0', 'x'],
 ['0', 'x', '0', 'x', '0', '0', 'x'],
 ['x', '0', '0', 'x', 'x', 'x', 'x'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
 ['x', 'x', 'x', 'x', 'x', 'x', 'x'],
 ['x', '0', '0', 'x', '0', '0', 'x'],
 ['x', '0', '0', 'x', '0', '0', 'x'],
 ['x', '0', '0', '0', '0', '0', 'x'],
 ['x', '0', '0', '0', '0', '0', 'x'],
 ['0', '0', '0', '0', '0', '0', '0'],
 ['G', '0', '0', '0', '0', '0', 'F']]
pprint(canvas)

# The idea is as follow:
# If the element in the nested list is == 'x', git commit.
# Elif the element is != 'x', do nothing.

# However It shall all be in reverse.

# A typical Github contribution tab canvas is as follow:

#      Jan   Feb   Mar   Apr   May   Jun   Jul   Aug   Sep   Oct   Nov   Dec
# Sun
# Mon
# Tue
# Wed
# Thu
# Fri
# Sat

# The way my basic auto commit script goes backward Today -1, d -2, -3 etc.

# Need to do:
# Flatten my nested listings in a 1D list, and reverse it.
# Get Index 0 of that flatten-reverse-list correspond to a specific Saturday.
# Then decrement from there at each iteration of git commit script. (If n == 0 do nothing, else git commit "blabla".)

# 1. Convert 2D Canvas into useable 1D List

for n in canvas:
    n.reverse()
canvas_flat = list(itertools.chain(*canvas))
print(canvas_flat)


# 2. When is the latest Saturday?


# 3. Start iteration through 1D canvas


# 4. If n == "x" then commit, else do nothing.
