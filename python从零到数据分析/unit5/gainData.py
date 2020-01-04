"""
    @Author:sumu
    @Date:2020-01-03 20:54
    @Email:xvzhifeng@126.com

"""

import urllib.request

import chardet

def gain_websource(url):

    page = urllib.request.urlopen(url)
    htmlCode = page.read()
    data = htmlCode#.decoe('utf-8')
    return data