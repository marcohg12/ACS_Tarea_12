import pytest
import tkinter as tk
from interface import create_window, display_window
import os

if os.environ.get('DISPLAY','') == '':
    os.environ.__setitem__('DISPLAY', ':0.0')

# Prueba la creación de una ventana con la función create_window
def test_create_window():

    window = create_window()
    assert isinstance(window, tk.Tk)
    assert window.title() == "Una Ventana"

# Prueba el despliegue de una ventana con la función display_window
def test_display_window(monkeypatch):

    def mock_exit():
        raise SystemExit
    
    monkeypatch.setattr(tk.Tk, 'mainloop', lambda self: mock_exit())
    window = tk.Tk()
    window.title("Una Ventana de Prueba")

    with pytest.raises(SystemExit):

        display_window(window)