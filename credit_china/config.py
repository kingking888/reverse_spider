# -*- coding: utf-8 -*-


# 信用陕西-行政处罚
xinyong_shanxi_settings = {
    "RETRY_ENABLED": True,
    "RETRY_TIMES": '9',
    "DOWNLOAD_TIMEOUT": '20',

    "ITEM_PIPELINES": {
        "credit_china.pipelines.CreditChinaPipeline": 300,
        "credit_china.pipelines.MongodbIndexPipeline": 340,
        # "credit_china.pipelines.MysqlTwistedPipeline": 360,
    },

    "DOWNLOADER_MIDDLEWARES": {
        "credit_china.middlewares.RandomUserAgentMiddleware": 400,
        "credit_china.middlewares.RandomProxyMiddlerware": 410,
        "credit_china.middlewares.RewriteRetryMiddleware": 420,
    }
}


# 中国市场监管行政处罚文书网
cfws_settings = {
    "RETRY_ENABLED": True,
    "RETRY_TIMES": '9',
    "DOWNLOAD_TIMEOUT": '20',

    "ITEM_PIPELINES": {
        "credit_china.pipelines.CreditChinaPipeline": 300,
        "credit_china.pipelines.MongodbIndexPipeline": 340,
        # "credit_china.pipelines.MysqlTwistedPipeline": 360,
    },

    "DOWNLOADER_MIDDLEWARES": {
        "credit_china.middlewares.RandomUserAgentMiddleware": 400,
        "credit_china.middlewares.RandomProxyMiddlerware": 410,
        "credit_china.middlewares.RewriteRetryMiddleware": 420,
    }
}


# 阿里巴巴文学
aliwx_settings = {
    "REDIRECT_ENABLED": False,
    "RETRY_ENABLED": True,
    "RETRY_TIMES": '9',
    "DOWNLOAD_TIMEOUT": '20',

    "SCHEDULER": "scrapy_redis.scheduler.Scheduler",
    "DUPEFILTER_CLASS": "scrapy_redis.dupefilter.RFPDupeFilter",
    "SCHEDULER_QUEUE_CLASS": "scrapy_redis.queue.SpiderPriorityQueue",
    "SCHEDULER_PERSIST": True,

    "ITEM_PIPELINES": {
        "credit_china.pipelines.CreditChinaPipeline": 300,
        "credit_china.pipelines.MongodbIndexPipeline": 340,
        # "credit_china.pipelines.MysqlTwistedPipeline": 360,
    },

    "DOWNLOADER_MIDDLEWARES": {
        "credit_china.middlewares.RandomUserAgentMiddleware": 400,
        "credit_china.middlewares.RandomProxyMiddlerware": 410,
        "credit_china.middlewares.RewriteRetryMiddleware": 420,
    }
}