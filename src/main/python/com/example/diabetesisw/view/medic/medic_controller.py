from typing import Optional
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt5.QtCore import Qt
from ...model.type.medic import Medic

class MedicController:
    def __init__(self, medic: Medic):
        self.medic = medic
        self.medic_widget = QWidget()
        self._setup_ui()
        self._setup_handlers()

    def _setup_ui(self):
        layout = QVBoxLayout()

        header = QLabel(f"Benvenuto, Dr. {self.medic.getFullNameCapitalized()}")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 20px; font-weight: bold; margin: 20px; color: #1976D2;")

        tab_widget = QTabWidget()

        patients_tab = QWidget()
        data_tab = QWidget()
        therapy_tab = QWidget()
        summary_tab = QWidget()

        tab_widget.addTab(patients_tab, "👥 Pazienti")
        tab_widget.addTab(data_tab, "📊 Dati")
        tab_widget.addTab(therapy_tab, "💊 Terapie")
        tab_widget.addTab(summary_tab, "📋 Riassunti")

        tab_widget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #cccccc;
                border-radius: 4px;
            }
            QTabBar::tab {
                padding: 10px 20px;
                margin: 2px;
                border-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #1976D2;
                color: white;
            }
        """)

        logout_btn = QPushButton("Logout")
        logout_btn.setStyleSheet("""
            QPushButton {
                padding: 10px 20px;
                background-color: #f44336;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)

        layout.addWidget(header)
        layout.addWidget(tab_widget)
        layout.addWidget(logout_btn)

        self.medic_widget.setLayout(layout)
        self.medic_widget.setWindowTitle(f"Dashboard Medico - Dr. {self.medic.getSurname()}")
        self.medic_widget.resize(900, 700)

        self.logout_btn = logout_btn

    def _setup_handlers(self):
        self.logout_btn.clicked.connect(self._on_logout_clicked)

    def _on_logout_clicked(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().goToMainMenu()

    def show(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().loadWidget(self.medic_widget)