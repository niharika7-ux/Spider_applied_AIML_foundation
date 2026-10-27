# Practising loops and simple calculations

print("Multiples of 3 up to 30:")
for number in range(3, 31, 3):
    print(number, end=" ")

print("\n\nTotal of numbers from 1 to 10:")
total = 0
for number in range(1, 11):
    total += number
print(total)

print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Start!")
