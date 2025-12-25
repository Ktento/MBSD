from urllib.parse import urlparse, parse_qs, urlsplit
import re

def getURL_para(url):

    # 削除する文字列(&のときにエスケープされるとパラメータ名に影響されるため)
    string_to_remove = "amp;"

    # 正規表現パターンを作成
    pattern = re.escape(string_to_remove)

    # 文字列から特定の文字列を削除
    modified_url = re.sub(pattern, "", url)


    # URLを解析してクエリ文字列を取得
    parsed_url = urlparse(modified_url)
    query_params = parse_qs(parsed_url.query)

    # URLを分割して取得
    parsed_url = urlsplit(modified_url)
    path = parsed_url.path
    passstr=""
    # パスパラメータを取得
    if(path != "" and path != "/"):
        path_parameters = parsed_url.path.strip('/')
        passstr+=f"パスパラメータ: {path_parameters}"
    else:
        passstr+="URLにはパスパラメータが存在しません。"

    # パラメータ群の出力
    for key, value in query_params.items():
        passstr+=f"パラメータ名: {key}, 値: {value[0]}"
    
    #結果が文字列型で返される
    return passstr

'''パスパラメータの数(いくつ連なっているか)をカウントする関数。使う予定だったが検査方法を変えたため使わなくなった
def count_path_para(url):
    parsed_url = urlparse(url)
    path = parsed_url.path

    # 最初の要素は空の文字列またはスラッシュになるため、除外する
    path_parameters = path.split('/')
        
    path_parameters = [param for param in path_parameters if param]
    return len(path_parameters)
'''

def getURL_path_para(url):
    # 削除する文字列
    string_to_remove = "amp;"

    # 正規表現パターンを作成
    pattern = re.escape(string_to_remove)

    # 文字列から特定の文字列を削除
    modified_url = re.sub(pattern, "", url)

    # URLを分割して取得
    parsed_url = urlsplit(modified_url)
    path = parsed_url.path

    # パスパラメータを取得
    if(path != "" and path != "/"):
        path_parameters = parsed_url.path.strip('/')

        #結果が文字列型配列で返される
        return path_parameters
    else:

        return ""