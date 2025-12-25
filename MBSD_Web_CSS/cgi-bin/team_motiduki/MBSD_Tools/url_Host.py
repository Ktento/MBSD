from urllib.parse import urlparse

#URLを解析してホストを取得する関数
def getURL_host(url):
	# URLを解析してホストを取得
	parsed_url = urlparse(url)
	host = parsed_url.netloc

	# ホストの出力(文字列型)
	return host
