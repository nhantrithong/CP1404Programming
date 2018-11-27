def main():
    list = []
    import random
    pick_num = int(input("How many quick picks would you like to generate?"))
    for i in range(pick_num):
        print("")
        for randnum in range(6):
            x=random.randint(1,46)
            if x not in list:
                list.append(x)
            else:
                randnum-=1
            list.sort()
        for num in list:
            print (num, end=' ')
        list=[]





main()
