from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTabWidget
from PyQt5.QtCore import Qt

class OperatorController:
    def __init__(self):
        self.operator_widget = QWidget()
        self._setup_ui()
        self._setup_handlers()

    def _setup_ui(self):
        layout = QVBoxLayout()

        header = QLabel("Pannello Responsabile")
        header.setAlignment(Qt.AlignCenter)
        header.setStyleSheet("font-size: 20px; font-weight: bold; margin: 20px; color: #E65100;")

        tab_widget = QTabWidget()

        medics_tab = QWidget()
        patients_tab = QWidget()
        reports_tab = QWidget()
        system_tab = QWidget()

        tab_widget.addTab(medics_tab, "👨‍⚕️ Medici")
        tab_widget.addTab(patients_tab, "👥 Pazienti")
        tab_widget.addTab(reports_tab, "📊 Report")
        tab_widget.addTab(system_tab, "⚙️ Sistema")

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
                background-color: #E65100;
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

        self.operator_widget.setLayout(layout)
        self.operator_widget.setWindowTitle("Dashboard Responsabile")
        self.operator_widget.resize(900, 700)

        self.logout_btn = logout_btn

    def _setup_handlers(self):
        self.logout_btn.clicked.connect(self._on_logout_clicked)

    def _on_logout_clicked(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().goToMainMenu()

    def show(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().loadWidget(self.operator_widget)