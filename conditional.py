# firsy type: simple if

try:
    num = input("give me a number pls")
    num = int(num)
    #check if number is odd
    if num % 2 ==1:
        print("odd number:", num)
    else:
        print("even number:", num)
except ValueError:
    print("that is not a number")

# third option, complex if
a = 10
b = 20
if a>b:
    print(a, "is greater than", b)
elif a==b:
    print(a, "is greater than", b)
else:
    print(a, "is less than", b)

money= 10
if money>1000000000:
    print("billionaire")
elif money > 100000000:
    print("multi millionaire")
elif money > 800000:
    print("almost but not quite millionaire")
elif money > 100000:
    print("six figure club")
elif money > 10000:
    print("technically not poor")
else:
    print("sorry, but you are poor")
