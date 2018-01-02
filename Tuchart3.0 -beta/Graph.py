#-*- coding:utf-8 -*-

from pyecharts import Kline, Line, Page,Overlap,Bar,Pie,Timeline
from pandas import DataFrame as df
import re
import tushare as ts
import time
import pandas as pd

import re



def graphpage(labels,mode_combo,startdate,enddate,optInterval,width1, height1):
    #optInterval='D/W/M' labels

    startdate = startdate.replace("/","-")#convert to tushare readable date
    enddate = enddate.replace("/","-")

    page = Page()

    for label in labels:  # generate numbers of graphs according to numbers of queries in treewidget
        label1 = re.split("-", label)
        overlap = Overlap()

        if label1[2]!="分笔" and label1[2]!="季度饼图": #"K线" "复权" "历史分钟"
            if mode_combo == "复权":
            #if optInterval == "qfq" or optInterval == "hfq":#复权
                array = ts.get_h_data(label1[1], start=startdate, end=enddate, autype="qfq")
                array = array.sort_index()
                time = array.index.format()  # 日期正是index
            elif mode_combo == "K线":
            #elif optInterval.isalnum() :#历史K线
                array = ts.get_k_data(label1[1], start=startdate, end=enddate, ktype=optInterval)
                time = array['date'].tolist()  # array.date
            elif mode_combo == "历史分钟":
                array_bfr = ts.get_tick_data(label1[1], date=startdate)
                array_bfr.sort_values("time")
                a = startdate + " " + array_bfr["time"]
                array_bfr["time"] = a
                array_bfr["time"] = pd.to_datetime(a)
                array_bfr = array_bfr.set_index("time")
                if label1[2] != "Volume" and label1[2] != "Amount":
                    price_df = array_bfr["price"].resample(optInterval).ohlc()  # resample重新取样,选出ohlc=open/high/low，提取除价格之外另外4列.close,tushare是ohcl
                    price_df = price_df.dropna()
                    array = price_df
                    time = price_df.index.format()

                elif label1[2] == "Volume":
                    vols = array_bfr["volume"].resample(optInterval).sum()  #resample重新取样，累加间隔内数值 relevant data processing algorithm taken from Jimmy, Creator of Tushare
                    vols = vols.dropna()
                    vol_df = pd.DataFrame(vols, columns=["volume"])
                    array = vol_df
                    time = vol_df.index.format()
                else:
                    amounts = array_bfr["amount"].resample(optInterval).sum()
                    amounts = amounts.dropna()
                    amount_df = pd.DataFrame(amounts, columns=["amount"])
                    array = amount_df
                    time = amount_df.index.format()

            #绘图方法

            if label1[2] == 'Kline':
                re_array = array[['open', 'close', 'high', 'low']]
                data_li = list(row.tolist() for index, row in re_array.iterrows())  # data_list = list(re_array.as_matrix())
                close = array['close'].tolist()
                kline = Kline(label1[0] + "-" + optInterval, width=width1*10/11, height = (height1*10/11) / len(labels))
                kline.add(label1[0], time, data_li, is_datazoom_show=True, datazoom_type="slider", yaxis_interval=1)
                overlap.add(kline)

                if len(close) > 10:
                    ma10 = calculateMa(close, 10)
                    line1 = Line(title_color="#C0C0C0")
                    line1.add(label1[0] + "-" + "MA10", time, ma10)
                    overlap.add(line1)
                if len(close) > 20:
                    ma20 = calculateMa(close, 20)
                    line2 = Line(title_color="#C0C0C0")
                    line2.add(label1[0] + "-" + "MA20", time, ma20)
                    overlap.add(line2)
                if len(close) > 30:
                    ma30 = calculateMa(close, 30)
                    line3 = Line(title_color="#C0C0C0")
                    line3.add(label1[0] + "-" + "MA30", time, ma30)
                    overlap.add(line3)

                page.add(overlap)
            else:#When label1[2]==open/close/volume
                if label1[2] == 'Open':
                    list_aft = array['open'].tolist()
                elif label1[2] == 'Close':
                    list_aft = close
                elif label1[2] == 'High':
                    list_aft = array['high'].tolist()
                elif label1[2] == 'Low':
                    list_aft = array['low'].tolist()
                elif label1[2] == 'Volume':#volume
                    list_aft = array['volume'].tolist()
                else:#amount
                    list_aft = array['amount'].tolist()

                line = Line(label1[0] + "-" + label1[2], width=width1 * 10 / 11, height=(height1 * 10 / 11) / len(labels))
                line.add(label1[0] + "-" + label1[2], time, list_aft, is_datazoom_show=True, yaxis_max="dataMax",
                         yaxis_min="dataMin", datazoom_type="slider")
                overlap.add(line)
                page.add(overlap)


        elif label1[2]=="分笔":
            array = ts.get_tick_data(label1[1], date=startdate)
            array = array.sort_values("time")
            date = array["time"].tolist()
            amount = array["amount"].tolist()
            atype = array["type"].tolist()
            price = array["price"].tolist()
            flag = ["bar" for i in date]
            for idx, val in enumerate(atype):
                if val == "卖盘":
                    amount[idx] = -amount[idx]
                if val == "中性盘":
                    amount[idx] = 0

            returnarray = list(zip(date, amount, flag, price))

            form = [e[1] for e in returnarray]
            time = [d[0] for d in returnarray]

            bar = Bar(label1[0] + "-" + label1[2], width=width1 * 10 / 11, height=(height1 * 10 / 11) / len(labels))
            bar.add(label1[0] + "-" + label1[2], time, form, is_datazoom_show=True, datazoom_type="slider", yaxis_min="dataMin", yaxis_max="dataMax")
            overlap.add(bar)

            line = Line(label1[0] + "price", width=width1 * 10 / 11, height=(height1 * 10 / 11) / len(labels))
            price = [e[3] for e in returnarray]
            line.add(label1[0] + "price", time, price, yaxis_min="dataMin", yaxis_max="dataMax", is_datazoom_show=True,
                     datazoom_type="slider",
                     yaxis_type="value")
            overlap.add(line, yaxis_index=1, is_add_yaxis=True)
            page.add(overlap)
        elif label1[2]=="季度饼图":
            datestr = startdate.split("-")
            thisyear = datestr[0]
            df2 = ts.top10_holders(code=label1[1], gdtype="1")
            test = df2[1]["quarter"].tolist()
            df_ready = df2[1]
            idxlist = []
            for idx, val in enumerate(test):
                a = val.split("-")
                if a[0] == thisyear:
                    # print a[0],idx
                    idxlist.append(idx)
            thing = df_ready.loc[idxlist]
            thing = thing.sort_values(["quarter", "name"])
            # print a[0],id
            name = thing["name"].tolist()
            value = thing["hold"].tolist()
            quarter = thing["quarter"].tolist()
            namearray = [name[i:i + 10] for i in range(0, len(name), 10)]
            valuearray = [value[j:j + 10] for j in range(0, len(value), 10)]
            quarterarray = [quarter[k:k + 10] for k in range(0, len(quarter), 10)]

            flag = ["pie" for i in namearray]
            num = [len(value) for k in namearray]
            returnarray = list(zip(namearray, valuearray, quarterarray, flag, num))

            timeline = Timeline(is_auto_play=False, timeline_bottom=0)  # zip(namearray,valuearray,quarter,flag,num)
            namearray = [c[0] for c in returnarray]
            valuearray = [d[1] for d in returnarray]
            quarter = [e[2] for e in returnarray]
            num = returnarray[0][4]

            for x in range(0, int(num / 10)):
                list1 = valuearray[x]
                names = namearray[x]
                quarters = quarter[x][0]

                for idx, val in enumerate(list1):
                    list1[idx] = float(val)

                pie = Pie(label1[0] + "-" + "前十股东", width=width1 * 10 / 11, height=(height1 * 10 / 11))

                pie.add(label1[0] + "-" + "前十股东", names, list1, radius=[30, 55], is_legend_show=False,
                        is_label_show=True, label_formatter="{b}: {c}\n{d}%")
                timeline.add(pie, quarters)
                # namearray = [y for y in namearray[x]]
            timeline.render()

    page.render()

def calculateMa(date, Daycount):
    sum = 0
    result = list(0 for x in date)  # used to calculate ma. Might be deprecated for future versions
    for i in range(0, Daycount):
        sum = sum + date[i] #累加每天数据
        #result[i] = round(sum / (i + 1),3) #每天平均数做成列表
        result[i] = None
    for i in range(Daycount, len(date)):
        sum = sum - date[i - Daycount] + date[i]#
        round(result[i], 3)
        result[i] =round(sum / Daycount,3)
    return result


