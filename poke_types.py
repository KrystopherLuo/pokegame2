types = {
    "normal": {
        "offensive": {
            "advantages": [],
            "disadvantages": ["rock", "steel"],
            "immune": ["ghost"]
        },
        "defensive": {
            "advantages": [],
            "disadvantages": ["fighting"],
            "immune": ["ghost"]
        },
    },

    "fire": {
        "offensive": {
            "advantages": ["grass", "ice", "bug", "steel"],
            "disadvantages": ["fire", "water", "rock", "dragon"],
            "immune": []
        },
        "defensive": {
            "advantages": ["fire", "grass", "ice", "bug", "steel", "fairy"],
            "disadvantages": ["water", "ground", "rock"],
            "immune": []
        },
    },

    "water": {
        "offensive": {
            "advantages": ["fire", "ground", "rock"],
            "disadvantages": ["water", "grass", "dragon"],
            "immune": []
        },
        "defensive": {
            "advantages": ["fire", "water", "ice", "steel"],
            "disadvantages": ["electric", "grass"],
            "immune": []
        },
    },

    "electric": {
        "offensive": {
            "advantages": ["water", "flying"],
            "disadvantages": ["electric", "grass", "dragon"],
            "immune": ["ground"]
        },
        "defensive": {
            "advantages": ["electric", "flying", "steel"],
            "disadvantages": ["ground"],
            "immune": []
        },
    },

    "grass": {
        "offensive": {
            "advantages": ["water", "ground", "rock"],
            "disadvantages": [
                "fire", "grass", "poison", "flying",
                "bug", "dragon", "steel"
            ],
            "immune": []
        },
        "defensive": {
            "advantages": ["water", "electric", "grass", "ground"],
            "disadvantages": ["fire", "ice", "poison", "flying", "bug"],
            "immune": []
        },
    },

    "ice": {
        "offensive": {
            "advantages": ["grass", "ground", "flying", "dragon"],
            "disadvantages": ["fire", "water", "ice", "steel"],
            "immune": []
        },
        "defensive": {
            "advantages": ["ice"],
            "disadvantages": ["fire", "fighting", "rock", "steel"],
            "immune": []
        },
    },

    "fighting": {
        "offensive": {
            "advantages": ["normal", "ice", "rock", "dark", "steel"],
            "disadvantages": ["poison", "flying", "psychic", "bug", "fairy"],
            "immune": ["ghost"]
        },
        "defensive": {
            "advantages": ["bug", "rock", "dark"],
            "disadvantages": ["flying", "psychic", "fairy"],
            "immune": []
        },
    },

    "poison": {
        "offensive": {
            "advantages": ["grass", "fairy"],
            "disadvantages": ["poison", "ground", "rock", "ghost"],
            "immune": ["steel"]
        },
        "defensive": {
            "advantages": ["grass", "fighting", "poison", "bug", "fairy"],
            "disadvantages": ["ground", "psychic"],
            "immune": []
        },
    },

    "ground": {
        "offensive": {
            "advantages": ["fire", "electric", "poison", "rock", "steel"],
            "disadvantages": ["grass", "bug"],
            "immune": ["flying"]
        },
        "defensive": {
            "advantages": ["poison", "rock"],
            "disadvantages": ["water", "grass", "ice"],
            "immune": ["electric"]
        },
    },

    "flying": {
        "offensive": {
            "advantages": ["grass", "fighting", "bug"],
            "disadvantages": ["electric", "rock", "steel"],
            "immune": []
        },
        "defensive": {
            "advantages": ["grass", "fighting", "bug"],
            "disadvantages": ["electric", "ice", "rock"],
            "immune": ["ground"]
        },
    },

    "psychic": {
        "offensive": {
            "advantages": ["fighting", "poison"],
            "disadvantages": ["psychic", "steel"],
            "immune": ["dark"]
        },
        "defensive": {
            "advantages": ["fighting", "psychic"],
            "disadvantages": ["bug", "ghost", "dark"],
            "immune": []
        },
    },

    "bug": {
        "offensive": {
            "advantages": ["grass", "psychic", "dark"],
            "disadvantages": ["fire", "fighting", "poison", "flying", "ghost", "steel", "fairy"],
            "immune": []
        },
        "defensive": {
            "advantages": ["grass", "fighting", "ground"],
            "disadvantages": ["fire", "flying", "rock"],
            "immune": []
        },
    },

    "rock": {
        "offensive": {
            "advantages": ["fire", "ice", "flying", "bug"],
            "disadvantages": ["fighting", "ground", "steel"],
            "immune": []
        },
        "defensive": {
            "advantages": ["normal", "fire", "poison", "flying"],
            "disadvantages": ["water", "grass", "fighting", "ground", "steel"],
            "immune": []
        },
    },

    "ghost": {
        "offensive": {
            "advantages": ["psychic", "ghost"],
            "disadvantages": ["dark"],
            "immune": ["normal"]
        },
        "defensive": {
            "advantages": ["poison", "bug"],
            "disadvantages": ["ghost", "dark"],
            "immune": ["normal", "fighting"]
        },
    },

    "dragon": {
        "offensive": {
            "advantages": ["dragon"],
            "disadvantages": ["steel"],
            "immune": ["fairy"]
        },
        "defensive": {
            "advantages": ["fire", "water", "electric", "grass"],
            "disadvantages": ["ice", "dragon", "fairy"],
            "immune": []
        },
    },

    "dark": {
        "offensive": {
            "advantages": ["psychic", "ghost"],
            "disadvantages": ["fighting", "dark", "fairy"],
            "immune": []
        },
        "defensive": {
            "advantages": ["ghost", "dark"],
            "disadvantages": ["fighting", "bug", "fairy"],
            "immune": ["psychic"]
        },
    },

    "steel": {
        "offensive": {
            "advantages": ["ice", "rock", "fairy"],
            "disadvantages": ["fire", "water", "electric", "steel"],
            "immune": []
        },
        "defensive": {
            "advantages": [
                "normal", "grass", "ice", "flying", "psychic",
                "bug", "rock", "dragon", "steel", "fairy"
            ],
            "disadvantages": ["fire", "fighting", "ground"],
            "immune": ["poison"]
        },
    },

    "fairy": {
        "offensive": {
            "advantages": ["fighting", "dragon", "dark"],
            "disadvantages": ["fire", "poison", "steel"],
            "immune": []
        },
        "defensive": {
            "advantages": ["fighting", "bug", "dark"],
            "disadvantages": ["poison", "steel"],
            "immune": ["dragon"]
        },
    },
}