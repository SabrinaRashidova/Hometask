# 1) RadioButtondan foydalanib 5ta test tuzing. Agar to'g'ri javob belgilansa +1bal qo'shilsin va agar noto'g'ri bo'lsa bal qo'shilmasin va oxirida umumiy bali chiqsin.

# from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QRadioButton,QPushButton,QMessageBox,QButtonGroup
# from PyQt5.QtGui import QFont
# import sys
# k=0
# app=QApplication(sys.argv)
# class Window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("RadioButton")
#         self.setGeometry(200,100,700,800)
#         self.start()
#     def font(self,ob,x,y):
#         ob.setFont(QFont("Times",24))
#         ob.move(x,y)
#     def start(self):
#         self.q1=QLabel("1.     2 * 5 = ",self)
#         self.font(self.q1,50,50)

#         self.s1=QRadioButton("A)  100  ",self)
#         self.s1.setFont(QFont("Times",20))
#         self.s1.move(100,100)

#         self.s2=QRadioButton("B)  10  ",self)
#         self.s2.setFont(QFont("Times",20))
#         self.s2.move(100,150)

#         self.s3=QRadioButton("C)  15  ",self)
#         self.s3.setFont(QFont("Times",20))
#         self.s3.move(100,200)
    
#         q1_group = QButtonGroup(self)
#         q1_group.addButton(self.s1)
#         q1_group.addButton(self.s2)
#         q1_group.addButton(self.s3)
#         #q1_group.addButton(self.ch4)


#         self.q22=QLabel("2.    2 * 2 = ",self)
#         self.font(self.q22,50,250)

#         self.c=QRadioButton("A) 4  ",self)
#         self.font(self.c,100,300)
#         self.c1=QRadioButton("B) 2  ",self)
#         self.font(self.c1,100,350)
#         self.c2=QRadioButton("C) 3  ",self)
#         self.font(self.c2,100,400)
        

#         q2_group = QButtonGroup(self)
#         q2_group.addButton(self.c)
#         q2_group.addButton(self.c1)
#         q2_group.addButton(self.c2)
        

#         self.q4=QLabel("4.    2 * 9 = ",self)
#         self.font(self.q4,350,50)

#         self.tt=QRadioButton("A) 4  ",self)
#         self.font(self.tt,350,100)
#         self.tt1=QRadioButton("B) 2  ",self)
#         self.font(self.tt1,350,150)
#         self.tt2=QRadioButton("C) 18  ",self)
#         self.font(self.tt2,350,200)
        

#         q4_group = QButtonGroup(self)
#         q4_group.addButton(self.tt)
#         q4_group.addButton(self.tt1)
#         q4_group.addButton(self.tt2)


#         self.q3=QLabel("3.    2 * 6 = ",self)
#         self.font(self.q3,50,450)

#         self.t=QRadioButton("A) 12  ",self)
#         self.font(self.t,100,500)
#         self.t1=QRadioButton("B) 2  ",self)
#         self.font(self.t1,100,550)
#         self.t2=QRadioButton("C) 3  ",self)
#         self.font(self.t2,100,600)
        

#         q3_group = QButtonGroup(self)
#         q3_group.addButton(self.t)
#         q3_group.addButton(self.t1)
#         q3_group.addButton(self.t2)


#         self.q5=QLabel("5.    6 * 9 = ",self)
#         self.font(self.q5,350,250)

#         self.b=QRadioButton("A) 4  ",self)
#         self.font(self.b,350,300)
#         self.b1=QRadioButton("B) 52  ",self)
#         self.font(self.b1,350,350)
#         self.b2=QRadioButton("C) 54  ",self)
#         self.font(self.b2,350,400)
        

#         q5_group = QButtonGroup(self)
#         q5_group.addButton(self.b)
#         q5_group.addButton(self.b1)
#         q5_group.addButton(self.b2)
        
#         self.button=QPushButton("😊",self)
#         self.setFont(QFont("Times",25))
#         self.button.move(450,650)
#         self.button.clicked.connect(self.run)
#     def run(self):
#         k=0
#         if self.s2.isChecked():
#             k=k+1
#         if self.c.isChecked():
#             k=k+1
#         if self.tt2.isChecked():
#             k=k+1
#         if self.t.isChecked():
#             k=k+1
#         if self.b2.isChecked():
#             k=k+1
#         min=QMessageBox(self)
#         min.setText(str(k)+'  correct')       
#         min.show()

# win=Window()
# win.show()
# app.exec_()







# 2) Restoran menyusini tuzuvchi dastur tuzing. 
# Unda 1-taomlar ro'yhati, 2-taomlar ro'yhati, ichimliklar va desert ro'yhatidagi kamida 5tadan ma'lumotlarni CheckBox orqali tanlaydi 
# va oxirida Chek ro'yhati chiqarilsin. 
# Chek quyidagi ko'rinishda bo'lishi kerak:
# 1-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# 2-taomlar: tanlanganlar ro'yhati (narxlari bilan)
# Ichimliklar: tanlanganlar ro'yhati (narxlari bilan)
# Desert: tanlanganlar ro'yhati (narxlari bilan)

from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QLineEdit,QPushButton,QComboBox,QMessageBox
from PyQt5.QtGui import QFont
import sys


app=QApplication(sys.argv)
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rayhon milliy taomlari")
        self.setGeometry(100,100,700,800)
        self.start()
    def start(self):
        self.meal1=QLabel("Birinchi taom uchun nima yeyishni xohlaysiz?",self)
        self.meal1.setFont(QFont("Times",24))
        self.meal1.move(50,50)

        self.m=QComboBox(self)
        self.m.addItems(["Sho'rva--5000","Mastava--4000","Suyuq lag'mon--6000","CHuchvara","Quyuq la'mon"])
        self.m.setFont(QFont("Times",24))
        self.m.move(100,100)


        self.meal2=QLabel("Ikkinchi taom uchun nima yeyishni xohlaysiz?",self)
        self.meal2.setFont(QFont("Times",24))
        self.meal2.move(50,200)

        self.m1=QComboBox(self)
        self.m1.addItems(["Shashlik","Kabob","Cho'poncha","Manti","Osh"])
        self.m1.setFont(QFont("Times",24))
        self.m1.move(100,250)


        self.drinks=QLabel("Qanday turdagi ichimlik ichishni xohlaysiz!",self)
        self.drinks.setFont(QFont("Times",24))
        self.drinks.move(50,350)

        self.m2=QComboBox(self)
        self.m2.addItems(["Kola","Pepsi","Limonad","Choy","Adrenalin"])
        self.m2.setFont(QFont("Times",24))
        self.m2.move(100,400)


        self.desert=QLabel("Disert uchun nima buyurtma qilasiz!",self)
        self.desert.setFont(QFont("Times",24))
        self.desert.move(50,500)

        self.m=QComboBox(self)
        self.m.addItems(["Muzqaymoq","Pirojniy","Tort","Meva","yana nimadir"])
        self.m.setFont(QFont("Times",24))
        self.m.move(100,550)

        self.ok=QPushButton("OK",self)
        self.ok.setFont(QFont("T",24))
        self.ok.move(400,650)
        # self.ok.clicked.connect(self.ok)

    # def check(self):
    #     mini=QMessageBox(self)
    #     mini.setText()

win=Window()
win.show()
app.exec_()





# 3) ComboBox orqali Tug'ilgan viloyatini, Tuman yoki shaharni, Jinsini va Millatini tanlasin va Barcha tanlangan haqida ma'lumot chiqarilsin.


# from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel,QMainWindow
# from PyQt5.QtWidgets import QComboBox,QLabel,QMessageBox,QCheckBox,QRadioButton
# from PyQt5.QtGui import QFont
# import sys
# app=QApplication(sys.argv)
# class Window(QWidget):
#     andijon = ["","Andijon shahri","Andijon tumani","Asaka tumani","Baliqchi tumani","Bo'z tumani","Buloqboshi tumani","Izboskan tumani","Jalolquduq tumani","Marhamat tumani","Oltinko'l tumani","Paxtaobod tumani","Qo'rg'ontepa tumani","Shahrixon tumani","Ulug'nor tumani","Xo'jaobod tumani","Xonobod shahri"]
#     listb = ["", "Kogon","Olot","Gijduvon","Qorako'l","Jondor"]
#     listJ = ["", "Zomin","Arnasoy","Gallaorol"]
#     listF = ["", "Bag'dod","Beshariq","Furqat","Oltiariq","Rishton"]
#     listNam = ["", "Chortoq","Chust","Kosonsoy","Norin","Pop"]
#     listSur = ["", "Termiz","Denov","Sherobod","Sho'rchi","Boysun"]
#     listSir = ["", "Guliston","Boyovut","Hovos","Oqoltin","Mirzobod"]
#     listN = ["", "Navoiy","Xatirchi","Qiziltepa","Tomdi","Nurota"]
#     listQ = ["", "Kitob","Qarshi","Yakkasaroy","Yakkabog'","Chiroqchi"]
#     listX = ["", "Xonqa","Bog'ot","Xiva","Urganch"]
#     listT = ["", "Toshkent","Yashnobod","Mirzo Ulug'bek","Chirchiq","Yunusobod"]
#     listSam = ["", "Samarqand","Chimboy","Chelak","Narpay","Toyloq"]
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("ComboBox")
#         self.setGeometry(100,100,500,600)
#         self.start1()
#         self.Gender()   
#         self.info()
#     def start1(self):
#         self.savol=QLabel("Siz qaysi viloyatda tug'ilgansiz?",self)
#         self.savol.setFont(QFont("Times",20))
#         self.savol.move(50,50)

#         self.combo=QComboBox(self)
#         self.combo.addItems(["","Andijon","Buxoro","Jizzax","Farg'ona","Namangan","Toshkent","Sirdaryo","Samarqand","Navoiy","Qashqadaryo","Surxondaryo","Xorazm"])
#         self.combo.setFont(QFont("Times",20))
#         self.combo.move(100,100)

#         self.combo1=QComboBox(self)
#         self.combo1.setFont(QFont("Times",20))
#         self.combo1.move(100,150)
#         self.combo1.hide()
        
#         self.combo.currentTextChanged.connect(self.andi)
   
        


#     def andi(self):
#         string = self.combo.currentText()
#         self.combo1.show()
#         if string == "Andijon":
#             self.combo1.clear()
#             self.combo1.addItems(self.andijon)
#         elif string == "Buxoro":
#             self.combo1.clear()
#             self.combo1.addItems(self.listb)
#         elif string == "Jizzax":
#             self.combo1.clear()
#             self.combo1.addItems(self.listJ)
#         elif string == "Farg'ona":
#             self.combo1.clear()
#             self.combo1.addItems(self.listF)
#         elif string == "Namangan":
#             self.combo1.clear()
#             self.combo1.addItems(self.listNam)
#         elif string == "Toshkent":
#             self.combo1.clear()
#             self.combo1.addItems(self.listT)
#         elif string == "Sirdaryo":
#             self.combo1.clear()
#             self.combo1.addItems(self.listSir)
#         elif string == "Samarqand":
#             self.combo1.clear()
#             self.combo1.addItems(self.listSam)
#         elif string == "Navoiy":
#             self.combo1.clear()
#             self.combo1.addItems(self.listN)
#         elif string == "Qashqadaryo":
#             self.combo1.clear()
#             self.combo1.addItems(self.listQ)
#         elif string == "Surxondaro":
#             self.combo1.clear()
#             self.combo1.addItems(self.listSur)
#         elif string == "Xorazm":
#             self.combo1.clear()
#             self.combo1.addItems(self.listX)
        
#     def Gender(self):
#         self.label1=QLabel("Jinsingizni tanlang",self)
#         self.label1.setFont(QFont("Times",20))
#         self.label1.move(100,250)

#         self.button1=QRadioButton("Ayol",self)
#         self.button1.setFont(QFont("Times",20))
#         self.button1.move(70,300)       

#         self.button=QRadioButton("Erkak",self)
#         self.button.setFont(QFont("Times",20))
#         self.button.move(200,300) 

#         self.label=QLabel("Millatingizni tanlang",self)
#         self.label.setFont(QFont("Times",20))
#         self.label.move(100,350)

#         self.nation=QComboBox(self)
#         self.nation.addItems(["","O'zbek","Qozoq","Rus","Ingliz"])
#         self.nation.setFont(QFont("Times",20))
#         self.nation.move(150,400)


#         self.button2=QPushButton("✅",self)
#         self.button2.setFont(QFont("T",20))
#         self.button2.move(400,500)
#         self.button2.clicked.connect(self.run)



#     def info(self):
#         self.info1=QLabel("Info: ",self)
#         self.info1.setFont(QFont("T",24))
#         self.info1.move(100,50)

#         self.info1.hide()

#     def run(self):
#         self.savol.hide()
#         self.combo.hide()
#         self.combo1.hide()
#         self.nation.hide()
#         self.button.hide()
#         self.label.hide()
#         self.button1.hide()
#         self.label1.hide()
#         self.info1.show()
 
# win=Window()
# win.show()
# sys.exit(app.exec_())





