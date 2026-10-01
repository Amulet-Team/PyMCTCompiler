from PyMCTCompiler.primitives.scripts.nbt import (
    NBTRemapHelper,
    EmptyNBT,
    merge,
    TranslationFile,
)
from .common import bedrock_is_movable, java_keep_packed

"""
Default
J113    "minecraft:command_block"		'{conditionMet: 0b, auto: 0b, CustomName: "{\"text\":\"@\"}", powered: 0b, Command: "", SuccessCount: 0, TrackOutput: 1b, UpdateLastExecution: 1b}'

B113	"CommandBlock"		            "{Command: "", CustomName: "", ExecuteOnFirstTick: 0b, LPCommandMode: 16064, LPCondionalMode: 63b, LPRedstoneMode: 0b, LastExecution: 0L, LastOutput: "", LastOutputParams: [], SuccessCount: 0, TickDelay: 0, TrackOutput: 1b, Version: 10, auto: 0b, conditionMet: 0b, isMovable: 1b, powered: 0b}"
"""

universal = {
    "nbt_identifier": ["universal_minecraft", "command_block"],
    "snbt": """{
        utags: {
            isMovable: 1b,
            auto: 0b,
            Command: "",
            conditionMet: 0b,
            CustomName: "{\\"text\\":\\"@\\"}",
            ExecuteOnFirstTick: 0b,
            LPCommandMode: 0,
            LPCondionalMode: 0b,
            LPRedstoneMode: 0b,
            LastExecution: 0l,
            LastOutput: "",
            LastOutputParams: [],
            powered: 0b,
            SuccessCount: 0,
            TickDelay: 0,
            TrackOutput: 1b,
            
            UpdateLastExecution: 1b
        }
    }""",
}

_J19 = NBTRemapHelper(
    [
        (
            ("auto", "byte", []),  # does not need power
            ("auto", "byte", [("utags", "compound")]),
        ),
        (("Command", "string", []), ("Command", "string", [("utags", "compound")])),
        (
            ("conditionMet", "byte", []),
            ("conditionMet", "byte", [("utags", "compound")]),
        ),
        (("CustomName", "string", []), (None, None, None)),
        (
            ("LastOutput", "string", []),
            ("LastOutput", "string", [("utags", "compound")]),
        ),
        (
            ("LastExecution", "long", []),
            ("LastExecution", "long", [("utags", "compound")]),
        ),
        (("powered", "byte", []), ("powered", "byte", [("utags", "compound")])),
        (("SuccessCount", "int", []), ("SuccessCount", "int", [("utags", "compound")])),
        (("TrackOutput", "byte", []), ("TrackOutput", "byte", [("utags", "compound")])),
    ],
    '{conditionMet: 0b, auto: 0b, powered: 0b, Command: "", SuccessCount: 0, TrackOutput: 1b}',
)

_J19_command_stats = NBTRemapHelper(
    [
        (
            ("CommandStats", "compound", []),
            ("CommandStats", "compound", [("utags", "compound")]),
        )
    ],
    "{}",
)

_J112_update_last = NBTRemapHelper(
    [
        (
            ("UpdateLastExecution", "byte", []),
            ("UpdateLastExecution", "byte", [("utags", "compound")]),
        )
    ],
    "{UpdateLastExecution: 1b}",
)

_JOldCustomName = TranslationFile(
    [
        {
            "function": "code",
            "options": {
                "input": ["nbt"],
                "output": ["new_nbt"],
                "function": "bedrock_cmd_custom_name_2u",
            },
        }
    ],
    [
        {
            "function": "code",
            "options": {
                "input": ["nbt"],
                "output": ["new_nbt"],
                "function": "bedrock_cmd_custom_name_fu",
            },
        }
    ],
    {"snbt": '{CustomName: "@"}'},
)

_J113 = NBTRemapHelper(
    [(("CustomName", "string", []), ("CustomName", "string", [("utags", "compound")]))],
    '{CustomName: "{\\"text\\":\\"@\\"}"}',
)

_B113 = NBTRemapHelper(
    [
        (
            ("auto", "byte", []),  # does not need power
            ("auto", "byte", [("utags", "compound")]),
        ),
        (("Command", "string", []), ("Command", "string", [("utags", "compound")])),
        (("conditionalMode", "byte", []), (None, None, None)),
        (
            ("conditionMet", "byte", []),
            ("conditionMet", "byte", [("utags", "compound")]),
        ),
        (("CustomName", "string", []), (None, None, None)),
        (
            ("ExecuteOnFirstTick", "byte", []),
            ("ExecuteOnFirstTick", "byte", [("utags", "compound")]),
        ),
        (
            (
                "LPCommandMode",
                "int",
                [],
            ),  # not sure what these three are for but they seem temporary
            ("LPCommandMode", "int", [("utags", "compound")]),
        ),
        (
            ("LPCondionalMode", "byte", []),
            ("LPCondionalMode", "byte", [("utags", "compound")]),
        ),
        (
            ("LPRedstoneMode", "byte", []),
            ("LPRedstoneMode", "byte", [("utags", "compound")]),
        ),
        (
            ("LastExecution", "long", []),
            ("LastExecution", "long", [("utags", "compound")]),
        ),
        (
            ("LastOutput", "string", []),
            ("LastOutput", "string", [("utags", "compound")]),
        ),
        (
            ("LastOutputParams", "list", []),
            ("LastOutputParams", "list", [("utags", "compound")]),
        ),
        (("powered", "byte", []), ("powered", "byte", [("utags", "compound")])),
        (("SuccessCount", "int", []), ("SuccessCount", "int", [("utags", "compound")])),
        (("TickDelay", "int", []), ("TickDelay", "int", [("utags", "compound")])),
        (("TrackOutput", "byte", []), ("TrackOutput", "byte", [("utags", "compound")])),
    ],
    '{Command: "", ExecuteOnFirstTick: 0b, LPCommandMode: 16064, LPCondionalMode: 63b, LPRedstoneMode: 0b, LastExecution: 0L, LastOutput: "", LastOutputParams: [], SuccessCount: 0, TickDelay: 0, TrackOutput: 1b, auto: 0b, conditionMet: 0b, powered: 0b}',
)

def bedrock_version(default_version: int) -> TranslationFile:
    return NBTRemapHelper(
        [
            (("Version", "int", []), ("BedrockCommandVersion", "int", [("utags", "compound")])),
        ],
        f"{{Version: {default_version}}}",
    )

_BCustomName = TranslationFile(
    [
        {
            "function": "code",
            "options": {
                "input": ["nbt"],
                "output": ["new_nbt"],
                "function": "bedrock_cmd_custom_name_2u",
            },
        }
    ],
    [
        {
            "function": "code",
            "options": {
                "input": ["nbt"],
                "output": ["new_nbt"],
                "function": "bedrock_cmd_custom_name_fu",
            },
        }
    ],
    {"snbt": '{CustomName: ""}'},
)

j19 = merge(
    [EmptyNBT("minecraft:command_block"), _J19, _J19_command_stats, _JOldCustomName],
    ["universal_minecraft:command_block"],
    abstract=True,
)

j112 = merge(
    [
        EmptyNBT("minecraft:command_block"),
        _J19,
        _J19_command_stats,
        _JOldCustomName,
        _J112_update_last,
    ],
    ["universal_minecraft:command_block"],
    abstract=True,
)

j113 = merge(
    [
        EmptyNBT("minecraft:command_block"),
        _J19,
        _J112_update_last,
        _J113,
        java_keep_packed,
    ],
    ["universal_minecraft:command_block"],
)

# def get_command_version(version: tuple[int, ...]) -> int:
#     if version >= (1, 26, 50):
#         return 52
#     elif version >= (1, 26, 40):
#         return 50
#     elif version >= (1, 26, 30):
#         return 49
#     elif version >= (1, 26, 20):
#         return 46
#     elif version >= (1, 21, 130):
#         return 45
#     elif version >= (1, 21, 90):
#         return 44
#     elif version >= (1, 21, 70):
#         return 43
#     elif version >= (1, 21, 30):
#         return 42
#     elif version >= (1, 21, 20):
#         return 41
#     elif version >= (1, 21, 0):
#         return 39
#     elif version >= (1, 20, 70):
#         return 38
#     elif version >= (1, 20, 60):
#         return 37
#     elif version >= (1, 20, 30):
#         return 36
#     elif version >= (1, 20, 10):
#         return 35
#     elif version >= (1, 20, 0):
#         return 34
#     elif version >= (1, 19, 80):
#         return 33
#     elif version >= (1, 19, 70):
#         return 32
#     elif version >= (1, 19, 60):
#         return 26
#     elif version >= (1, 19, 50):
#         return 25
#     elif version >= (1, 19, 40):
#         return 24
#     elif version >= (1, 19, 30):
#         return 23
#     elif version >= (1, 19, 10):
#         return 21
#     elif version >= (1, 19, 0):
#         return 20
#     elif version >= (1, 18, 30):
#         return 19
#     elif version >= (1, 18, 10):
#         return 18
#     elif version >= (1, 18, 0):
#         return 17
#     elif version >= (1, 17, 30):
#         return 16
#     elif version >= (1, 16, 220):
#         return 15
#     elif version >= (1, 16, 210):
#         return 14
#     elif version >= (1, 16, 100):
#         return 13
#     elif version >= (1, 16, 0):
#         return 12
#     elif version >= (1, 13, 0):
#         return 10
#     elif version >= (1, 9, 0):
#         return 9
#     else:
#         # There may be older versions but the servers do not go back that far
#         return 8

b7 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(8), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
    abstract=True,
)

b9 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(9), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
    abstract=True,
)

b13 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(10), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b16 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(12), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b16100 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(13), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b16210 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(14), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b16220 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(15), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1730 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(16), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b18 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(17), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1810 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(18), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1830 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(19), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b19 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(20), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1910 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(21), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1930 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(23), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1940 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(24), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1950 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(25), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1960 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(26), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1970 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(32), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b1980 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(33), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b20 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(34), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2010 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(35), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2030 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(36), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2060 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(37), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2070 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(38), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b21 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(39), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2120 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(41), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2130 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(42), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2170 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(43), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2190 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(44), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b21130 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(45), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2620 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(46), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2630 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(49), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2640 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(50), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)

b2650 = merge(
    [EmptyNBT(":CommandBlock"), _B113, bedrock_version(52), _BCustomName, bedrock_is_movable],
    ["universal_minecraft:command_block"],
)
