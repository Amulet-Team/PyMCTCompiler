from PyMCTCompiler.compilers.nbt_blockstate_compiler import NBTBlockstateCompiler
import os

compiler = NBTBlockstateCompiler(
    os.path.dirname(__file__),
    version=[1, 19, 30],
    version_max_known=[1, 19, 31],
    version_max=[1, 19, 40, -1],
    parent_version="bedrock_1_19_20",
    data_version=17959425,
    data_version_max_known=17959425,
    data_version_max=17959425,
)
