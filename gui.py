from PyQt5.QtWidgets import *
from PyQt5 import uic
import os
import sys
from xlrd import open_workbook
import paho.mqtt.client as mqtt
import pickle


class Ui(QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        self.wb2g = open_workbook('stats3G.xls').sheet_by_index(0)
        self.wb3g = open_workbook('stats3G.xls').sheet_by_index(0)
        self.wb4g = open_workbook('stats3G.xls').sheet_by_index(0)
        self.maindir = 'tmp'
        self.makeDirs()
        self.message = self.getData()
        uic.loadUi('int.ui', self)
        self.show()
        self.update_var()
        self.save_2g_info()
        self.save_3g_info()
        self.save_4g_info()
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
        #self.uccs_3.clicked.connect(self.changer_ucss_3) 
        self.uccs_3.clicked.connect(self.ow)
    def ow(self):
        app2 = Ui2(self)
        app2.exec()
    def save_2g_info(self):
        sheet = self.wb2g
        psdrops = self.message['2g']['dropps']['valeur']
        csdrops = self.message['2g']['dropcs']['valeur']
        cssrpss = self.message['2g']['cssrPs']['valeur']
        cssrcss = self.message['2g']['cssrCs']['valeur']
        file1 = open(os.path.join(self.maindir,'2g','dropPs','mineur.dat'),'wb')
        file2 = open(os.path.join(self.maindir,'2g','dropPs','majeur.dat'),'wb')
        file3 = open(os.path.join(self.maindir,'2g','dropPs','critique.dat'),'wb')

        file4 = open(os.path.join(self.maindir,'2g','dropCs','mineur.dat'),'wb')
        file5 = open(os.path.join(self.maindir,'2g','dropCs','majeur.dat'),'wb')
        file6 = open(os.path.join(self.maindir,'2g','dropCs','critique.dat'),'wb')

        file7 = open(os.path.join(self.maindir,'2g','cssrCs','mineur.dat'),'wb')
        file8 = open(os.path.join(self.maindir,'2g','cssrCs','majeur.dat'),'wb')
        file9 = open(os.path.join(self.maindir,'2g','cssrCs','critique.dat'),'wb')

        file10 = open(os.path.join(self.maindir,'2g','cssrPs','mineur.dat'),'wb')
        file11 = open(os.path.join(self.maindir,'2g','cssrPs','majeur.dat'),'wb')
        file12 = open(os.path.join(self.maindir,'2g','cssrPs','critique.dat'),'wb')

        for i in range(sheet.nrows-1):
            e ={}
            e['ucell_name'] = sheet.cell_value(i+1,2)
            e['Local_cell_ID'] = sheet.cell_value(i+1,3)
            e['availablity'] = sheet.cell_value(i+1,6)
            e['csdrop'] = sheet.cell_value(i+1,7)
            e['psdrop'] = sheet.cell_value(i+1,8)
            e['cssrCS'] = sheet.cell_value(i+1,9)
            e['cssrPS'] = sheet.cell_value(i+1,10)
            # != str 3al #div 0
            if type(e['csdrop'])!=str:
                if e['csdrop']>csdrops:
                    # Critique
                    pickle.dump(e,file6)
                elif e['csdrop']==csdrops:
                    # majeur
                    pickle.dump(e,file5)
                else:
                    # mineur
                    pickle.dump(e,file4)

            if type(e['psdrop'])!=str:
                if e['psdrop']>psdrops:
                    # Critique
                    pickle.dump(e,file3)
                elif e['psdrop']==psdrops:
                    # majeur
                    pickle.dump(e,file2)
                else:
                    # mineur
                    pickle.dump(e,file1)

            if type(e['cssrCS'])!=str:
                if e['cssrCS']<cssrcss:
                    # Critique
                    pickle.dump(e,file9)
                elif e['cssrCS']==cssrcss:
                    # majeur
                    pickle.dump(e,file8)
                else:
                    # mineur
                    pickle.dump(e,file7)

            if type(e['cssrPS'])!=str:
                if e['cssrPS']<cssrpss:
                    # Critique
                    pickle.dump(e,file12)
                elif e['cssrPS']==cssrpss:
                    # majeur
                    pickle.dump(e,file11)
                else:
                    # mineur
                    pickle.dump(e,file10)
        file1.close()
        file2.close()
        file3.close()

        file4.close()
        file5.close()
        file6.close()

        file7.close()
        file8.close()
        file9.close()

        file10.close()
        file11.close()
        file12.close()


    def save_3g_info(self):
        sheet = self.wb3g
        psdrops = self.message['3g']['dropps']['valeur']
        csdrops = self.message['3g']['dropcs']['valeur']
        cssrpss = self.message['3g']['cssrPs']['valeur']
        cssrcss = self.message['3g']['cssrCs']['valeur']
        file1 = open(os.path.join(self.maindir,'3g','dropPs','mineur.dat'),'wb')
        file2 = open(os.path.join(self.maindir,'3g','dropPs','majeur.dat'),'wb')
        file3 = open(os.path.join(self.maindir,'3g','dropPs','critique.dat'),'wb')

        file4 = open(os.path.join(self.maindir,'3g','dropCs','mineur.dat'),'wb')
        file5 = open(os.path.join(self.maindir,'3g','dropCs','majeur.dat'),'wb')
        file6 = open(os.path.join(self.maindir,'3g','dropCs','critique.dat'),'wb')

        file7 = open(os.path.join(self.maindir,'3g','cssrCs','mineur.dat'),'wb')
        file8 = open(os.path.join(self.maindir,'3g','cssrCs','majeur.dat'),'wb')
        file9 = open(os.path.join(self.maindir,'3g','cssrCs','critique.dat'),'wb')

        file10 = open(os.path.join(self.maindir,'3g','cssrPs','mineur.dat'),'wb')
        file11 = open(os.path.join(self.maindir,'3g','cssrPs','majeur.dat'),'wb')
        file12 = open(os.path.join(self.maindir,'3g','cssrPs','critique.dat'),'wb')

        for i in range(sheet.nrows-1):
            e ={}
            e['ucell_name'] = sheet.cell_value(i+1,2)
            e['Local_cell_ID'] = sheet.cell_value(i+1,3)
            e['availablity'] = sheet.cell_value(i+1,6)
            e['csdrop'] = sheet.cell_value(i+1,7)
            e['psdrop'] = sheet.cell_value(i+1,8)
            e['cssrCS'] = sheet.cell_value(i+1,9)
            e['cssrPS'] = sheet.cell_value(i+1,10)
            # != str 3al #div 0
            if type(e['csdrop'])!=str:
                if e['csdrop']>csdrops:
                    # Critique
                    pickle.dump(e,file6)
                elif e['csdrop']==csdrops:
                    # majeur
                    pickle.dump(e,file5)
                else:
                    # mineur
                    pickle.dump(e,file4)

            if type(e['psdrop'])!=str:
                if e['psdrop']>psdrops:
                    # Critique
                    pickle.dump(e,file3)
                elif e['psdrop']==psdrops:
                    # majeur
                    pickle.dump(e,file2)
                else:
                    # mineur
                    pickle.dump(e,file1)

            if type(e['cssrCS'])!=str:
                if e['cssrCS']<cssrcss:
                    # Critique
                    pickle.dump(e,file9)
                elif e['cssrCS']==cssrcss:
                    # majeur
                    pickle.dump(e,file8)
                else:
                    # mineur
                    pickle.dump(e,file7)

            if type(e['cssrPS'])!=str:
                if e['cssrPS']<cssrpss:
                    # Critique
                    pickle.dump(e,file12)
                elif e['cssrPS']==cssrpss:
                    # majeur
                    pickle.dump(e,file11)
                else:
                    # mineur

                    pickle.dump(e,file10)

        file1.close()
        file2.close()
        file3.close()

        file4.close()
        file5.close()
        file6.close()

        file7.close()
        file8.close()
        file9.close()

        file10.close()
        file11.close()
        file12.close()


    def save_4g_info(self):
        sheet = self.wb4g
        psdrops = self.message['4g']['dropps']['valeur']
        csdrops = self.message['4g']['dropcs']['valeur']
        cssrpss = self.message['4g']['cssrPs']['valeur']
        cssrcss = self.message['4g']['cssrCs']['valeur']
        file1 = open(os.path.join(self.maindir,'4g','dropPs','mineur.dat'),'wb')
        file2 = open(os.path.join(self.maindir,'4g','dropPs','majeur.dat'),'wb')
        file3 = open(os.path.join(self.maindir,'4g','dropPs','critique.dat'),'wb')

        file4 = open(os.path.join(self.maindir,'4g','dropCs','mineur.dat'),'wb')
        file5 = open(os.path.join(self.maindir,'4g','dropCs','majeur.dat'),'wb')
        file6 = open(os.path.join(self.maindir,'4g','dropCs','critique.dat'),'wb')

        file7 = open(os.path.join(self.maindir,'4g','cssrCs','mineur.dat'),'wb')
        file8 = open(os.path.join(self.maindir,'4g','cssrCs','majeur.dat'),'wb')
        file9 = open(os.path.join(self.maindir,'4g','cssrCs','critique.dat'),'wb')

        file10 = open(os.path.join(self.maindir,'4g','cssrPs','mineur.dat'),'wb')
        file11 = open(os.path.join(self.maindir,'4g','cssrPs','majeur.dat'),'wb')
        file12 = open(os.path.join(self.maindir,'4g','cssrPs','critique.dat'),'wb')

        for i in range(sheet.nrows-1):
            e ={}
            e['ucell_name'] = sheet.cell_value(i+1,2)
            e['Local_cell_ID'] = sheet.cell_value(i+1,3)
            e['availablity'] = sheet.cell_value(i+1,6)
            e['csdrop'] = sheet.cell_value(i+1,7)
            e['psdrop'] = sheet.cell_value(i+1,8)
            e['cssrCS'] = sheet.cell_value(i+1,9)
            e['cssrPS'] = sheet.cell_value(i+1,10)
            # != str 3al #div 0
            if type(e['csdrop'])!=str:
                if e['csdrop']>csdrops:
                    # Critique
                    pickle.dump(e,file6)
                elif e['csdrop']==csdrops:
                    # majeur
                    pickle.dump(e,file5)
                else:
                    # mineur
                    pickle.dump(e,file4)

            if type(e['psdrop'])!=str:
                if e['psdrop']>psdrops:
                    # Critique
                    pickle.dump(e,file3)
                elif e['psdrop']==psdrops:
                    # majeur
                    pickle.dump(e,file2)
                else:
                    # mineur
                    pickle.dump(e,file1)

            if type(e['cssrCS'])!=str:
                if e['cssrCS']<cssrcss:
                    # Critique
                    pickle.dump(e,file9)
                elif e['cssrCS']==cssrcss:
                    # majeur
                    pickle.dump(e,file8)
                else:
                    # mineur
                    pickle.dump(e,file7)

            if type(e['cssrPS'])!=str:
                if e['cssrPS']<cssrpss:
                    # Critique
                    pickle.dump(e,file12)
                elif e['cssrPS']==cssrpss:
                    # majeur
                    pickle.dump(e,file11)
                else:
                    # mineur
                    pickle.dump(e,file10)
        file1.close()
        file2.close()
        file3.close()

        file4.close()
        file5.close()
        file6.close()

        file7.close()
        file8.close()
        file9.close()

        file10.close()
        file11.close()
        file12.close()






    def makeDirs(self):
        try:
            os.mkdirs(self.maindir)
        except:
            print('dir exist')
        parentdirs = ['2g','3g','4g']
        parentydirs = ['dropPs','dropCs','cssrCs','cssrPs']
        for i in parentdirs:
            try:
                os.makedirs(self.maindir,i)
                for j in parentydirs:
                    os.makedirs(os.path.join(self.maindir,i,j))
            except:
                print('dir exist')
                for j in parentydirs:
                    try:
                        os.makedirs(os.path.join(self.maindir,i,j))
                    except: 
                        print('dir exist')
        if not(os.path.exists(os.path.join(self.maindir,'data.dat'))):
            self.init_file()

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
        with open(os.path.join(self.maindir,'data.dat'),'rb') as fileData:
            return(pickle.load(fileData))
    def change_valeur(self,resau,kpi,champ,valeurjdida):
        msg = self.getData()
        msg[resau][kpi][champ] = valeurjdida
        self.changecc(msg)
    def init_file(self):
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
        with open(os.path.join(self.maindir,'data.dat'),'wb') as fileData:
            pickle.dump(new,fileData)
        mqttc = mqtt.Client()
        mqttc.connect("test.mosquitto.org", 1883)
        mqttc.publish("tunisie/telecom", str(new),retain=True)
        mqttc.loop(2)
class Ui2(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
        uic.loadUi("second.ui",self)
app = QApplication(sys.argv)
UIWindow = Ui()
app.exec_()
