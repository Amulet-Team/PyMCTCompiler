from PyMCTCompiler.compilers.java_blockstate_compiler import JavaBlockstateCompiler
import os

compiler = JavaBlockstateCompiler(
    os.path.dirname(__file__),
    version=[26, 2, 0],
    version_max_known=[26, 2],
    version_max=[26, 3, -1],
    parent_version="java_26_1",
    data_version=4901,
    data_version_max_known=4903,
    data_version_max=4903,
)
