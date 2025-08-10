AIndex - AI Trend Tracking Platform

AIndex - AI Trend Tracking Platform is a web application developed in the Django framework using Python and an SQLite database.
The platform enables browsing, filtering, and analyzing articles on Generative Artificial Intelligence (GenAI), with a focus on monitoring technological trends.
It implements the MVT architecture, supports light/dark mode, and features automatic content updates.
Project structure:

Features

    - Browse and filter articles on Generative AI

    - Analyze trends in emerging technologies

    - MVT (Model–View–Template) architecture

    - Light/Dark mode toggle

    - Automatic content updates

    - Responsive design

Project Structure:

PZPIATT      # Платформа за праћење и анализу технолошких трендова
│
├── env        # Виртуелно окружење
│
├── static/    # Фолдер за CSS фајлове и слике
│   └── images
│
├── tech_trends/        # Конфигурација пројекта
│   ├── settings.py
│   └── urls.py
│
├── templates/          # Фолдер за HTML фајлове
│   └── articles
│
├── trends/             # Главна апликација
│   ├── __pycache__
│   ├── migrations/
│   └── static/
│	├──trends
│	├──	includes
│	├──	js
│   	└── templates/
│	    └──trends/
│	         └──includes
│
├── db.sqlite3           # База података
└── manage.py          # Контролна скрипта

Installation & Setup
1. Clone the repository
	git clone https://github.com/yourusername/AIndex-Trend-Platform.git
	cd AIndex-Trend-Platform

2. Create and activate a virtual environment
	python -m venv env

3. Install dependencies
	pip install -r requirements.txt

4. Run the application
	python manage.py runserver

Open your browser and visit:
	http://127.0.0.1:8000/trends/

Notes:
    - The env/ folder (virtual environment) is not included in the repository.

    - Database file (db.sqlite3) can be excluded if you prefer users to run migrations and create their own database:
	python manage.py migrate

    - Make sure you have Python 3.9+ installed.

