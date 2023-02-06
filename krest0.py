import os

clear = lambda: os.system('cls')

def Win(setka,hod):

    Render (setka,'')
    print('\033[92mпобеда за {}\033[00m'.format(hod))
    print()
    print("\033[33menter for restart\033[00m")

    if input("\033[31mq for quit\033[00m\n\n") == 'q':
        quit()

    Start()

def CheckWin (setka,hod,count):


    for i in range (0,9,3):
        if (len(set(setka[i:(i+3)]))==1):
            setka[i:(i+3)] = ["\033[92m"+ hod +"\033[36m"]*3
            Win(setka,hod)

    for i in range(3):
        if (len(set(setka[i::3]))==1):
            setka[i::3] = ["\033[92m"+ hod +"\033[36m"]*3
            Win(setka,hod)

    if len(set(setka[2:7:2])) == 1:
            setka[2:7:2] = ["\033[92m"+ hod +"\033[36m"]*3
            Win(setka,hod)


    if len(set(setka[::4])) == 1:
            setka[::4] = ["\033[92m"+ hod +"\033[36m"]*3
            Win(setka,hod)

    if count == 9:
        print()
        print('Ничья')
        print()
        input("enter for restart")

        Start()

    return

def Render (setka,hod):

    clear()
    print("\033[34mКрестики нолики ")
    print("\033[36m")



    for i,val in enumerate(setka):
        if (i+1)%3:
            print(val,end=' ')
        else:
            print(val)

    print("\033[00m")

    if hod:
        print("ход за {} \n".format(hod))

    return

def Vvod (setka,hod):

    while True:
        
        try:
            num = int(input())
        except ValueError as e:
            Render (setka,hod) 
            print("Введите число от 1 до 9")
            continue

        if num > 9 or num <1:
            Render (setka,hod) 
            print("Введите число от 1 до 9")
            continue

        if not str(setka[num-1]).isdigit():
            Render (setka,hod) 
            print("Введите пустую клетку")
            continue

        return num

def Start ():
    
    setka, hod = list(range(1,10)), "X"

    count = 0

    while True:

        Render (setka,hod)

        num = Vvod(setka,hod)

        setka[num-1] = hod

        count+=1

        CheckWin(setka,hod,count)

        hod = 'X' if hod == 'O' else "O"

Start()