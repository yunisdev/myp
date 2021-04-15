flaskmng = {
    "body": {
        "scripts":{
            "newapp":{
                "command":"flaskmng startapp",
                "description":"Creating new app for project."
            },
            "rmapp":{
                "command":"flaskmng removeapp",
                "description":"Removing app from project."
            },
            "mkmig":{
                "command":"flask db commit {args}",
                "description":"Make migrations for project."
            },
            "mig":{
                "command":"flask db upgrade",
                "description":"Upgrade db for project."
            },
            "start":{
                "command":"flask run",
                "description":"For starting project."
            }
        }
    }
}