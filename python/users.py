import pandas as pd

# dataframe을 생성하는 다른 방법
users = [
    ['철수', 180, 5],
    ['민수', 175, 5],
    ['짱구', 130, 5]
]
users
# [['철수', 180, 5], ['민수', 175, 5], ['짱구', 130, 5]]

dfUsers = pd.DataFrame(users)
print(dfUsers)
#      0   1   2  
# 0  철수  180  5
# 1  민수  175  5
# 2  짱구  130  5

# 컬럼 설정해보기
dfUsers.columns = ['name', 'height', 'age']
print(dfUsers)
#     name  height  age
# 0   철수     180    5
# 1   민수     175    5
# 2   짱구     130    5

# 딕셔너리 전달
users = {
    'name':['철수', '민수', '짱구'],
    'height': [180, 175, 130],
    'age': [25, 30, 5]
}
users
# {'name': ['철수', '민수', '짱구'], 'height': [180, 175, 130], 'age': [25, 30, 5]}

dfUsers = pd.DataFrame(users)
dfUsers
#     name  height  age
# 0   철수     180   25
# 1   민수     175   30
# 2   짱구     130    5

# 리스트 in 딕셔너리 전달
# 실제 현업에서는 api 요청의 결과로 이런 형식의 데이터 포멧으로 올 가능성이 크다.
users = [
    {'name': '철수', 'height': 180, 'age': 25},
    {'name': '민수', 'height': 170, 'age': 30},
    {'name': '짱구', 'height': 130, 'age': 5}
]
users
# [{'name': '철수', 'height': 180, 'age': 25},
#  {'name': '민수', 'height': 170, 'age': 30},
#  {'name': '짱구', 'height': 130, 'age': 5}]

dfUsers = pd.DataFrame(users)
dfUsers
#     name  height  age
# 0   철수     180   25
# 1   민수     175   30
# 2   짱구     130    5

