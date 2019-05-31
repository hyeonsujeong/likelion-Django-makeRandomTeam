from django.shortcuts import render, redirect
from .models import MakeTeam
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    logs = MakeTeam.objects
    return render(request, 'about.html', {'logs' : logs})

def create(request):
    team = MakeTeam()
    team.date = request.GET['date']
    team.week = request.GET['week']
    groups = createTeam(origin)
    team.team1 = groups[0]
    team.team2 = groups[1]
    team.team3 = groups[2]
    team.team4 = groups[3]
    team.team5 = groups[4]
    team.save()
    return render(request, 'new.html', {'team' : team})

def new(request):
    return render(request, 'new.html')

origin = ['도형', '지윤', '슬옹', '정규', '성학', '세아', '태원',
'현수', '성필', '민정', '기려', '시현', '지영', '혜선','시은']

backUpOrigin = ['도형', '지윤', '슬옹', '정규', '성학', '세아', '태원',
'현수', '성필', '민정', '기려', '시현', '지영', '혜선','시은']

numOfGroup = 5
countNum = {}

def teamCount(origin, groups):
    whichTeam = {}              #몇번 팀에 들어있는지 저장하는 변수
    for teamNumber in range(len(groups)):   #teamNumber - groups 안에서 몇번째 인덱스에 있는 팀인지
        for member in origin:
            if member in groups[teamNumber]:
                whichTeam[member] = teamNumber
    sameTeam = set()        #같이 팀이 된 사람끼리 짝지어서 저장
    for member1 in origin:
        for member2 in origin:
            if member1==member2:            #member1과 memeber2가 같은 사람이면 패쓰
                pass
            else:
                if whichTeam[member1] == whichTeam[member2]:        #2whichTeam에 저장된 value가 같으면 같은팀이므로 짝지어서 정렬 후 합쳐서 이름 저장
                    team=[member1,member2]
                    team.sort()
                    sameTeam.add(''.join(team))

    global countNum #몇번 만났는지 저장하는 딕셔너리

    for couples in sameTeam:                    #couples - 같은 팀이 된 짝(ex_ 성학정규, 도형슬옹)
        if couples in countNum:                 #딕셔너리에 이미 추가된 경우
            countNum[couples] = countNum[couples] + 1   #valuse에 1 추가
        else:
            countNum[couples] = 1

    return countNum

def randomOrigin(origin):
    random.shuffle(origin)

def divGroup(origin, num):
    groups=[]
    for i in range(5):
        group = origin[i*3:i*3+3]
        groups.append(group)
    return groups

def createTeam(origin):
    randomOrigin(origin)
    global countNum
    groups = divGroup(origin, 5)
    whichTeam = {}
  
    for teamNumber in range(len(groups)):   #teamNumber - groups 안에서 몇번째 인덱스에 있는 팀인지
        for member in origin:
            if member in groups[teamNumber]:
                whichTeam[member] = teamNumber
              
    sameTeam = set()        #같이 팀이 된 사람끼리 짝지어서 저장
    for member1 in origin:
        for member2 in origin:
            if member1==member2:            #member1과 memeber2가 같은 사람이면 패쓰
                pass
            else:
                if whichTeam[member1] == whichTeam[member2]:        #1whichTeam에 저장된 value가 같으면 같은팀이므로 짝지어서 정렬 후 합쳐서 이름 저장
                    team=[member1,member2]
                    team.sort()
                    sameTeam.add(''.join(team))

    for couples in sameTeam:
        if (couples not in countNum) or (countNum[couples] < 2):
            breakPoint=1            #breakPoint는 Main함수를 종료시킬지 재귀로 들어갈지 결정하는 변수
        else:
            breakPoint=2
            break
    if breakPoint==1:
        countNum = teamCount(origin, groups)
        return groups
    else:
        return createTeam(origin)