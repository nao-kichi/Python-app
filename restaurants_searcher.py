# 公開APIからデータを取得するアプリ
# 実行ができない場合は、pip install requestsまたはpip3 install requests
# python restaurants_searcher.pyで実行を掛ける。
# restaurants_searcher.py

import json
import csv
import requests

# 初期設定
# KEYIDはリクルートWEBサービスから取得する
KEYID = "54bf87489ac8247b"
COUNT = 100
PREF = "Z011"
FREEWORD = "渋谷駅"
FORMAT = "json"

PARAMS = {"key": KEYID, "count":COUNT, "large_area":PREF, "keyword":FREEWORD, "format":FORMAT}

# 最後に.textをつけることで、必要な核心部分のデータだけをテキスト形式で取得する。
# responseデータを取得。
def write_data_to_csv(params):
    restaurants = [["名称","営業日","住所","アクセス"]]
    json_res = requests.get("http://webservice.recruit.co.jp/hotpepper/gourmet/v1/", params=params).text
    response = json.loads(json_res)
    if "error" in response["results"]:
      # 検索条件やURLなどに不備がある場合
        return print("エラーが発生しました！")
    for restaurant in response["results"]["shop"]:
        rest_info = [restaurant["name"], restaurant["open"], restaurant["address"], restaurant["access"]]
        restaurants.append(rest_info)
        # 店舗名のリストであるrestaurantsを、最終的にCSVとして書き出す処理を行う。
        # 受け取ったデータの順番はランダムとなっている。
    with open("restaurants_list.csv", "w") as f:
        writer = csv.writer(f)
        # writerowsで1行にまとめないで複数行で見やすくなる。
        writer.writerows(restaurants)
    return print(restaurants)
# この後に、Googleのマイマップの共有方法→GoogleマイマップのインポートでCSVやスプレッドシートを利用する
write_data_to_csv(PARAMS)
