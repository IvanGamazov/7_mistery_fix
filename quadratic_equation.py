from math import sqrt
from pprint import pprint


def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        if discriminant == 0:
            return root1, None
        else:
            return root1, root2
    else:
        return None, None


def check_coefficients(a ,b ,c):
    if not a:
        a = 0
    else:
        a = int(a)
    if not b:
        b = 0
    else:
        b = int(b)
    if not c:
        c = 0
    else:
        c = int(c)
    return a, b, c


def print_result(root1, root2):
    pprint("Solution: first root : {0}, second root: {1}".format(root1, root2))


def main():
    a = input("Enter the a-coefficient for x^2 --> ")
    b = input("Enter the b-coefficient for x --> ")
    c = input("Enter the c-coefficient - a free member of the equation --> ")

    a, b, c = check_coefficients(a, b, c)
    root1, root2 = get_roots(a, b, c)
    print_result(root1, root2)


if __name__ == "__main__":
    main()


