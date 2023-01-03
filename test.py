import numpy as np
import pandas as pd

data = {
  'year': [2016, 2017, 2018],
  'GDP rate': [2.8, 3.1, 3.0],
  'GDP': ['1.637M', '1.73M', '1.83M']
}
# 데이터 생성
df = pd.DataFrame(data, index=data['year'])
# 인덱스 추가 가능
print(df)
#       year  GDP rate     GDP
# 2016  2016       2.8  1.637M
# 2017  2017       3.1   1.73M
# 2018  2018       3.0   1.83M
print("row labels:", df.index)
# row labels: Int64Index([2016, 2017, 2018], dtype='int64')
print("column labels:", df.columns)
# column labels: Index(['year', 'GDP rate', 'GDP'], dtype='object')
print("head:", df.head())