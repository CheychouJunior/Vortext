import sys, json
from ui_editor import *        #Import the UI file ui_editor.py
from Custom_Widgets import *        # Import the Custom_Widgets file (QT-PyQt-PySide-Custom-Widgets)

from PySide6.QtWidgets import QFileDialog


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Setting up the ui interface from the ui_vortext.py
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Get the path to the root directory of the bundled executable
        root_directory = os.path.dirname(os.path.abspath(__file__))

        # Specify the path to 'Textstyle.json' relative to the root directory
        json_file_path = os.path.join(root_directory, 'Textstyle.json')

        # Applying the Json stylesheet
        file = open(json_file_path,)
        data = json.load(file)
        applyJsonStyle(self, self.ui, data)

        self.ui.copyBtn.clicked.connect(self.copy)
        self.ui.cutBtn.clicked.connect(self.cut)
        self.ui.prevBtn.clicked.connect(self.previous)
        self.ui.nextBtn.clicked.connect(self.next)
        self.ui.saveBtn.clicked.connect(self.save)

    def copy(self):
        self.ui.textEdit.copy()

    def cut(self):
        self.ui.textEdit.cut()

    def previous(self):
        self.ui.textEdit.undo()

    def next(self):
        self.ui.textEdit.redo()

    def save(self):
        text = self.ui.textEdit.toPlainText()

        options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)", options=options)

        if file_path:
            with open(file_path, 'w') as file:
                file.write(text)
        
