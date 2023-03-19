import time
from random import randint
hb = input("Enter the name of birthday boy or girl: ")
for i in range(1,85):
    print('')
space = ''
for i in range(1,1000):
    count = randint(1,100)
    while(count>0):
        space += ' '
        count -= 1
    if(i%10==0):
        print(space + '🎉Happy Birthday {}🎉!'.format(hb))
    elif(i%9==0):
        print(space + "🍰")
    elif(i%8==0):
        print(space + "❤")
    elif(i%7==0):
        print(space + "😍")
    elif(i%5==0):
        print(space + "🎉")
    elif(i%6==0):
        print(space + "Happy vala birthday {}💕!".format(hb))
    else:
        print(space + "🥰")
    space = ' '
    time.sleep(0.2)