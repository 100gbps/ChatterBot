from importlib import import_module as import_string
from inspect import isclass


def import_module(dotted_path):
    """
    Imports the specified module based on the
    dot notated import path for the module.
    """

    module_path, class_name = dotted_path.rsplit('.', 1)

    module = import_string(module_path)

    if hasattr(module, class_name):
        return getattr(module, class_name)

    return import_string(dotted_path)

