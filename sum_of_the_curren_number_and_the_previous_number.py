#Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.
numbers_in_range = [0,0,1,2,3,4,5,6,7,8,9,] 

for i in range (10):
    number_in_range_current = numbers_in_range[i]
    number_in_range_previous = numbers_in_range[i-1]
    number_in_range_current_and_previous_sum = int(number_in_range_previous) + int(number_in_range_current)

    print(number_in_range_current_and_previous_sum)
