# -*- coding: utf-8 -*-
import scrapy
import scrapy_splash as spalsh


class HomepageSpider(scrapy.Spider):
    name = 'homepage'
    allowed_domains = ['baidu.com']
    start_urls = ['http://image.baidu.com/search/index?tn=baiduimage&word=%E7%BE%8E%E5%A5%B3']
    
    def start_requests(self):
        #args设置的是端点API的参数，关于API参数问题，请参考: `Splash HTTP API <./api.html>`_
        yield spalsh.SplashRequest(
            args={
                'html': 1,
                'png': 1,
                # 可选参数，表示spalsh在执行完成之后会等待一段时间后返回
                'wait': 5,
                #url是一个必须的参数，表明将要对哪个url进行请求
                'url' : self.start_urls[0],
                #http_method:表示Splash将向目标url发送何种请求
                'http_method': 'GET'
                # 'body' 用于POST请求，作为请求的请求体
                # 'lua_source' 如果需要执行lua脚本，那么这个参数表示对应lua脚本的字符串
            }
        )

    def parse(self, response):
        # 将response.body写入到一个.html文件中
        res: scrapy.http.response.Response = response
        page_data = str(res.body, encoding='utf-8')
        with open('./image.baidu.com.html', 'w+', encoding='utf-8') as fs:
            fs.write(page_data)