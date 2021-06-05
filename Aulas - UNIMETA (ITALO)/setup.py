import sys
from cx_Freeze import setup, Executable
from tkinter import*

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("aula.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ['tkinter'],
        include_files = [],
        excludes = []
)




setup(
    name = "Teste",
    version = "1.0",
    description = "Descrição do programa",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
