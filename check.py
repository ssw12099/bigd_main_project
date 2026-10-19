import pandas as pd
import matplotlib.pyplot as plt

watchlist_df = pd.read_csv("watchlist.csv")
print("1. dtype 없이 읽은 결과")
print(watchlist_df["code"].tolist())
#[5930, 660, 5380]
# 17쪽: dtype 없이 읽기

watchlist_df = pd.read_csv("watchlist.csv", dtype={"code": str})
print("\n2. dtype 적용한 결과")
print(watchlist_df["code"].tolist())
['005930', '000660', '005380']
# 20쪽: dtype을 str로 지정해서 읽기

print("\n3. dict(zip()) 결과")
print(dict(zip(watchlist_df["code"], watchlist_df["name"])))
# 14쪽: 종목코드와 종목명 연결