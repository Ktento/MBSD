@echo on
chcp 65001

python -m ensurepip --default-pip
python -m pip install --upgrade pip
python -m pip install urllib3

REM Python 3のHTTPサーバーをCGIモードで起動
start python -m http.server --cgi

REM 指定したURLを開く（注意: ここでは URL のスペースを削除しています）
start "" "http://localhost:8000/hello.html"

REM ユーザーがキーを押すまで待機
pause
