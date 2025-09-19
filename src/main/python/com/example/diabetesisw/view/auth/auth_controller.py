from typing import Optional
from enum import Enum
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt

class UserType(Enum):
    Operator = "Operator"
    Medic = "Medic"
    Patient = "Patient"

class AuthController:
    ERROR_MESSAGE = "Nome o Password errati. Riprova"

    def __init__(self, target: UserType):
        self.target = target
        self.auth_widget = QWidget()
        self.message_label: Optional[QLabel] = None
        self.email_field: Optional[QLineEdit] = None
        self.password_field: Optional[QLineEdit] = None
        self.back_btn: Optional[QPushButton] = None
        self.login_btn: Optional[QPushButton] = None

        self._setup_ui()
        self._setup_handlers()

    def _setup_ui(self):
        layout = QVBoxLayout()

        title_text = "Login "
        if self.target == UserType.Operator:
            title_text += "Responsabile"
        elif self.target == UserType.Medic:
            title_text += "Medico"
        elif self.target == UserType.Patient:
            title_text += "Paziente"

        title = QLabel(title_text)
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size: 18px; font-weight: bold; margin: 20px;")

        self.message_label = QLabel("")
        self.message_label.setAlignment(Qt.AlignCenter)
        self.message_label.setStyleSheet("color: red; margin: 10px;")

        self.email_field = QLineEdit()
        self.email_field.setPlaceholderText("Email")
        self.email_field.setStyleSheet("padding: 8px; margin: 5px;")

        self.password_field = QLineEdit()
        self.password_field.setEchoMode(QLineEdit.Password)
        self.password_field.setPlaceholderText("Password")
        self.password_field.setStyleSheet("padding: 8px; margin: 5px;")

        button_layout = QHBoxLayout()
        self.back_btn = QPushButton("Indietro")
        self.login_btn = QPushButton("Login")

        self.back_btn.setStyleSheet("padding: 10px; margin: 5px;")
        self.login_btn.setStyleSheet("padding: 10px; margin: 5px; background-color: #4CAF50; color: white;")

        button_layout.addWidget(self.back_btn)
        button_layout.addWidget(self.login_btn)

        layout.addWidget(title)
        layout.addWidget(self.message_label)
        layout.addWidget(self.email_field)
        layout.addWidget(self.password_field)
        layout.addLayout(button_layout)

        self.auth_widget.setLayout(layout)
        self.auth_widget.setWindowTitle(f"Autenticazione {self.target.value}")
        self.auth_widget.resize(400, 300)

    def _setup_handlers(self):
        self.back_btn.clicked.connect(self._on_back_clicked)
        self.login_btn.clicked.connect(self._on_login_clicked)
        self.password_field.returnPressed.connect(self._on_login_clicked)

    def _on_back_clicked(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().goToMainMenu()

    def _on_login_clicked(self):
        try:
            email = self.email_field.text().lower()
            password = self.password_field.text()

            if self.target == UserType.Operator:
                from ...model.model_operators import ModelOperators
                if ModelOperators.getInstance().isAuthorized(email, password):
                    from ..operator.operator_controller import OperatorController
                    controller = OperatorController()
                    controller.show()
                else:
                    self.message_label.setText(self.ERROR_MESSAGE)

            elif self.target == UserType.Medic:
                self.message_label.setText("Database medici in via di sviluppo. Usa login operatore.")

            elif self.target == UserType.Patient:
                self.message_label.setText("Database pazienti in via di sviluppo. Usa login operatore.")

        except Exception as e:
            self.message_label.setText(f"Errore: {str(e)}")

    def show(self):
        from ..scene_loader import SceneLoader
        SceneLoader.getInstance().loadWidget(self.auth_widget)