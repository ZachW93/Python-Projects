from random import randint

correct = 0
difficulty = input("Enter difficulty BEGINNER, INTERMEDIATE, AND ADVANCED: ").upper() 
num = int(input("Enter The Number of Questions: "))
if difficulty == 'BEGINNER':    
    for i in range(num):
        n1 = randint(1,8)
        n2 = randint(1,8)
        n3 = randint(1, 2)
        if n3 == 1:
            prod = n1 + n2
            ans = input("What's %d plus %d? " %(n1,n2))
            if int(ans) == prod:
                print("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d plus %d? " %(n1,n2))
        elif n3 == 2:
            prod = n1 - n2
            ans = input("What's %d minus %d? " %(n1,n2))
            if int (ans) == prod:
                print ("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d minus %d? " %(n1,n2))

elif difficulty == 'INTERMEDIATE':
    for i in range(num):
        n1 = randint(1,25)
        n2 = randint(1,25)
        n3 = randint(1, 4)
        if n3 == 1:
            prod = n1 + n2
            ans = input("What's %d plus %d? " %(n1,n2))
            if int(ans) == prod:
                print("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d plus %d? " %(n1,n2))
        elif n3 == 2:
            prod = n1 - n2
            ans = input("What's %d minus %d? " %(n1,n2))
            if int (ans) == prod:
                print ("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d minus %d? " %(n1,n2))
        elif n3 == 3:
            prod = n1*n2
            ans = input("What's %d times %d? " %(n1,n2))
            if int(ans) == prod:
                print("That's right -- well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d times %d? " %(n1,n2))
        elif n3 == 4:
            prod = n1/n2
            prod = round(prod, 2)
            ans = input("What's %d divided by %d?(2 decimal places) " %(n1,n2))
            if float(ans) == prod:
                print("That's right -- well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %f.2 \n" %prod)
                ans = input("What's %d divided by %f.2?(2 decimal places) " %(n1,n2))
elif difficulty == 'ADVANCED':
    for i in range(num):
        n1 = randint(1,100)
        n2 = randint(1,100)
        n3 = randint(1, 5)
        n4 = randint(1, 100)
        if n3 == 1:
            prod = n1 + n2 - n4
            ans = input("What's %d plus %d minus %d? " %(n1,n2,n4))
            if int(ans) == prod:
                print("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d plus A%d? minus %d? " %(n1,n2,n4))
        elif n3 == 2:
            prod = n1 - n2 * n4
            ans = input("What's %d minus %d times %d? " %(n1,n2,n4))
            if int (ans) == prod:
                print ("That's right −− well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d minus %d? times %d? " %(n1,n2,n4))
        elif n3 == 3:
            prod = n1 * n2 / n4
            prod = round(prod, 2)
            ans = input("What's %d times %d divided by %d?(2 decimal places) " %(n1,n2,n4))
            if float(ans) == prod:
                print("That's right -- well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %d. \n" %prod)
                ans = input("What's %d times %d divided by %d?(2 decimal places) " %(n1,n2,n4))
                #I finished this part
        elif n3 == 4:
            #I have worked a little bit on this part.
            prod = abs(n1 - n2 / n4)
            prod = round(prod, 2)
            ans = input("What's %d divided by %d?(2 decimal places) " %(n1,n2,))
            if float(ans) == prod:
                print("That's right -- well done. \n")
                correct = correct + 1
            else:
                print("No, I'm afraid the answer is %f.2 \n" %prod)
                ans = input("What's %d divided by %f.2?(2 decimal places) " %(n1,n2))
        #zcw5@nau.edu
        

print("\n I asked you %d questions . You got %d of them right."
% (num , correct))
print("Well done!")
