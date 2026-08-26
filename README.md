# Kalqui

Calculadora desktop com interface gráfica em Tkinter, tema rosa pastel e foco em uma experiência simples e agradável. O projeto separa a lógica matemática da interface e inclui testes automatizados para as operações e para o tratamento de overflow.

## Funcionalidades

- Adição, subtração, multiplicação e divisão
- Potenciação e módulo
- Raiz quadrada e fatorial
- Botões para limpar a expressão, apagar o último caractere e limpar tudo
- Formatação de números grandes em notação científica
- Proteção contra resultados muito grandes e expoentes fora do limite

## Requisitos

- Python 3.8 ou superior
- Tkinter instalado no sistema

No Ubuntu ou Debian, instale o Tkinter com:

```bash
sudo apt install python3-tk
```

As dependências listadas em `requirements.txt` são usadas para o ambiente de testes.

## Como executar

Na raiz do projeto, execute:

```bash
python3 src/main.py
```

## Como testar

Execute a suíte completa com:

```bash
python3 tests/test_kalqui.py
```

Para uma saída mais detalhada:

```bash
python3 tests/test_kalqui.py -v
```

## Limites numéricos

- Fatoriais até `170!`
- Expoentes entre `-1000` e `1000`
- Valores limitados aproximadamente ao intervalo suportado por `float64`
- Expressões da interface limitadas a 40 caracteres

## Estrutura do projeto

```text
kalqui/
├── assets/
│   └── screenschots/
├── src/
│   ├── calculator.py    # Lógica das operações matemáticas
│   ├── interface.py     # Interface gráfica Tkinter
│   └── main.py          # Ponto de entrada da aplicação
├── tests/
│   └── test_kalqui.py   # Testes automatizados
├── requirements.txt
└── README.md
```

## Arquitetura

`Calculator` concentra as operações e as validações numéricas. `CalculatorApp` gerencia a janela, os botões e o display, delegando os cálculos para a classe `Calculator`.
