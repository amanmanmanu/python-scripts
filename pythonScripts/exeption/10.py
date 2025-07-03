# 10. Simulate ClassNotFoundException → AttributeError or ModuleNotFoundError

import importlib

module_name = input("Enter module name (e.g. math or fakeone): ")

try:
    mod = importlib.import_module(module_name)
    class_name = input("Enter class name (e.g. sqrt or FakeClass): ")
    attr = getattr(mod, class_name)
    print("Found:", attr)
except ModuleNotFoundError:
    print("Module not found.")
except AttributeError:
    print("Class or function not found in module.")
