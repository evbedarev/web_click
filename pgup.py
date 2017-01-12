import win32com.client as comclt
import random
import time
import move_mouse

wsh= comclt.Dispatch("WScript.Shell")# send the keys you want

def randC():
    rand = random.randint(7,15)+random.random()+random.random()+random.random()
    print(rand)
    return rand
    
def main():
    ran = random.randint(2,10)
    for i in range(1,ran):
        if random.randint(1,10)%2 > 0:
            wsh.SendKeys("{PGUP}")
            move_mouse.main()
            print("page up") 
            # time.sleep(2)
            time.sleep(randC())
        else:
            wsh.SendKeys("{PGDN}")
            print("page down")
            move_mouse.main()
            time.sleep(randC())
            # time.sleep(2)
    return True
