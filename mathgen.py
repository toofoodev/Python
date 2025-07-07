# Math Generator | 110 Lines
# Made by Wes
# If you edit or share this script, please give credits!
# For more scripts, go to: https://github.com/toofoodev/Python

import random

elist = list(range(1, 25))
nlist = list(range(1, 50))
hlist = list(range(1, 100))

elist2 = list(range(1, 20))
nlist2 = list(range(1, 35))
hlist2 = list(range(1, 65))

score = 0
diff = "N/A"
spacer = "---------------"

def main():
    # DiffHandle
    global diff
    if diff == "easy":
        mode = "Easy"
        mathmode = elist
        mathmode2 = elist2
    elif diff == "normal":
        mode = "Normal"
        mathmode = nlist
        mathmode2 = nlist2
    elif diff == "hard":
        mode = "Hard"
        mathmode = hlist
        mathmode2 = hlist2
    
    global score
    print("\n")
    print(f"Mode: {mode}")
    print(f"Score: {score}")
    print("Select your Math!")
    print("Add - Subtract - Multiply - Divide - Random")
    math = input()
    print("\n")
    if math == "add":
        num1 = random.choice(mathmode)
        num2 = random.choice(mathmode)
        ans = num1 + num2
        print(f"{num1} + {num2}= ")
        usans = int(input())
        if usans == ans:
            print("Nice one! +1 Score")
            score += 1
            easy()
        else:
            print("Maybe next time.")
            easy()
    elif math == "subtract":
        num1 = random.choice(mathmode)
        num2 = random.choice(mathmode)
        while num2 > num1:
            num2 = random.choice(mathmode)
        ans = num1 - num2
        print(f"{num1} - {num2}= ")
        usans = int(input())
        if usans == ans:
            print("Nice one! +1 Score")
            score += 1
            easy()
        else:
            print("Maybe next time! I beleve in you!")
            easy()
    elif math == "multiply":
        num1 = random.choice(mathmode2)
        num2 = random.choice(mathmode2)
        ans = num1 * num2
        print(f"{num1} x {num2}= ")
        usans = int(input())
        if usans == ans:
            print("Nice one! +1 Score")
            score += 1
            easy()
        else:
            print("Maybe next time! I beleve in you!")
            easy()
    elif math == "divide":
        ans = random.choice(mathmode2)
        num2 = random.choice(mathmode2)
        num1 = num2 * ans
        print(f"{num1} x {num2}= ")
        usans = int(input())
        if usans == ans:
            print("Nice one! +1 Score")
            score += 1
            easy()
        else:
            print("Maybe next time! I beleve in you!")
            easy()
    
def home():
    print("Math")
    print("Generator")
    print(spacer)
    print("Made by Wes")
    print("\n")
    print("Diffuculties: Easy, Normal, Hard")
    udiff = input()
    global diff
    diff = f"{udiff}"
    main()
home()
