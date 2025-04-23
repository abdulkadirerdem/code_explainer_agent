import json
import pytest
from unittest.mock import patch, mock_open
from core.input_loader import load_dummy_input


@patch("builtins.open", new_callable=mock_open, read_data='{"test": "data"}')
def test_load_dummy_input(mock_file):
    # Fonksiyonu çağır
    result = load_dummy_input()
    
    # Dosya doğru parametrelerle açıldı mı?
    mock_file.assert_called_once_with("examples/dummy_input.json", "r", encoding="utf-8")
    
    # Sonuçlar doğru mu?
    assert isinstance(result, dict)
    assert result == {"test": "data"}


@patch("builtins.open", new_callable=mock_open, read_data='{"custom": "value"}')
def test_load_dummy_input_custom_path(mock_file):
    # Özel yol ile fonksiyonu çağır
    result = load_dummy_input("custom/path.json")
    
    # Doğru dosya açıldı mı?
    mock_file.assert_called_once_with("custom/path.json", "r", encoding="utf-8")
    
    # Sonuçlar doğru mu?
    assert result == {"custom": "value"} 