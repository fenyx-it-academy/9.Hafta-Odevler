from functools import reduce
print("********** Score Calculation **********")
monday = [ { "name": 'To study functions', "duration": 180},{ "name": 'To try to solve the samples', "duration": 120},
           { "name": 'To check homework', "duration": 20},{ "name": 'To congratulate each other’s bairam', "duration": 200} ]

tuesday = [ { "name": 'Preparation for next week', "duration": 240}, { "name": 'To continue to solve the samples', "duration": 180},
            { "name": 'Coffee break', "duration": 10, }, { "name": 'To read books', "duration": 200, }, { "name": 'To do sport', "duration": 40, } ]
minute=[]
for i in range(0,len(monday)):
    minute.append(monday[i]["duration"])
for i in range(0,len(tuesday)):
    minute.append(tuesday[i]["duration"])
hours = list(map(lambda x: x/60,minute))
hours_2= list(filter(lambda x: x if x>=2 else False,hours))
score=list(map(lambda x: x*20,hours_2))
print("Your hourly scores are:",*score)
score_round=[]
for i in score:
    score_round.append(round(i))
print("Your rounded hourly scores are:",*score_round)
print("Your sCore is:",reduce(lambda x,y:x+y,score_round))
#Nested form of functions:
print("Your sCore is:",(reduce(lambda x,y:x+y,map(lambda x: round(x),map(lambda x: x*20,filter(lambda x: x if x>=2 else False,map(lambda x: x/60,minute)))))))

