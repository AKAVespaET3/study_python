#slice
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "peach"]
type(thislist)
# <class 'list'>
# special variables
# function variables
len(thislist)
# 8
thislist[1:3]
# ['banana', 'cherry']
thislist[:-1]
# ['apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango']

# change value in list
thislist[1]  = 'watermelon'
# thislist[1:3] = ['cherry', 'watermelon'] 2번째 3번째 수정
# thislist.sort() 오름차순
# thislist.sort(reverse=True) 내림차순

# 붙여넣기

thislist = ["apple", "banana", "cherry"]

#추가
thislist.append('orange') 

#삭제
thislist.pop()

# 초기화 방식
thislist = []
thislist = list() 
# List thislist = new List();

# 형변환
words = str()
pass

