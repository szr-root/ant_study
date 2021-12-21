class UrlManger():
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_url(self, url):
        if url is None or len(url) == 0:
            return
        if url in self.new_urls or url in self.old_urls:
            return
        self.new_urls.add(url)

    def add_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.new_urls.add(url)

    def get_url(self):
        if self.has_new_url():
            url = self.new_urls.pop()
            self.old_urls.add(url)
            return url
        else:
            return None

    def has_new_url(self):
        return len(self.new_urls) > 0


if __name__ == '__main__':
    url_manager = UrlManger()
    url_manager.add_url('url1')
    url_manager.add_urls(['', ' ', 'url1', 'url2'])
    print(url_manager.new_urls, url_manager.old_urls)
    print('#' * 30)
    f = url_manager.get_url()
    print(f, url_manager.new_urls, url_manager.old_urls)
    print('#' * 30)
    f2 = url_manager.get_url()
    print(f2, url_manager.new_urls, url_manager.old_urls)
