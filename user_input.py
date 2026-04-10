#input() = A function that prompts the user to enter data
#      Returns the entered data as string

name = input("What is your name?: ")                    #The input() will return some data as a string
age = input("What is your age?: ")
age=int(age)

age =+ age + 1                                          #make sure to use '=+' and not '+='
                                                        #Because =+ means to increment the var by adding +1 to it i.e. x =+ x+1
                                                        #and += means x+x+1

                                                        #If we don't typecast age as int(age) then it will show error
                                                        #To avoid error we will first typecast age which is string into integer
                                                        #i.e. age = int(age)


print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old.")


# instead of typecasting string into integer using extra line we can directly type cast it into integer at beginning
# while taking user input i.e. age = int(name("How old are you?: ")
# instead of taking user input age = name (How old are you?: ") and then typecasting string into integer
# by writing age = int(age)

age= int(input("What is your age?: "))
age =+ age+1


print(f"You are {age} years old.")


