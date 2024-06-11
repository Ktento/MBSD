visited_urls = set()
visited_urls_use_getter = set()

#URLにアクセスしたかをチェックする関数(URL全体用)
def is_visited(url):
    return url in visited_urls

#URLにアクセスしたかをチェックする関数(同じURLを削除する関数用)
def is_visited_use_getter(url):
    return url in visited_urls_use_getter

#URLにアクセスしたときにアクセスしたことをマーク(保存)する関数(URL全体用)
def mark_visited(url):
    visited_urls.add(url)

#URLにアクセスしたときにアクセスしたことをマーク(保存)する関数(同じURLを削除する関数用)
def mark_visited_use_getter(url):
    visited_urls_use_getter.add(url)

#保存されたURLをリセット(全削除)する関数(URL全体用)
def reset_visited_urls():
    visited_urls.clear()

#保存されたURLをリセット(全削除)する関数(同じURLを削除する関数用)
def reset_visited_urls_use_getter():
    visited_urls_use_getter.clear()
