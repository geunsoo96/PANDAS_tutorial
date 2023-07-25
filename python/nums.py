import pandas as pd
nums = [i for i in range(1, 11)]
# 1부터 10까지 숫자 출력
nums
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# series 데이터 생성하는 법
seriesNums = pd.Series(nums)
seriesNums
# 0     1
# 1     2s
# 2     3
# 3     4
# 4     5
# 5     6
# 6     7
# 7     8
# 8     9
# 9    10
# dtype: int64

seriesNums.mean()
# 1부터 10까지 평균
# 5.5

seriesNums.describe()
# 데이터 표현 또는 묘사
# count    10.00000
# mean      5.50000
# std       3.02765
# min       1.00000
# 25%       3.25000
# 50%       5.50000
# 75%       7.75000
# max      10.00000
# dtype: float64

# dataframe 생성하는 법
nums = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
# 3개의 series가 데이터를 이루고 있음

dfNums = pd.DataFrame(nums)
print(dfNums)
print(pd.__version__)
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9

# series와 dataframe 관계
type(dfNums)
# pandas.core.frame.DataFrame

dfNums[0]
# 0    1
# 1    4
# 2    7
# Name: 0, dtype: int64

type(dfNums[0])
# pandas.core.series.Series