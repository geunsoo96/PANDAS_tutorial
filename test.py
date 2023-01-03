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
print("row labels:", df.index)