from typing import Callable, Iterable

from PyMCTCompiler.primitives.scripts.nbt import (
    NBTRemapHelper,
    TranslationFile,
    EmptyNBT,
    merge,
)
from .common import bedrock_is_movable, java_keep_packed

"""
Default
J113    "minecraft:skull"		"{}"

B113	"Skull"		"{MouthMoving: 0b, MouthTickCount: 0, Rotation: -90.0f, SkullType: 0b, isMovable: 1b}"
"""

universal = {
    "nbt_identifier": ["universal_minecraft", "head"],
    "snbt": """{
        utags: {
            isMovable: 1b,
            MouthMoving: 0b,
            MouthTickCount: 0
        }
    }""",
}

_B17 = NBTRemapHelper(
    [
        (("MouthMoving", "byte", []), ("MouthMoving", "byte", [("utags", "compound")])),
        (
            ("MouthTickCount", "int", []),
            ("MouthTickCount", "int", [("utags", "compound")]),
        ),
        (("Rotation", "float", []), (None, None, None)),
    ],
    "{MouthMoving: 0b, MouthTickCount: 0, Rotation: 0.0f, SkullType: 0b}",
)

SkullTypes = [
    '"skeleton"',
    '"wither_skeleton"',
    '"zombie"',
    '"player"',
    '"creeper"',
    '"dragon"',
]

bedrock_wall_directions = ['"north"', '"south"', '"west"', '"east"']
no_drop_bits = ['"false"', '"true"']

_BExtra_17 = TranslationFile(
    [
        {
            "function": "walk_input_nbt",
            "options": {
                "type": "compound",
                "keys": {
                    "SkullType": {
                        "type": "byte",
                        "functions": [
                            {
                                "function": "map_nbt",
                                "options": {
                                    "cases": {
                                        f"{skull_num}b": [
                                            {
                                                "function": "new_properties",
                                                "options": {"mob": skull_type},
                                            }
                                        ]
                                        for skull_num, skull_type in enumerate(
                                            SkullTypes
                                        )
                                    }
                                },
                            }
                        ],
                    }
                },
            },
        },
        {
            "function": "map_properties",
            "options": {
                "block_data": {
                    str(data8 * 8 + 1): [
                        {
                            "function": "code",
                            "options": {
                                "input": ["nbt"],
                                "output": ["new_properties"],
                                "function": "bedrock_skull_rotation_2u",
                            },
                        }
                    ]
                    for data8, no_drop_bit in enumerate(no_drop_bits)
                }
            },
        },
    ],
    {
        "universal_minecraft:head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    },
                    "rotation": {
                        f'"{rot}"': [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {
                                        "key": "Rotation",
                                        "value": f"{rot * 22.5 - 360 * (rot > 8)}f",
                                    }
                                ],
                            }
                        ]
                        for rot in range(16)
                    },
                },
            }
        ],
        "universal_minecraft:wall_head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    }
                },
            }
        ],
    },
)

_BExtra_113 = TranslationFile(
    [
        {
            "function": "walk_input_nbt",
            "options": {
                "type": "compound",
                "keys": {
                    "SkullType": {
                        "type": "byte",
                        "functions": [
                            {
                                "function": "map_nbt",
                                "options": {
                                    "cases": {
                                        f"{skull_num}b": [
                                            {
                                                "function": "new_properties",
                                                "options": {"mob": skull_type},
                                            }
                                        ]
                                        for skull_num, skull_type in enumerate(
                                            SkullTypes
                                        )
                                    }
                                },
                            }
                        ],
                    }
                },
            },
        },
        {
            "function": "map_properties",
            "options": {
                "facing_direction": {
                    "1": [
                        {
                            "function": "code",
                            "options": {
                                "input": ["nbt"],
                                "output": ["new_properties"],
                                "function": "bedrock_skull_rotation_2u",
                            },
                        }
                    ]
                }
            },
        },
    ],
    {
        "universal_minecraft:head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    },
                    "rotation": {
                        f'"{rot}"': [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {
                                        "key": "Rotation",
                                        "value": f"{rot * 22.5 - 360 * (rot > 8)}f",
                                    }
                                ],
                            }
                        ]
                        for rot in range(16)
                    },
                },
            }
        ],
        "universal_minecraft:wall_head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    }
                },
            }
        ],
    },
)

_BExtra_12140 = TranslationFile(
    [
        {
            "function": "map_properties",
            "options": {
                "facing_direction": {
                    "1": [
                        {
                            "function": "code",
                            "options": {
                                "input": ["nbt"],
                                "output": ["new_properties"],
                                "function": "bedrock_skull_rotation_2u",
                            },
                        }
                    ]
                }
            },
        },
    ],
    {
        "universal_minecraft:head": [
            {
                "function": "map_properties",
                "options": {
                    "rotation": {
                        f'"{rot}"': [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {
                                        "key": "Rotation",
                                        "value": f"{rot * 22.5 - 360 * (rot > 8)}f",
                                    }
                                ],
                            }
                        ]
                        for rot in range(16)
                    },
                },
            }
        ],
        "universal_minecraft:wall_head": [],
    },
)

_J19 = TranslationFile(
    [
        {
            "function": "walk_input_nbt",
            "options": {
                "type": "compound",
                "keys": {
                    "SkullType": {
                        "type": "byte",
                        "functions": [
                            {
                                "function": "map_nbt",
                                "options": {
                                    "cases": {
                                        f"{skull_num}b": [
                                            {
                                                "function": "new_properties",
                                                "options": {"mob": skull_type},
                                            }
                                        ]
                                        for skull_num, skull_type in enumerate(
                                            SkullTypes
                                        )
                                    }
                                },
                            }
                        ],
                    },
                    "Rot": {
                        "type": "byte",
                        "functions": [
                            {
                                "function": "map_properties",
                                "options": {
                                    "block_data": {
                                        "1": [
                                            {
                                                "function": "map_nbt",
                                                "options": {
                                                    "cases": {
                                                        f"{rot}b": [
                                                            {
                                                                "function": "new_properties",
                                                                "options": {
                                                                    "rotation": f'"{rot}"'
                                                                },
                                                            }
                                                        ]
                                                        for rot in range(16)
                                                    }
                                                },
                                            }
                                        ]
                                    }
                                },
                            }
                        ],
                    },
                },
            },
        }
    ],
    {
        "universal_minecraft:head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    },
                    "rotation": {
                        f'"{rot}"': [
                            {
                                "function": "new_nbt",
                                "options": [{"key": "Rotation", "value": f"{rot}b"}],
                            }
                        ]
                        for rot in range(16)
                    },
                },
            }
        ],
        "universal_minecraft:wall_head": [
            {
                "function": "map_properties",
                "options": {
                    "mob": {
                        skull_type: [
                            {
                                "function": "new_nbt",
                                "options": [
                                    {"key": "SkullType", "value": f"{skull_num}b"}
                                ],
                            }
                        ]
                        for skull_num, skull_type in enumerate(SkullTypes)
                    }
                },
            }
        ],
    },
)


def get_player_translation_file(
    tag_name: str, universal_name: str, func_name: str, default_block: str
) -> Callable[[Iterable[str]], TranslationFile]:
    def get(universal_names: Iterable[str]) -> TranslationFile:
        return TranslationFile(
            [
                {
                    "function": "walk_input_nbt",
                    "options": {
                        "type": "compound",
                        "keys": {
                            tag_name: {
                                "type": "compound",
                                "functions": [
                                    {
                                        "function": "carry_nbt",
                                        "options": {
                                            "path": [["utags", "compound"]],
                                            "key": universal_name,
                                        },
                                    }
                                ],
                            }
                        },
                    },
                }
            ],
            {
                name: [
                    {"function": "new_block", "options": default_block},
                    {
                        "function": "map_properties",
                        "options": {
                            "mob": {
                                '"player"': [
                                    {
                                        "function": "code",
                                        "options": {
                                            "input": ["nbt"],
                                            "output": ["new_nbt"],
                                            "function": func_name,
                                        },
                                    }
                                ]
                            }
                        },
                    },
                ]
                for name in universal_names
            },
        )

    return get


_Player_J19 = get_player_translation_file(
    "Owner", "owner_j19", "java_skull_fu_19", "minecraft:skull"
)

# 2514 (1.16 snapshot)
# Renamed Owner -> SkullOwner
# SkullOwner[Id] string converted to list[int, 4]
_Player_J116 = get_player_translation_file(
    "SkullOwner", "owner_j116", "java_skull_fu_116", "minecraft:skeleton_skull"
)

# 3818 (1.20.5 snapshot)
# Renamed SkullOwner -> profile
# Properties -> properties and refactored
_Player_J1205 = get_player_translation_file(
    "profile", "owner_j1205", "java_skull_fu_1215", "minecraft:skeleton_skull"
)

j19 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J19(["universal_minecraft:head", "universal_minecraft:wall_head"]),
        _J19,
    ],
    ["universal_minecraft:head", "universal_minecraft:wall_head"],
    abstract=True,
)

j113 = merge(
    [EmptyNBT("minecraft:skull"), java_keep_packed], ["universal_minecraft:head"]
)

wall_j113 = merge(
    [EmptyNBT("minecraft:skull"), java_keep_packed],
    ["universal_minecraft:wall_head"],
)

player_j113 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J19(["universal_minecraft:head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:head"],
)

player_wall_j113 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J19(["universal_minecraft:wall_head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:wall_head"],
)

player_j116 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J116(["universal_minecraft:head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:head"],
)

player_wall_j116 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J116(["universal_minecraft:wall_head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:wall_head"],
)

player_j1205 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J1205(["universal_minecraft:head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:head"],
)

player_wall_j1205 = merge(
    [
        EmptyNBT("minecraft:skull"),
        _Player_J1205(["universal_minecraft:wall_head"]),
        java_keep_packed,
    ],
    ["universal_minecraft:wall_head"],
)

b17 = merge(
    [EmptyNBT(":Skull"), _B17, _BExtra_17, bedrock_is_movable],
    ["universal_minecraft:head", "universal_minecraft:wall_head"],
    abstract=True,
)

b113 = merge(
    [EmptyNBT(":Skull"), _B17, _BExtra_113, bedrock_is_movable],
    ["universal_minecraft:head", "universal_minecraft:wall_head"],
)

b12140 = merge(
    [EmptyNBT(":Skull"), _B17, _BExtra_12140, bedrock_is_movable],
    ["universal_minecraft:head", "universal_minecraft:wall_head"],
)
