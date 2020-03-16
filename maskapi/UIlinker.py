import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from apireader import ds
from data_collection import data_collect
import folium
import webbrowser
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("title.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    addr=""
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.setupUI()
        #Textediter
        #self.urlreader.clicked.connect(self.printurl)
        self.btn_parse.clicked.connect(self.pars_start)
        self.btn_map.clicked.connect(self.show_foliummap)

    def setupUI(self):
        self.datatable.setRowCount(len(ds.ds_data_list))
        self.datatable.setColumnCount(2)

    def printurl(self):
        print(self.urlreader.toPlainText())

    def pars_start(self):
        #주소입력창의 글자를 토대로 ds객체에 데이터들을 업데이트하는 함수
        self.addr = self.urlreader.toPlainText()
        print(self.addr)
        data_collect(self.addr)
        self.datatable.setRowCount(len(ds.ds_data_list))
        self.setTableWidgetData()

    def setTableWidgetData(self):
        #데이터표에 알맞은 데이터들을 채워넣는 함수
        for i in range(0,len(ds.ds_data_list)):
            self.datatable.setItem(i,0,QTableWidgetItem(ds.ds_name[i]))
            self.datatable.setItem(i, 1, QTableWidgetItem(ds.ds_remain[i]))
        self.datatable.resizeColumnsToContents()
        self.datatable.resizeRowsToContents()

    def show_foliummap(self):
        self.pars_start()
        print("pushed")
        map_osm = folium.Map(location=[ds.ds_lat[0],ds.ds_lng[0]],zoom_start=15)
        for i in range(0,len(ds.ds_data_list)):
            #ds.remain의 데이터타입은 리스트이므로 +연산이 불가능하다.
            #따라서, 문자열로 강제 형변환 후 더해준다.
            popup=folium.Popup(str(ds.ds_name[i]),max_width=200)

            #tooltip=folium.Tooltip(str(ds.ds_remain[i]),max_width=200)
            folium.Marker(location=[ds.ds_lat[i],ds.ds_lng[i]],
                          popup=popup,tooltip=str(ds.ds_remain[i])).add_to(map_osm)

        map_osm.save('map.html')
        webbrowser.open_new_tab('map.html')

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스
    app = QApplication(sys.argv)

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass()

    #프로그램 화면을 보여주는 코드
    myWindow.show()

    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()