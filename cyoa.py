def farming():
  print("John starts a farm with what little money he had left. You soon begin to pick up as you find a cheap new fertilizer that increases your crop growth by over 1000%. John is finally happy")

def beggar():
  print("John is forced to become a beggar.")

def police():
  print("The police catch John stealing the money. It turns out that John was hallucinating and the money was candy, and the bank was a baby. John is sentenced to life without parole for stealing candy from a baby. That monster.")
  

print("John is unhappy with his life, He'd tell you himself. In fact, he will. 'I dont like my life. Im unhappy with my job, and lets be honest, my apartment is all but ideal. I live in a small two bedroom apartment with my cousin. I work a dead end job serving corporations that I hate, and doing something I hate even more. Staring at a screen'")
choice = input("Im unhappy, do I just quit, or do I walk out? - Quit, or Walk Out. - ")
if choice == 'Quit':
  print("You know what you're right. I should just quit this dead end job. Im walking to the CEO's office right now to tell him first hand")
  print("That, -that, that ugh. He didn't even say anything he just nodded. I really could've done with anything but a nod.")
  x = input("Now I need to make money somehow. I should really stop acting solely on impulse. Should I call up any friends and see if they have jobs available or should I take what money I do have and start a farm? Jobs or Farm? - ")
  if x == "Farm":
      farming()
  if x == "Jobs":
      print("It turns out that my boss slandered me to every other boss in town and I was denied every job I tried")
      beggar()
if choice == "Walk Out":
  print("You're right. John said as he stormed out of the front door of the building.")
  print("He soon calls you to ask an important question")
  x = input("What do I do for money now? Do I rob a bank, or should I take my money and try to start a farm? Bank or Farm? - ")
  if x == 'Bank':
    police()
  if x == 'Farm':
    print("While John's farm initially takes off, it soon fails after a scandal with his fertilizing practice")
    beggar()
