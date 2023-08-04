
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]
Loops_count = "{0} : \"{1}\" "
count = input("Loops count : ")

while count != 'Q':
    if count.isdigit() and int(count) <= 8:
        for idx in range(int(count)):
            print(Loops_count.format(idx + 1, fruits[idx]))
    else:
        print("올바른 값을 입력하세요. 8이하 숫자나 Q를 입력하세요")

    count = input("Loops count : ")

print("종료합니다.")