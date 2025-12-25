import urllib.request
import time
import re
from MBSD_Tools import GET_HTML,getURL_selected_by_domain,getURL_para,visited_urls_setter,is_visited,MBSD_SEARCH,GET_INPUT,HTML_TITLE
##検査するURLを入力
start_url='https://javeo.jp/practice_scraping/'

#指定されたURLの検査
html=GET_HTML(start_url)
print("\n\n検査対象URL:")
print(start_url)
#MBSD{XXX}のリスト
print("MBSDのリスト:",end="")
print(MBSD_SEARCH(html))
##inputの数
tagVul,tagcount = GET_INPUT(html)
for j in range(0,len(tagVul),1):
	print(tagVul[j]+" = "+str(tagcount[j])+"  ",end="")
##タイトル
print("\nタイトル:",end="")
print(str(HTML_TITLE(html)))
##パラメータ
getURL_para(start_url)

#指定されたＵＲＬの中の有効なドメインのURLの検査
start_sate = getURL_selected_by_domain(start_url,html)
visited_urls_setter(start_sate)
for i in range(0,len(start_sate),1):
	html=GET_HTML(start_sate[i])
	print("\n\n検査対象URL:")
	print(start_sate[i])
	#MBSD{XXX}のリスト
	print("MBSDのリスト:",end="")
	print(MBSD_SEARCH(html))
	##<input type=text,file,password,hidden>,<form><textarea>の数
	tagVul,tagcount = GET_INPUT(html)
	for j in range(0,len(tagVul),1):
		print(tagVul[j]+" = "+str(tagcount[j])+"  ",end="")

	##タイトル
	print("\nタイトル:",end="")
	print(str(HTML_TITLE(html)))

	##パラメータ
	getURL_para(start_sate[i])


print("実行時間 ",end="")
print(time.perf_counter())