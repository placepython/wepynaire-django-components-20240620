def menu(request):
    return {
        "menu": {
            "entries": [
                {
                    "url": "#",
                    "label": "Articles",
                },
                {
                    "url": "#",
                    "label": "Débutez ici !",
                },
                {
                    "url": "#",
                    "label": "A propos",
                },
                {
                    "url": "#",
                    "label": "Plan du site",
                },
            ]
        }
    }
