sum_of_even_from_1_to_100 = 0

for i in range(1, 101):
    if i % 2 == 0:
        sum_of_even_from_1_to_100 += i

print(f"Sum of all even numbers from 1 to 100 is: {sum_of_even_from_1_to_100}")
