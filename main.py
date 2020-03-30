# -*- coding: utf-8 -*-
from scrapy.cmdline import execute


# 信用陕西-行政处罚-更新前5页
# execute("scrapy crawl credit_shanxi".split())
# 中国市场监管行政处罚文书网
# execute("scrapy crawl cfws_samr".split())
# 阿里巴巴文学小说
execute("scrapy crawl aliwx".split())
# 一次运行所有spider
# execute("scrapy crawlall".split())