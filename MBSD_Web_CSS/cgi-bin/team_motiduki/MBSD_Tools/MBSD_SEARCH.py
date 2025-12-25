import re
from .GetTAG import GET_TAG
def MBSD_SEARCH(html):
    pattern = r'MBSD\{([^}]*)\}'    ##MBSD{xxxx}の正規表現

    matches = re.findall(pattern,html)  ##抽出してmatchesに格納
    
    return(matches)