__author__ = 'Parthan'

"""JSON encoder"""

def json_encode(data):
    if isinstance(data, bool):
        return str(data).lower()
    elif isinstance(data, str):
        return '"'+ data +'"'
    elif isinstance(data, int):
        return str(data)
    elif isinstance(data, list):
        x = [json_encode(d) for d in data]
        return "[" + ", ".join(x) + "]"
    elif isinstance(data, dict):
        x = [json_encode(key)+": "+json_encode(value) for key, value in data.iteritems()]
        return "{" + ', '.join(x) + "}"

# {"x": [1,2,3], "y": "apple", "z": {1: "one", 2: "two"}}
sample = {'x': [1,2,3], 'y': 'apple', 'z': {1: 'one', 2: 'two'}}
