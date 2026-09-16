from PyMCTCompiler.compilers.java_blockstate_compiler import JavaBlockstateCompiler
import os

compiler = JavaBlockstateCompiler(
    os.path.dirname(__file__),
    version=[26, 3, 0],
    version_max_known=[26, 3],
    version_max=[100, -1],
    parent_version="java_26_2",
    data_version=5020,
    data_version_max_known=5023,
    data_version_max=2147483647,
)
