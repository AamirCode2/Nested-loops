n = int(input("Enter an integer to find its binary representation: "))

def conversion(num):
    binary_digits = ""

    while num > 0:
        remainder = num%2
        binary_digits += str(remainder)

        num//2

    return binary_digits[::-1]

answer = conversion(n)
print("The binary value of you number is ", answer)