import json
from core.formatter import format_as_json, format_as_markdown


def test_format_as_json():
    # Test verileri
    file = "test_file.py"
    summarized = [
        {
            "name": "test_function",
            "code": "def test_function():\n    return True",
            "explanation": "Bu bir test fonksiyonudur"
        }
    ]
    
    # Json formatına dönüştürme
    result = format_as_json(file, summarized)
    
    # JSON olarak parse edilebilmeli
    parsed = json.loads(result)
    
    # Beklenen yapıya sahip olduğunu kontrol etme
    assert parsed["file"] == file
    assert len(parsed["summarized_functions"]) == 1
    assert parsed["summarized_functions"][0]["name"] == "test_function"


def test_format_as_markdown():
    # Test verileri
    file = "test_file.py"
    summarized = [
        {
            "name": "test_function",
            "code": "def test_function():\n    return True",
            "explanation": "Bu bir test fonksiyonudur"
        }
    ]
    
    # Markdown formatına dönüştürme
    result = format_as_markdown(file, summarized)
    
    # Markdown içeriğini kontrol etme
    assert f"# 📄 Documentation for `{file}`" in result
    assert "## 🔹 Function: `test_function`" in result
    assert "```python\ndef test_function():\n    return True\n```" in result
    assert "**Explanation:**" in result
    assert "Bu bir test fonksiyonudur" in result 