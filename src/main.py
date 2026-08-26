"""
Arquivo principal da aplicação Kalqui
Executa a interface gráfica da calculadora.
"""

import sys
from pathlib import Path

# Adiciona o diretório src ao path para importar os módulos
sys.path.insert(0, str(Path(__file__).parent))

from interface import main

if __name__ == "__main__":
    main()
