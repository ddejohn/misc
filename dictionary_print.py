d = {
    'description': 'room 0 description',
    'x': 1,
    'y': 3,
    'adjacent': {
        'north': None,
        'south': None,
        'east': None,
        'west': 'room 1'
    },
    'players': {
        'player 0': {
            'description': 'player 0 description',
            'location': 'room 0',
            'inventory': {
                'ashen gauntlets of weeping': {
                    'type': 'armor',
                    'description': '',
                    'stats': {
                        'attack': 0,
                        'amount': 0,
                        'strength': 21,
                        'weight': 32,
                        'luck': 12,
                        'equipable': True
                    }
                },
                'eerie scroll of truth': {
                    'type': 'magic consumables',
                    'description': '',
                    'stats': {
                        'attack': 28,
                        'amount': 5,
                        'strength': 14,
                        'weight': 0,
                        'luck': 13,
                        'equipable': True
                    }
                }
            },
            'equipped': [
                'ashen gauntlets of weeping',
                'eerie scroll of truth'
            ]
        },
        'oagwn': {
            'name': 'oagwn',
            'description': 'the hero of dork!',
            'location': 'room 0',
            'inventory': {},
            'equipped': []
        }
    },
    'inventory': {
        'derelict note': {
            'type': 'filler',
            'description': '',
            'stats': {
                'attack': 0,
                'amount': 0,
                'strength': 0,
                'weight': 12,
                'luck': 7,
                'equipable': False
            }
        },
        'dirty charcoal': {
            'type': 'filler',
            'description': '',
            'stats': {
                'attack': 0,
                'amount': 0,
                'strength': 0,
                'weight': 7,
                'luck': -4,
                'equipable': False
            }
        },
        'greater potion of destruction': {
            'type': 'magic consumables',
            'description': '',
            'stats': {
                'attack': 28,
                'amount': 7,
                'strength': 8,
                'weight': 0,
                'luck': 13,
                'equipable': True
            }
        },
        'rusty meteorite longbow': {
            'type': 'weapon',
            'description': '',
            'stats': {
                'attack': 16,
                'amount': 0,
                'strength': 0,
                'weight': 14,
                'luck': 7,
                'equipable': True
            }
        }
    }
}


def verbose_print(data, calls=0):
    out = ""
    t = "   "
    for key, val in data.items():
        if isinstance(val, dict):
            out += t*calls + f"{key}:\n{verbose_print(val, calls+1)}"
        else:
            out += t*calls + f"{key}: {val}\n"
    return out


print(verbose_print(d))
