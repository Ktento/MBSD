import urllib.request
from .GetHTML import GET_HTML
def GET_TAG(html):
    html=list(html)
    taglist = [] ##タグを１個ずつ格納
    first_tag=0
    for i in range(0,len(html),1):  ##0からリストhtmlの長さまで1ずつ繰り返す
        if html[i]=='<':    ##文字が<だったら
            first_tag=1
            tag = html[i]
        elif first_tag == 1:
            tag += html[i]
            if html[i]=='>' and first_tag==1:   ##文字が>かつfirst_tagが1だったら
                first_tag=0                     ##first_tagを０にする            
                taglist.append(tag)
    return taglist
