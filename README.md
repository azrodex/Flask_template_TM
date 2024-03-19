# Basic Flask Application for 3rd Year Gymnasium Students as part of their Maturity Project

## Author
Ethan Roten, Collège du Sud.

## Description
The current directory is as a foundational Flask template connected to an SQLite database, serving as a starting point for 3rd-year students at Collège du Sud as for their Maturity Project. With pedagogical objectives in mind, and to provide a fundamental grasp of web application architecture, the project intentionally omits any Object-Relational Mapping (ORM) or data validation modules.

## How to run the project
1.Créer un environnement virtuel
```bash
python -m venv <VIRTUAL-ENVIRONMENT-NAME>
```

2. Activer l'environnement virtuel
  * Windows users:
```bash
<VIRTUAL-ENVIRONMENT-NAME\Scripts\activate
```
  * MacOS users:
```bash
source <VIRTUAL-ENVIRONMENT-NAME>/bin/activate
```

3. Installer les modules indépendants de requirements.txt
```bash
pip install -r requirements.txt
```
4. Ajouter un fichier config.py à la racine du projet qui contient les variables 
```bash
SECRET_KEY= ‘VOTRE_CLE_SECRETE’
DATABASE=’NOM_DE_VOTRE_DB’
```
la clé secrète peut être générée grâce au script 
```bash
import secrets
secret_key = secrets.token_hex(16)
print(secret_key)
```

5. Run the project
```bash
python -m flask run --debug
```
