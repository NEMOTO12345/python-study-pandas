import pandas as pd

df_u = pd.read_excel('data/denki_uriage.xlsx',skiprows=[0,1])
# skiprow=は行を飛ばす
# usecols=は必要な列だけ読み込む
# print(df_u)

takeyama = df_u[df_u['担当者']=='竹山']
# print(takeyama)

tantou = set(df_u['担当者'].to_list())
#setで重複を消して、to_listで列のリストを作る
# print(tantou)

total = df_u.groupby('商品名').sum(numeric_only=True)
# print(total)
#groupbyは同じ値を持つデータをまとめて、それぞれの塊に対して共通の操作を行いたい時に使う。
#numeric_only=Trueは文字列を排除して数値だけの足し算をしてくれるオプション

tantou_uriage = df_u.groupby('担当者').sum(numeric_only=True)
# print(tantou_uriage)

uriage_matome = {}
for name in tantou:
    # {'吉田', '森', '竹山', '斉藤', '西村'}
    uriage_matome[name]=df_u[df_u['担当者']==name]

# print(uriage_matome)