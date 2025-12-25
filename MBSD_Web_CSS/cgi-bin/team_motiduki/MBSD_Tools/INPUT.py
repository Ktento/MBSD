import urllib.request
from .GetTAG import GET_TAG
from .GetHTML import GET_HTML
def GET_INPUT(html):
    tags=GET_TAG(html)
    target = ["<input>","<form>","<textarea>"] ##検出したいタグを指定
    tagcontent=[]   ##タグの分けた内容
    taglist=[]

    for i in range(0,len(tags),1):
        if len(tags[i].split(' '))>=2:
            taglist.append(tags[i].split(' ')[0]+">")
            tagcontent.append(tags[i].split(' ')[1])
        else:
            taglist.append(tags[i])
            tagcontent.append("NULL")

    tagVul = ['<input>','text','file','password','hidden','<form>','<textarea>']   ##タグ脆弱性リスト
    tagcount=[0,0,0,0,0,0,0,0]
   ##タグの表示
    for j in range(0,len(taglist),1):
        if (taglist[j] == target[0]):
            tagcount[0] =  tagcount[0]+ 1
            if 'type="text"' in tagcontent[j]: ##<input type="text">
                tagcount[1] = tagcount[1] + 1
            elif 'type="file"' in tagcontent[j]:   ##<input type="file">
                tagcount[2] = tagcount[2] + 1
            elif 'type="password"' in tagcontent[j]:   ##<input type="password">
                tagcount[3] = tagcount[3] + 1
            elif 'type="hidden"' in tagcontent[j]: ##<input type="hidden">
                tagcount[4] = tagcount[4] + 1
        elif(taglist[j] == target[1]):  ##<form>
            tagcount[5] = tagcount[5]+ 1
        elif(taglist[j] == target[2]):
            tagcount[6] = tagcount[6] + 1

    return tagVul,tagcount