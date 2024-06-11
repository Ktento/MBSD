from .MBSD_SEARCH import MBSD_SEARCH
from .mbsd_title import HTML_TITLE
from .INPUT import GET_INPUT
def danger_url(html):
	ht_mbsd=MBSD_SEARCH(html)
	ht_title=HTML_TITLE(html)
	tagVul, tagcount = GET_INPUT(html)
	flag=0
	if len(ht_mbsd)==0 and all(element == 0 for element in tagcount[1:6]):
		flag=1

	return ht_mbsd,ht_title,tagVul, tagcount,flag