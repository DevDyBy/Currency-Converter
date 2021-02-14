import sys
from cx_Freeze import setup, Executable

base = None
if (sys.platform == "win32"):
    base = "Win32GUI"

executables = [Executable("main1.py", base=base, icon="icon.png")]

packages = ["idna", "PyQt5", "currency_converter", "sys"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Converter",
    options = options,
    version = "<1.0.1>",
    description = '',
    executables =[Executable("main1.py", base=base)]
)