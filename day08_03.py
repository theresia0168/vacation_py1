#4학기
#1학기 3과목 시험
#2학기 2과목 시험
#3학기 4과목 시험
#4학기 1과목 시험

score=[]

score.append([])
score[0].append(4.3)
score[0].append(3.5)
score[0].append(3.7)

score.append([])
score[1].append(2.8)
score[1].append(4.3)

score.append([])
score[2].append(3.1)
score[2].append(4.1)
score[2].append(4.2)
score[2].append(3.9)

score.append([])
score[3].append(4.1)

print(score)

sum = 0
for i in score:
    for j in i:
        sum+=j

