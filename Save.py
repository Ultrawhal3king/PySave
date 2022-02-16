import threading
import sys
import random

def readsave():
        ReadSave = open("SaveFile.txt", "r")
        ReadSave = ReadSave.read()
        return ReadSave

def atf(wora,thing):
    WriteSave = open("SaveFile.txt", wora)
    WriteSave.write(thing)

while True:
    
    msg = input("> ")
    msglist = msg.split()
    savecon = readsave()
    savelist = savecon.split()
    usrn = "Jack"

    def income(money):
        if usrn in savelist:
            updatesave = ""
            coin = savelist.index(usrn) + 1
            coin = int(savelist[coin])
            coin+=money
            savelist[savelist.index(usrn) + 1] = str(coin) 
            for word in savelist:
                updatesave+=word + " "
                atf("w",updatesave)

    
    def work():
        com = ""
        if msg == "stopjob":
            com = msg
        wrk = threading.Timer(1.0, work)
        wrk.start()
        if com == "stopjob":
            com = ""
            wrk.cancel()
        income(1)

    if msg.startswith("signup"):
        if usrn not in savelist:
            atf("a",f"{usrn} 0 unemployed" )
        else:
            print(f"{usrn} you have already signed up")
            
    if msg == "beg":
        moneygiven = random.randint(1,15)
        income(moneygiven)
        namestxt = open("names.txt", "r")
        namestxt = namestxt.read().split()
        print(f"{namestxt[random.randint(0,len(namestxt)-1)]} gave you ${moneygiven} dollars")
    
    if msg == "startjob":
        work()
            
    if msg == "close()":
        sys.exit("Closed")