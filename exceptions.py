prompt = "What is your name?"
name = input(prompt)
# If name == "bob" :
#   print("FU bob)
# else:
#   print("nice to meet you,", name)

try:
    promt2 = "how old are you," + name + "?"
    age= input(promt2)
    # convert to in
    age= int(age)
    print("you were born in,", 2025 - age)
   # primt("nice knowing you")
   # a = 7/0
except ValueError:
    print("sorry,", name, "but that is not a number")
except NameError:
    print("sorry that is not a valid name for print")
except:
    print("all other exceptions go here!")
else:
    print("thank you for playing fair and square")
finally:
    print("this is always at the end no matter what")
