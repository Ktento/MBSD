import re
def HTML_TITLE(html):
    a_pattern=re.compile(r'<title>(.*?)<\/title>')

    title=re.findall(a_pattern,html)
    if not title:
        title = ["Title not found"]
    return title