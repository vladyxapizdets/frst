
import pprint as p
list = [{"a": 1},  {"a": "asd"}, {"b": {"c": 1}}, {"b": {"c": "1", "d": [True]}}, {"b": 1}]
finally_dict= {}

def app(key, value):
    if key in finally_dict:
        finally_dict[key].append(str(type(value))[8:-2])
    else:
        finally_dict[key] = [str(type(value))[8:-2]]

def if_dict(dict):
    for key, value in dict.items():
        if type(value) == dict:
            if_dict(value)
        else:
            app(key, value)

for i in list:
    if type(i)==dict:
        if_dict(i)
    else:
        print("vladick gay")
p.pprint(finally_dict)
