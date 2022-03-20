from PyQt5.QtWidgets import *
from PyQt5 import uic
from os.path import exists
import sys
import paho.mqtt.client as mqtt
import pickle


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        if not(exists('data.dat')):
            self.change_difinition()
        self.message = self.getData()
        uic.loadUi('int.ui', self)
        self.show()
        self.update_var()

        self.udps_1.clicked.connect(self.changer_udps_1)
        self.udps_2.clicked.connect(self.changer_udps_2)
        self.udps_3.clicked.connect(self.changer_udps_3)


        self.udcs_1.clicked.connect(self.changer_udcs_1)
        self.udcs_2.clicked.connect(self.changer_udcs_2)
        self.udcs_3.clicked.connect(self.changer_udcs_3)

        self.ucps_1.clicked.connect(self.changer_ucps_1)
        self.ucps_2.clicked.connect(self.changer_ucps_2)
        self.ucps_3.clicked.connect(self.changer_ucps_3)


        self.uccs_1.clicked.connect(self.changer_ucss_1) 
        self.uccs_2.clicked.connect(self.changer_ucss_2) 
        self.uccs_3.clicked.connect(self.changer_ucss_3) 


    def changer_ucss_1(self):
        self.change_valeur('2g', 'cssrCs', 'valeur', self.ccs_1.value())
    def changer_ucss_2(self):
        self.change_valeur('3g', 'cssrCs', 'valeur', self.ccs_2.value())
    def changer_ucss_3(self):
        self.change_valeur('4g', 'cssrCs', 'valeur', self.ccs_3.value())

    def changer_ucps_1(self):
        self.change_valeur('2g', 'cssrPs', 'valeur', self.cps_1.value())
    def changer_ucps_2(self):
        self.change_valeur('3g', 'cssrPs', 'valeur', self.cps_2.value())
    def changer_ucps_3(self):
        self.change_valeur('4g', 'cssrPs', 'valeur', self.cps_3.value())

    def changer_udcs_1(self):
        self.change_valeur('2g', 'dropcs', 'valeur', self.dcs_1.value())
    def changer_udcs_2(self):
        self.change_valeur('3g', 'dropcs', 'valeur', self.dcs_2.value())
    def changer_udcs_3(self):
        self.change_valeur('4g', 'dropcs', 'valeur', self.dcs_3.value())



    def changer_udps_1(self):
        self.change_valeur('2g', 'dropps', 'valeur', self.dps_1.value())

    def changer_udps_2(self):
        self.change_valeur('3g', 'dropps', 'valeur', self.dps_2.value())

    def changer_udps_3(self):
        self.change_valeur('4g', 'dropps', 'valeur', self.dps_3.value())

    def update_var(self): 
        self.dps_3.setValue(self.message['4g']['dropps']['valeur'])
        self.dcs_3.setValue(self.message['4g']['dropcs']['valeur'])
        self.cps_3.setValue(self.message['4g']['cssrPs']['valeur'])
        self.ccs_3.setValue(self.message['4g']['cssrCs']['valeur'])

        self.dps_2.setValue(self.message['3g']['dropps']['valeur'])
        self.dcs_2.setValue(self.message['3g']['dropcs']['valeur'])
        self.cps_2.setValue(self.message['3g']['cssrPs']['valeur'])
        self.ccs_2.setValue(self.message['3g']['cssrCs']['valeur'])

        self.dps_1.setValue(self.message['2g']['dropps']['valeur'])
        self.dcs_1.setValue(self.message['2g']['dropcs']['valeur'])
        self.cps_1.setValue(self.message['2g']['cssrPs']['valeur'])
        self.ccs_1.setValue(self.message['2g']['cssrCs']['valeur'])

    def getData(self):
        with open('data.dat','rb') as fileData:
            return(pickle.load(fileData))
        
    # resau(2g,3g,4g) kpi(kpi1,kpi2,kpi3,kpi4) champ(mineur,majeur,critique,valeur)
    def change_valeur(self,resau,kpi,champ,valeurjdida):
        msg = self.getData()
        msg[resau][kpi][champ] = valeurjdida
        self.changecc(msg)

    def change_difinition(self):
        # Dictionaire jdid lehna kan t7eby tbadly lforme ta3 message
        res2g={
            'dropps': {'valeur':0.1,'mineur':0,'majeur':0,'critique':0},
            'dropcs': {'valeur':0.123,'mineur':0,'majeur':0,'critique':0},
            'cssrPs': {'valeur':98,'mineur':0,'majeur':0,'critique':0},
            'cssrCs': {'valeur':80,'mineur':0,'majeur':0,'critique':0}
        }
        res3g={
            'dropps': {'valeur':0.1222,'mineur':0,'majeur':0,'critique':0},
            'dropcs': {'valeur':0.1232,'mineur':0,'majeur':0,'critique':0},
            'cssrPs': {'valeur':97,'mineur':0,'majeur':0,'critique':0},
            'cssrCs': {'valeur':96,'mineur':0,'majeur':0,'critique':0}
        }
        res4g={
            'dropps': {'valeur':0.01,'mineur':0,'majeur':0,'critique':0},
            'dropcs': {'valeur':0.002,'mineur':0,'majeur':0,'critique':0},
            'cssrPs': {'valeur':95,'mineur':0,'majeur':0,'critique':0},
            'cssrCs': {'valeur':94,'mineur':0,'majeur':0,'critique':0}
        }
        msg = {
            '2g':res2g,
            '3g':res3g,
            '4g':res4g
        }
        self.changecc(msg)        

    def changecc(self,new):
        # T7ot Ldata fil file bech matdhi3ch
        with open('data.dat','wb') as fileData:
            pickle.dump(new,fileData)
        # hadhi tb3th lmssg
        mqttc = mqtt.Client()
        mqttc.connect("test.mosquitto.org", 1883)
        mqttc.publish("tunisie/telecom", str(new),retain=True)
        mqttc.loop(2)
        


app = QApplication(sys.argv)

UIWindow = Ui()

app.exec_()
