config = {
    "server": {
        "host": "127.0.0.1",
        "port": "22"
    },
    "configuration": {
        "ssh": {
            "access": True,
            "login": "some",
            "password": "some"
        },
        "name": "2491Oaaf1414"
    }
}

print(config['ssh']['login'])