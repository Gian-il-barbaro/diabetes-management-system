# Sistema di Gestione Pazienti Diabetici

## Descrizione
Questo è un sistema completo per la gestione di pazienti diabetici, tradotto dal progetto JavaFX originale per pazienti ipertesi. Il sistema mantiene la stessa struttura, nomi delle classi e funzionalità del progetto originale, ma è stato adattato per il dominio del diabete.

## Caratteristiche Principali
- **Gestione Pazienti**: Registrazione e monitoraggio dei pazienti diabetici
- **Monitoraggio Glicemico**: Tracciamento dei livelli di glucosio nel sangue
- **Sistema di Allerte**: Notifiche automatiche per valori glicemici anomali
- **Gestione Terapie**: Prescrizione e monitoraggio di farmaci diabetici
- **Dashboard per Medici**: Interfaccia per la gestione dei pazienti
- **Interfaccia Paziente**: Dashboard per l'inserimento dati quotidiani

## Requisiti di Sistema
- Python 3.8+
- PyQt5
- SQLite3

## Installazione

1. **Clona o scarica il progetto**
```bash
cd diabetes_management_system
```

2. **Installa le dipendenze**
```bash
pip install -r requirements.txt
```

3. **Avvia l'applicazione**
```bash
python src/main/python/com/example/diabetesisw/application.py
```

## Struttura del Progetto

```
diabetes_management_system/
├── src/
│   ├── main/
│   │   └── python/
│   │       └── com/example/diabetesisw/
│   │           ├── model/
│   │           │   ├── type/          # Classi di dominio
│   │           │   └── table/         # Gestione database
│   │           ├── view/              # Interfacce utente
│   │           ├── utils/             # Utilità e helper
│   │           └── application.py     # Applicazione principale
│   └── test/
│       └── python/                    # Test unitari
├── requirements.txt
├── setup.py
└── README.md
```

## Classi Principali

### Model
- **Patient**: Gestione dati pazienti diabetici
- **Medic**: Gestione dati medici (rinominato da Doctor)
- **DailySurveys**: Rilevazioni giornaliere (rinominato da BloodPressureMeasurement)
- **Alert**: Sistema di notifiche per valori glicemici
- **TakingDrug**: Assunzione farmaci diabetici
- **Therapy**: Terapie diabetiche (rinominato da HypertensionTherapy)

### View Controllers
- **AuthController**: Gestione autenticazione
- **MedicController**: Dashboard medico
- **PatientController**: Dashboard paziente
- **OperatorController**: Pannello responsabile

## Soglie Glicemiche

Il sistema monitora i seguenti valori:
- **Normale**: 70-100 mg/dL (digiuno), 70-140 mg/dL (post-prandiale)
- **Ipoglicemia**: <70 mg/dL
- **Iperglicemia lieve**: 100-126 mg/dL (digiuno), 140-180 mg/dL (post-prandiale)
- **Iperglicemia moderata**: 126-200 mg/dL (digiuno), 180-250 mg/dL (post-prandiale)
- **Iperglicemia grave**: >200 mg/dL (digiuno), >250 mg/dL (post-prandiale)

## Test

Esegui i test con:
```bash
python run_tests.py
```

## Accesso di Default

**Responsabile:**
- Email: admin@diabetesystem.com
- Password: admin123

## Funzionalità Tradotte

Tutte le funzionalità del progetto originale sono state mantenute e adattate:

1. **Sistema di Autenticazione**: Identico al progetto originale
2. **Gestione Pazienti**: Adattato per diabete invece di ipertensione
3. **Monitoraggio**: Glicemia invece di pressione arteriosa
4. **Terapie**: Farmaci diabetici invece di antipertensivi
5. **Allerte**: Soglie glicemiche invece di pressorie
6. **Interfacce**: Replicate con PyQt5 invece di JavaFX

## Struttura Database

Il database SQLite include le seguenti tabelle:
- `medic`: Dati medici
- `patient`: Dati pazienti
- `dailysurveys`: Rilevazioni quotidiane
- `alert`: Sistema allerte
- `takingdrug`: Assunzione farmaci
- `therapy`: Terapie prescritte
- `symptoms`: Sintomi registrati

## Licenza

Questo progetto è sviluppato per scopi educativi e di ricerca.