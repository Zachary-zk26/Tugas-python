numbers=[5,4,3,2,1]

total=sum(numbers)
print(total)

max_number=max(numbers)
print(max_number)

numbers.sort()
max_number=numbers[-1]
print(max_number)

max_number=numbers[0]
for number in numbers:
    if number>max_number:
        max_number=number
print(max_number)