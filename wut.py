from pprint import pprint

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12)
# ]

# prices = []
# for item in items:
#     prices.append(item[1])

# print(prices)


# prices = list(filter(lambda item: item[1] >= 10, items))

# print("prices", prices)
# x = 10
# y = 11

# x, y = y, x

# # print(x, y)

# sentence = "This is a common interview question"

# char_frequency = {}
# for char in sentence:
#     if char in char_frequency:
#         char_frequency[char] += 1
#     else:
#         char_frequency[char] = 1
# char_frequency_sorted = sorted(
#     char_frequency.items(),
#     key=lambda kv: kv[1],
#     reverse=True)
# pprint(char_frequency_sorted[0])
try:
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
