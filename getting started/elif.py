print("this program cheacks")

salary=int(input("how much is your salaruy\n"))
if (salary>1000):
    amount=200
    print("you can get loan" ,amount,"monthly")
elif(500<salary<1000):
    amount=500
    print("you can get loan with higher",amount,"monthly")
else:
       print("sorry")
