def factorial(number):
    fact = 1
    for i in range(abs(number)):
      fact += (fact * i)
    if number < 0 :
      fact = -fact
    return fact

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320