def count_and_sum_divisible_by_5(start,end):
    count=0
    total_sum=0
    for num in range(start,end):
        if(num%5==0):
            count+=1
            total_sum+= num
    return count,total_sum
start_range=int(input("Enter the start of the range:"))
end_range=int(input("Enter the end of the range:"))
count,total_sum=count_and_sum_divisible_by_5(start_range,end_range)
print("Number of integers divisible by 5:",count)
print("Sum of all integers divisible by 5:",total_sum)
