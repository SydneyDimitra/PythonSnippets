"""Run script from any DCC """
import os
import sys
from importlib import import_module

script = "/full/path/to/script.py"
script_module_name = os.path.splitext(os.path.basename(script))[0]
script_path = os.path.dirname(script)
if script_path not in sys.path:
    sys.path.insert(0, script_path)

script_module = import_module(script_module_name)
reload(script_module)
script_module.main()
