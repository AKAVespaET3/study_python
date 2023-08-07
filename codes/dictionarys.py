# 초기화 방법
thisdict = {} # empty inital
thisdict = dict() # empty inital

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
dict_format = "key : {0}, value : {1}" 
for key, value in thisdict.items():
    print(dict_format.format(key, value))
    pass
pass

# add item in dict
thisdict['color'] = 'red'

# remove item
del thisdict['year']

# 데이터 갯수 확인?
len(thisdict)
# 3

# 타입 확인?
type(thisdict)
# <class 'dict'>

#model에 해당하는 값 확인?
thisdict['model']
# 'Mustang'

#브랜드 변경(값변경)
thisdict['brand'] = "yoju"

# key 값 확인?
thisdict.keys()
# dict_keys(['brand', 'model', 'year'])
# special variables
# function variables
# mapping:
# mappingproxy({'brand': 'yoju', 'model': 'Mustang', 'year': 1964})

# 모르겠다
type(thisdict.keys())
# <class 'dict_keys'>
# thisdict.values()
# dict_values(['yoju', 'Mustang', 1964])
# special variables
# mapping:
# mappingproxy({'brand': 'yoju', 'model': 'Mustang', 'year': 1964})
# special variables
# function variables