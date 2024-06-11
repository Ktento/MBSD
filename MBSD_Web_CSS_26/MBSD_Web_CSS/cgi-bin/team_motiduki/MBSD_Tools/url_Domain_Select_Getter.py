from .url_Host import getURL_host
from .url_Getter import getURL
from .is_image_url import image_del

#ドメイン名が同じのときにTure,その他はFalseを返す関数
def is_getURL_selected_by_domain(source_url, comparison_url):
	if getURL_host(source_url) in comparison_url:
		return True
	else:
		return False

#画像URLや.js、.json、.cssが含まれるURL,引数で指定したurlのドメイン名のURLでURLを絞る関数
def getURL_selected_by_domain(url,html):
	domain_urls = getURL(url,html)

	#引数で指定したurlのドメイン名でURLを絞る処理(引数で指定したurlのドメイン名ではない場合削除する)
	i = 0
	while i < len(domain_urls):
		if is_getURL_selected_by_domain(url,domain_urls[i]):
			pass
		else:
			del domain_urls[i]
			i -= 1
		i += 1

	#画像URLや.js、.json、.cssが含まれるURLが見つかった場合削除
	image_del(domain_urls)

	#結果が文字列型配列で返される
	return domain_urls
