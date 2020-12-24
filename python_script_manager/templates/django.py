def django_oninit():
    print("Thanks for using django template!!!")


django = {
    "body": {
        "scripts": {
            "start": {
                "command": "python manage.py runserver",
                "description": "Run Django server"
            },
            "mig": {
                "command": "python manage.py migrate",
                "description": "Migrate database"
            },
            "mkmig": {
                "command": "python manage.py makemigrations",
                "description": "Make migrations"
            }
        }
    },
    "oninit":django_oninit
}
