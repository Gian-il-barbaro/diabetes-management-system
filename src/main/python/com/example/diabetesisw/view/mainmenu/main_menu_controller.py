from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QHBoxLayout
from PyQt5.QtCore import Qt

class MainMenuController:
    def __init__(self):
        self.main_menu_widget = QWidget()
        self._setup_ui()
        self._setup_handlers()

    def _setup_ui(self):
        layout = QVBoxLayout()

        title = QLabel("Sistema di Gestione Pazienti Diabetici")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 24px; font-weight: bold; margin: 30px; color: #2E7D32;")

        subtitle = QLabel("Seleziona il tipo di utente per accedere")
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("font-size: 14px; margin: 10px; color: #666;")

        button_layout = QVBoxLayout()
        button_layout.setSpacing(15)

        self.operator_btn = QPushButton("🏥 Responsabile")
        self.medic_btn = QPushButton("👨‍⚕️ Medico")
        self.patient_btn = QPushButton("🧑‍🦽 Paziente")

        button_style = """
            QPushButton {
                padding: 15px 30px;
                font-size: 16px;
                border: 2px solid #4CAF50;
                border-radius: 8px;
                background-color: white;
                color: #4CAF50;
                margin: 5px;
            }
            QPushButton:hover {
                background-color: #4CAF50;
                color: white;
            }
            QPushButton:pressed {
                background-color: #45a049;
            }
        """

        self.operator_btn.setStyleSheet(button_style)
        self.medic_btn.setStyleSheet(button_style)
        self.patient_btn.setStyleSheet(button_style)

        button_layout.addWidget(self.operator_btn)
        button_layout.addWidget(self.medic_btn)
        button_layout.addWidget(self.patient_btn)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addStretch()
        layout.addLayout(button_layout)
        layout.addStretch()

        self.main_menu_widget.setLayout(layout)
        self.main_menu_widget.setWindowTitle("Menu Principale - Sistema Diabete")
        self.main_menu_widget.resize(500, 400)

    def _setup_handlers(self):
        self.operator_btn.clicked.connect(self._on_operator_clicked)
        self.medic_btn.clicked.connect(self._on_medic_clicked)
        self.patient_btn.clicked.connect(self._on_patient_clicked)

    def _on_operator_clicked(self):
        from ..auth.auth_controller import AuthController, UserType
        controller = AuthController(UserType.Operator)
        controller.show()

    def _on_medic_clicked(self):
        from ..auth.auth_controller import AuthController, UserType
        controller = AuthController(UserType.Medic)
        controller.show()

    def _on_patient_clicked(self):
        from ..auth.auth_controller import AuthController, UserType
        controller = AuthController(UserType.Patient)
        controller.show()

    def show(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().loadWidget(self.main_menu_widget)