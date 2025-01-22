import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QWidget
from PyQt5.uic import loadUi
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainwindow.ui", self)  # Load the main window UI

        # Connect button signals to slots
        self.add_btn.clicked.connect(self.select_song)
        self.del_btn.clicked.connect(self.close)

    def select_song(self):
        """Open a file dialog to select a song and launch the second window."""
        song_file, _ = QFileDialog.getOpenFileName(self, "Select Song", "", "Audio Files (*.mp3 *.wav);;All Files (*)")
        if song_file:
            self.open_performance_screen(song_file)

    def open_performance_screen(self, song_file):
        """Open the second window (performance screen) and pass the selected song file."""
        self.performance_screen = PerformanceScreen(song_file)  # Pass the song file to the second window
        self.performance_screen.show()


class PerformanceScreen(QDialog):
    def __init__(self, song_file):
        super().__init__()
        loadUi("performancescreen.ui", self)  # Load the performance screen UI

        # Here you can set the song or handle the song file as needed
        self.song_file = song_file
        self.setup_ui()

    def setup_ui(self):
        """Setup UI for the performance screen."""
        # You could, for example, display the song path in a label or use it for further processing
        self.label_2.setText(f"Song selected: {self.song_file}")
        # Perform any other setup specific to the performance screen


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
