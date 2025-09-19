from typing import Optional
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt5.QtCore import Qt
from ...model.type.patient import Patient

class PatientController:
    def __init__(self, patient: Patient):
        self.patient = patient
        self.patient_widget = QWidget()
        self._setup_ui()
        self._setup_handlers()

    def _setup_ui(self):
        layout = QVBoxLayout()

        header = QLabel(f"Benvenuto, {self.patient.getFullNameCapitalized()}")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 20px; font-weight: bold; margin: 20px; color: #388E3C;")

        tab_widget = QTabWidget()

        surveys_tab = QWidget()
        medications_tab = QWidget()
        reports_tab = QWidget()
        alerts_tab = QWidget()

        tab_widget.addTab(surveys_tab, "📝 Questionari")
        tab_widget.addTab(medications_tab, "💉 Farmaci")
        tab_widget.addTab(reports_tab, "📊 Report")
        tab_widget.addTab(alerts_tab, "🚨 Avvisi")

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
                background-color: #388E3C;
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

        self.patient_widget.setLayout(layout)
        self.patient_widget.setWindowTitle(f"Dashboard Paziente - {self.patient.getFullName()}")
        self.patient_widget.resize(800, 600)

        self.logout_btn = logout_btn

    def _setup_handlers(self):
        self.logout_btn.clicked.connect(self._on_logout_clicked)

    def _on_logout_clicked(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().goToMainMenu()

    def show(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().loadWidget(self.patient_widget)