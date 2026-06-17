from PyMCTCompiler.primitives.scripts.nbt import (
    EmptyNBT,
    merge,
    NBTRemapHelper,
)

"""
Default
J26.2       {countdown: 0} # countdown is seconds

B26.30      {}
"""

universal = {
    "nbt_identifier": ["universal_minecraft", "potent_sulfur"],
    "snbt": """{
        utags: {
            countdown: 0
        }
    }""",
}

_J262 = NBTRemapHelper(
    [
        (("countdown", "int", []), ("countdown", "int", [("utags", "compound")]))
    ],
    "{countdown: 0}",
)

j262 = merge([EmptyNBT("minecraft:potent_sulfur"), _J262], ["universal_minecraft:potent_sulfur"])

b2620 = merge([EmptyNBT(":PotentSulfurBlock")], ["universal_minecraft:potent_sulfur"])
