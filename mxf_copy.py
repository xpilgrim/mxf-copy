#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Autor: Joerg Sorge
Distributed under the terms of GNU GPL version 2 or later
Copyright (C) Joerg Sorge joergsorge@gmail.com
2012-06-20

Dieses Programm kopiert mxf-Files, 
wie sie z.B. von der Canon XF100 aufgezeichnet werden
aus den Unterverzeichnissen in ein gewünschtes Zielverzeichnis.
Bei Bedarf kann den Zieldateien ein Prefix vorangestellt werden.

With this program, you can copy mxf-video-files e.g. from 
Canon XF100 out from his subdirectorys to your 
destination-directory in a flat structure. 
If necessary, you can add a prefix.

""" 
 
from PyQt4 import QtGui, QtCore
import sys
import os
import shutil
import mxf_copy_ui
 
class MxfCopy(QtGui.QMainWindow, mxf_copy_ui.Ui_MxfCopyMain):
 
    def __init__(self, parent=None):
        super(MxfCopy, self).__init__(parent)
        # This is because Python does not automatically
        # call the parent's constructor.
        self.setupUi(self)
        # Pass this "self" for building widgets and
        # keeping a reference.
        self.app_debugMod = "yes"
        self.connectActions()
        
    def connectActions(self):
        self.toolButton_1.clicked.connect(self.actionOpenSource)
        self.toolButton_2.clicked.connect(self.actionOpenDest)
        self.commandLinkButton.clicked.connect(self.actionRun)
        self.pushButton.clicked.connect(self.actionQuit)
        
 
    def actionOpenSource(self):
        dirSource = QtGui.QFileDialog.getExistingDirectory(
                        self,
                        "Quell-Ordner",
                        QtCore.QDir.homePath()
                    )
        # Don't attempt to open if open dialog
        # was cancelled away.
        if dirSource:
            self.lineEdit_1.setText(dirSource)
            self.textEdit.append("Quelle:")
            self.textEdit.append(dirSource)
            
    
    def actionOpenDest(self):
        dirDest = QtGui.QFileDialog.getExistingDirectory(
                        self,
                        "Ziel-Ordner",
                        QtCore.QDir.homePath()
                    )
        # Don't attempt to open if open dialog
        # was cancelled away.
        if dirDest:
            self.lineEdit_2.setText(dirDest)
            self.textEdit.append("Ziel:")
            self.textEdit.append(dirDest)
        
        
    def actionRun(self):
        if self.lineEdit_1.text()== "Quell-Ordner":
            errorMessage = u"Quell-Ordner wurde nicht ausgewaehlt.."
            self.showDialogCritical( errorMessage )
            return
            
        if self.lineEdit_2.text()== "Ziel-Ordner":
            errorMessage = u"Ziel-Ordner wurde nicht ausgewaehlt.."
            self.showDialogCritical( errorMessage )
            return
        
        self.showDebugMessage(  self.lineEdit_1.text() )
        self.showDebugMessage(  self.lineEdit_2.text() )
        
        try:
            dirsSource = os.listdir( self.lineEdit_1.text())
        except Exception, e:
            logMessage = u"read_files_from_dir Error: %s" % str(e)
            self.showDebugMessage( logMessage)
        
        self.showDebugMessage( dirsSource )
        
        self.textEdit.append("Kopieren:")
        z = 0
        zList = len(dirsSource)
        self.showDebugMessage(  zList )
        for item in dirsSource:
            if item == "JOURNAL":
               z +=1
               self.refreshProgress( zList,  z )
               continue

            if item == "INDEX.MIF":
               z +=1
               self.refreshProgress( zList,  z )
               continue
            
            fileToCopySource = self.lineEdit_1.text() + "/" + item + "/"  + item + "01.MXF"
            fileNotExist = None
            try:
                with open(fileToCopySource) as f: pass
            except IOError as e:
                self.showDebugMessage(  u"File not exists" )
                fileNotExist = "yes"
                # max Anzahl korrigieren und Progress aktualisieren
                zList = zList -1
                pZ = z *100 / zList 
                self.progressBar.setValue(pZ)
   
            if  fileNotExist is None:
                # Prefix oder nicht
                if self.lineEdit_3.text() is not None:
                    fileToCopyDest = self.lineEdit_2.text() + "/" + self.lineEdit_3.text() + item + "01.mxf"
                else:
                    fileToCopyDest = self.lineEdit_2.text() + "/" + item + "01.mxf"
                
                self.textEdit.append(fileToCopyDest)
                self.showDebugMessage( fileToCopySource )
                self.showDebugMessage( fileToCopyDest )
                z +=1
                shutil.copy( fileToCopySource, fileToCopyDest )
                self.refreshProgress( zList,  z )
            else:
                self.textEdit.append("<b>Uebersprungen</b>:")
                self.textEdit.append(fileToCopySource)
        
        self.showDebugMessage( z )
    
    def refreshProgress(self, zList,  z ):
        self.showDebugMessage( z )
        self.showDebugMessage( zList )
        pZ = z *100 / zList 
        self.showDebugMessage( pZ )
        self.progressBar.setValue(pZ)
    
    def showDialogCritical(self,  errorMessage):
        QtGui.QMessageBox.critical(self, "Achtung", errorMessage)
    
    def showDebugMessage(self,  debugMessage):
        if self.app_debugMod == "yes":
            print debugMessage
    
    
    def actionQuit(self):
        QtGui.qApp.quit()
    
    def main(self):
        self.showDebugMessage( u"let's rock" )
        self.progressBar.setValue(0)
        self.show()
 
if __name__=='__main__':
    app = QtGui.QApplication(sys.argv)
    mxfc = MxfCopy()
    mxfc.main()
    app.exec_()
