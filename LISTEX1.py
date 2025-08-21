students=["anu","ani","bala","ravi","raju","jack"]
cgpa=[59,66,47,88,78,69]
arrear=[0,1,2,1,0,0]
for i in range(6):
    if arrear[i]==0 and cgpa[i]>60:
        print(students[i])