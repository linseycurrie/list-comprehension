numbers = range(1,11)
even_squared = [number * number for number in numbers if number % 2 == 0]

# for number in numbers:
#     if number % 2 == 0:
#         even_squared.append(number * number)
# print(even_squared)

# ages = [5, 15, 64, 27, 84, 26]

# odd_ages = [age for age in ages if age % 2 != 0]
# print(odd_ages)

# chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]

# name_greater_than_ten = [chicken for chicken in chicken_names if (len(chicken) > 10) ]
# print(name_greater_than_ten)

# name_start_H = [chicken for chicken in chicken_names if ((chicken[0])== ('H' or 'h'))]
# print(name_start_H)

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

letters = [word[0].lower() for word in words]
print(letters)
