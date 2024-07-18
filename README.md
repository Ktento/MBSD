<div id="top"></div>

# ３criler
## 概要
MBSD Cybersecurity Challenges 2023で作成したWebアプリケーションの脆弱性診断ツールです
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
今回作成したツールは、大会を主催しているMBSDから提示されている競技概要に則り自動巡回ツールを作成した。ツールに搭載する為に考えた機能としては、複数あるので個々に挙げる。

診断対象先であるWebサイトの入力フォーム数
Webサイト内に存在するURLの検出及び出力
診断対象のパラメータの出力
Webサイトのコンテンツ内に含まれている`MBSD｛××××｝`のキーワードの出力
診断URLにページタイトルが含まれる場合に出力をする
これら機能に加えて実行時にできるだけ処理時間を短くし実行結果をわかりやすく表示させる機能を持ち合わせた自動巡回ツールの作成を目指した。

### 2. 目標・目的
Webサイトを網羅的に検査をしできるだけ脆弱性を検出でき、実際に運用が出来るような自動巡回ツールを作ることを目標として作成を開始した。

### 3. 参考にさせてもらったもの<br>
 [Pythonプログラミング VTuber サプー](https://www.youtube.com/@pythonvtuber9917/videos)
<br><br>
[【Pythonプログラミング入門】メモ化で高速化！cacheデコレータを使ってみよう！〜初心者向け〜](https://youtu.be/lRaSMlHY3aY?feature=shared)
<br><br>
[【Pythonプログラミング入門】自作モジュールの使い方を解説！〜VTuberと学習〜 【初心者向け】](https://youtu.be/X3uBMY3JQqM?feature=shared)
<br><br>
[HTMLでチェックボックスを表示する方法！基本的な作り方と使い方を解説　byウェブカツ #初心者 - Qiita](https://qiita.com/kazukichi/items/1af73244df0e67137531)
<br><br>
[【バッチファイル】ログの出力方法と日時取得／ログファイル名に日時取得 #bat – Qiita](https://qiita.com/pekosyu/items/a2d416f9f2afe9c40066)
<br><br>
[ローカルにpythonのCGI環境を構築　ほどよく解説しながらスピード重視で説明するよ](https://jimaru.blog/programming/python/local-cgi-python/)
<br><br>
[HTMLでformタグのaction属性に複数の送信先を指定する方法を現役エンジニアが解説【初心者向け】](https://magazine.techacademy.jp/magazine/32105)
<br><br>
[Webサーバーで動くPythonアプリ 【Windows 版】](https://irohaplat.com/windows-python-http-server-calculator-application/)
<br><br>
[CSSのコピペだけ！おしゃれな見出しのデザイン例まとめ6](https://saruwakakun.com/html-css/reference/h-design)
<br><br>
[図解！PythonでWEB スクレイピングを始めよう！(サンプルコード付きチュートリアル)](https://ai-inter1.com/python-webscraping/#st-toc-h-2)
<br><br>
[【HTML】フォーム作成の基本！formとinputの使い方](https://creive.me/archives/13526/)
<br><br>
[スクレイピング練習場（ベータ）](https://scraping-training.vercel.app/)
<br><br>
[図解！PythonのRequestsを徹底解説！(インストール・使い方)](https://ai-inter1.com/python-requests/)
<br><br>
[【コピペで完成】HTML・CSSのみで作る棒グラフのデザイン2選【アニメーション対応】 (pote-chil.com)](https://pote-chil.com/html-maker/bar-chart)
<br><br>
[table・tr・th・tdタグ | HTMLでの正しい表の構造と使い方・作り方を徹底解説 | Webのいろは (webnoiroha.net)](https://www.webnoiroha.net/html-table/)
<br><br>

## 機能
### 1. クローラにより実行可能な事
- 検査対象のWebサイトの脆弱性の検査
- Webサイトの規模の調査
- ローカル環境下によるツールの実行
- URL・パラメータ・ページタイトル・性能審査用のキーワードを表にして出力
- ドメインの指定
- 診断対象個数のそれぞれの合計割合をグラフで表示
- 検査するURLの数の制限
### 2. 抽出可能な診断対象
- HTML内に含まれる`「input type=”text”」(入力フォーム)`
<br>検出可能な脆弱性：クロスサイトスクリプティング(XSS)<br><br>

- HTML内に含まれる`「input type=”file”」`
<br>検出可能な脆弱性：不正ファイルのアップロード<br><br>

- HTML内に含まれる`「input type=”password”」`
<br>検出可能な脆弱性：パスワードセキュリティ<br><br>

- HTML内に含まれる`「input type=”hidden”」`
<br>検出可能な脆弱性：隠しフィールドに保存されているデータの悪用<br><br>

- HTML内に含まれる`「form」`
<br>検出可能な脆弱性：クロスサイトリクエストフォージェリ(CSRF)<br><br>

- HTML内に含まれる`「textarea」`
<br>検出可能な脆弱性：クロスサイトスクリプティング(XSS)<br><br>

- Webサイトを構築するHTMLに含まれる`MBSD{××××}`の内容
<br>検出可能：MBSD{××××}に含まれるキーワード<br><br>

- URL内に含まれるパラメータ
<br>検出可能な脆弱性：クエリ文字インジェクション<br><br>

## 実行例
### 1. サーバースタート.batファイルの実行
MBSD＿Web＿CSS.zipを解凍しサーバースタート.batファイルを実行してください。<br>
![image](https://github.com/user-attachments/assets/044757d8-2bc3-42ca-9795-15f39f039f79)
### 2. 許可確認画面
初めて実行する場合Pythonから権限の許可を問われる場合があります。その場合は、許可をしてください。<br>
※python自体がインストールされていない場合はインストールしてください。<br>
![image](https://github.com/user-attachments/assets/741246eb-c4fb-4d55-940e-96f0caa5cb11)<br>
Windowsからの許可を問われる場合があります。その場合は、許可をしてください。<br>
詳細情報をクリックして、右の画面に遷移するので実行してください。<br>
![image](https://github.com/user-attachments/assets/3355312d-cc08-41a6-bb19-73abd89584a0)
### 3. 診断のツールの実行
立ち上がったらテキストフィールドに検索対象のURLを入力し送信ボタンを押してください。<br>
検出するURLを制限する場所にチェックを入れると検査するURLの個数が制限されます。<br>
※URL入力欄には自分で空白(スペース)や、改行を入力しないでください。<br>
![image](https://github.com/user-attachments/assets/b6d18355-8677-4d46-9da2-773132798a28)
### 4. 実行結果の確認
このような形にになれば検査完了です。<br>
※棒グラフの長さは適切でないときがあります。<br>
![image](https://github.com/user-attachments/assets/30788f85-29ba-4678-b595-afa3a1276e65)
![image](https://github.com/user-attachments/assets/709f5baf-458f-435a-b5d9-40ad13197f81)
<br>
※注意事項
・Webサイトによっては検出までに時間がかかります。ブラウザのタブ部分が読込み中の場合は正常に動作しています。
・送信ボタンを二回押さないでください。
・二回目の検査をする場合は一度元の画面に戻り再読み込みをしてから行ってください。
## 動作条件
| 言語・フレームワーク   | バージョン |
| --------------------- | ---------- |
| Python                | 3.9.12     |
| urllib3               | 2.0.6      |

| 実行ブラウザ           | バージョン                                         |
| --------------------- | -------------------------------------------------- |
| Microsoft Edge        | 119.0.2151.44  (公式ビルド)　(64 ビット)         　　|
| Google Chrome         | 119.0.6045.124（Official Build) (64 ビット）        |
| Firefox               | 116.0.3        (64ビット)                           |

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
検査するURLを受けとりそのURLを元に解析をして結果を表示する<br>
動作概要<br>
①検査URLをフォームから受け取る<br>
②結果を表示するHTMLファイルを取得<br>
③検査URLの検査を開始<br>
④検査結果をHTMLのテーブルテンプレートとして保存する<br>
⑤検査URLの中の脆弱性がある同じドメインのURLの検査を開始<br>
⑥同様にテーブルテンプレートを保存<br>
⑦ドメインURLの数だけ⑤、⑥を繰り返す<br>
⑧②のHTMLファイルを保存したテーブルを表示するように書き換え<br>
⑨書き換えたHTMLを出力する<br>


### 2. GetHTML.py
- ①GET＿HTML<br>
引数 : url(文字列型)<br>
戻り値 : html(文字列型)<br>


　与えられたurlを元にHTMLを取得<br>
　utf-8でhtmlをデコードしエラーが出た場合はShift-JISでデコード<br>
　デコードができなかった場合はからのhtmlの文字列を返す<br>
　メモ化をしており引数が同じの二回目以降の処理は短縮される<br>

### 3. GetTAG.py
- ①GET_TAG<br>
引数 : html(文字列型)<br>
戻り値 : taglist(文字列型配列)<br>

与えられたhtmlを元に存在するタグを抽出。<br>
タグを一つ一つ分けて配列に格納<br>


### 4. INPUT.py
- ①GET＿INPUT<br>
引数 : 文字列型　html…html文が文字列として格納されている。<br>
戻り値 ：リスト  tagVul…タグの種類<br>
リスト  tagcount…検出したタグの個数<br>

変数htmlを引数として関数を実行すると、html文の中にあるタグの種類の個数を
tagcountに格納して返す。<br>
検出するタグは、&lt;input&gt;&lt;form&gt;&lt;textarea&gt;の３つと&lt;input&gt;の属性である　<br>　
text,file,password,hiddenを対象にして検出している。<br>
リストtagVulは添え字が0から始まり、<br>
&lt;input&gt;,text,file,password,hidden,&lt;form&gt;,&lt;textarea&gt;の順に格納されている。<br>
また、リストtagcountの個数の格納順はリストtagVulと共通である。<br>


### 5. MBSD＿SEARCH.py
- ①MBSD_SEARCH<br>
引数 : html(文字列型)<br>
戻り値 : result(文字列型配列)<br>

与えられたhtmlの中からMBSD{XXXX}のXXXXの内容があるか探す。<br>
あった場合は配列に格納してその結果を返す。<br>


### 6. mbsd_title.py
- ①HTML_TITLE<br>
引数 : html(文字列型)<br>
戻り値 : title(文字列型配列)<br>

与えられたhtmlからタイトルを抽出しその結果を配列で返す。<br>

### 7. url_Getter.py
- ①getURL(url,html) <br>
引数:url(文字列型),html(html文書を文字列で取得したもの:文字列型)<br>
戻り値: urls(文字列型配列)<br>

アクセス先に含まれる別のURLを重複がないように取り出す。(複雑すぎるパラメータを含む場合はそのURLは取り出せない)<br>
この関数は<a>タグ内のhrefのリンクとhtml文書を解析してURLらしきものを全て検出できるようにしました。この解析処理を高速に終わらせる
ために正規表現を用いました。<br>


- ②del_equal_url(urls)<br>
引数:urls(文字列型配列)<br>
戻り値: urls(文字列型配列)<br>

同じURLが含まれていた場合に削除します<br>
mark_visited(url),is_visited(url),reset_visited_urls()の関数を用いて同じURLを削除する機構を作りました。使う関数ごとに差別化する(保存する領域を差別化する)ためにdel_equal_url(urls)内では同じ動作をする別の関数を用いています。<br>


### 8. url_Host.py
- ①getURL_host(url)<br>
引数:url(文字列型)<br>
戻り値: host(文字列型)<br>
ホスト名を取得します<br>


### 9. url_Parameter.py
- ① getURL_para(url)<br>
引数:url(文字列型)<br>
戻り値:passstr(文字列型)<br>

URLを取得した際のパラメータが'&'などの文字列が'&amp;'のようにエスケープされる<br>
とパラメータが正常に取得できないので正常に取得できるように工夫しました。<br>

- ②getURL_path_para(url)<br>
引数:url(文字列型)<br>
戻り値:path_parameters(文字列型)又はなし<br>

URLに含まれるパスパラメータのみを取得する。パスパラメータがない場合は戻り値は返されません。<br>


### 10. is_image_url.py
- ①is_image_url(url)<br>
引数:url(文字列型)<br>
戻り値:Ture、False<br>

URLに画像ファイル、.js、.json、.cssを含むURLがある  時にTrue,ない時にFalseが
戻り値として返す正規表現を用いてURL(文字列型)に対する検索をかけました。<br>
より高速に解析できると考えます。<br>

- ②image_del(urls)<br>
引数:urls(文字列型配列)<br>
戻り値:urls(文字列型配列)<br>

URLにis_image_url(url)を適用、TrueのときにそのURLを削除しurlsの上書き保存し
ます。<br>


### 11. url_Visited.py
- ①mark_visited(url)<br>
引数:url(文字列型)<br>
戻り値:なし<br>

URLを保存します(マークする)。<br>


- ②is_visited(url)<br>
引数:url(文字列型)<br>
戻り値:Ture、False<br>

url(文字列型)が保存されている(mark_visited(url)が既に実行されている)ときにTrue,そ
れ以外はFalseが戻り値として返します。<br>


- ③reset_visited_urls()<br>
引数:なし<br>
戻り値:なし<br>

mark_visited(url)で保存されたデータを全て削除します。<br>


### 12. url_Domain_Select_Getter.py
- ①is_getURL_selected_by_domain(source_url, comparison_url)<br>
引数:source_url(文字列型),comparison_urll(文字列型)<br>
戻り値:Ture、False<br>

引数として指定されたURL(文字列型)2つに対して、ドメイン名が同じの場合True,ドイン名が異なる時にFalseが戻り値として返します。<br>







- ②getURL_selected_by_domain(url,html)<br>
引数:url(文字列型),html(html文書を文字列で取得したもの:文字列型)<br>
戻り値:domain_urls(文字列型配列)<br>

引数として指定されたURL(文字列型)とhtml(html文書を文字列で取得したもの)に対してドメイン名で絞りだした後にimage_del(urls)を用いて画像URLなどを削除します。その結果を戻り値として返します。<br>


### 13. url_Crawler .py
- ①url_crawling(url,html)<br>
引数:url(文字列型),html(html文書を文字列で取得したもの:文字列型)<br>
CRAWLING_RESTRICTIONの値を変えることで制限を変えることができる。<br>
値を増やすと検出するURLの個数が少なくなる。(初期値3)<br>
例：CRAWLING_RESTRICTIONの値が３の時、開始URLを含んで３個までのURLを取得してそこまでのURLのクローリングを実行し検査する
戻り値: crawling_urls(文字列型配列)<br>


引数として指定されたurl(文字列型)とhtml(html文書を文字列で取得したもの)に対し
てクローリングを実行し、結果を戻り値として返します<br>

### 14. danger_url.py
- ①danger_url.py(html)<br>
引数:html(html文書を文字列で取得したもの:文字列型)<br>
戻り値:ht_mbsd(文字列型配列),ht_title(文字列型配列),tagVul(文字列型配列), 
tagcount(整数列型配列),flag(整数型)<br>

引数として指定されたhtml(html文書を文字列で取得したもの)に対してMBSD{xxxx}の
xxxxの文字をht_mbsd、タイトルをht_title、脆弱性タグリスト名をtagVul、それに対応
するタグの個数をtagcountに格納して返します。<br>
flagは脆弱性が0の時に1になって返します。(ht_mbsd,tagcount全てが空値か0の時)<br>

