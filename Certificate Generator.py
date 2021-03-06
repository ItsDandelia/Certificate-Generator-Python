from PySide2 import QtWidgets,QtCore  #For User Interface
import UI_1  #GUI python file generated from Qt Designer
import os
from Google import Create_Service #Python file to create service instance
from googleapiclient import discovery
import time
import random
from apiclient.http import MediaFileUpload
from PIL import Image, ImageDraw, ImageFont #For adding text on Image


class MyQtApp(UI_1.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.clicked)
        self.toolButton.clicked.connect(self.NFonts)
        self.toolButton_2.clicked.connect(self.CFonts)
        self.toolButton_3.clicked.connect(self.UFonts)
        self.toolButton_4.clicked.connect(self.Temp)
        self.toolButton_5.clicked.connect(self.Location)
        self.pushButton_2.clicked.connect(self.clicked2)


    def clicked(self): #For first tab
        #Taking inputs from the screen
        spreadsheet_id1 = str(self.lineEdit.text())
        spreadsheet_id2 = str(self.lineEdit_2.text())
        spreadsheet_id3 = str(self.lineEdit_3.text())
        spreadsheet_id4 = str(self.lineEdit_4.text())
        wshop = str(self.lineEdit_5.text())
        year = str(self.lineEdit_6.text())

        message = QtWidgets.QMessageBox.about(self, 'Info', 'Wait until Unique IDs are generated')
        #Using Google API
        CLIENT_SECRET_FILE = 'Oauth Credentials.json'
        API_NAME = 'sheets'
        API_VERSION = 'v4'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        final = []

        if spreadsheet_id1 != 'None':
            final.append(spreadsheet_id1)

        if spreadsheet_id2 != 'None':
            final.append(spreadsheet_id2)

        if spreadsheet_id3 != 'None':
            final.append(spreadsheet_id3)

        if spreadsheet_id4 != 'None':
            final.append(spreadsheet_id4)

        flist = []
#To read data from sheets and store in list for faster access
        if len(final) == 3:
            total1 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id1, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total1 = total1['values']
            count = len(total1)
            total2 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id2, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total2 = total2['values']
            total3 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id3, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total3 = total3['values']
            i = -1
            while (i < count - 1):
                i += 1
                if (total1[i] in total2) and (total1[i] in total3) and ((total1[i] not in flist) or (flist == [])):
                    flist.append(total1[i])
                else:
                    continue

        elif len(final) == 2:
            total1 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id1, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total1 = total1['values']
            count = len(total1['values'])
            total2 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id2, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total2 = total2['values']
            i = -1
            while (i < count - 1):
                i += 1
                if (total1[i] in total2) and ((total1[i] not in flist) or (flist == [])):
                    flist.append(total1[i])
                else:
                    continue

        elif len(final) == 4:
            total1 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id1, range='Sheet1',
                                                         majorDimension='ROWS')
            total1 = total1.execute()
            total1 = total1['values']
            count = len(total1['values'])
            total2 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id2, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total2 = total2['values']
            total3 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id3, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total3 = total3['values']
            total4 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id4, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total4 = total4['values']
            i = -1
            while (i < count - 1):
                i += 1
                if (total1[i] in total2) and (total1[i] in total3) and (total1[i] in total4) and (
                        (total1[i] not in flist) or flist == []):
                    flist.append(total1[i])
                else:
                    continue

        elif len(final) == 1:
            total1 = service.spreadsheets().values().get(spreadsheetId=spreadsheet_id1, range='Sheet1',
                                                         majorDimension='ROWS').execute()
            total1 = total1['values']
            count = len(total1['values'])
            i = -1
            while (i < count - 1):
                i += 1
                if ((total1[i] not in flist) or flist == []):
                    flist.append(total1[i])

        #Creating new spreadsheet
        properties = {
            'properties': {
                'title': 'Final Sheet' + wshop
            }
        }
        fspreadsheet = service.spreadsheets().create(body=properties,
                                                     fields='spreadsheetId').execute()
        fspreadsheet_id = fspreadsheet['spreadsheetId']
        i = 1
        while (i <= len(flist)):
            frange = 'A' + str(i) + ':' + 'C' + str(i)
            values = [flist[i - 1]]
            value_range_body = {
                'majorDimension': 'ROWS',
                'values': values
            }
            request2 = service.spreadsheets().values().append(spreadsheetId=fspreadsheet_id, range=frange,
                                                              valueInputOption='RAW',
                                                              insertDataOption='OVERWRITE', body=value_range_body)
            response = request2.execute()
            i += 1

        part1 = wshop
        part2 = year[-2:]
        uqids = dict()

        participants = service.spreadsheets().values().get(spreadsheetId=fspreadsheet_id, range='Sheet1',
                                                           majorDimension='ROWS').execute()
        participants = len(participants['values'])
        i = 1
#Will be generating Unique IDs for all participants
        while (i <= participants):

            range = 'A' + str(i) + ':' + 'C' + str(i)
            request = service.spreadsheets().values().get(spreadsheetId=fspreadsheet_id, range=range,
                                                          valueRenderOption='FORMATTED_VALUE', majorDimension='ROWS',
                                                          dateTimeRenderOption='SERIAL_NUMBER')

            values = request.execute()
            name = values['values'][0][0]

            part3 = str(random.randrange(00000, 99999))
            part3 = part3.zfill(5)
            uqid = part1 + '_' + part2 + '_' + part3
            if name == 'Name ':
                values = [['Unique_ID']]

            elif (name not in uqids.keys() or uqids.keys() is None) and (
                    uqid not in uqids.values() or uqids.values() is None):
                uqids[name] = uqid
                values = [[uqid]]

            value_range_body = {
                'majorDimension': 'ROWS',
                'values': values
            }
            range2 = 'D' + str(i)
#Updating the generated Unique IDs in newly created sheet
            request2 = service.spreadsheets().values().append(spreadsheetId=fspreadsheet_id, range=range2,
                                                              valueInputOption='RAW',
                                                              insertDataOption='OVERWRITE',
                                                              body=value_range_body).execute()

            i += 1

        message2 = QtWidgets.QMessageBox.about(self, 'Info', 'All Unique IDs are generated')

    def clicked2(self): #For Certificate Generation
        #Using Google APIs
        CLIENT_SECRET_FILE = 'Oauth Credentials.json'
        API_NAME = 'sheets'
        API_VERSION = 'v4'
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
        CLIENT_SECRET_FILE1 = 'Oauth Credentials.json'
        API_NAME1 = 'drive'
        API_VERSION1 = 'v3'
        SCOPES1 = ['https://www.googleapis.com/auth/drive']
        service1 = Create_Service(CLIENT_SECRET_FILE1, API_NAME1, API_VERSION1, SCOPES1)

#Taking input from the screen
        fspreadsheet_id = str(self.lineEdit_7.text())
        workshop = str(self.lineEdit_8.text())

        name_f=str(self.lineEdit_9.text())
        name_cs=str(self.lineEdit_11.text())
        name_cs=name_cs.split(',')
        name_c=list()
        for i in range(len(name_cs)):
            name_c.append(int(name_cs[i]))
        name_c=tuple(name_c)
        ycoord = int(str(self.lineEdit_10.text())) #For determining position of Name on template
        content = str(self.textEdit.toPlainText())
        name_s=int(self.lineEdit_20.text())
        content_f=str(self.lineEdit_12.text())
        content_cs=str(self.lineEdit_13.text())
        content_cs = content_cs.split(',')
        content_c = list()
        for i in range(len(content_cs)):
            content_c.append(int(content_cs[i]))
        content_c = tuple(content_c)
        content_s=int(self.lineEdit_19.text())
        uqid_f=str(self.lineEdit_18.text())
        uqid_cs=str(self.lineEdit_15.text())
        uqid_cs = uqid_cs.split(',')
        uqid_c = list()
        for i in range(len(uqid_cs)):
            uqid_c.append(int(uqid_cs[i]))
        uqid_c = tuple(uqid_c)
        uqid_s=int(self.lineEdit_14.text())
        temp_location=str(self.lineEdit_16.text())
        save_location=str(self.lineEdit_17.text())


        #Reading Data from spreadsheet into List
        final = service.spreadsheets().values().get(spreadsheetId=fspreadsheet_id, range='Sheet1',
                                                    majorDimension='ROWS').execute()
        final = final['values']

        count = len(final)
        content = content.split(',')
        #Creating new folder on Google Drive
        drivename = 'Certificates ' + workshop
        file_metadata = {
            'name': drivename,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        service1.files().create(body=file_metadata).execute()
        #folderid = input('Enter folder ID')
        text,result=QtWidgets.QInputDialog.getText(self,'Folder ID','Enter the folder ID created in Google Drive')
        if result==True:
            folderid=text
#Generating Certificates with Name,Unique ID,etc. using PIL
        for i in range(1, count):
            name = final[i][0]
            uqid = final[i][3]
            img = Image.open(temp_location) #Opening the img from user entered location
            draw = ImageDraw.Draw(img)
            W, H = img.size


            font = ImageFont.truetype(name_f, name_s)
            w, h = draw.textsize(name, font)
            location = ((W - w) / 2, ycoord)
            draw.text(location, name, fill=name_c, font=font)
            adjust = 0
            for i in range(len(content)):
                font2 = ImageFont.truetype(content_f, content_s)

                #Making adjustments and setting coordinates for the text to be added on image
                w1, h1 = draw.textsize(content[i], font2)
                location2 = ((W - w1) / 2, ycoord + 150 + adjust)
                draw.text(location2, content[i], fill=content_c, font=font2)
                adjust += 40

            font3 = ImageFont.truetype(uqid_f, uqid_s)


            w2, h2 = draw.textsize(uqid, font3)
            location3 = (150, 220)
            draw.text(location3, uqid, fill=uqid_c, font=font3)

            img = img.convert('RGB')
            img.save(save_location + '/' + name + '.jpg') #Saving the image locally on laptop
            #Uploading the image on Google Drive in the folder created earlier
            uploadname = name + '.jpg'
            mimetype2 = 'image/jpeg' 
            file2_metadata = {
                'name': uploadname,
                'parents': [folderid]
            }
            media = MediaFileUpload(save_location + '/' + name + '.jpg', mimetype=mimetype2)
            service1.files().create(
                body=file2_metadata,
                media_body=media,
                fields='id'
            ).execute()

        message3 = QtWidgets.QMessageBox.about(self, 'Info', 'All Certificates have been generated and uploaded')

    def NFonts(self): #For displaying Font Dialog on UI
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Font (*.ttf)", options=options)
        if fileName:
            self.lineEdit_9.setText(fileName)

    def CFonts(self): #For displaying Font Dialog on UI
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Font (*.ttf)", options=options)
        if fileName:
            self.lineEdit_12.setText(fileName)

    def UFonts(self): #For displaying Font Dialog on UI
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Font (*.ttf)", options=options)
        if fileName:
            self.lineEdit_18.setText(fileName)

    def Temp(self): #For opening the template image in UI, the img on which text will be added 
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Images (*.jpg *.png *.jpeg)", options=options)
        if fileName:
            self.lineEdit_16.setText(fileName)

    def Location(self): #Location for saving the generated certificates
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog
        fileName = QtWidgets.QFileDialog.getExistingDirectory(None, 'Select project folder:', 'F:\\', QtWidgets.QFileDialog.ShowDirsOnly)
        if fileName:
            self.lineEdit_17.setText(fileName)




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    qt_app = MyQtApp()
    qt_app.show()
    app.exec_()
