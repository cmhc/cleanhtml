clean style
===========

简介：清理代码中的样式，class和id但是不清理标签

###功能和用途###

用作抓取网页中含有大量的无用标记，本程序能够有效的清理,但是请注意，程序使用正则表达式
性能的消耗可能会不小，请在自己的本机上跑，避免在服务器上运行




###使用方法###

如果项目很小，那么可以直接将html.py直接放入你的项目里面，如果项目比较大，那么可以将cs放入你的项目里面作为包导入。


###函数参考###

####clean(html,ignore,tags)####

该模块主要的清理函数，用作清理标签里面的class，id和style，保留标签结构，不会清理标签，下面是一个演示

清理之前
	
	<p class="main">你好，这是一段<span class="bold">文本</span></p>

清理之后

	<p>你好，这是一段<spa>文本</span></p>
	
#####参数#####

<code>html</code> ，必须参数，需要清理的hmtl内容

<code>ignore</code> ，可选参数，需要忽略清理的标签，默认为img,如果有忽略的标签，请使用竖线分隔，比如span|a|ignore

<code>deltags</code> ，可选参数，需要删除的标签，默认为a|span ,如果有需要删除的标签，可以填写，有多个请用竖线隔开，比如a|span
