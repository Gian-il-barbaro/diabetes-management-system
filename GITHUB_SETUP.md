# 🚀 Come Caricare su GitHub

## Metodo 1: Usando GitHub CLI (Raccomandato)

Se hai `gh` installato:

```bash
# Crea repository su GitHub e pusha tutto
gh repo create diabetes-management-system --public --source=. --remote=origin --push
```

## Metodo 2: Usando l'interfaccia web di GitHub

### Passo 1: Crea un nuovo repository su GitHub
1. Vai su https://github.com
2. Clicca "New repository" (+ in alto a destra)
3. Nome repository: `diabetes-management-system`
4. Descrizione: `Sistema di gestione pazienti diabetici con PyQt5 e SQLite`
5. Seleziona "Public" o "Private" secondo le tue preferenze
6. NON aggiungere README, .gitignore o license (li abbiamo già)
7. Clicca "Create repository"

### Passo 2: Collega il repository locale a GitHub
```bash
# Sostituisci YOUR_USERNAME con il tuo username GitHub
git remote add origin https://github.com/YOUR_USERNAME/diabetes-management-system.git

# Pusha il codice
git branch -M main
git push -u origin main
```

## Metodo 3: Usando GitHub Desktop
1. Apri GitHub Desktop
2. File → Add Local Repository
3. Seleziona la cartella del progetto
4. Clicca "Publish repository"
5. Scegli il nome e se renderlo pubblico/privato
6. Clicca "Publish repository"

## Verifica
Dopo il caricamento, il repository dovrebbe essere visibile su:
`https://github.com/YOUR_USERNAME/diabetes-management-system`

## Clonare il Repository
Altri possono clonare il progetto con:
```bash
git clone https://github.com/YOUR_USERNAME/diabetes-management-system.git
cd diabetes-management-system
pip install -r requirements.txt
python src/main/python/com/example/diabetesisw/application.py
```

## Credenziali di Test
- **Email**: admin@diabetesystem.com
- **Password**: admin123