from pathlib import Path

import yaml

CARPETA = Path(__file__).resolve().parents[1]


def test_hay_casos_de_evaluacion_ficticios():
    casos = yaml.safe_load((CARPETA / "evaluacion" / "casos.yaml").read_text(encoding="utf-8"))
    assert casos and all(caso.get('entrada') and caso.get('se_espera') for caso in casos)
