#coding:utf8

'''

clean style
===========
简介：清理代码中的样式，但是不清理标签

###功能和用途###

用作抓取网页中含有大量的无用标记，本程序能够有效的清理,但是请注意，程序使用正则表达式
性能的消耗可能会不小，请在自己的本机上跑，避免在服务器上运行

'''

import re


#默认忽略参数

#清理，参数为html内容
def clean(html,ignore="img",deltags="a|span"):
    
    #首先只留下标签
    if ignore == '':
        exp = "<(?P<tag>\w*)\s[^>]*>"#忽略为空，清除所有的标记
    else:
        exp = "<(?P<tag>(?!"+ignore+")\w*)\s[^>]*>"#只留下标签,但是保留a标签和img标签
        
    match =re.match(exp,html)
    sub = "<\g<tag>>"
    html = re.sub(exp,sub,html);
        
    #去除内有内容的标签,反向引用之前匹配到的tag
    exp = "<(?P<tag>\w*)>\s{0,}</(?P=tag)[^>]>"
    sub = ''
    html = re.sub(exp,sub,html)

    #清除脚本和样式表以及空行
    exp = "<(?P<tag>script|style)>[^<]*</(?P=tag)>"
    sub = ''
    html = re.sub(exp,sub,html)

    #删除a和span标签
    if deltags != '':
        exp = "</?(?:" +deltags+ ")?>"
        sub = ''
        html = re.sub(exp,sub,html)
    
    #清除所有换行符
    html = html.replace("\n","")
    return html

'''
进行测试
'''
#print clean("<strong sdfsd>he</strong><img src='' /><span>这是span标签</span><br /><a  href=''>这是a标签</a><html sdfs></html>","","")
