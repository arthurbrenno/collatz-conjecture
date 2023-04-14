import numpy as np;
import matplotlib.pyplot as plt;


def main():
    number = 47
    numbers = [number]
    while (number > 1):
        number = step(number)
        numbers.append(number)

    plt.plot(numbers)
    plt.show()


def step(number):
    if number % 2 == 0:
        number>>=2
    else:
        number = (3 * number) + 1
    return number

if __name__ == '__main__':
    main()
