from collections import defaultdict

fruits = ["apple", "apple", "banana", "apple", "banana", "mango"]

fruit_count = defaultdict(int)

for fruit in fruits:
    fruit_count[fruit] += 1

print(fruit_count)

names = {
    "saba": 1
}
names["dato"] = 1
names["dato"] += 1
print(names)
