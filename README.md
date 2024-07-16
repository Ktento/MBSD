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

## 前談
### 1. どのような機能を目指したか
今回作成したツールは、大会を主催しているMBSDから提示されている競技概要に則り自動巡回ツールを作成した。ツールに搭載する為に考えた機能としては、複数あるので個々に挙げる。

診断対象先であるWebサイトの入力フォーム数
Webサイト内に存在するURLの検出及び出力
診断対象のパラメータの出力
Webサイトのコンテンツ内に含まれているMBSD｛××××｝のキーワードの出力
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
## 実行例
## 動作条件
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
