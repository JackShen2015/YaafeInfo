# -*- coding:utf-8 -*-

from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui
import sys, os
import MIR
import numpy as np
import matplotlib.pyplot as plt
import eyed3
from pydub import AudioSegment
import wave


class Window(QMainWindow, ui.Ui_MainWindow):
    global musicFilePath
    global selectedMethod

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.musicFilePath = ""

        self.setupUi(self)
        self.ButtionActionConnect()

    def ButtionActionConnect(self):
        QObject.connect(self.selectFileButton, SIGNAL("clicked()"), self.openMusicFile)
        QObject.connect(self.cancelButton, SIGNAL("clicked()"), self.cancelFileSelected)
        QObject.connect(self.yesButton, SIGNAL("clicked()"), self.submitFileAndMethod)
        QObject.connect(self.translate, SIGNAL("clicked()"), self.mp3ToWav)

    # mp3toWav
    def mp3ToWav(self):
        if self.musicFilePath == "" or self.musicFilePath == None:
            print "错误"
        else:
            print "你好"
            print self.musicFilePath
            AudioSegment.converter = "/usr/bin/ffmpeg"
            sound = AudioSegment.from_mp3(self.musicFilePath)
            name1, name2 = os.path.split(self.musicFilePath)
            # print name1 + '/'
            sound.export(name1 + "/temp/" + name2.replace("mp3", "wav"), format="wav")

    # 打开音乐文件
    def openMusicFile(self):
        musicFilePath = QFileDialog.getOpenFileName(self, "Choose a file to open", "./music",
                                                    "Music (*.mp3 *.wav)")
        self.musicFilePath = unicode(QString(musicFilePath).toUtf8(), 'utf-8', 'ignore')
        self.selectFilePath.setText(self.musicFilePath)

    # 取消选择的文件
    def cancelFileSelected(self):
        self.selectFilePath.clear()
        self.musicFilePath = ""

    # 确认提交的文件，并显示输出选择的特性
    def submitFileAndMethod(self):
        if self.musicFilePath == "" or self.musicFilePath == None:
            print "错误"
        else:
            musicPath = self.musicFilePath
            musicInfoRaw = self.selectInfoCombo.currentText()
            musicInfo = unicode(QString(musicInfoRaw).toUtf8(), 'utf-8', 'ignore')
            print type(musicPath)
            print type(musicInfo)
            showFeather(musicPath, musicInfo)


# 获得相应的特征值
def getFeather(musicPath, musicInfo):
    MIR.init()
    MIR.startEngine(musicPath)
    return MIR.getFeature(musicInfo)


# 绘制图像
def showGraFeather(songData, title, time):
    data = np.array(songData)
    xNum, yNum = data.shape
    xAxis = np.linspace(0, int(time), yNum)
    plt.figure('Feather', figsize=(20, 5))
    plt.title(title)

    if xNum == 1:
        plt.plot(xAxis, data[0])
    else:
        for i in range(0, xNum):
            plt.plot(xAxis, data[i], label='data' + str(i))

        plt.legend(loc='upper right')
    plt.show()

    # 获取相应的特征值和绘制图像


def showFeather(musicPath, musicInfo):
    print musicPath, musicInfo
    name1, name2 = os.path.split(musicPath)
    title = musicInfo + " for " + name2
    data = getFeather(musicPath, musicInfo)
    if musicPath.endswith(".mp3"):
        time1 = eyed3.load(musicPath)
        print('time: {} second'.format(time1.info.time_secs))
        time = format(time1.info.time_secs)
    else:
        time1 = wave.Wave_read(musicPath)

        time = 20

    showGraFeather(data, title, time)


app = QApplication(sys.argv)
demo = Window()
demo.show()
sys.exit(app.exec_())
