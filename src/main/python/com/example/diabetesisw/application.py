import sys
from PyQt5.QtWidgets import QApplication

# Import handling for both module and direct execution
try:
    from .view.scene_loader import SceneLoader
    from .view.mainmenu.main_menu_controller import MainMenuController
except ImportError:
    # Direct execution - use absolute imports
    from view.scene_loader import SceneLoader
    from view.mainmenu.main_menu_controller import MainMenuController

class Application:
    def __init__(self):
        self.scene_loader = SceneLoader.getInstance()

    def start(self):
        self.scene_loader.initializeApp()

        # Inizializza il database
        try:
            try:
                from .model.model import Model
            except ImportError:
                from model.model import Model
            model = Model.getInstance()
            model.initializeDatabase()
            print("Database initialized successfully")
        except Exception as e:
            print(f"Errore nell'inizializzazione del database: {e}")
            # Continua comunque per poter testare l'UI

        main_menu = MainMenuController()
        main_menu.show()

        return self.scene_loader.exec()

def main():
    app = Application()
    sys.exit(app.start())

if __name__ == "__main__":
    main()