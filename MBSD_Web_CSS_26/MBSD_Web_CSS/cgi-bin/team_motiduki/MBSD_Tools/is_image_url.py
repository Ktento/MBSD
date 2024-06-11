import re

def is_image_url(url):
    image_pattern = re.compile(r'\b(https?)://[^\s/$.?#].[^\s]*\.(png|jpe?g|gif|bmp|svg|webp|ico|js|json|css)\b')
    if re.match(image_pattern, url):
        return True
    else:
        return False

def image_del(urls):
    i = 0
    while i < len(urls):
        if is_image_url(urls[i]):
            del urls[i]
            i -= 1
        i += 1
    return urls