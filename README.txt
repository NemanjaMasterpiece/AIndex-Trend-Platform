AIndex – AI Trend Tracking Platform is a web application developed in the Django framework using Python and an SQLite database.
The platform enables browsing, filtering, and analyzing articles on Generative Artificial Intelligence (GenAI), with a focus on monitoring technological trends.
It implements the MVT architecture, supports light/dark mode, and features automatic content updates.

Project structure:
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
