# Gavin King        11/20/2025
# Lab 9
# This program is a set of tests for the myMath functions.

from myMath import add
from myMath import divide
from myMath import factorial
from myMath import is_prime
from myMath import sum_of_digits
from myMath import gcd
from myMath import fib
from myMath import lcm
from myMath import square_root
from myMath import abs_diff
from myMath import log
from myMath import mod
from myMath import mean
from myMath import median
from myMath import mode
from myMath import celsius_to_fahrenheit
from myMath import fahrenheit_to_celsius
from myMath import inverse
from myMath import triangular_number





def test_add():
    assert add(3, 5) == 8

def test_divide():
    assert divide(2, 4) == 2
    assert divide (4, 64) == 8
    assert divide(0, 4) == 0
    assert divide(4, 0) == ValueError

def test_factorial():
    assert factorial(5) == 120
    assert factorial(-6) == ValueError

def test_is_prime():
   assert is_prime(1) == False
   assert is_prime(36) == True
   assert is_prime(49) == False
   assert is_prime(89) == True

def test_sum_of_digits():
    assert sum_of_digits(136) == 10
    assert sum_of_digits(5) == 5


def test_gcd():
    assert gcd(3,9) == 3
    assert gcd(6,124) == 2

def test_fib():
    assert fib(5)
    assert fib(3)
    assert fib(10)

def test_lcm():
    assert lcm(4, 3)
    assert lcm(3, 5)

def test_squareroot():
    assert square_root(8)

def test_abs_diff():
    assert abs_diff(8, 6)
    assert abs_diff(16, 3.5)

def test_log():
    assert log(2, 10)
    assert log(2, 6)

def test_mod():
    assert mod(6, 2) == 0


def test_mean():
    assert mean()

def test_median():
    assert median()

def test_mode():
    assert mode()

def test_CtF():
    assert celsius_to_fahrenheit(100) == 212
    assert celsius_to_fahrenheit(0) == 32

def test_FtC():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_celsius(212) == 100

def test_inverse():
    inverse()

def test_triangular_number():
    triangular_number()












if __name__ == "__main__":
    pass