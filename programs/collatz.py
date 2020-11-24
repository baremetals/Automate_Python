def collatz(num):
    if num % 2 == 0:
        print(num // 2)
        return num // 2
    else:
        print(3 * num + 1)
        return 3 * num + 1
#collatz(101)

print('Provide a number')
user_input = int(input())
while user_input != 1:
    user_input = collatz(user_input)
