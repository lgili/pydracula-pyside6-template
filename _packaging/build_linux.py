from cx_Freeze import setup, Executable

# ADD FILES
files = ['icon.ico','pydracula/themes/']

# TARGET
target = Executable(
    script="run.py",
    icon="icon.ico"
)

options = {
    "build_exe": {
        "excludes": [
            "tkinter",
            "PyQt5",
            "PyQt6",
        ],
        "zip_include_packages": ["PySide6"],
        'include_files' : files
    },
}

# SETUP CX FREEZE
setup(
    name = "PyDracula",
    version = "1.0",
    description = "Modern GUI for Python applications",
    author = "Wanderson M. Pimenta",
    options = options,
    executables = [target]    
)