import random
import time

q = '''
  O
 /|\ 
 / \ 
       '''


w = '''
  O
 /|\ 
 / \ 

============= 
       '''

e = '''
   
            ||
            ||
      O     ||
     /|\    ||
     / \    ||
            ||            
================= 
       '''

r = '''
        \   ||
         \  ||
          \ ||
      O     ||
     /|\    ||
     / \    ||
            ||            
================= 
       '''

t = '''
+===========++
        \   ||
         \  ||
          \ ||
      O     ||
     /|\    ||
     / \    ||
            ||
            ||            
================= 
       '''

y = '''
+===========++
      | \   ||
      |  \  ||
      |   \ ||
      O     ||
     /|\    ||
     / \    ||
            ||
            ||            
================= 
       '''

list_of_words = ["apple","orange","watermelon","pig","dog","wolf","dragon","blackpanther","rampage","stampede",
                 "crocodile","bull","biriyani","kebab"]

x = random.choice(list_of_words)
def hint():
    if x == "apple" or x == "orange" or x == "watermelon":
        print("It is a fruit")

    elif x == "pig" or x == "dog" or x == "wolf" or x == "dragon" or x == "blackpanther" or x == "crocodile" or x == "bull":
        print("its an animal")
    elif x == "biriyani" or x == "kebab":
        print("it is a food")
    elif x == "rampage" or x == "stampede":
        print("word used instead of sudden panicked running")


print("It is a", len(x), "letters word.")
list1 = []
list2 = []

for i in range(len(x)):
    list1.append("_")

for a in x:
    list2.append(a)
count = 0
i = 0
while i < len(x)+6:
    print(list1)
    time.sleep(2)
    guess = input("type me a letter: ").lower()
    for letter in range(len(x)):
        position = x[letter]
        if position == guess:
            list1[letter] = position
    if guess not in list2:
        print("Wrong letter")
        count += 1
        if count == 1:
            print(q)
        elif count == 2:
            print(w)
        elif count == 3:
            print(e)
            do = input("Do you want a hint(y/n): ").lower()
            time.sleep(2)
            if do == "y":
                hint()
        elif count == 4:
            print(r)
        elif count == 5:
            print(t)
        elif count == 6:
            print(y)
            print("You are death")
            break
    i += 1

    if "_" not in list1:
        print("you have found the word")
        print(x)
        break


if "_" in list1:
    print("game over you have not found the word")
    print("the word was ", x)
