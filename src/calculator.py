"""
Este módulo contém a classe Calculator com operações matemáticas básicas e avançadas.
Implementa proteções contra overflow e erros numéricos.
"""


class Calculator:
    """
    Classe que implementa uma calculadora com operações matemáticas.
    
    Fornece métodos para realização de operações aritméticas como adição, subtração,
    multiplicação, divisão, potenciação, módulo, raiz quadrada e fatorial.
    
    Inclui proteção contra overflow e validação de limites numéricos.
    """
    
    # Constantes de limite para proteção contra overflow
    MAX_VALUE = 1e308          # Limite máximo de valor (próximo ao limite do float64)
    MIN_VALUE = 1e-308        # Limite mínimo de valor positivo
    MAX_FACTORIAL = 170        # Máximo para fatorial (171! causa overflow)
    
    def _validate_overflow(self, resultado, operacao=""):
        """
        Valida se um resultado está dentro dos limites aceitáveis.
        
        Args:
            resultado: Número a validar
            operacao: Nome da operação (para mensagem de erro)
            
        Returns:
            resultado se válido
            
        Raises:
            OverflowError: Se o resultado ultrapassar os limites
        """
        try:
            if isinstance(resultado, (int, float)):
                # Verifica se é infinito ou NaN
                if resultado != resultado:  # NaN check
                    raise OverflowError(f"Operação {operacao} resultou em NaN")
                if resultado == float('inf') or resultado == float('-inf'):
                    raise OverflowError(f"Operação {operacao} resultou em overflow")
                
                # Verifica limites de magnitude
                if resultado != 0:
                    abs_resultado = abs(resultado)
                    if abs_resultado > self.MAX_VALUE:
                        raise OverflowError(f"Resultado muito grande: {abs_resultado:.2e}")
                    if abs_resultado < self.MIN_VALUE and resultado != 0:
                        # Arredonda para 0 se for muito pequeno
                        return 0
            
            return resultado
        except OverflowError:
            raise
        except Exception as e:
            raise OverflowError(f"Erro na validação: {str(e)}")
    
    def _validate_operands(self, a, b=None):
        """
        Valida se os operandos estão dentro dos limites aceitáveis.
        
        Args:
            a: Primeiro operando
            b: Segundo operando (opcional)
            
        Raises:
            OverflowError: Se algum operando estiver fora dos limites
        """
        for operando in [a, b]:
            if operando is not None:
                try:
                    valor = float(operando)
                    if valor != 0 and abs(valor) > self.MAX_VALUE:
                        raise OverflowError(f"Operando muito grande: {valor:.2e}")
                except (ValueError, TypeError):
                    raise ValueError(f"Operando inválido: {operando}")
    
    def add(self, a, b):
        """
        Realiza a adição de dois números.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            A soma de a e b
        """
        return a + b

    def subtract(self, a, b):
        """
        Realiza a subtração de dois números.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            A diferença de a menos b
        """
        return a - b

    def multiply(self, a, b):
        """
        Realiza a multiplicação de dois números.
        
        Args:
            a: Primeiro número
            b: Segundo número
            
        Returns:
            O produto de a e b
            
        Raises:
            OverflowError: Se o resultado ultrapassar os limites
        """
        self._validate_operands(a, b)
        resultado = a * b
        return self._validate_overflow(resultado, "multiplicação")

    def divide(self, a, b):
        """
        Realiza a divisão de dois números.
        
        Args:
            a: Dividendo
            b: Divisor
            
        Returns:
            O quociente de a dividido por b
            
        Raises:
            ValueError: Se b for igual a zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b

    def power(self, a, b):
        """
        Calcula a potência de um número.
        
        Args:
            a: Base
            b: Expoente
            
        Returns:
            a elevado à potência b
            
        Raises:
            OverflowError: Se o resultado ultrapassar os limites
        """
        self._validate_operands(a, b)
        
        # Proteção adicional para potências muito grandes
        if b > 1000:
            raise OverflowError(f"Expoente muito grande: {b}")
        if b < -1000:
            raise OverflowError(f"Expoente muito pequeno: {b}")
        
        resultado = a ** b
        return self._validate_overflow(resultado, "potência")

    def modulus(self, a, b):
        """
        Calcula o módulo (resto da divisão) de dois números.
        
        Args:
            a: Dividendo
            b: Divisor
            
        Returns:
            O resto da divisão de a por b
            
        Raises:
            ValueError: Se b for igual a zero
        """
        if b == 0:
            raise ValueError("Cannot perform modulus by zero.")
        return a % b

    def square_root(self, a):
        """
        Calcula a raiz quadrada de um número.
        
        Args:
            a: Número para o qual calcular a raiz quadrada
            
        Returns:
            A raiz quadrada de a
            
        Raises:
            ValueError: Se a for negativo
        """
        if a < 0:
            raise ValueError("Cannot compute square root of a negative number.")
        return a ** 0.5

    def factorial(self, n):
        """
        Calcula o fatorial de um número inteiro não-negativo.
        
        Args:
            n: Número inteiro não-negativo
            
        Returns:
            O fatorial de n (n!)
            
        Raises:
            ValueError: Se n for negativo
            OverflowError: Se n for muito grande (> 170)
        """
        if n < 0:
            raise ValueError("Cannot compute factorial of a negative number.")
        
        # Proteção contra overflow - 171! causa overflow em float64
        if n > self.MAX_FACTORIAL:
            raise OverflowError(f"Fatorial muito grande. Máximo permitido: {self.MAX_FACTORIAL}!")
        
        # Caso base: 0! = 1 e 1! = 1
        if n == 0 or n == 1:
            return 1
        
        # Cálculo iterativo do fatorial
        result = 1
        for i in range(2, n + 1):
            result *= i
            # Verifica overflow durante o cálculo
            if result > self.MAX_VALUE:
                raise OverflowError(f"Fatorial resultou em overflow em {i}!")
        
        return result

    