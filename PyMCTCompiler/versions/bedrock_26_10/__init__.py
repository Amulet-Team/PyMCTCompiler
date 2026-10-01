from PyMCTCompiler.compilers.nbt_blockstate_compiler import NBTBlockstateCompiler
import os

compiler = NBTBlockstateCompiler(
    os.path.dirname(__file__),
    version=[26, 10, 0],
    version_max_known=[26, 14],
    version_max=[26, 20, -1],
    parent_version="bedrock_1_21_130",
    data_version=18168865,
    data_version_max_known=18168865,
    data_version_max=18168865,
)
