def do_twice(f, num):
    f(num)
    f(num)


def print_spam():
    print('spam')

def print_twice(bruce):
    print(bruce)
    print(bruce)

#do_twice(print_spam)

do_twice(print_twice, 'spam')
