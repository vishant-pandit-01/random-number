# a=10
# if a<20:
#     print("hello")
# else:
#     print("bye")


                #  nesting
# a=int(input("enter first number:-"))
# b=int(input("enter second number:-"))
# c=int(input("enter third number:-"))

# if a>b:
#     if a>c:
#         print("a is greatest:-")

# elif b>c:
#         print("b is greatest:-")
# else:
#     print("c is greatest:-")
    
                            #    error 
# a=int(input("enter first number:-"))
# b=int(input("enter second number:-"))
# c=int(input("enter third number:-"))
# if a<b:
#     print("a")
# elif b<c:
#     print("b")
# elif c==a:
#     print("c")
# else:
#     print("d")



                #    range
# for i in range(10):
#     print(i)


# sum=0
# for i in range(1,11):
#     sum=sum+i
#     print(sum)


# n= int(input("enter your number"))
# print("table of",n)
# for i in range(1,11):
#     m=n*i
#     print(n,"x",i,"=",m)

            #   error
# a= "anything"
# count=0
# for i in "hello i am learning python":
#     if i==a:
#         count=count+i
# print(count)



# i=2
# while(i<=101):
#     print(i)
#     i+=2



# i=0
# while (i<100):
#    if i==20:
#       continue
#    else:
#       print(i)
#    i=i+1


# i=100
# while (i>=0):
#    if i%2!=0:
#       print(i)
#    i=i-1


'''functions'''  
                         #   take nothing return nothing
# def record():
#     print("enter your name:-")
#     n=input()
#     print("wellcome",n)
# record()

                         #    take somnething return nothing
# def record(n):
#     print(n)

# print("enter your name:-")
# name=input()
# record(name)

                        #    take nothing return something
# def record():
#     print("enter your name:-")
#     n=input()
# record()


# def sum():
#     a=eval(input("enter first number"))
#     b=eval(input("enter second number"))
#     c=a+b
#     print(c)
# sum()


                # take nothing return something
# def add():
#     a= int(input("enter first number:-"))
#     b=int(input("enter second number:-"))
#     c=a+b
#     return c
# x=add()
# print(x)



                #    take something return something
def add(a,b):
    c=a+b
    return c
x=int(input("enter first number"))
y=int(input("enter second number"))
s1=add(x,y)
print(s1)