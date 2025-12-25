from urllib.error import URLError
import re
from .url_Host import getURL_host
from .url_Visited import is_visited_use_getter,mark_visited_use_getter,reset_visited_urls_use_getter
from .url_Parameter import getURL_path_para

#同じURLを削除する関数(厳密には同じ文字列がある時に削除する関数)
def del_equal_url(urls):

	i = 0
	while i < len(urls):
		if is_visited_use_getter(urls[i]):
			del urls[i]
			i -= 1
		else:
			mark_visited_use_getter(urls[i])
		i += 1
	reset_visited_urls_use_getter()

	#結果が文字列型配列で返される
	return urls

#HTML文書中から全てのURLを取得する関数
def getURL(url, html):

	# URLを取り出すための正規表現パターン
	url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))[^<"\',\s]+')

	# URLの正規表現パターンに合致するものを全て見つけ出す。引数のURLをurlsの先頭に格納
	urls = re.findall(url_pattern, html)
	urls = [url] + urls

	# タグを検出するための正規表現パターン
	a_pattern = re.compile(r'<a\s+.*?href=[\'"]?([^\'" >]+)')

	# HTMLコードからタグを検出して表示する
	rinks = re.findall(a_pattern, html)

	#<a>タグのリンクとして検出したものを先ほど見つけ出したURLと比較してなければurlsに格納
	for i in range(0,len(rinks),1):
		a = 0
		for j in range(0,len(urls),1):
			if(rinks[i] != urls[j]):
				a += 1
		#ここのif文でurlsにrinks[i]が含まれていないときにture,<a>タグのhrefの表示形式に応じて適切なURLを取得
		if(a == len(urls)):
			check_rink = rinks[i]
			if check_rink.startswith('//'):
				if 'https' in url:
					urls.append('https:' + rinks[i])
				elif 'http' in url:
					urls.append('http:' + rinks[i])
				else:
					urls.append('file:' + rinks[i])
			elif check_rink.startswith('./'):
				urls.append(rinks[i])
			elif check_rink.startswith('/'):
				if 'https' in url:
					urls.append('https://' + getURL_host(url) + rinks[i])
				elif 'http' in url:
					urls.append('http://' + getURL_host(url) + rinks[i])
				else:
					urls.append('file://' + getURL_host(url) + rinks[i])
			elif '#' in check_rink:
				if 'https' in url:
					urls.append('https://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i].split('#')[0])
				elif 'http' in url:
					urls.append('http://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i].split('#')[0])
				else:
					urls.append('file://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i].split('#')[0])
			else:
				try:
					if 'https' in url:
						urls.append('https://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i])
					elif 'http' in url:
						urls.append('http://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i])
					else:
						urls.append('file://' + getURL_host(url) + '/' + getURL_path_para(url) + '/' + rinks[i])
				except URLError as e:
					print(f"URLエラーが発生しました: {e}")
					urls.append(rinks[i])


	#同じURLを取得したときに削除する
	del_equal_url(urls)
	
	#結果が文字列型配列で返される
	return urls