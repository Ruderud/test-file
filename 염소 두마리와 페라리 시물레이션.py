#테스트용
print("="*50)


import time
start = time.time()
import random

count = 0
win = 0
while count <10000000:
    count+=1
    gacha = ['염소','염소','페라리 911']
    num = [0,1,2]                           #0,1,2중, 처음으로 선택할 숫자를 무작위로 출력

    del num[random.choice(num)]             #num=[0,1,2] 중에서 하나를 처음선택한 숫자를 제외시킴

    for i in num:                           #남은 num중에서 앞에서부터 하나씩 가져옴
        if gacha[i] != '염소':               #만일 가져온 숫자에 해당하는 문뒤에 염소가 없을경우 다음번호를 가져옴.
            continue
        else:                               #(나머지경우)가져온 숫자의 문뒤에 염소가 있으며, 나머지 하나의 문뒤에 염소가 없을때,
            break                           #해당 가져온 숫자 i에서 종료.

    num.remove(i)
    if gacha[num[0]] == '페라리 911':
        win+=1

print('당첨확률:',win/count*100,'%')

end=time.time()
print('걸린시간:',end-start)

'''
import random

count = 0
win = 0
while count <30:
    count+=1
    print('%d번째 실험입니다.'%count)
    gacha = ['염소','염소','페라리 911']
    random.shuffle(gacha)                   #gacha내의 배열을 랜덤으로 바꿈 (편의상 리스트의 위치에따라 0,1,2번째로 지정)

    num = [0,1,2]
    first_pick = random.choice(num)         #0,1,2중, 처음으로 선택할 숫자를 무작위로 출력

    print('처음 선택한 문의 번호는 %d입니다'%first_pick)

    del num[first_pick]                     #num=[0,1,2] 중에서 하나를 처음선택한 숫자를 제외시킴

    for i in num:                           #남은 num중에서 앞에서부터 하나씩 가져옴
        if gacha[i] != '염소':               #만일 가져온 숫자에 해당하는 문뒤에 염소가 없을경우 다음번호를 가져옴.
            continue
        elif gacha[i] == gacha[num[-1]]:    #만일 가져온 숫자에 해당하는 문뒤에 염소가 있고, 선택하지 않은 또 다른 문에도 염소가있을경우,
            i=random.choice(num)            #둘중 하나의 문의 숫자를 무작위로 추출하고 가져오는것을 종료
            break
        else:                               #(나머지경우)가져온 숫자의 문뒤에 염소가 있으며, 나머지 하나의 문뒤에 염소가 없을때,
            break                           #해당 가져온 숫자 i에서 종료.

    print("%d번에 염소가 있습니다."%i)
    num.remove(i)
    print('선택지를 %d로 바꿨습니다.'%num[0])

    print('최종결과는',gacha[num[0]],'입니다.')
    if gacha[num[0]] == '페라리 911':
        win+=1

print('당첨확률:',win/count*100,'%')
'''

print("="*50)