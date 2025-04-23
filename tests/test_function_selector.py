from core.function_selector import select_key_functions, score_function


def test_score_function():
    # Temel test fonksiyonu
    fn_base = {
        "name": "test_function",
        "fan_in": 0,
        "fan_out": 0,
        "is_entry_point": False,
        "docstring": ""
    }
    
    # Temel durumda puan sıfır olmalı
    assert score_function(fn_base) == 0
    
    # Fan-in etkisi (x2 çarpan)
    fn_fan_in = fn_base.copy()
    fn_fan_in["fan_in"] = 3
    assert score_function(fn_fan_in) == 6
    
    # Fan-out etkisi (x1 çarpan)
    fn_fan_out = fn_base.copy()
    fn_fan_out["fan_out"] = 4
    assert score_function(fn_fan_out) == 4
    
    # Entry point etkisi (+5 puan)
    fn_entry = fn_base.copy()
    fn_entry["is_entry_point"] = True
    assert score_function(fn_entry) == 5
    
    # Docstring etkisi (+2 puan)
    fn_doc = fn_base.copy()
    fn_doc["docstring"] = "This is a test function"
    assert score_function(fn_doc) == 2
    
    # Hepsi birlikte
    fn_all = {
        "name": "test_function",
        "fan_in": 3,
        "fan_out": 4,
        "is_entry_point": True,
        "docstring": "This is a test function"
    }
    # 3*2 + 4 + 5 + 2 = 17
    assert score_function(fn_all) == 17


def test_select_key_functions():
    # Sıralanacak fonksiyon listesi
    functions = [
        {
            "name": "low",
            "fan_in": 1,
            "fan_out": 0,
            "is_entry_point": False,
            "docstring": ""
        },
        {
            "name": "medium",
            "fan_in": 2,
            "fan_out": 1,
            "is_entry_point": False,
            "docstring": "docstring"
        },
        {
            "name": "high",
            "fan_in": 3,
            "fan_out": 2,
            "is_entry_point": True,
            "docstring": "docstring"
        }
    ]
    
    # Puan sıralaması:
    # high = 3*2 + 2 + 5 + 2 = 15
    # medium = 2*2 + 1 + 0 + 2 = 7
    # low = 1*2 + 0 + 0 + 0 = 2
    
    # Hepsini seçersek, puan sırasına göre gelmeliler
    all_selected = select_key_functions(functions, top_n=3)
    assert [f["name"] for f in all_selected] == ["high", "medium", "low"]
    
    # Sadece en önemli 2 taneyi seçersek
    top_two = select_key_functions(functions, top_n=2)
    assert [f["name"] for f in top_two] == ["high", "medium"]
    
    # Sadece en önemliyi seçersek
    top_one = select_key_functions(functions, top_n=1)
    assert [f["name"] for f in top_one] == ["high"]
    
    # Top_n fonksiyon sayısından büyükse, tüm fonksiyonlar dönmeli
    too_many = select_key_functions(functions, top_n=5)
    assert len(too_many) == 3 