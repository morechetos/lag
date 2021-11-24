import sys
from cx_Freeze import setup, Executable

base = None

if sys.platform == "win32":
    base = "Win32GUI"

setup(name="puzzle",
      version="0.1",
      description="Fun computer game",
      executables=[Executable("client.py", base=base)])

# python setup.py build
