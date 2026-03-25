from PyMCTCompiler.compilers.nbt_blockstate_compiler import NBTBlockstateCompiler
import os

compiler = NBTBlockstateCompiler(
    os.path.dirname(__file__),
    version=[26, 10],
    version_max_known=[26, 10],
    version_max=[100, -1],
    parent_version="bedrock_1_21_110",
    data_version=18168865,
    data_version_max_known=18168865,
    data_version_max=4294967295,
)
