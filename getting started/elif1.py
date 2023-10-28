print("this is a elif checks program")

price=120
times=int(input("how many times did you go to this place\n"))
if(times==3):
    price=120-30
    print("your total discount will be$",price)
elif(times==4):
    price=120-50
    print("your total discount will be $",price)
elif(times==5):
    price=120-60
    print("your total discount will be $",price)
elif(times>=6):
     price=120-70
     print("your total discount will be $",price)
else:
    print("your total discount will be $",price,"and you are not eligble")
