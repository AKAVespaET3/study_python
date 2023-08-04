
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]
Loops_count = "{0} : \"{1}\" "
count = input("Loops count : ")

while count != 'Q':
    if count.isdigit() and int(count) <= len(fruits): #isdigit() count 값이 상수일 경우 if 안에서 돌아
        for index in range(int(count)):
            print(Loops_count.format(index + 1, fruits[index]))
    else:
        print("올바른 값을 입력하세요. 8이하 숫자나 Q를 입력하세요")

    count = input("Loops count : ")

print("종료합니다.")

