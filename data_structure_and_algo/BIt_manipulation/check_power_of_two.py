
def is_power_of_two(number) :
    count = 0 
    while number :
        number = number & (number - 1)
        count = count + 1

    if count == 1 :
        return True
    else :
        return False
    

print(is_power_of_two(2))
print(is_power_of_two(4))
print(is_power_of_two(6))