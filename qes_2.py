binary_Number = input("Please Write a binary number: ")

if not all(char in '01'  for char in binary_Number):
    raise("Invalid input, please enter a binary number")

else:
    decimal = int(binary_Number, 2)
    print("your decimal number: ", decimal)