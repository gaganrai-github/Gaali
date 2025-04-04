import random
import keyboard
import time


msg = []
print("============================================= WELCOME =============================================")
print("================================ This bot are created by Gagan Rai ================================")


nm = int(input("Enter number of messages you want to send : "))

for i in range(nm):
    if i == 0:
        continue
    else:
        a = input(f"Write {i} messages : ")
        msg.append(a)

print(f"your meassage is {msg}")
n = int(input("Enter nunber of repetitions of messages: "))

print("#####################    WARNING : Now open your messenger in 10 seconds   #####################")

time.sleep(15)

for _ in range(n):
    random_message = random.choice(msg)
    # keyboard.write(name + " " + random_message)
    keyboard.write(random_message)
    time.sleep(0.2)
    keyboard.press("enter")
    time.sleep(0.3)

##############################################################################################

