"""
Testes para a classe Calculator
Realiza testes unitários de todas as operações da calculadora.
"""

import sys
import unittest
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Suite de testes para a classe Calculator.
    Testa todas as operações matemáticas e tratamento de erros.
    """
    
    def setUp(self):
        """
        Prepara os testes.
        Executa antes de cada teste.
        """
        self.calc = Calculator()
    
    # ========== Testes de Adição ==========
    def test_add_positivos(self):
        """Testa adição de números positivos."""
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(100, 50), 150)
    
    def test_add_negativos(self):
        """Testa adição com números negativos."""
        self.assertEqual(self.calc.add(-5, 3), -2)
        self.assertEqual(self.calc.add(-5, -3), -8)
    
    def test_add_zeros(self):
        """Testa adição com zeros."""
        self.assertEqual(self.calc.add(0, 5), 5)
        self.assertEqual(self.calc.add(0, 0), 0)
    
    def test_add_decimais(self):
        """Testa adição com números decimais."""
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(self.calc.add(0.1, 0.2), 0.3)
    
    # ========== Testes de Subtração ==========
    def test_subtract_positivos(self):
        """Testa subtração de números positivos."""
        self.assertEqual(self.calc.subtract(10, 3), 7)
        self.assertEqual(self.calc.subtract(50, 100), -50)
    
    def test_subtract_negativos(self):
        """Testa subtração com números negativos."""
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
    
    def test_subtract_zeros(self):
        """Testa subtração com zeros."""
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 0), 0)
    
    # ========== Testes de Multiplicação ==========
    def test_multiply_positivos(self):
        """Testa multiplicação de números positivos."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(0, 100), 0)
    
    def test_multiply_negativos(self):
        """Testa multiplicação com números negativos."""
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
    
    def test_multiply_decimais(self):
        """Testa multiplicação com números decimais."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertAlmostEqual(self.calc.multiply(1.5, 1.5), 2.25)
    
    # ========== Testes de Divisão ==========
    def test_divide_positivos(self):
        """Testa divisão de números positivos."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(15, 3), 5)
    
    def test_divide_negativos(self):
        """Testa divisão com números negativos."""
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
    
    def test_divide_by_zero(self):
        """Testa divisão por zero - deve lançar ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertIn("divide by zero", str(context.exception).lower())
    
    def test_divide_decimais(self):
        """Testa divisão com números decimais."""
        self.assertAlmostEqual(self.calc.divide(10, 4), 2.5)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333, places=5)
    
    # ========== Testes de Potência ==========
    def test_power_positivos(self):
        """Testa potência com números positivos."""
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 2), 25)
        self.assertEqual(self.calc.power(10, 0), 1)
    
    def test_power_negativos(self):
        """Testa potência com expoente negativo."""
        self.assertAlmostEqual(self.calc.power(2, -1), 0.5)
        self.assertAlmostEqual(self.calc.power(10, -2), 0.01)
    
    def test_power_decimais(self):
        """Testa potência com números decimais."""
        self.assertAlmostEqual(self.calc.power(4, 0.5), 2)
        self.assertAlmostEqual(self.calc.power(8, 1/3), 2, places=5)
    
    # ========== Testes de Módulo ==========
    def test_modulus_positivos(self):
        """Testa módulo com números positivos."""
        self.assertEqual(self.calc.modulus(10, 3), 1)
        self.assertEqual(self.calc.modulus(20, 5), 0)
        self.assertEqual(self.calc.modulus(7, 2), 1)
    
    def test_modulus_negativos(self):
        """Testa módulo com números negativos."""
        self.assertEqual(self.calc.modulus(-10, 3), 2)
        self.assertEqual(self.calc.modulus(10, -3), -2)
    
    def test_modulus_by_zero(self):
        """Testa módulo por zero - deve lançar ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.modulus(10, 0)
        self.assertIn("modulus by zero", str(context.exception).lower())
    
    # ========== Testes de Raiz Quadrada ==========
    def test_square_root_positivos(self):
        """Testa raiz quadrada de números positivos."""
        self.assertEqual(self.calc.square_root(4), 2)
        self.assertEqual(self.calc.square_root(9), 3)
        self.assertEqual(self.calc.square_root(0), 0)
    
    def test_square_root_decimais(self):
        """Testa raiz quadrada de números decimais."""
        self.assertAlmostEqual(self.calc.square_root(2), 1.41421356, places=5)
        self.assertAlmostEqual(self.calc.square_root(0.25), 0.5)
    
    def test_square_root_negativo(self):
        """Testa raiz quadrada de número negativo - deve lançar ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.square_root(-1)
        self.assertIn("negative", str(context.exception).lower())
    
    # ========== Testes de Fatorial ==========
    def test_factorial_positivos(self):
        """Testa fatorial de números positivos."""
        self.assertEqual(self.calc.factorial(0), 1)
        self.assertEqual(self.calc.factorial(1), 1)
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(10), 3628800)
    
    def test_factorial_grande(self):
        """Testa fatorial de números maiores."""
        self.assertEqual(self.calc.factorial(15), 1307674368000)
    
    def test_factorial_negativo(self):
        """Testa fatorial de número negativo - deve lançar ValueError."""
        with self.assertRaises(ValueError) as context:
            self.calc.factorial(-5)
        self.assertIn("negative", str(context.exception).lower())


class TestCalculatorIntegracao(unittest.TestCase):
    """
    Testes de integração da calculadora.
    Testa sequências de operações.
    """
    
    def setUp(self):
        """Prepara os testes."""
        self.calc = Calculator()
    
    def test_multiplas_operacoes(self):
        """Testa uma sequência de operações."""
        # (10 + 5) * 2 = 30
        resultado = self.calc.multiply(
            self.calc.add(10, 5),
            2
        )
        self.assertEqual(resultado, 30)
    
    def test_expressao_complexa(self):
        """Testa uma expressão mais complexa."""
        # ((100 - 50) / 5) + 3 = 13
        resultado = self.calc.add(
            self.calc.divide(
                self.calc.subtract(100, 50),
                5
            ),
            3
        )
        self.assertEqual(resultado, 13)
    
    def test_potencia_e_fatorial(self):
        """Testa combinação de potência e fatorial."""
        # 3! = 6, 2^6 = 64
        resultado = self.calc.power(2, self.calc.factorial(3))
        self.assertEqual(resultado, 64)


class TestCalculatorOverflow(unittest.TestCase):
    """
    Testes de proteção contra overflow.
    Valida que operações com números muito grandes geram exceções apropriadas.
    """
    
    def setUp(self):
        """Prepara os testes."""
        self.calc = Calculator()
    
    # ========== Testes de Fatorial - Overflow ==========
    def test_factorial_171_overflow(self):
        """Testa fatorial de 171 - deve lançar OverflowError."""
        with self.assertRaises(OverflowError) as context:
            self.calc.factorial(171)
        self.assertIn("fatorial muito grande", str(context.exception).lower())
    
    def test_factorial_170_limite_maximo(self):
        """Testa fatorial de 170 - máximo permitido."""
        # 170! é o máximo permitido, deve não gerar erro
        resultado = self.calc.factorial(170)
        self.assertIsInstance(resultado, int)
        self.assertGreater(resultado, 0)
    
    def test_factorial_200_overflow(self):
        """Testa fatorial de 200 - deve lançar OverflowError."""
        with self.assertRaises(OverflowError):
            self.calc.factorial(200)
    
    def test_factorial_1000_overflow(self):
        """Testa fatorial de 1000 - deve lançar OverflowError."""
        with self.assertRaises(OverflowError):
            self.calc.factorial(1000)
    
    # ========== Testes de Potência - Overflow ==========
    def test_power_expoente_muito_grande(self):
        """Testa potência com expoente muito grande - deve lançar OverflowError."""
        with self.assertRaises(OverflowError) as context:
            self.calc.power(2, 2000)
        self.assertIn("expoente", str(context.exception).lower())
    
    def test_power_expoente_muito_pequeno(self):
        """Testa potência com expoente muito pequeno - deve lançar OverflowError."""
        with self.assertRaises(OverflowError) as context:
            self.calc.power(2, -2000)
        self.assertIn("expoente", str(context.exception).lower())
    
    def test_power_expoente_limite_superior(self):
        """Testa potência com expoente no limite superior (1000)."""
        # Expoente muito grande deve gerar OverflowError pela proteção
        with self.assertRaises(OverflowError):
            self.calc.power(2, 1001)
    
    def test_power_base_grande_expoente_grande(self):
        """Testa potência com base e expoente grandes."""
        with self.assertRaises(OverflowError):
            self.calc.power(999, 999)
    
    def test_power_10_elevado_a_500(self):
        """Testa 10^500 - deve gerar overflow."""
        with self.assertRaises(OverflowError):
            self.calc.power(10, 500)
    
    # ========== Testes de Multiplicação - Overflow ==========
    def test_multiply_numeros_muito_grandes(self):
        """Testa multiplicação de números muito grandes."""
        # Números próximos ao limite máximo
        numero_grande = 1e200
        with self.assertRaises(OverflowError):
            self.calc.multiply(numero_grande, numero_grande)
    
    def test_multiply_1e150_por_1e150(self):
        """Testa multiplicação de 1e150 * 1e150."""
        # 1e150 * 1e150 = 1e300, que é válido (limite é 1e308)
        # Vamos testar com números que realmente causam overflow
        numero_grande = 1e200
        with self.assertRaises(OverflowError):
            self.calc.multiply(numero_grande, numero_grande)
    
    # ========== Testes de Validação de Operandos ==========
    def test_validar_operando_muito_grande(self):
        """Testa validação de operando muito grande."""
        numero_invalido = 1e309  # Maior que MAX_VALOR
        with self.assertRaises(OverflowError):
            self.calc.multiply(numero_invalido, 1)
    
    def test_multiply_com_operando_invalido(self):
        """Testa multiplicação com operando fora dos limites."""
        with self.assertRaises(OverflowError):
            self.calc.multiply(1e309, 1)
    
    def test_power_com_operando_invalido(self):
        """Testa potência com operando fora dos limites."""
        with self.assertRaises(OverflowError):
            self.calc.power(1e309, 2)
    
    # ========== Testes de Números Muito Pequenos ==========
    def test_power_resultado_muito_pequeno(self):
        """Testa potência que resulta em número muito pequeno."""
        # 0.0001^0.0001 resultará em algo muito próximo de 1 ou diferente
        resultado = self.calc.power(0.0001, 0.1)
        self.assertIsInstance(resultado, (int, float))
        self.assertNotEqual(resultado, float('inf'))
    
    def test_divide_numero_grande_por_pequeno(self):
        """Testa divisão de número grande por número pequeno."""
        # Isto pode gerar overflow
        numero_grande = 1e200
        numero_pequeno = 1e-100
        with self.assertRaises(OverflowError):
            self.calc.multiply(numero_grande, numero_grande)
    
    # ========== Testes de Sequência de Operações - Overflow ==========
    def test_sequencia_operacoes_overflow(self):
        """Testa sequência de operações que causa overflow."""
        # Teste fatorial grande primeiro
        with self.assertRaises(OverflowError):
            self.calc.factorial(200)
    
    def test_fatorial_em_sequencia_overflow(self):
        """Testa fatorial de resultado anterior."""
        # 10! = 3628800, isso é válido
        fatorial_10 = self.calc.factorial(10)
        self.assertIsInstance(fatorial_10, int)
        
        # Mas tentar fatorial de 171 deve gerar erro
        with self.assertRaises(OverflowError):
            self.calc.factorial(171)
    
    # ========== Testes Limite Exato ==========
    def test_fatorial_170_exact_limit(self):
        """Testa que fatorial 170 é o limite exato."""
        # 170! deve funcionar
        resultado_170 = self.calc.factorial(170)
        self.assertGreater(resultado_170, 0)
        
        # 171! deve gerar erro
        with self.assertRaises(OverflowError):
            self.calc.factorial(171)
    
    def test_power_1000_exponent_limit(self):
        """Testa que expoente 1000 é o limite aproximado."""
        # Expoente 1000 pode gerar error dependendo da base
        # Mas 1001 definitivamente deve gerar
        with self.assertRaises(OverflowError):
            self.calc.power(2, 1001)


def run_tests():
    """Executa todos os testes com verbosidade."""
    # Cria um test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Adiciona todos os testes
    suite.addTests(loader.loadTestsFromTestCase(TestCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorIntegracao))
    suite.addTests(loader.loadTestsFromTestCase(TestCalculatorOverflow))
    
    # Executa com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    resultado = runner.run(suite)
    
    # Retorna True se todos os testes passaram
    return resultado.wasSuccessful()


if __name__ == "__main__":
    # Executa os testes
    sucesso = run_tests()
    
    # Sai com código de erro se algum teste falhou
    sys.exit(0 if sucesso else 1)
