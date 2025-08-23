import random
no=int(input("no.of team names"))
teams=[]
for i in range(no):
    d=input(" no.of teams:")
    teams.append(d)
meet=int(input("no.of meetings btwn two matches"))
matches=[]
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(meet):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print(f"matches{i+1} : {matches[i][0]} vs {matches[i][1]}")

