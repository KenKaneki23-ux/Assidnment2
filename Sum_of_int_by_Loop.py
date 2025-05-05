start = int(input("Enter the number that you want to start from: "))
end = int(input("Enter the number that you want end in: "))

total = 0
for i in range(start, end + 1):
    total += i

print("Sum of your given numbers are: ", total)
