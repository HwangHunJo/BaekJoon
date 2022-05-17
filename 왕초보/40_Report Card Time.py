n = int(input())

for i in range(n):
    name, grade = map(str, input().split())
    grade = int(grade)
    if(grade >= 97):
        grade = "A+"
    elif(grade >= 90):
        grade = "A"
    elif(grade >= 87):
        grade = "B+"
    elif(grade >= 80):
        grade = "B"
    elif(grade >= 77):
        grade = "C+"
    elif(grade >= 70):
        grade = "C"
    elif(grade >= 67):
        grade = "D+"
    elif(grade >= 60):
        grade = "D"
    else:
        grade = "F"
    print(name, grade)