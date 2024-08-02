<div id="top"></div>

# ３ criler

## 概要

MBSD Cybersecurity Challenges 2023 で作成した Web アプリケーションの脆弱性診断ツールです

## 使用技術一覧

[![My Skills](https://skillicons.dev/icons?i=html,css,js,py,sublime,vscode&perline=6)](https://skillicons.dev)

## 目次

### 1. [前談](#前談)

### 2. [機能](#機能)

### 3. [実行例](#実行例)

### 4. [動作条件](#動作条件)

### 5. [ディレクトリ構成](#ディレクトリ構成)

### 6. [関数の説明](#関数の説明)

## 前談

### 1. どのような機能を目指したか

今回作成したツールは、大会を主催している MBSD から提示されている競技概要に則り自動巡回ツールを作成した。ツールに搭載する為に考えた機能としては、複数あるので個々に挙げる。

診断対象先である Web サイトの入力フォーム数
Web サイト内に存在する URL の検出及び出力
診断対象のパラメータの出力
Web サイトのコンテンツ内に含まれている`MBSD｛××××｝`のキーワードの出力
診断 URL にページタイトルが含まれる場合に出力をする
これら機能に加えて実行時にできるだけ処理時間を短くし実行結果をわかりやすく表示させる機能を持ち合わせた自動巡回ツールの作成を目指した。

### 2. 目標・目的

Web サイトを網羅的に検査をしできるだけ脆弱性を検出でき、実際に運用が出来るような自動巡回ツールを作ることを目標として作成を開始した。

### 3. 参考にさせてもらったもの<br>

[Python プログラミング VTuber サプー](https://www.youtube.com/@pythonvtuber9917/videos)
<br><br>
[【Python プログラミング入門】メモ化で高速化！cache デコレータを使ってみよう！〜初心者向け〜](https://youtu.be/lRaSMlHY3aY?feature=shared)
<br><br>
[【Python プログラミング入門】自作モジュールの使い方を解説！〜VTuber と学習〜 【初心者向け】](https://youtu.be/X3uBMY3JQqM?feature=shared)
<br><br>
[HTML でチェックボックスを表示する方法！基本的な作り方と使い方を解説　 by ウェブカツ #初心者 - Qiita](https://qiita.com/kazukichi/items/1af73244df0e67137531)
<br><br>
[【バッチファイル】ログの出力方法と日時取得／ログファイル名に日時取得 #bat – Qiita](https://qiita.com/pekosyu/items/a2d416f9f2afe9c40066)
<br><br>
[ローカルに python の CGI 環境を構築　ほどよく解説しながらスピード重視で説明するよ](https://jimaru.blog/programming/python/local-cgi-python/)
<br><br>
[HTML で form タグの action 属性に複数の送信先を指定する方法を現役エンジニアが解説【初心者向け】](https://magazine.techacademy.jp/magazine/32105)
<br><br>
[Web サーバーで動く Python アプリ 【Windows 版】](https://irohaplat.com/windows-python-http-server-calculator-application/)
<br><br>
[CSS のコピペだけ！おしゃれな見出しのデザイン例まとめ 6](https://saruwakakun.com/html-css/reference/h-design)
<br><br>
[図解！Python で WEB スクレイピングを始めよう！(サンプルコード付きチュートリアル)](https://ai-inter1.com/python-webscraping/#st-toc-h-2)
<br><br>
[【HTML】フォーム作成の基本！form と input の使い方](https://creive.me/archives/13526/)
<br><br>
[スクレイピング練習場（ベータ）](https://scraping-training.vercel.app/)
<br><br>
[図解！Python の Requests を徹底解説！(インストール・使い方)](https://ai-inter1.com/python-requests/)
<br><br>
[【コピペで完成】HTML・CSS のみで作る棒グラフのデザイン 2 選【アニメーション対応】 (pote-chil.com)](https://pote-chil.com/html-maker/bar-chart)
<br><br>
[table・tr・th・td タグ | HTML での正しい表の構造と使い方・作り方を徹底解説 | Web のいろは (webnoiroha.net)](https://www.webnoiroha.net/html-table/)
<br><br>

## 機能

### 1. クローラにより実行可能な事

- 検査対象の Web サイトの脆弱性の検査
- Web サイトの規模の調査
- ローカル環境下によるツールの実行
- URL・パラメータ・ページタイトル・性能審査用のキーワードを表にして出力
- ドメインの指定
- 診断対象個数のそれぞれの合計割合をグラフで表示
- 検査する URL の数の制限

### 2. 抽出可能な診断対象

- HTML 内に含まれる`「input type=”text”」(入力フォーム)`
  <br>検出可能な脆弱性：クロスサイトスクリプティング(XSS)<br><br>

- HTML 内に含まれる`「input type=”file”」`
  <br>検出可能な脆弱性：不正ファイルのアップロード<br><br>

- HTML 内に含まれる`「input type=”password”」`
  <br>検出可能な脆弱性：パスワードセキュリティ<br><br>

- HTML 内に含まれる`「input type=”hidden”」`
  <br>検出可能な脆弱性：隠しフィールドに保存されているデータの悪用<br><br>

- HTML 内に含まれる`「form」`
  <br>検出可能な脆弱性：クロスサイトリクエストフォージェリ(CSRF)<br><br>

- HTML 内に含まれる`「textarea」`
  <br>検出可能な脆弱性：クロスサイトスクリプティング(XSS)<br><br>

- Web サイトを構築する HTML に含まれる`MBSD{××××}`の内容
  <br>検出可能：MBSD{××××}に含まれるキーワード<br><br>

- URL 内に含まれるパラメータ
  <br>検出可能な脆弱性：クエリ文字インジェクション<br><br>

## 実行例

### 1. サーバースタート.bat ファイルの実行

MBSD＿Web＿CSS.zip を解凍しサーバースタート.bat ファイルを実行してください。<br>
![image](https://github.com/user-attachments/assets/044757d8-2bc3-42ca-9795-15f39f039f79)

### 2. 許可確認画面

初めて実行する場合 Python から権限の許可を問われる場合があります。その場合は、許可をしてください。<br>
※python 自体がインストールされていない場合はインストールしてください。<br>
![image](https://github.com/user-attachments/assets/741246eb-c4fb-4d55-940e-96f0caa5cb11)<br>
Windows からの許可を問われる場合があります。その場合は、許可をしてください。<br>
詳細情報をクリックして、右の画面に遷移するので実行してください。<br>
![image](https://github.com/user-attachments/assets/3355312d-cc08-41a6-bb19-73abd89584a0)

### 3. 診断のツールの実行

立ち上がったらテキストフィールドに検索対象の URL を入力し送信ボタンを押してください。<br>
検出する URL を制限する場所にチェックを入れると検査する URL の個数が制限されます。<br>
※URL 入力欄には自分で空白(スペース)や、改行を入力しないでください。<br>
![image](https://github.com/user-attachments/assets/b6d18355-8677-4d46-9da2-773132798a28)

### 4. 実行結果の確認

このような形にになれば検査完了です。<br>
※棒グラフの長さは適切でないときがあります。<br>
![image](https://github.com/user-attachments/assets/30788f85-29ba-4678-b595-afa3a1276e65)
![image](https://github.com/user-attachments/assets/709f5baf-458f-435a-b5d9-40ad13197f81)
<br>
※注意事項

<li>Webサイトによっては検出までに時間がかかります。</li>
<li>ブラウザのタブ部分が読込み中の場合は正常に動作しています。</li>
<li>送信ボタンを二回押さないでください。</li>
<li>二回目の検査をする場合は一度元の画面に戻り再読み込みをしてから行ってください。</li>
<li>巡回ツールは許可されたサイトで使用してください。</li>

## 動作条件

| 言語・フレームワーク | バージョン |
| -------------------- | ---------- |
| Python               | 3.9.12     |
| urllib3              | 2.0.6      |

| 実行ブラウザ   | バージョン                                   |
| -------------- | -------------------------------------------- |
| Microsoft Edge | 119.0.2151.44 (公式ビルド)　(64 ビット) 　　 |
| Google Chrome  | 119.0.6045.124（Official Build) (64 ビット） |
| Firefox        | 116.0.3 (64 ビット)                          |

## ディレクトリ構成

<pre>
.
│  .gitattributes.txt
│  MBSD_.docx
│  MBSD_Web_CSS_26.zip
│  MBSD__2.docx
│  README.md
│
└─MBSD_Web_CSS_26
    └─MBSD_Web_CSS
        │  answer.html
        │  hello.css
        │  hello.html
        │  pythonin.bat
        │  サーバースタート.bat
        │
        ├─.vscode
        │      launch.json
        │      settings.json
        │      tasks.json
        │
        ├─cgi-bin
        │  └─team_motiduki
        │      │  MBSDmain.py
        │      │  MBSDmain_HTML.py
        │      │  MBSD_test.html
        │      │  テーブル.html
        │      │
        │      └─MBSD_Tools
        │          │  danger_url.py
        │          │  GetHTML.py
        │          │  GetTAG.py
        │          │  HTML_CONTENT.py
        │          │  INPUT.py
        │          │  is_image_url.py
        │          │  MBSD_SEARCH.py
        │          │  mbsd_title.py
        │          │  url_Crawler.py
        │          │  url_Domain_Select_Getter.py
        │          │  url_Getter.py
        │          │  url_Host.py
        │          │  url_Parameter.py
        │          │  url_Visited.py
        │          │  __init__.py
        │          │
        │          └─__pycache__
        └─css
            └─answer.css
</pre>
<p align="right">(<a href="#top">トップへ</a>)</p>

## 関数の説明

### 1. MBSDmain_HTML.py

検査する URL を受けとりその URL を元に解析をして結果を表示する<br>
動作概要<br>
① 検査 URL をフォームから受け取る<br>
② 結果を表示する HTML ファイルを取得<br>
③ 検査 URL の検査を開始<br>
④ 検査結果を HTML のテーブルテンプレートとして保存する<br>
⑤ 検査 URL の中の脆弱性がある同じドメインの URL の検査を開始<br>
⑥ 同様にテーブルテンプレートを保存<br>
⑦ ドメイン URL の数だけ ⑤、⑥ を繰り返す<br>
⑧② の HTML ファイルを保存したテーブルを表示するように書き換え<br>
⑨ 書き換えた HTML を出力する<br>

### 2. GetHTML.py

- ①GET＿HTML<br>
  引数 : url(文字列型)<br>
  戻り値 : html(文字列型)<br>

与えられた url を元に HTML を取得<br>
　 utf-8 で html をデコードしエラーが出た場合は Shift-JIS でデコード<br>
　デコードができなかった場合はからの html の文字列を返す<br>
　メモ化をしており引数が同じの二回目以降の処理は短縮される<br>

### 3. GetTAG.py

- ①GET_TAG<br>
  引数 : html(文字列型)<br>
  戻り値 : taglist(文字列型配列)<br>

与えられた html を元に存在するタグを抽出。<br>
タグを一つ一つ分けて配列に格納<br>

### 4. INPUT.py

- ①GET＿INPUT<br>
  引数 : 文字列型　 html…html 文が文字列として格納されている。<br>
  戻り値 ：リスト tagVul…タグの種類<br>
  リスト tagcount…検出したタグの個数<br>

変数 html を引数として関数を実行すると、html 文の中にあるタグの種類の個数を
tagcount に格納して返す。<br>
検出するタグは、&lt;input&gt;&lt;form&gt;&lt;textarea&gt;の３つと&lt;input&gt;の属性である　
text,file,password,hidden を対象にして検出している。
リスト tagVul は添え字が 0 から始まり、
&lt;input&gt;,text,file,password,hidden,&lt;form&gt;,&lt;textarea&gt;の順に格納されている。
また、リスト tagcount の個数の格納順はリスト tagVul と共通である。<br>

### 5. MBSD＿SEARCH.py

- ①MBSD_SEARCH<br>
  引数 : html(文字列型)<br>
  戻り値 : result(文字列型配列)<br>

与えられた html の中から MBSD{XXXX}の XXXX の内容があるか探す。<br>
あった場合は配列に格納してその結果を返す。<br>

### 6. mbsd_title.py

- ①HTML_TITLE<br>
  引数 : html(文字列型)<br>
  戻り値 : title(文字列型配列)<br>

与えられた html からタイトルを抽出しその結果を配列で返す。<br>

### 7. url_Getter.py

- ①getURL(url,html) <br>
  引数:url(文字列型),html(html 文書を文字列で取得したもの:文字列型)<br>
  戻り値: urls(文字列型配列)<br>

アクセス先に含まれる別の URL を重複がないように取り出す。(複雑すぎるパラメータを含む場合はその URL は取り出せない)<br>
この関数は<a>タグ内の href のリンクと html 文書を解析して URL らしきものを全て検出できるようにしました。この解析処理を高速に終わらせる
ために正規表現を用いました。<br>

- ②del_equal_url(urls)<br>
  引数:urls(文字列型配列)<br>
  戻り値: urls(文字列型配列)<br>

同じ URL が含まれていた場合に削除します<br>
mark_visited(url),is_visited(url),reset_visited_urls()の関数を用いて同じ URL を削除する機構を作りました。使う関数ごとに差別化する(保存する領域を差別化する)ために del_equal_url(urls)内では同じ動作をする別の関数を用いています。<br>

### 8. url_Host.py

- ①getURL_host(url)<br>
  引数:url(文字列型)<br>
  戻り値: host(文字列型)<br>
  ホスト名を取得します<br>

### 9. url_Parameter.py

- ① getURL_para(url)<br>
  引数:url(文字列型)<br>
  戻り値:passstr(文字列型)<br>

URL を取得した際のパラメータが'&'などの文字列が'&amp;'のようにエスケープされる<br>
とパラメータが正常に取得できないので正常に取得できるように工夫しました。<br>

- ②getURL_path_para(url)<br>
  引数:url(文字列型)<br>
  戻り値:path_parameters(文字列型)又はなし<br>

URL に含まれるパスパラメータのみを取得する。パスパラメータがない場合は戻り値は返されません。<br>

### 10. is_image_url.py

- ①is_image_url(url)<br>
  引数:url(文字列型)<br>
  戻り値:Ture、False<br>

URL に画像ファイル、.js、.json、.css を含む URL がある 時に True,ない時に False が
戻り値として返す正規表現を用いて URL(文字列型)に対する検索をかけました。<br>
より高速に解析できると考えます。<br>

- ②image_del(urls)<br>
  引数:urls(文字列型配列)<br>
  戻り値:urls(文字列型配列)<br>

URL に is_image_url(url)を適用、True のときにその URL を削除し urls の上書き保存し
ます。<br>

### 11. url_Visited.py

- ①mark_visited(url)<br>
  引数:url(文字列型)<br>
  戻り値:なし<br>

URL を保存します(マークする)。<br>

- ②is_visited(url)<br>
  引数:url(文字列型)<br>
  戻り値:Ture、False<br>

url(文字列型)が保存されている(mark_visited(url)が既に実行されている)ときに True,そ
れ以外は False が戻り値として返します。<br>

- ③reset_visited_urls()<br>
  引数:なし<br>
  戻り値:なし<br>

mark_visited(url)で保存されたデータを全て削除します。<br>

### 12. url_Domain_Select_Getter.py

- ①is_getURL_selected_by_domain(source_url, comparison_url)<br>
  引数:source_url(文字列型),comparison_urll(文字列型)<br>
  戻り値:Ture、False<br>

引数として指定された URL(文字列型)2 つに対して、ドメイン名が同じの場合 True,ドイン名が異なる時に False が戻り値として返します。<br>

- ②getURL_selected_by_domain(url,html)<br>
  引数:url(文字列型),html(html 文書を文字列で取得したもの:文字列型)<br>
  戻り値:domain_urls(文字列型配列)<br>

引数として指定された URL(文字列型)と html(html 文書を文字列で取得したもの)に対してドメイン名で絞りだした後に image_del(urls)を用いて画像 URL などを削除します。その結果を戻り値として返します。<br>

### 13. url_Crawler .py

- ①url_crawling(url,html)<br>
  引数:url(文字列型),html(html 文書を文字列で取得したもの:文字列型)<br>
  CRAWLING_RESTRICTION の値を変えることで制限を変えることができる。<br>
  値を増やすと検出する URL の個数が少なくなる。(初期値 3)<br>
  例：CRAWLING_RESTRICTION の値が３の時、開始 URL を含んで３個までの URL を取得してそこまでの URL のクローリングを実行し検査する
  戻り値: crawling_urls(文字列型配列)<br>

引数として指定された url(文字列型)と html(html 文書を文字列で取得したもの)に対し
てクローリングを実行し、結果を戻り値として返します<br>

### 14. danger_url.py

- ①danger_url.py(html)<br>
  引数:html(html 文書を文字列で取得したもの:文字列型)<br>
  戻り値:ht_mbsd(文字列型配列),ht_title(文字列型配列),tagVul(文字列型配列),
  tagcount(整数列型配列),flag(整数型)<br>

引数として指定された html(html 文書を文字列で取得したもの)に対して MBSD{xxxx}の
xxxx の文字を ht_mbsd、タイトルを ht_title、脆弱性タグリスト名を tagVul、それに対応
するタグの個数を tagcount に格納して返します。<br>
flag は脆弱性が 0 の時に 1 になって返します。(ht_mbsd,tagcount 全てが空値か 0 の時)<br>

<p align="right">(<a href="#top">トップへ</a>)</p>
