# -*- coding: utf-8 -*-
import time
import cgi
import datetime
import os
from MBSD_Tools import GET_HTML, getURL_para,url_crawling,mark_visited,danger_url
# 処理の開始時刻を記録
start_time = time.time()
form = cgi.FieldStorage()
start_url = form['text'].value
urllimit = form.getvalue('urllimit', '0')
urllimit=int(urllimit)
#入力されたURLの改行、空白を削除
start_url=start_url.replace("\n", "").replace(" ", "").replace("　", "")
# 現在のスクリプトのディレクトリを取得
script_dir = os.path.dirname(os.path.abspath(__file__))

# 相対パスを使ってファイルにアクセス
relative_path = "../../answer.html"
file_path = os.path.join(script_dir, relative_path)
# HTMLテンプレートを読み込む
with open(file_path, "r", encoding="shift-jis") as template_file:
    template = template_file.read()

urlcount=0
danger_tag=0
sumtext=0
sumfile=0
sumpassword=0
sumhidden=0
sumform=0
sumtextarea=0
html=""
table_html = ""

html=GET_HTML(start_url)
# 指定されたＵＲＬの中の有効なドメインのURLの検査
start_sate = url_crawling(start_url, html,urllimit)

# 各URLに対してテーブルを生成して追加
for start_sate in start_sate:
    html = GET_HTML(start_sate)
    ht_mbsd,ht_title,tagVul, tagcount,flag = danger_url(html)
    if flag == 1:
        pass
    else:
        danger_tag=danger_tag+sum(tagcount[1:6])
        sumtext=sumtext+tagcount[1]
        sumfile=sumfile+tagcount[2]
        sumpassword=sumpassword+tagcount[3]
        sumhidden=sumhidden+tagcount[4]
        sumform=sumform+tagcount[5]
        sumtextarea=sumtextarea+tagcount[6]
        # 仮のデータ
        graph_data_list = [
            {"検出URL": start_sate, "text": tagcount[1], "file": tagcount[2],
            "password": tagcount[3], "hidden": tagcount[4], "form": tagcount[5], "textarea": tagcount[6],
            "MBSDのリスト": ht_mbsd, "タイトル": ht_title, "パラメータ": getURL_para(start_sate),
            "検出した結果": 10, "備考": ""},
        ]
            # テーブルの生成
        for j,graph_data in enumerate(graph_data_list):
            urlcount=urlcount+1
            table_html += f"""
                <h1>{graph_data["検出URL"]}</h1>
                <table class="msr_table03">
                    <thead>
                        <tr>
                            <th>検出対象</th>
                            <th>検出した結果</th>
                            <th>備考</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th><p>input type="text"</p></th>
                            <td><p>{graph_data["text"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>input type="file"</p></th>
                            <td><p>{graph_data["file"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>input type="password"</p></th>
                            <td><p>{graph_data["password"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>input type="hidden"</p></th>
                            <td><p>{graph_data["hidden"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>&lt;form&gt;</p></th>
                            <td><p>{graph_data["form"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>&lt;textarea&gt;</p></th>
                            <td><p>{graph_data["textarea"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>タイトルの内容</p></th>
                            <td><p>{graph_data["タイトル"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>画面内のMBSDの内容</p></th>
                            <td><p>{graph_data["MBSDのリスト"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                        <tr>
                            <th><p>パラメータ</p></th>
                            <td><p>{graph_data["パラメータ"]}</p></td>
                            <td><p>{graph_data["備考"]}</p></td>
                        </tr>
                    </tbody>
                </table>
            """
# プレースホルダーを実際の値に置き換え
# 文字コードエラーが発生しても無視してエンコード
table_html_encoded = table_html.encode('shift-jis', errors='ignore')
# 文字コードエラーが発生しても無視してデコード
table_html_decoded = table_html_encoded.decode('shift-jis', errors='ignore')
template = template.replace("<!-- ここにテーブルデータを表示 -->", table_html_decoded)
# プレースホルダーを実際の値に置き換え
template = template.replace("<!-- ここにurlcountの値を表示 -->", str(urlcount))
# プレースホルダーを実際の値に置き換え
template = template.replace("<!-- ここにdanger_tagの値を表示 -->", str(danger_tag))

# 各変数の合計が100%になるようにスケーリング
total_sum = sumtext + sumfile + sumpassword + sumhidden + sumform + sumtextarea
# 各変数の合計が0でないか確認
if total_sum != 0:
    texper = round((sumtext / total_sum) * 100, 2)
    filper = round((sumfile / total_sum) * 100, 2)
    pasper = round((sumpassword / total_sum) * 100, 2)
    hidper = round((sumhidden / total_sum) * 100, 2)
    forper = round((sumform / total_sum) * 100, 2)
    areper = round((sumtextarea / total_sum) * 100, 2)
else:
    # ゼロで割り算が発生する場合の処理（例: すべての値をゼロに設定）
    texper = 0
    filper = 0
    pasper = 0
    hidper = 0
    forper = 0
    areper = 0

template2=f"""    
        <div>
            <dt>input type="text"</dt>
            <dd style="width:{texper} %">{texper}%</dd>
        </div>
        <div>
            <dt>input type="file"</dt>
            <dd style="width: {filper}%">{filper}%</dd>
        </div>
        <div>
            <dt>input type="password"</dt>
            <dd style="width: {pasper}%">{pasper}%</dd>
        </div>
        <div>
            <dt>input type="hidden"</dt>
            <dd style="width: {hidper}%">{hidper}%</dd>
        </div>
        <div>
            <dt>&lt;form&gt;</dt>
            <dd style="width: {forper}%">{forper}%</dd>
        </div>
        <div>
            <dt>&lt;textarea&gt;</dt>
            <dd style="width: {areper}%">{areper}%</dd>
        </div>"""

template = template.replace("<!-- ここに棒グラフを表示 -->  ",template2)


# 処理の終了時刻を記録
end_time = time.time()
# 経過時間を計算して表示
elapsed_time = end_time - start_time
# timedeltaオブジェクトに変換
elapsed_time_timedelta = datetime.timedelta(seconds=elapsed_time)
# プレースホルダーを実際の値に置き換え
template = template.replace("<!-- ここに実行時間を表示 -->", str(elapsed_time_timedelta))
# Content-Typeヘッダーを出力
print("Content-Type: text/html; charset=shift-jis")
print()

# 修正されたHTMLテンプレートを出力
print(template)