import sys
from pathlib import Path

# Garante que a raiz do projeto esteja no PYTHONPATH (Pulumi executa de src/pulumi)
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from src.equiny.gcp.stack import build_stack

build_stack()
