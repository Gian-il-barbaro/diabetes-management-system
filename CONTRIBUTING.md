# 🤝 Contributing to Diabetes Management System

## Struttura del Progetto

```
diabetes_management_system/
├── src/main/python/com/example/diabetesisw/
│   ├── model/          # Data models e database
│   ├── view/           # UI controllers
│   ├── utils/          # Utility functions
│   └── application.py  # Main application
├── src/test/python/    # Unit tests
└── requirements.txt    # Dependencies
```

## Setup di Sviluppo

1. **Clone del repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/diabetes-management-system.git
   cd diabetes-management-system
   ```

2. **Ambiente virtuale**:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Linux/Mac
   # o
   .venv\Scripts\activate     # Windows
   ```

3. **Installazione dipendenze**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Test dell'applicazione**:
   ```bash
   python src/main/python/com/example/diabetesisw/application.py
   ```

## Aree di Sviluppo

### 🔮 Features da Implementare
- [ ] Database setup per medici e pazienti
- [ ] Sistema di registrazione utenti
- [ ] Dashboard analytics per pazienti
- [ ] Export/import dati
- [ ] Sistema di notifiche
- [ ] Grafici delle rilevazioni glicemiche
- [ ] Report medici automatici

### 🐛 Bug Known
- Database medici e pazienti non implementato
- Mancano validazioni input
- UI potrebbe essere più responsive

### 🎨 UI/UX Improvements
- Aggiungere dark theme
- Migliorare responsive design
- Aggiungere animazioni
- Icons più moderni

## Guidelines

### Code Style
- Segui PEP 8
- Usa type hints quando possibile
- Commenta il codice complesso
- Nomi variabili/funzioni in inglese

### Commit Messages
```
<type>: <description>

Examples:
feat: add patient registration form
fix: resolve login button navigation issue
ui: improve dashboard layout
docs: update installation instructions
```

### Pull Requests
1. Fork del repository
2. Crea un branch per la feature: `git checkout -b feature/nome-feature`
3. Commit delle modifiche
4. Push del branch: `git push origin feature/nome-feature`
5. Apri una Pull Request

## Testing

```bash
# Run tests
python run_tests.py

# Test specifico
python -m pytest src/test/python/test_patient.py
```

## Architettura

- **MVC Pattern**: Model-View-Controller
- **Database**: SQLite con auto-initialization
- **UI**: PyQt5 con custom widgets
- **Navigation**: Centralized SceneLoader

## Credenziali di Test

- **Admin**: admin@diabetesystem.com / admin123
- **Database**: Si auto-crea al primo avvio

## Supporto

Per domande o problemi:
1. Apri un Issue su GitHub
2. Descrivi il problema dettagliatamente
3. Includi screenshot se necessario