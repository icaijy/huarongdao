import os
import random
import time

a = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13," ",14,15]
]
finish = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15," "]
]

def shuffle(p):
    for x in range(p):
        blank = search(" ")
        x,y = blank[0],blank[1]
        c = []
        if (x - 1) >= 0:
            c.append("a[x-1][y],a[x][y]=a[x][y],a[x-1][y]")
        if (x + 1) <= 3:
            c.append("a[x+1][y],a[x][y]=a[x][y],a[x+1][y]")
        if (y - 1) >= 0:
            c.append("a[x][y-1],a[x][y]=a[x][y],a[x][y-1]")
        if (y + 1) <= 3:
            c.append("a[x][y+1],a[x][y]=a[x][y],a[x][y+1]")
        exec(random.choice(c))

def printBoard():
    for x in a:
        for j in x:
            if len(str(j))==2:
                print(j,end=" ")
            else:
                print(j,end="  ")
        print()
def search(n):
    for x in range(4):
        for y in range(4):
            if a[x][y]==n:
                return (x,y)

def swap(blank,num):
    a[blank[0]][blank[1]] = a[num[0]][num[1]]
    a[num[0]][num[1]] = " "


def swapable(num):
    x,y=num[0],num[1]
    if a[x-1][y]==" " and (x-1)>=0:
        return True
    if (x+1)<=3 and a[x+1][y] == " ":
        return True
    if a[x][y-1]==" " and (y-1)>=0:
        return True
    if (y+1)<=3 and a[x][y+1] == " ":
        return True
    else:
        return False
shuffle(1000)
printBoard()
n = search(int(input()))
start = time.time()
os.system("cls")
try:
    if swapable(n):
        swap(search(" "),n)
    else:
        print("Can't swap!无法交换！")
except:
    print("Wrong input!输入错误！")
if a==finish:
    t2 = time.time()
    print("You win!你赢了！")
    print("你花了" + str(round(t2-start)) + "秒")
    exit(0)

def main():
    while True:
        printBoard()
        n = search(int(input()))
        os.system("cls")
        try:
            if swapable(n):
                swap(search(" "),n)
            else:
                print("Can't swap!无法交换！")
        except:
            print("Wrong input!输入错误！")
        if a==finish:
            t2 = time.time()
            print("You win!你赢了！")
            print("你花了"+str(round(t2-start))+"秒")
            break

main()