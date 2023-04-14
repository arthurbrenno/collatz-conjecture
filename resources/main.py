import numpy as np;
import matplotlib.pyplot as plt;
import sys;


def main():
    number = int(sys.argv[1])
    numbers = [number]
    while (number > 1):
        number = step(number)
        numbers.append(number)
    print(number)
    plt.plot(numbers)
    plt.show()


def step(number):
    if number % 2 == 0:
        number>>=1
    else:
        number = (3 * number) + 1
    return number

if __name__ == '__main__':
    main()
