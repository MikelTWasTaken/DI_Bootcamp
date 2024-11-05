number = int(input("give me a number please: "))
length = int(input("how long is the list? "))

list_of_multiples = [number * i for i in range(1, length + 1)]

print(list_of_multiples)