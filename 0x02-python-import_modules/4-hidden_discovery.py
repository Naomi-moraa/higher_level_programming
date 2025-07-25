#!/usr/bin/python3
if __name__ == "__main__":
    import importlib.util
    import os

    # Path to the compiled module
    file_path = "hidden_4.pyc"

    # Load the module from .pyc file
    spec = importlib.util.spec_from_file_location("hidden_4", file_path)
    hidden_4 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(hidden_4)

    # Get all names in the module
    names = dir(hidden_4)

    # Filter and sort names that don't start with '__'
    for name in sorted(name for name in names if not name.startswith("__")):
        print(name)
