'''
prime 
'''
# 10 => 1 , 2 , 5 , 10
# 7 ==> 1 ,7 
# 5 ==> 1 ,5 

# num =int(input("Enter your numebr :- "))
# fact = []
# for i in range(1,num+1):
#     if num%i==0:
#         fact.append(i)
# print(fact)
# if len(fact) == 2:
#     print("Prime")
# else:
#     print("Composite")


# l1 = ['python','java','c','c++','python','php','html','python']   #find all index containing python
# # print(l1.index('python'))
# l2 = []
# for i in range(len(l1)):
#     if l1[i] == 'python':
#         l2.append(i)

# print(l2)

# 0 , 1 ,2 
# for i in l1:

'''      01234   
0        *****
1        *****
2        *****
3        *****
'''

# for i in range(0,4):# 4 
#     for j in range(0,5): # 5 ==> 4 * 5 ==> 20 
#         print("*",end="")
#     print("")



'''  01234
0    *
1    **
2    ***
3    ****
4    *****

j ==> i 

****
***
**
*
'''

# for i in range(0,5):
#     # 0 1 
#     for j in range(0,i+1):
#         # 0
#         # 01
#         # 012
#         # 0123
#         # 01234
#         print("*",end="")
#     print("")



# for i in range(5,-1,-1):
#     for j in range(0,i+1):
#         print("*",end="")
#     print("")

# for i in range(10,-1,-1):
#     print(i)

'''
    *
   **
  ***
 ****
*****  
'''

# 3 >> rows , col , space

for i in range(0,5):
    # 0 1
    for k in range(0,5-i):
        
        print(" ",end="")
    for j in range(0,i+1):
        print("*",end="")
    prixz