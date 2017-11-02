#-*- coding:utf-8 -*-
from __future__ import print_function
import os,sys,sip,time
from datetime import datetime,timedelta
from qtpy.QtWidgets import QTreeWidgetItem,QMenu,QApplication,QAction,QMainWindow
from qtpy import QtGui,QtWidgets
from qtpy.QtCore import Qt,QUrl,QDate
from Graph import graphpage
from layout import Ui_MainWindow
from pandas import DataFrame as df
import pandas as pd
import tushare as ts
import cPickle
import numpy as np
import warnings
warnings.filterwarnings("ignore")
list1 = []


class MyUi(QMainWindow):
    def __init__(self):
        super(MyUi, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        cwd = os.getcwd()
        cwd = str(cwd)
        if os.path.isfile(cwd+"/time"):
            with open("time","r") as outfile:#reads current time
                history = cPickle.load(outfile)
            if (datetime.now()-history).total_seconds()<43200: #measures if time elapse>12 hours
                print("Less than 12 hours. Loading previously saved Pickle...")
                #with open("time","w") as infile: #update time
                    #cPickle.dump(datetime.now(),infile)

            else:
                print("More than 12 hours. Updating Pickle...")
                data = ts.get_industry_classified()
                with open("class","w+") as outfile:
                    cPickle.dump(data,outfile)
                now = datetime.now()
                with open("time", "w+") as outfile: #update time
                    cPickle.dump(now, outfile)

        else:
            print("No Pickle found!") #If this is first time using tuchart in this directory
            data = df()
            data = ts.get_industry_classified()
            with open('class', 'w+') as outfile: #records pickle
                cPickle.dump(data, outfile)
            now = datetime.now()
            with open("time", "w+") as outfile:
                cPickle.dump(now,outfile)

        with open("class", "r") as infile:  # reads current time
            series = cPickle.load(infile)
        #series = pd.read_json(cwd + "\\class.json")
        #series = ts.get_industry_classified()
        series = pd.DataFrame(series)

        curdate = time.strftime("%Y/%m/%d")  # gets current time to put into dateedit
        curdateQ = QDate.fromString(curdate,"yyyy/MM/dd")

        dateobj = datetime.strptime(curdate, "%Y/%m/%d")#converts to datetime object

        past = dateobj - timedelta(days = 7)  #minus a week to start date
        pasttime = datetime.strftime(past, "%Y/%m/%d")
        pastQ = QDate.fromString(pasttime,"yyyy/MM/dd") #convert to qtime so that widget accepts the values



        pastL = dateobj - timedelta(days=30)  # minus a month to start date
        pasttimeL = datetime.strftime(pastL, "%Y/%m/%d")
        pastQL = QDate.fromString(pasttimeL, "yyyy/MM/dd")


        np_indexes = np.array([['sh', '上证指数', '大盘指数'],
                               ['sz', '深证成指', '大盘指数'],
                               ['hs300', '沪深300指数', '大盘指数'],
                               ['sz50', '上证50', '大盘指数'],
                               ['zxb', '中小板', '大盘指数'],
                               ['cyb', '创业板', '大盘指数']])
        indexes = df(data=np_indexes,
                     index=range(5000, 5006),
                     columns=["code", "name", "c_name"])
        series = indexes.append(series)
        list1_bfr = series["c_name"].tolist()  #Get industry categories. Filters out redundant ones
        list1 = list(set(list1_bfr))
        list1.sort(key=list1_bfr.index)
        #w = database()
        #zsparent = QTreeWidgetItem(self.ui.treeWidget)
        #zsparent.setText(0,"股票指数")
        #zsnames =["上证指数-sh","深圳成指-sz","沪深300指数-hs300","上证50-"]

        self.init_treeWidget(list1,series)

        self.ui.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeWidget.customContextMenuRequested.connect(self.openMenu)

        #self.ui.webView.setGeometry(QtCore.QRect(0, 30,1550, 861))
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "render.html")) #path to read html file
        local_url = QUrl.fromLocalFile(file_path)
        self.ui.webView.load(local_url)
        #self.ui.commandLinkButton.setFixedSize(50, 50)
        self.ui.search_btn.clicked.connect(lambda: self.search_comp(series))
        self.ui.init_code_btn.clicked.connect(lambda: self.code_sort_tree(series))
        self.ui.init_category_btn.clicked.connect(lambda: self.init_treeWidget(list1, series))

        self.ui.commandLinkButton.clicked.connect(self.classify)  #when the arrow button is clicked, trigger events


        #self.ui.commandLinkButton.clicked.connect(lambda action: self.classify(action, self.ui.treewidget))
        #  QSizePolicy
        try:
            retain_size = self.ui.dateEdit_2.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.dateEdit_2.setSizePolicy(retain_size)
            retain_size = self.ui.comboBox.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.comboBox.setSizePolicy(retain_size)
            retain_size = self.ui.label_2.sizePolicy()
            retain_size.setRetainSizeWhenHidden(True)
            self.ui.label_2.setSizePolicy(retain_size)
        except AttributeError:
            print("No PYQT5 Binding! Widgets might be deformed")
        self.ui.dateEdit.setDate(pastQL)
        self.ui.dateEdit_2.setDate(curdateQ)#populate widgets
        self.ui.dateEdit.setCalendarPopup(True)
        self.ui.dateEdit_2.setCalendarPopup(True)
        self.ui.comboBox.addItems(["D", "W", "M", "5", "15", "30", "60"])
        self.ui.treeWidget_2.setDragDropMode(self.ui.treeWidget_2.InternalMove)
        self.ui.treeWidget_2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.treeWidget_2.customContextMenuRequested.connect(self.openWidgetMenu)
        #self.ui.toolbutton.clicked.connect(lambda action: self.graphmerge(action, CombineKeyword))
        self.ui.combobox.currentIndexChanged.connect(lambda: self.modifycombo(pastQL,pastQ))

    def init_treeWidget(self, list1, series):
        self.ui.treeWidget.clear()
        for j in list1:
            parent = QTreeWidgetItem(self.ui.treeWidget)  #populate treewidget with names
            parent.setText(0,j)
            var = series.loc[series["c_name"] == j]
            list2 = var["code"].tolist()
            name = var["name"].tolist()
            #var = showcollection(i) #Display database items
            for idx,val in enumerate(list2):
                child = QTreeWidgetItem(parent)
                child.setText(0, name[idx]+"-"+str(val))
                #for i in Drag:
                    #grandson = QTreeWidgetItem(child)     #Commented out because increases program response time
                    #grandson.setText(0, i)
        #self.ui.treeWidget.itemDoubleClicked.connect(self.onClickItem) #Display Collection items

    def code_sort_tree(self, companies):
        self.ui.treeWidget.clear()
        sorted_comps = companies.sort_values(["code"])
        code_list = sorted_comps["code"].tolist()
        name_list = sorted_comps["name"].tolist()
        shares_parent = QTreeWidgetItem(self.ui.treeWidget)
        shares_parent.setText(0, "个股行情")
        for idx, val in enumerate(code_list):
            child = QTreeWidgetItem(shares_parent)
            child.setText(0, name_list[idx] + "-" + str(val))
        self.ui.treeWidget.expandToDepth(0)

    def search_comp(self, companies):
        self.ui.treeWidget.clear()
        text = self.ui.search_lineEdit.text()
        filtered_codes = companies[companies['code'].str.contains(text)]
        filtered_names = companies[companies['name'].str.contains(text)]
        filtered_comps = filtered_codes.append(filtered_names)
        code_list = filtered_comps["code"].tolist()
        name_list = filtered_comps["name"].tolist()
        parent = QTreeWidgetItem(self.ui.treeWidget)
        parent.setText(0, "搜索结果")
        for idx, val in enumerate(code_list):
            child = QTreeWidgetItem(parent)
            child.setText(0, name_list[idx] + "-" + str(val))
        self.ui.treeWidget.expandToDepth(0)


    def modifycombo(self,pastQL,pastQ):
        if self.ui.combobox.currentText()==u"复权": #if 复权 is selected, clear all existing queries to avoid value conflict
            self.ui.label_2.show()
            self.ui.dateEdit_2.show()
            self.ui.dateEdit.setDate(pastQL)
            self.ui.interval_label.show()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["hfq", "qfq"])
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"K线":
            self.ui.label_2.show()
            self.ui.dateEdit_2.show()
            self.ui.dateEdit.setDate(pastQL)
            self.ui.interval_label.show()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["D", "W", "M", "5", "15", "30", "60"])#same as above
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"分笔数据":
            self.ui.interval_label.hide()
            self.ui.comboBox.hide()
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.dateEdit.setDate(pastQ)
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"历史分钟":
            self.ui.interval_label.hide()
            self.ui.comboBox.show()
            self.ui.comboBox.clear()
            self.ui.comboBox.addItems(["1min","5min","15min","30min","60min"])
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.dateEdit.setDate(pastQ)
            self.ui.treeWidget_2.clear()
        if self.ui.combobox.currentText()==u"十大股东":
            self.ui.interval_label.hide()
            self.ui.comboBox.hide()
            self.ui.label_2.hide()
            self.ui.dateEdit_2.hide()
            self.ui.treeWidget_2.clear()

    def openMenu(self,position):
        indexes = self.ui.treeWidget.selectedIndexes()
        item = self.ui.treeWidget.itemAt(position)
        db_origin = ""
        #if item.parent():
         #   db_origin = item.parent().text(0)
        collec = str(item.text(0).encode("utf-8"))
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            while index.parent().isValid():
                index = index.parent()
                level = level + 1
            menu = QMenu()
            #print((collec, db_origin))
            if level ==0:
                pass
            else:
                #keyarray = GetKeys(collec, db_origin)
                #if "Open" in keyarray:
                if self.ui.combobox.currentText()==u"K线":
                    menu.addAction(QAction("Kline", menu, checkable=True))
                    menu.addAction(QAction("Open", menu, checkable=True))
                    menu.addAction(QAction("Close", menu, checkable=True))#open up different menu with different kind of graphs
                    menu.addAction(QAction("High", menu, checkable=True))
                    menu.addAction(QAction("Low", menu, checkable=True))
                    menu.addAction(QAction("Volume", menu, checkable=True))
                    #menu.addAction(QAction("P_change", menu, checkable=True))
                    #menu.addAction(QAction("Turnover",menu,checkable=True))
                if self.ui.combobox.currentText()==u"复权":
                    menu.addAction(QAction("Kline", menu, checkable=True))
                    menu.addAction(QAction("Open", menu, checkable=True))
                    menu.addAction(QAction("Close", menu, checkable=True))
                    menu.addAction(QAction("High", menu, checkable=True))
                    menu.addAction(QAction("Low", menu, checkable=True))
                    menu.addAction(QAction("Volume", menu, checkable=True))
                    menu.addAction(QAction("Amount", menu, checkable=True))
                if self.ui.combobox.currentText()==u"分笔数据":
                    menu.addAction(QAction("分笔", menu, checkable=True))
                if self.ui.combobox.currentText()==u"历史分钟":
                    menu.addAction(QAction("Kline", menu, checkable=True))
                    menu.addAction(QAction("Open", menu, checkable=True))
                    menu.addAction(QAction("Close", menu, checkable=True))
                    menu.addAction(QAction("High", menu, checkable=True))
                    menu.addAction(QAction("Low", menu, checkable=True))
                    menu.addAction(QAction("Volume", menu, checkable=True))
                    menu.addAction(QAction("Amount", menu, checkable=True))
                if self.ui.combobox.currentText()==u"十大股东":
                    menu.addAction(QAction("季度饼图", menu, checkable=True))
                    #menu.addAction(QAction("持股比例", menu, checkable=True))
                #for g in keyarray:
                #menu.addAction(QAction(g, menu, checkable=True))
        menu.triggered.connect(lambda action: self.methodSelected(action, collec))
        menu.exec_(self.ui.treeWidget.viewport().mapToGlobal(position))

    def methodSelected(self, action, collec):
        # print(action.text()) #Choice
        # if (self.ui.treewidget.count() == 5):
        #   self.ui.label.setText("Maximum number of queries")
        #   return
        # self.ui.label.setText("")
        Choice = action.text()
        Stock = collec
        # print(collec)  #Stock Name
        # print(db_origin)  #DataBase name
        # list1 = [self.tr(Stock+"-"+Choice+"-"+db_origin)]
        # self.ui.treewidget.addItems(list1)
        parent = QTreeWidgetItem(self.ui.treeWidget_2)
        parent.setText(0, Stock.decode("utf-8") + "-" + Choice)


    def openWidgetMenu(self,position):
        indexes = self.ui.treeWidget_2.selectedIndexes()
        item = self.ui.treeWidget_2.itemAt(position)
        if item == None:
            return
        #item = self.ui.listWidget.itemAt(position)
        if len(indexes) > 0:
            menu = QMenu()
            menu.addAction(QAction("Delete", menu,checkable = True))#This function is perhaps useless
            #menu.triggered.connect(self.eraseItem)
            item = self.ui.treeWidget_2.itemAt(position)
            #collec = str(item.text())
            menu.triggered.connect(lambda action: self.ListMethodSelected(action, item))
        menu.exec_(self.ui.treeWidget_2.viewport().mapToGlobal(position))

    def ListMethodSelected(self, action, item):
        if action.text() == "Delete":
            self.eraseItem()
        if action.text() == "Combine":
            global CombineKeyword
            collec = str(item.text())
            CombineKeyword.append(collec)#Useless function(maybe?)
            list1 = [self.tr(collec)]
            self.ui.listwidget.addItems(list1)
            self.eraseItem()

    def eraseItem(self):
        for x in self.ui.treeWidget_2.selectedItems():#delete with write click menu
            #item = self.ui.treewidget.takeItem(self.ui.treewidget.currentRow())
            sip.delete(x)
            #item.delete

    def classify(self, folder):

        startdate = self.ui.dateEdit.date()
        startdate = startdate.toPyDate()
        startdate = startdate.strftime("%Y/%m/%d")#converts date from dateedit to tushare readable date
        enddate = self.ui.dateEdit_2.date()
        enddate = enddate.toPyDate()
        enddate = enddate.strftime("%Y/%m/%d")
        option = self.ui.comboBox.currentText()
        option = str(option)
        #if (self.ui.treewidget) == 0:
            #self.ui.label.setText("Need to select at least one query")
            #return
        root = self.ui.treeWidget_2.invisibleRootItem()# This is for iterating child items
        child_count = root.childCount()
        texts = []
        if child_count==0:
            return
        for i in range(child_count):
            item = root.child(i)
            text = item.text(0)#with 3 part'stock_name'+'-'+'code'+'-'+action
            texts.append(text)
        labels = [k for k in texts]
        #items = ([x.encode("utf-8") for x in labels])
        width = self.ui.webView.width()#give width and height of user's screen so that graphs can be generated with dynamic size
        height = self.ui.webView.height()
        graphpage(labels, startdate,enddate,option,width, height)#labels:复权ork线or分笔 option:hfq, qfq or 15, 30, D, etc
        self.ui.webView.reload()#refreshes webengine
        self.ui.webView.repaint()
        self.ui.webView.update()

    def graphmerge(self, combineKeyword):
        sth = ""
        for i in combineKeyword:
            if sth == "":
                sth = sth + i
            else :
                sth = sth + "\n" + "&"+ "-"+i
        list1 = sth
        return sth
        global CombineKeyword
        CombineKeyword = []
        self.ui.listwidget.clear()  #combine stuff so that different graphs can be drawn together


app = QApplication(sys.argv)
w = MyUi()
w.show()
sys.exit(app.exec_())
