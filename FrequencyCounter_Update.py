# This program counts the appearance of integers from 1 to 100 in a list of user input.

try:
    n = input("Please enter integers between 1 and 100, separated by spaces: ")
    n = n.split()
    n = [int(num) for num in n if int(num) >= 1 and int(num) <= 100]
except:
    print("Invalid input. Please enter integers between 1 and 100.")
    exit()

count = 100 * [0]

for num in n:
    count[num - 1] += 1

for i in range(len(count)):
    if count[i] == 1:
        print(f"{i+1} appears 1 time")
    elif count[i] > 1:
        print(f"{i+1} appears {count[i]} times")