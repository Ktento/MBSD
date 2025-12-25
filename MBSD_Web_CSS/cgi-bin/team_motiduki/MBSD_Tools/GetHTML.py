import urllib.request
from functools import cache
@cache
def GET_HTML(url):
    try:
        response = urllib.request.urlopen(url)
        content = response.read()
        html = content.decode('utf-8', 'replace')  # 無効なバイトを置き換える
    except UnicodeDecodeError as e:
        try:
            html = content.decode('shift-jis', 'ignore')  # Shift-JISでデコードする（無視して処理）
        except UnicodeDecodeError as e:
            print(f"decode EROOR\: {e}")
            html = ""
    except Exception as e:
        print(f"ERROR: {e}")
        html = ""

    return html
