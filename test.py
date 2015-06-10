from client import getmongo

getmongo = getmongo()
good = getmongo.getValue()

for line in good:
    print good[line]
