from PyMCTCompiler.compilers.java_blockstate_compiler import JavaBlockstateCompiler
import os

compiler = JavaBlockstateCompiler(
    os.path.dirname(__file__),
    version=[26, 1, 0],
    version_max_known=[26, 1],
    version_max=[100, -1],
    parent_version="java_1_21_9",
    data_version=4786,
    data_version_max_known=4786,
    data_version_max=2147483647,
)
