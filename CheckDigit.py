import sys

def intSplitEmu(n):
    x = n//10
    y = n%10
    return x + y

def calc(length, char):
    evens = 0
    odds = 0
    flag = True
    for i in range(length):
        if flag:
            evens += intSplitEmu(int(char[i])*2)
        else:
            odds += int(char[i])
        flag = not flag       
    return evens+odds
    
def check(total):
    if total/10 is not 0:
        z = total%10
        digit = 10-z
    return digit

##########   
print("モード選択。1.チェックデジットをつくる。2.チェックデジットの評価")
mode = input()
if mode is not "1" and mode is not "2":
    sys.exit()

print("数値を入力")
num = input() #適当な数字
char = list(num)

if mode == "1":
    print("digit:", check(calc(len(char), char)))
elif mode == "2":
    if int(char[len(char)-1]) == check(calc(len(char)-1, char)):
        print("OK.")
    else:
        print("Failure.")

