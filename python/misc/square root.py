value = input('Value you want square root of: ')
value = int(value)
guess = value/2

# babylonian method implementation

while True:
    guess = (guess+(value/guess))/2
    if (guess*guess - value) < 0.00000001:
        break
# can add rounding or whatever here as well
print(guess)


value = input('Value you want square root of: ')
value = int(value)

# binary search implementation
top_pointer = value
lower_pointer = 0

while True:
    midpoint = (top_pointer + lower_pointer)/2
    square = midpoint * midpoint
    if abs(square - value) < 0.00000001:
        break
    elif square > value:
        top_pointer = midpoint
    elif square < value:
        lower_pointer = midpoint
    
print(midpoint)