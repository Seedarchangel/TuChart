TuChart
=================
[English Doc](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/En_US.md)

TuChart是一个基于Echarts和Tushare的股票视觉化应用
## 使用截图
#### 个股K线
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%203.30.19%20PM.png?raw=true)
#### 个股分笔
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%202.12.53%20AM.png)
#### 个股季度十大股东
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Revised.gif)
#### 多图并列，可拖拽／缩放
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/sample.gif)
#### 个股历史高频数据（例为1分钟线）
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-09-05%20at%2011.55.53%20PM.png)

## 使用方法
命令行```pip install tuchart```

#### 注意：为了保证最佳的使用效果，请确保您下载的是最新版本0.1.2.5

之后在tuchart的路径下，如

```/user/anaconda/lib/python2.7/site-packages/tuchart```

运行```python main.py```

tuchart在您电脑具体的目录路径可以使用```pip show tuchart```指令下返回的Location查看，如:
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/tuchart_path.png)
使用时在此路径后追加```/tuchart```即可

在左上角的盒子选择数据类型

![manual](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-09-06%20at%201.33.26%20PM.png)

可以搜索你想要查看的股票

![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-11-06%20at%203.34.29%20PM.png)

然后在左侧的菜单右键想要进行绘制的股票，选择类型，之后点击绿色箭头即可生成。不建议同时绘制超过5张以上。

![Manual](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/SLYJiZEBeD.gif)


## 依赖
请安装anaconda 2.7或者3.6,并另外安装

1. pyecharts==0.2.0
2. tushare==0.8.6（更高版本会导致崩溃）
3. qtpy

使用
```pip install tushare==0.8.6```

```pip install qtpy```

以及

```pip install pyecharts==0.2.0```


即可安装.

python 3版本由@cansijyun提供，目前还未测试，可以在github下载后从Tuchart3.0 -beta文件夹运行，和2.7版本一样在文件夹下运行

```python main.py```即可


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
4. 个股高频历史数据（历史分钟）
* 1分钟线
* 5分钟线
* 15分钟线
* 30分钟线
* 60分钟线
##### 注意：可以使用新的历史分钟项查看历史任意单日的个股高频数据。高频数据由单日Tick计算得出，具体计算方法来自Tushare作者Waditu：[如何用TICK数据生成分钟线数据](https://mp.weixin.qq.com/s?__biz=MzAwOTgzMDk5Ng==&mid=2650833965&idx=1&sn=e3e74639c068e7a1e41a35bb1decd313&chksm=80adb316b7da3a00de4191d4da6a5a7cab60fa3d282876fcf0b4d6dd8fc234528a316f5aa50a&mpshare=1&scene=1&srcid=090514fJTxEaB4CbnBI85x60&pass_ticket=qA7MkXEYQz2xA0uHwCD8eF43XfYsQMFMTyDT0euW7YFDRhLeVPR8dAxIaK6gxprk#rd)
5. 个股10大股东排行。选择日期即可显示该年的各季度10大股东排行。

如图，选择2016年任意一天将呈现2016年每个季度的10大股东排行。
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-09-06%20at%2012.33.55%20AM.png?raw=true)



## 更新信息
0.1.2.6
* 增加了搜索功能，可以搜索股票代码／名称
* 支持根据编号陈列股票
* 优化了UI

0.1.2.5
* 增加了个股高频历史数据
  * 1分钟线
  * 5分钟线
  * 15分钟线
  * 30分钟线
  * 60分钟线
* 增加了个股10大股东排行 
  
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
* 数字货币，包括比特币，莱特币等


## 联系作者
* 邮箱：rzli2@illinois.edu

## Contributers
Special thanks to
* cansijyu（python3 版本，ui优化和搜索功能）
* cclauss







