\# ShieldPME



\*\*Plateforme de supervision et de gestion des risques de cybersécurité pour les PME.\*\*



ShieldPME est un projet de plateforme de cybersécurité visant à aider les petites et moyennes entreprises à centraliser la surveillance de leurs actifs informatiques, détecter les activités suspectes, gérer les incidents et évaluer leurs risques de sécurité.



L'objectif est de proposer une solution accessible, modulaire et évolutive, adaptée aux organisations qui ne disposent pas nécessairement d'un Security Operations Center (SOC).



\## Objectifs du projet



\- Centraliser les informations relatives aux actifs informatiques.

\- Collecter et analyser des événements de sécurité.

\- Détecter des comportements suspects à l'aide de règles de détection.

\- Classifier et suivre les alertes de sécurité.

\- Évaluer les risques selon leur probabilité et leur impact.

\- Gérer les incidents et suivre les mesures correctives.

\- Générer des rapports de sécurité.



\## Architecture technique



| Composant | Technologie |

|---|---|

| Backend | Python / FastAPI |

| ORM | SQLAlchemy |

| Base de données actuelle | SQLite |

| Base de données cible | PostgreSQL |

| Frontend prévu | React / Tailwind CSS |

| Supervision prévue | Wazuh |

| Versionnement | Git / GitHub |



\## Modules fonctionnels



| Module | Description | État |

|---|---|---|

| Backend API | Initialisation de l'API FastAPI | En cours |

| Modèles de données | Utilisateurs, actifs, alertes, incidents et risques | Initialisé |

| Dashboard | Vue globale de la sécurité | À développer |

| Gestion des actifs | Inventaire et suivi des équipements | À développer |

| Threat Monitoring | Importation et analyse des logs | À développer |

| Détection | Identification des comportements suspects | À développer |

| Risk Assessment | Évaluation et classification des risques | À développer |

| Incident Management | Suivi des incidents et remédiations | À développer |

| Rapports | Génération de rapports PDF | À développer |

| Intégration Wazuh | Exploitation des événements de sécurité | Prévue |



\## Structure du projet



```text

ShieldPME/

│

├── backend/

│   ├── app.py

│   ├── database.py

│   ├── models.py

│   └── requirements.txt

│

├── frontend/

├── detection-rules/

├── sample-logs/

├── docs/

│

├── .gitignore

└── README.md

```



\## Installation et démarrage



\### 1. Cloner le repository



```bash

git clone https://github.com/Ranim-jb/ShieldPME.git

cd ShieldPME

```



\### 2. Configurer le backend



```bash

cd backend

python -m venv venv

```



Sous Windows :



```cmd

venv\\Scripts\\activate

```



\### 3. Installer les dépendances



```bash

pip install -r requirements.txt

```



\### 4. Lancer l'API



```bash

python -m uvicorn app:app --reload

```



L'API sera accessible à l'adresse :



`http://127.0.0.1:8000`



Documentation interactive :



`http://127.0.0.1:8000/docs`



\## Sécurité



Le projet prévoit notamment :



\- Authentification et gestion des rôles.

\- Protection des mots de passe par hachage sécurisé.

\- Validation des données côté serveur.

\- Contrôle des accès aux ressources.

\- Journalisation des opérations sensibles.

\- Gestion sécurisée des variables d'environnement.



Ces mécanismes seront implémentés et testés progressivement.



\## Roadmap



1\. Initialisation de l'environnement et de l'architecture.

2\. Développement du backend et de la base de données.

3\. Authentification et gestion des utilisateurs.

4\. Développement de l'interface frontend.

5\. Gestion des actifs informatiques.

6\. Collecte et analyse des logs.

7\. Développement du moteur de détection.

8\. Évaluation des risques.

9\. Gestion des incidents.

10\. Intégration Wazuh et génération des rapports.

11\. Tests, documentation et démonstration.



\## Auteur



\*\*Ranim Jbeli\*\*



\- GitHub : \[Ranim-jb](https://github.com/Ranim-jb)

\- LinkedIn : \[Ranim Jbeli](https://www.linkedin.com/in/ranim-jbeli-3bb244317/)



\---



\*ShieldPME est un projet en cours de développement. Les fonctionnalités indiquées comme prévues ou à développer ne sont pas encore considérées comme opérationnelles.\*

