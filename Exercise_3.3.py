#Kevin Lee
#Assin 1

#examples from text  book
# print('+','-','-','-','-','+','-','-','-','-','+')
# print('+', end=' ')
# print('-')
# print('|', ' ', ' ', ' ',' ', '|', ' ', ' ', ' ',' ' ,'|')

#creating 2x2
#first create each side by string of charc
string1 = "+----+----+"
string2 ="|    |    |"
# print(string1)

#create a function 2 different aruments as inputs
#cprint as much as problem asks to
def easy(arg1, arg2):
    print(arg1)
    print(arg2)
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )
    print(arg2)
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )

easy(string1,string2)

#double the length from previous stringg
#since it is being called later, overwirte can be performed
string1 = "+----+----+----+----+"
string2 ="|    |    |    |    |"
def easy2(arg1, arg2):
    print( arg1 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg2 )
    print( arg1 )

easy2( string1 , string2 )