flaskmng = {
    "body": {
        "dependencies": {
            "common": [
                'alembic',
                'astroid',
                'bcrypt',
                'blinker',
                'cffi',
                'click',
                'colorama',
                'dnspython',
                'email-validator',
                'Flask',
                'Flask-Bcrypt',
                'Flask-Login',
                'Flask-Mail',
                'Flask-Migrate',
                'Flask-SQLAlchemy',
                'Flask-WTF',
                'idna',
                'isort',
                'itsdangerous',
                'Jinja2',
                'lazy-object-proxy',
                'Mako',
                'MarkupSafe',
                'mccabe',
                'Pillow',
                'pycparser',
                'python-dateutil',
                'python-editor',
                'six',
                'SQLAlchemy',
                'toml',
                'Werkzeug',
                'wrapt',
                'WTForms',
                'wheel'
            ],
            "prod": [
                'uwsgi',
                'gunicorn'
            ],
            "dev": [
                'autopep8',
                'pylint'
            ]
        },
        "scripts": {
            "newapp": {
                "command": "flaskmng startapp",
                "description": "Creating new app for project."
            },
            "rmapp": {
                "command": "flaskmng removeapp",
                "description": "Removing app from project."
            },
            "mkmig": {
                "command": "flask db migrate -m \"{m}\"",
                "description": "Make migrations for project."
            },
            "mig": {
                "command": "flask db upgrade",
                "description": "Upgrade db for project."
            },
            "dbinit": {
                "command": "flask db init",
                "description": "Initialize db for project."
            },
            "start": {
                "command": "flask run",
                "description": "For starting project."
            }
        }
    }
}
