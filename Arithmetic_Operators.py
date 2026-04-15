#friends = 0
#friends += 1  (friends+1)
#friends = 4
#friends -= 3  (friends-3)
#friends = 5
#friends *= 3  (friends*3)
#friends = 3
#friends /= 2   (friends/2)
#friends = 5
#friends **= 2      (** = to the power)
#print(friends)



#friends = 10
#remainder = friends % 3  #Modulus operator
#print(remainder)

#Example
Salary = float(input("Enter your Salary: "))
EID_CASH = (0.5)*Salary
print(f"EID_CASH is {EID_CASH}:")
Wife = int(input("Number of wife: "))
Kids = int(input("Enter the number of Kids :"))


Wifes_Eidi = (0.50)*EID_CASH
Eidi_per_head = (0.25)*((EID_CASH - Wifes_Eidi) / Kids)

print(f"Each of my child will get Rs{Eidi_per_head} as Eidi")
print(f"Each of my beloved wife will receive Eidi of Rs{Wifes_Eidi}")

print(f"Eid Mubarak Guys")
