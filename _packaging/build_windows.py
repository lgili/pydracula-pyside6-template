
from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','pydracula/themes/']

# TARGET
target = Executable(
    script="run.py",
    base="Win32GUI",
    icon="icon.ico"
)

# SETUP CX FREEZE
setup(
    name = "PyDracula",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Wanderson M. Pimenta",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]    
)