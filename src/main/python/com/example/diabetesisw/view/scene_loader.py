from typing import Optional
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QWidget
from PyQt5.QtCore import QObject
import sys

class SceneLoader(QObject):
    _instance: Optional['SceneLoader'] = None

    def __init__(self):
        super().__init__()
        self.app: Optional[QApplication] = None
        self.main_window: Optional[QMainWindow] = None
        self.stacked_widget: Optional[QStackedWidget] = None

    @classmethod
    def getInstance(cls) -> 'SceneLoader':
        if cls._instance is None:
            cls._instance = SceneLoader()
        return cls._instance

    def initializeApp(self) -> None:
        if self.app is None:
            self.app = QApplication(sys.argv)
            self.main_window = QMainWindow()
            self.stacked_widget = QStackedWidget()
            self.main_window.setCentralWidget(self.stacked_widget)
            self.main_window.setWindowTitle("Sistema Gestione Diabete")
            self.main_window.resize(800, 600)

    def loadWidget(self, widget: QWidget) -> None:
        # Assicurati che l'app sia inizializzata
        if self.app is None or self.main_window is None or self.stacked_widget is None:
            self.initializeApp()

        if self.stacked_widget is not None:
            # Rimuovi tutti i widget precedenti per evitare accumuli
            while self.stacked_widget.count() > 0:
                old_widget = self.stacked_widget.widget(0)
                self.stacked_widget.removeWidget(old_widget)
                if old_widget is not None:
                    old_widget.close()

            self.stacked_widget.addWidget(widget)
            self.stacked_widget.setCurrentWidget(widget)
            if self.main_window is not None:
                self.main_window.show()

    def goToMainMenu(self) -> None:
        # Assicurati che l'app sia inizializzata
        if self.app is None or self.main_window is None:
            self.initializeApp()

        from .mainmenu.main_menu_controller import MainMenuController
        controller = MainMenuController()
        controller.show()

    def show(self) -> None:
        if self.main_window is not None:
            self.main_window.show()

    def exec(self) -> int:
        if self.app is not None:
            return self.app.exec_()
        return 0