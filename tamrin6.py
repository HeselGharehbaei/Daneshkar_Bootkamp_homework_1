
first_end_input_numbers = list(map(int, input("input first, end numbers(separated tnumbers by ', '):").split(", ")))
bazeh = range(first_end_input_numbers[0]+1, first_end_input_numbers[1])
prime_numbers = []
for item in bazeh:
    count = 0
    for number in range(1, int((item+2)/2)):
        if item%number == 0:
           count+=1
    if count == 1:
        prime_numbers.append(str(item))
print(", ".join(prime_numbers))
