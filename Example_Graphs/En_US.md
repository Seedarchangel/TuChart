TuChart
=================
TuChart is a plotting tool for the Chinese stock market, based on Tushare and Echarts.


## Usage Examples
#### Candlestick Charts
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%203.30.19%20PM.png?raw=true)
#### Tick Charts
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/Screen%20Shot%202017-08-29%20at%202.12.53%20AM.png)
#### Major Shareholders
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/New_Top_10.gif?raw=true)
#### Drag and Zoom
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/sample.gif)

## How to Use
First, install dependencies

```pip install tushare, pyecharts==0.2.0```

To install Tuchart, enter
```pip install tuchart```
in your terminal

#### Notice：For best plotting experience，please download the latest version = 0.1.2.5

then, under your tuchart directory, e.g:

```/user/anaconda/lib/python2.7/site-packages/tuchart```

run```python main.py```

The exact path of tuchart in your directory can be located by```pip show tuchart```which will return its location:
![notebook-0](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/tuchart_path.png)
add```/tuchart```to pinpoint the tuchart directory.

Right click to choose the name of stock and type of data you would like to plot. Then, press the green arrow button to plot. Due to the constraints of size, it is recommended to plot fewer than 5 graphs at the same time.

![Manual](https://github.com/Seedarchangel/TuChart/blob/master/Example_Graphs/SLYJiZEBeD.gif)

## Currently Supported Datatypes
* Raw Stock Data
  * Daily average
  * Weekly average
  * Monthly average
  * 15 minute average
  * 30 minute average
* Restoration Data
  * Daily average
  * Weekly average
  * Monthly average
  * 15 minute average
  * 30 minute average
* Tick data of individual stocks
* High frequency data within one day
* Top Shareholders

## Updates
0.1.2.5
* Supports plotting for High frequency data 
  * 1 minute average
  * 5 minute average
  * 15 minute average
  * 30 minute average
* Supports plotting of top shareholders within a year.

0.1.2.4
* Fixed dependency issues when user has PYQT4 Layer

0.1.2.3
* Added script to save stock list every 12 hours
* Increased stability
* Auto-resize Image according to size of the app
* Added more stock indexes

## Contact:
Email: rzli2@illinois.edu

Wechat: seedarchangel

