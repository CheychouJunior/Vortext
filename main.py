import sys, cv2, pytesseract
from ui_vortext import *        #Import the UI file ui_vortext.py
from Custom_Widgets import *        # Import the Custom_Widgets file (QT-PyQt-PySide-Custom-Widgets)
import Textmain
from screen import *
from os import system

import numpy as np
from PIL import Image

from PySide6.QtWidgets import QFileDialog, QApplication
from PySide6.QtCore import QUrl, QTime, QTimer
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput  
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtGui import QKeySequence, QPixmap  # Import QKeySequence for key sequence handling


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Setting up the ui interface from the ui_vortext.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        system('mkdir /tmp/vortext') # directory where will be stored the screenshot.png and text.txt
   
        # Open the text editor
        self.editorWindow = Textmain.MainWindow()

        """ # Applying the Json stylesheet
        loadJsonStyle(self, self.ui) """
        # Due to the problem that occured during the execution of the bundled app (JSON file not found)
        # Get the path to the root directory of the bundled executable
        root_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the path to 'Textstyle.json' relative to the root directory
        json_file_path = os.path.join(root_directory, 'style.json')

        # Applying the Json stylesheet (could use loadJsonStyle(self, self.ui) but i needed to precise the json file name(default style.json))
        file = open(json_file_path,)
        data = json.load(file)
        applyJsonStyle(self, self.ui, data)

        # Create a media player
        self.mediaPlayer = QMediaPlayer()

        # Adding sound to the media player
        self.audioOutput = QAudioOutput()
        self.mediaPlayer.setAudioOutput(self.audioOutput)

        # Create a video widget
        self.videoWidget = QVideoWidget()
        self.videoWidget.show()

        # Set up the layout
        layout = QVBoxLayout(self.ui.screenWidget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.videoWidget)

        # Connect the media player to the Video Widget
        self.mediaPlayer.setVideoOutput(self.videoWidget)

        # Connect buttons to their respective functions
        self.ui.openBtn.clicked.connect(self.openFile)
        self.ui.pauseBtn.clicked.connect(self.pause)
        self.ui.copyBtn.clicked.connect(self.open_window)

        self.ui.volumeSlider.valueChanged.connect(self.volumeChange)

        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)

        self.ui.videoSlider.setRange(0,0)
        self.ui.videoSlider.sliderMoved.connect(self.setPosition)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDuration)

        self.shortcut = QShortcut(QKeySequence(Qt.Key_F), self)
        self.shortcut.activated.connect(self.toggle_full_screen)
#----------------------------------------------------------------------------------------------------
        # Screenshot part

        self.area = None
        self.ui.selectBtn.clicked.connect(self.selectArea)

    def selectArea(self):
        xs = XSelect(display.Display())
        self.area = xs.get_mouse_selection()
        self.shootScreen()

    def shootScreen(self):
        # Garbage collect any existing image first.
        self.originalPixmap = None
        screen = QApplication.primaryScreen()
        self.originalPixmap = screen.grabWindow(0)
        if self.area is not None:
            qi = self.originalPixmap.toImage()
            qi = qi.copy(
                int(self.area[0]),
                int(self.area[1]),
                int(self.area[2]),
                int(self.area[3])
            )
            self.originalPixmap = None
            self.originalPixmap = QPixmap.fromImage(qi)

        self.originalPixmap.save("/tmp/vortext/screenshot.png", 'png')

        img = Image.open("/tmp/vortext/screenshot.png")
        ocr_result = pytesseract.image_to_string(img)

        # creating the file and writing the data inside
        with open("/tmp/vortext/text.txt", "w",encoding="utf-8") as file:
            file.write(ocr_result)


#----------------------------------------------------------------------------------------------------
    
    # You will also move later
    def open_window(self):
        f = open('/tmp/vortext/text.txt') #Open the file containing the extracted text
        text = f.read()
        f.close()

        self.editorWindow.ui.textEdit.setText("") #In order to clear the editor everytime it is opened
        self.text = text
        self.index = 0

        self.textTimer = QTimer(self)
        self.textTimer.timeout.connect(self.printChar)
        self.textTimer.start(20) #Number of miliseconds that will pass after the printing of 1 character
        self.editorWindow.show()

    def printChar(self):
        if self.index < len(self.text):
            char = self.text[self.index]

            self.editorWindow.ui.textEdit.insertPlainText(char)
            self.index += 1
        else:
            self.textTimer.stop()

    def openFile(self):
        self.mediaPlayer.stop()
        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Video File", "", "Video Files (*.mp4 *.avi *.mkv);;All Files (*)", options=options)
        if fileName:
            self.mediaPlayer.setSource(QUrl.fromLocalFile(fileName))
            self.mediaPlayer.play()
            self.ui.volumeSlider.setValue(self.audioOutput.volume())

            video_name = fileName.split("/")[-1]
            self.ui.videoNameLabel.setText(video_name)

            duration = self.mediaPlayer.duration()
            # Convert the duration time from milliseconds to QTime (HH:MM:SS)
            duration_time = QTime(0,0)
            duration_time = duration_time.addMSecs(duration)
            self.ui.timeLabel.setText(duration_time.toString('hh:mm:ss'))

            # Setup the timer to update after every 1 seconds
            self.timer.start(1000)

    def updateDuration(self):
        currentPosition = self.mediaPlayer.position()

        # Convert the current postion from milliseconds to QTime (HH:MM:SS)
        current_time = QTime(0,0)
        current_time = current_time.addMSecs(currentPosition)
        self.ui.cur_timeLabel.setText(current_time.toString('hh:mm:ss'))

    def toggle_full_screen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def pause(self):
        if self.mediaPlayer.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.mediaPlayer.pause()
            icon = QIcon()
            icon.addFile(u":/icons/play.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pauseBtn.setIcon(icon)
            self.ui.pauseBtn.setIconSize(QSize(40, 40))
        else:
            self.mediaPlayer.play()
            icon = QIcon()
            icon.addFile(u":/icons/pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.pauseBtn.setIcon(icon)
            self.ui.pauseBtn.setIconSize(QSize(40, 40))
            
    def volumeChange(self, volume):
        self.audioOutput.setVolume(volume)
        if volume == 0:
            self.ui.label.setMaximumSize(QSize(20, 20))
            self.ui.label.setPixmap(QPixmap(u":/icons/volume min.png"))
            self.ui.label.setScaledContents(True)
        elif volume == 99:
            self.ui.label.setMaximumSize(QSize(20, 20))
            self.ui.label.setPixmap(QPixmap(u":/icons/volume max.png"))
            self.ui.label.setScaledContents(True)       
        elif volume > 0 and volume < 50:
            self.ui.label.setMaximumSize(QSize(20, 20))
            self.ui.label.setPixmap(QPixmap(u":/icons/volume 1.png"))
            self.ui.label.setScaledContents(True)
        else:
            self.ui.label.setMaximumSize(QSize(20, 20))
            self.ui.label.setPixmap(QPixmap(u":/icons/volume 2.png"))
            self.ui.label.setScaledContents(True)

    def positionChanged(self, position):
        self.ui.videoSlider.setValue(position)

    def durationChanged(self, duration):
        self.ui.videoSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    