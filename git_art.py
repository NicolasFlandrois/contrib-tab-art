import os

## Number of days you want to make commits
#for i in range(1, 365*2 + 1):
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
os.system('git push -u origin master')
