'''import urllib.request
from .GetTAG import GET_TAG
from .GetHTML import GET_HTML
def HTML_CONTENT(html):
    remove=GET_TAG(html)
    for i in range(0,len(remove),1):
        html=html.replace(remove[i],"")
    html=html.replace("\n","")
    html=html.replace("\t","")
    html=html.replace("\s","")
    return(html)
'''