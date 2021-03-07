def mysort(listnum): #
    wordList = []
    ordernum = 1
    while listnum > 0:
        wordList.append(input(f'Enter your {ordernum} word:  '))
        listnum -= 1
        ordernum += 1

    newList = []

    letterList = "H7IJKL6MNOPQRST543210UVWXYZ A9BCD8EFG"
    res = [i for j in letterList for i in j]


    for word in wordList: 
        if len(newList) == 0:  
            newList.append(word)
        else:
            control = 0;  
            for i in range (0,len(newList)):  
                for k,l in zip(word,newList[i]):  
                    if res.index(k) != res.index(l):  
                        if res.index(k) > res.index(l):  
                            break
                        else:
                            newList.insert(i, word)  
                            control = 1  
                            break
                if control == 1:  
                    break
                if i == len(newList)-1: 
                    newList.append(word)

    print(newList)

N = int(input("How many words?: "))

mysort(N)