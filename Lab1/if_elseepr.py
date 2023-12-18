def check_username(username):
    if(len(username)<3):
        print("Invalid Username please enter valid !!")
    elif(len(username)>13):
        print("Username must be at most 13 characters..")
    else:
        print("Valid Name")
        
name=input("Enter name:")
check_username(name)



def diff(a,b):
    z=a-b
    return z
print(diff(5,3))