# 从爬虫入门到周紫薇吃饱
  1，可口可乐冰激凌
  2.华莱士鸡肉卷
# 爬虫框架
# 数据方面
# 内容推荐
  1.了解http理论基础
  2.学习并掌握一些常见的加密算法
  3.了解一些网站开发技术和数据传输方式
  4.掌握JS基础语法以及浏览器的调试方法
# 方法推荐（掌握前端反爬的方法和思路）
  1.实战训练，多分析网站的反爬思路
    常见的反爬技术
      1检测User—Agent 使用session会话的形式储存cookie达到登录状态
      2检测IP请求频率
      3检测账户请求频率
      4检测referer
      5检测cookie钓鱼
      6异步数据加载
      7字体反爬
      8多种网页HTML结构
      9网页的随机class
      10防盗链
  2.查阅HTTP协议，请求各字段的含义和响应的状态信息
  3.学习JS语法，事件绑定，数据封装。
  4.多使用云服务商的产品和架构

  # 第二章
    http基础内容
    https
      TCP三次同步握手
      客户端验证服务器数字证书
# 第三章
   1.验证码的多种类型
    图像验证码
    滑块验证
    点击验证
    人机交互
    短信验证
    电话验证码
# 如何优化爬虫
    抓取解析存储三模块相互独立，逐步调用
 分布式爬虫的优势
    爬虫任务量是相通的
    爬虫的数量可以随意的加大和减少
 cookie的设置
    响应头的set-Cookie
    javascript代码设置成cookie
# mysql
    数据库定义语言：对数据库，表，列等结构进行改变的语句 关键字create,alter,drop
    数据库查询语言：用于查询数据库中表记录的语言。 关键字select,from,where,order by等
    数据操作语言：对表中的记录进行添加，删除，修改操作的语句。关键字delete,insert,update
    数据控制语言：用于定义数据库的访问权限和安全级别。 关键字grant revoke
# pymysql
# scrapy
  创建爬虫文件
    scrapy startproject 项目名称
  进入项目
   cd项目名称
  创建爬虫文件
    scrapy genspider 名字 域名
  修改start_urls成你想要爬取的页面
  对数据进行解析，在spider中的parse(response)中进行改写
    def parse(self, response):
      response.text获取网页源代码
      response.xpath()
      response.class()
      等等获取想要的数据
      xpath默认返回的是selector对象
            想要返回需要#extract()返回列表，extract_first() 返回一个数据，如果没有，返回None
  创建一个字典保存数据，用yield将字典返回给pipelines，进行持久化存储
  在pipelines中，进行数据存储
      class GamePipeline:#随意定义一个类
      def process_item(self, item, spider):  #处理数据的专用方法  item数据 spider爬虫
          return item#必须返回一个数据，否则下一个管道拿不到数据
  在settings中将管道打开
    ITEM_PIPELINES = {
   "game.pipelines.GamePipeline": 300,
    '管道的路径':优先级,优先级数越小，优先级越高
    }
  运行爬虫
    scrapy crawl 爬虫名字
# scrapy_splash
  安装尽量在linux中,
