from pprint import pprint


def introspection_info(obj):
    info = {
        "type": type(obj).__name__,
        "attributes": [],
        "methods": [],
        "module": getattr(obj, "__module__", None)
    }

    for attr in dir(obj):
        if callable(getattr(obj, attr)):
            info["methods"].append(attr)
        else:
            info["attributes"].append(attr)

    return info

number_info = introspection_info(42)
pprint(number_info)

class ExampleClass:
    def __init__(self, value):
        self.value = value

    def example_method(self):
        return self.value

example_object = ExampleClass(100)
example_info = introspection_info(example_object)
pprint(example_info)