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
