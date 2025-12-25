from .url_Domain_Select_Getter import getURL_selected_by_domain
from .url_Getter import del_equal_url
from .url_Visited import is_visited,mark_visited
from .GetHTML import GET_HTML
import urllib.request
import sys

#クローリングを実行する関数
def url_crawling(url,html,urllimit):
	# 検査するURLの制限
	CRAWLING_RESTRICTION = 3
	crawling_urls = getURL_selected_by_domain(url,html)
	mark_visited(url) #開始したURLのマーク

	#クローリングを実行する繰返し
	i = 0
	while i < len(crawling_urls):
		if i >= CRAWLING_RESTRICTION and urllimit==1:
			break
		target_url = crawling_urls[i]
		if is_visited(target_url):
			pass
		else:
			#URLの検査が終了したURLをマーク
			mark_visited(target_url)
			#検査したURLを一時的に格納する
			resistor_urls = getURL_selected_by_domain(target_url,GET_HTML(target_url))
			#一時的に格納されたURLをクローリングの結果が格納される配列に付け加える
			crawling_urls += resistor_urls
			#同じURLが格納される可能性があるので同じURLを削除する
			del_equal_url(crawling_urls)
		i += 1
		# ログを標準エラー出力に出力
		print('i = ' + str(i),file=sys.stderr)
		

	#有効ではないURLを削除
	a = 0
	while a < len(crawling_urls):
		try:
			f = urllib.request.urlopen(crawling_urls[a])
			f.close()
		except:
			del crawling_urls[a]
			a -= 1
		a += 1
		print('a = ' + str(a))

	#クローリングの結果が文字列型配列で返す
	return crawling_urls