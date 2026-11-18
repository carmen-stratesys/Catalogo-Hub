import importlib.util
from pathlib import Path

import pytest

CARPETA = Path(__file__).resolve().parents[1]
TOOLS = ['leer_tickets', 'leer_sprints']


def cargar(nombre):
    ruta = CARPETA / "src" / "tools" / f"{nombre}.py"
    spec = importlib.util.spec_from_file_location(f"prueba_{nombre}", ruta)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return getattr(modulo, nombre)


@pytest.mark.parametrize('nombre', TOOLS)
def test_tool_devuelve_datos_ficticios(nombre):
    resultado = cargar(nombre)("proyecto-demo")
    assert resultado and resultado[0]['id'] == 'demo-1'


@pytest.mark.parametrize('nombre', TOOLS)
def test_tool_rechaza_proyecto_vacio(nombre):
    with pytest.raises(ValueError):
        cargar(nombre)(" ")
