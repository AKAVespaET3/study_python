thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]

# for item in items:
#     pass

for fruit in thislist: 
    print(fruit)
pass
range(2, 10)
# java for문
# for (int i = 2 ;i <= 10 ; i++){
#     print()
# }

#python
for i in range(2, 10, 2):
    print(i)

#while
first = 3
while (first < 6) : 
    pass
    print('while count {}'.format(first))
    first = first + 1

#list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]
# enumerate 원리 이해
fruits_enumerate = enumerate(fruits)
# next(fruits_enumerate)
# (0, 'apple')
# next(fruits_enumerate)
# (1, 'banana')
# next(fruits_enumerate)
# (2, 'cherry')
# next(fruits_enumerate)
# (3, 'orange')
# next(fruits_enumerate)
# (4, 'kiwi')
# next(fruits_enumerate)
# (5, 'melon')
# next(fruits_enumerate)
# (6, 'mango')
# next(fruits_enumerate)
# (7, 'peach')
# next(fruits_enumerate)
# Traceback (most recent call last):
#   File "<string>", line 1, in <module>
# StopIteration

#list with numbering
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]
fruits_enumerate = enumerate(fruits)
for index_fruit in fruits_enumerate: #듀플 묶음
    print(index_fruit)

fruits_enumerate = enumerate(fruits)
fruit_print_format = "number: {0}, fruit name : {1}"
for (index, fruit) in fruits_enumerate: #듀플 묶음
    print(fruit_print_format.format(index, fruit))
    pass
pass
