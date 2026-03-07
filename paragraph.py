                   #    for upper and lower
def for_uppercase():
    print("enter your string:-")
    a=input()
    
    if a.isupper():
        print("already in uppercase")
    else:
        u=a.upper()
        print( "change in upper case:-",u)
