TuChart
=================
TuChart是一个基于Echarts和Tushare的股票视觉化应用

[English Doc](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/En_US.md)
## 使用截图
#### 个股K线
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%203.30.19%20PM.png?raw=true)
#### 个股分笔
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%202.12.53%20AM.png)
#### 个股季度前十大股东
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Top_10.gif)
#### 多图并列，可拖拽／缩放
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/sample.gif)
#### 个股历史高频数据（例为1分钟线）
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-09-05%20at%2011.55.53%20PM.png)
##### 高频数据由单日Tick计算得出，具体计算方法来自Tushare作者Waditu：[如何用TICK数据生成分钟线数据](https://mp.weixin.qq.com/s?__biz=MzAwOTgzMDk5Ng==&mid=2650833965&idx=1&sn=e3e74639c068e7a1e41a35bb1decd313&chksm=80adb316b7da3a00de4191d4da6a5a7cab60fa3d282876fcf0b4d6dd8fc234528a316f5aa50a&mpshare=1&scene=1&srcid=090514fJTxEaB4CbnBI85x60&pass_ticket=qA7MkXEYQz2xA0uHwCD8eF43XfYsQMFMTyDT0euW7YFDRhLeVPR8dAxIaK6gxprk#rd)

## 使用方法
命令行```pip install tuchart```

#### 注意：为了保证最佳的使用效果，请确保您下载的是最新版本0.1.2.3

之后在tuchart的路径下，如

```/user/anaconda/lib/python2.7/site-packages/tuchart```

运行```python main.py```

tuchart在您电脑具体的目录路径可以使用```pip show tuchart```指令下返回的Location查看，如:
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/tuchart_path.png)
使用时在此路径后追加```/tuchart```即可

在左侧的菜单右键想要进行绘制的股票，选择数据类型，之后点击绿色箭头即可绘制。不建议同时绘制超过5张以上。


![Manual](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/SLYJiZEBeD.gif)



## 依赖
请安装anaconda 2.7,并另外安装

1. pyecharts
2. tushare
3. qtpy

使用```pip install tushare, qtpy```

以及

```pip install pyecharts==0.2.0```


即可安装


## 数据类型
Tuchart目前支持的数据类型有：
1. 未复权数据
* 日线
* 周线
* 月线
* 15分钟线
* 30分钟线
2. 前／后复权数据
* 日线
* 周线
* 月线
* 5分钟线
* 15分钟线
* 30分钟线
3. 个股分笔交易数据
##### 注意：因为数据源限制，使用5分钟线，15分钟线和30分钟线时，将无法定义日期。

## 更新信息
0.1.2.4
* 修复了Anaconda ver<4.0.2时，pyqt4不兼容的问题
* 为了更加稳定的绘图，修改dependency为pyecharts==0.2.0

0.1.2.3 
* 增加了每12小时缓存一次行业个股数据的脚本，12小时内将读取本地json，大幅缩短开启时间／降低接口负担
* 提高稳定性，降低崩溃几率
* 生成的图表尺寸根据当前窗口的大小自动调整
* 加入了新的大盘指数：
  1. 上证指数
  2. 深圳成指
  3. 沪深300指数
  4. 上证50
  5. 中小板
  6. 创业板



欢迎提交Issues。下个版本将加入
* 前十股东持股占比
* 多图绘制在同一个坐标轴内
* 其他


## 联系作者
* 邮箱：rzli2@illinois.edu
* 微信：seedarchangel








