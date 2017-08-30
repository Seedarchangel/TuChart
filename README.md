TuChart
=================
TuChart是一个基于Echarts和Tushare的股票视觉化应用
## 使用截图
#### 个股K线
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%203.30.19%20PM.png?raw=true)
#### 个股分笔
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%202.12.53%20AM.png)
#### 多图并列
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-28%20at%209.01.12%20PM.png)
#### 可拖拽／缩放
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/sample.gif)

## 使用方法
```pip install tuchart```

之后在tuchart的路径下，如

```/user/anaconda/lib/python2.7/site-packages/tuchart```

运行```python main.py```

tuchart在您电脑具体的目录路径可以使用```pip show tuchart```指令下返回的Location查看，如:
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/tuchart_path.png)
使用时在此路径后追加```/tuchart```即可

在左侧的菜单右键想要进行绘制的股票，选择数据类型，之后点击绿色箭头即可绘制。不建议同时绘制超过5张以上。
##### 注意：在下方绘图项数量为0时，点击箭头将会导致程序崩溃，将在下个版本做修复

![Manual](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/SLYJiZEBeD.gif)



## 依赖
请安装anaconda 2.7,并另外安装

1. pyecharts
2. tushare
使用```pip install pyecharts, tushare```即可安装

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

## 版本信息
下个版本将加入
* 各大指数数据
* 前十股东持股占比
* 股票行业列表缓存，避免每次开启程序时的加载
## 联系作者
* 邮箱：rzli2@illinois.edu
* 微信：seedarchangel








