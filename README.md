# frst
входящие данные: список словарей, словари могу быть вложенными (значением словаря может выступать другой словарь)
выходящие данные: словарь со всеми возможными ключами словарей из списка, где значения - список типов данных. В случае вложенного словаря для него сделать тоже самое. 

пример входящих данных: [{"a": 1},  {"a": "asd"}, {"b": {"c": 1}}, {"b": {"c": "1", "d": [True]}}, {"b": 1}]


пример результата: {"a": [int, str], "b": [int, {"c": [int, str], "d": list}]}
