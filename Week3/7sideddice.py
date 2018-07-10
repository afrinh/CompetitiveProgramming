import random


def rand5():
    return random.randint(1, 5)


def rand7():

    # Implement rand7() using rand5()
   
    r = rand5() + rand5() * 5 - 6
    return (r % 7) + 1 if r < 21 else rand7()

    return 0


print 'Rolling 7-sided die...'
print rand7()