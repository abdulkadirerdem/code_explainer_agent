from core.function_selector import select_key_functions


def test_select_key_functions():
    functions = [
        {
            "name": "a",
            "fan_in": 5,
            "docstring": "yes",
            "fan_out": 1,
            "is_entry_point": False,
        },
        {
            "name": "b",
            "fan_in": 1,
            "docstring": "",
            "fan_out": 0,
            "is_entry_point": True,
        },
    ]

    top = select_key_functions(functions, top_n=1)
    assert top[0]["name"] == "a"  # fan_in daha yüksek olan "a" seçilmeli

    print(top)
