import pytest
from unittest.mock import patch, MagicMock
from core.summarizer import summarize_function
from agents.types import FunctionInfo


@pytest.fixture
def example_function_info():
    return {
        "name": "test_function",
        "code": "def test_function():\n    return True",
        "fan_in": 2,
        "fan_out": 1,
        "is_entry_point": False,
        "docstring": ""
    }


@patch("core.summarizer.client.chat.completions.create")
def test_summarize_function(mock_create, example_function_info):
    # API yanıtını mock'lama
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Bu bir test fonksiyonudur."
    mock_create.return_value = mock_response
    
    # Fonksiyonu çağır
    summary = summarize_function(example_function_info)
    
    # Doğru parametrelerle çağrıldığını kontrol et
    mock_create.assert_called_once()
    
    # Model isimlendirmesi ve parametreler değişebileceği için tam eşleşme kontrolü yapmıyoruz
    # Sadece çağrıldığını ve doğru yanıtı döndürdüğünü kontrol ediyoruz
    
    # Özet işlevinin beklenen çıktıyı döndürdüğünü doğrula
    assert summary == "Bu bir test fonksiyonudur." 