if __name__ == '__main__':
    urls = [
        ('事业', 'https://jshrss.jiangsu.gov.cn/col/col57210/index.html'),
        ('企业', 'https://jshrss.jiangsu.gov.cn/col/col57210/index.html'),
        ('民办非企业社团', 'https://jshrss.jiangsu.gov.cn/col/col57210/index.html')
    ]
    for parent_title, url in urls:
        print(url, parent_title)
