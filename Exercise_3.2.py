#Kevin Lee
#assign 1-1

#example from textbook
def do_twice(f, num):
    f(num)
    f(num)

#example from textbook
def print_spam():
    print('spam')

#print twice question
def print_twice(bruce):
    print(bruce)
    print(bruce)

#input string, and put it into pring_twice function
#as result, total output 4.
do_twice(print_twice, 'spam')
