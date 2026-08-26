"""
Interface Gráfica da Calculadora
Este módulo contém a interface gráfica em Tkinter para a calculadora.
Utiliza uma paleta de cores rosa pastel para um visual fofinho.
"""

import tkinter as tk
from tkinter import font
from calculator import Calculator


class CalculatorApp:
    """
    Interface gráfica da calculadora usando Tkinter.
    
    Fornece uma interface visual para interagir com a classe Calculator,
    com um tema rosa pastel, botões arredondados e sombra.
    """
    
    # Paleta de cores em rosa pastel
    COLORS = {
        'background': '#FFF5F7',           # Rosa claro muito suave
        'display': '#FFFBFC',         # Branco rosa muito suave para o display
        'button_number': '#FFD4E5',    # Rosa pastel médio
        'button_operation': '#FFB3D9',  # Rosa pastel um pouco mais escuro
        'button_equal': '#FF99CC',     # Rosa pastel para resultado
        'button_clear': '#FFC0E0',    # Rosa pastel claro
        'text': '#8B4A6E',           # Roxo escuro para o texto
        'shadow': '#E8A8C8',          # Sombra em tom rosa mais escuro
    }
    
    # Constantes de limite para proteção contra overflow
    MAX_EXPRESSION_LENGTH = 40    # Máximo de caracteres na expressão
    MAX_DISPLAY_DIGITS = 15          # Máximo de dígitos a exibir
    
    def __init__(self, root):
        """
        Inicializa a interface da calculadora.
        
        Args:
            root: Janela principal do Tkinter
        """
        self.root = root
        self.root.title("Kalqui")
        self.root.geometry("520x680")
        self.root.resizable(False, False)
        self.root.configure(bg=self.COLORS['background'])
        
        # Instancia a calculadora
        self.calculator = Calculator()
        
        # Variáveis de estado
        self.current_expression = ""
        self.result = ""
        
        # Cria a interface
        self._create_widgets()
        
    def _create_widgets(self):
        """Cria todos os widgets da interface."""
        # Frame principal com padding
        main_frame = tk.Frame(
            self.root,
            bg=self.COLORS['background'],
            padx=20,
            pady=25
        )
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = tk.Label(
            main_frame,
            text="Kalqui",
            font=("Arial", 28, "bold"),
            fg=self.COLORS['text'],
            bg=self.COLORS['background']
        )
        titulo.pack(pady=(0, 25))
        
        # Display
        self._create_display(main_frame)
        
        # Botões
        self._create_buttons(main_frame)
        
    def _create_display(self, parent):
        """
        Cria o display que mostra os números e resultados.
        
        Args:
            parent: Widget pai
        """
        # Frame para a sombra do display
        shadow_frame = tk.Frame(
            parent,
            bg=self.COLORS['shadow'],
            height=100,
            relief=tk.SUNKEN,
            bd=2
        )
        shadow_frame.pack(fill=tk.X, pady=(0, 20), padx=2)
        
        # Frame principal do display
        display_frame = tk.Frame(
            shadow_frame,
            bg=self.COLORS['display'],
            height=100,
            relief=tk.RIDGE,
            bd=3
        )
        display_frame.pack(fill=tk.BOTH, expand=True, padx=3, pady=3)
        
        self.display = tk.Entry(
            display_frame,
            font=("Arial", 32, "bold"),
            fg=self.COLORS['text'],
            bg=self.COLORS['display'],
            border=0,
            justify='right',
            state='readonly'
        )
        self.display.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
    def _create_buttons(self, parent):
        """
        Cria o layout dos botões.
        
        Args:
            parent: Widget pai
        """
        # Frame dos botões
        buttons_frame = tk.Frame(parent, bg=self.COLORS['background'])
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # Layout dos botões: 4 colunas, 6 linhas
        button_layout = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', '=', '+'],
            ['C', '√', '²', '!'],
            ['←', 'DEL', '', '']
        ]
        
        for row, button_row in enumerate(button_layout):
            for column, label in enumerate(button_row):
                if label:  # Pula espaços vazios
                    self._create_button(buttons_frame, label, row, column)
    
    def _create_button(self, parent, label, row, column):
        """
        Cria um botão individual com efeito de sombra e arredondamento.
        
        Args:
            parent: Widget pai
            label: Texto do botão
            row: Linha no grid
            column: Coluna no grid
        """
        # Determina a cor e a função do botão
        if label in ['=']:
            cor = self.COLORS['button_equal']
            comando = self._calculate
        elif label in ['C']:
            cor = self.COLORS['button_clear']
            comando = self._clear
        elif label in ['/', '*', '-', '+']:
            cor = self.COLORS['button_operation']
            comando = lambda: self._add_operation(label)
        elif label in ['√', '²', '!', '←', 'DEL']:
            cor = self.COLORS['button_operation']
            comando = lambda value=label: self._special_function(value)
        else:
            cor = self.COLORS['button_number']
            comando = lambda value=label: self._add_number(value)
        
        # Frame para simular sombra
        shadow_frame = tk.Frame(
            parent,
            bg=self.COLORS['shadow'],
            relief=tk.RAISED,
            bd=2
        )
        shadow_frame.grid(row=row, column=column, padx=6, pady=6, sticky='nsew')
        
        # Botão principal com arredondamento visual
        botao = tk.Button(
            shadow_frame,
            text=label,
            font=("Arial", 20, "bold"),
            fg=self.COLORS['text'],
            bg=cor,
            border=0,
            relief=tk.RAISED,
            activebackground='#FF88BB',
            activeforeground=self.COLORS['text'],
            padx=12,
            pady=18,
            command=comando,
            overrelief=tk.SUNKEN,
            highlightthickness=0,
            cursor='hand2'
        )
        
        # Configura o tamanho: botões vazios não aparecem
        if label == '':
            shadow_frame.config(bg=self.COLORS['background'], relief=tk.FLAT, bd=0)
            botao.config(state='disabled', bg=self.COLORS['background'])
        
        botao.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
        
        # Configurar peso das linhas e colunas para responsividade
        parent.grid_rowconfigure(row, weight=1)
        parent.grid_columnconfigure(column, weight=1)
    
    def _update_display(self, value):
        """
        Atualiza o display com um novo valor.
        Trata overflow de caracteres e formata números grandes.
        
        Args:
            value: Valor a ser exibido
        """
        value_str = str(value)
        formatted_value = self._format_value_display(value_str)
        
        self.display.config(state='normal')
        self.display.delete(0, tk.END)
        self.display.insert(0, formatted_value)
        self.display.config(state='readonly')
    
    def _format_value_display(self, value_str):
        """
        Formata um valor para exibição no display.
        Trata overflow de caracteres e números muito grandes.
        
        Args:
            value_str: String do valor a formatar
            
        Returns:
            String formatada para exibição
        """
        # Se o valor é muito longo, tenta usar notação científica
        if len(value_str) > self.MAX_DISPLAY_DIGITS:
            try:
                number = float(value_str)
                # Usa notação científica para números muito grandes
                if abs(number) >= 1e10 or (abs(number) < 1e-5 and number != 0):
                    return f"{number:.6e}"
                # Se ainda for muito longo, trunca
                if len(str(number)) > self.MAX_DISPLAY_DIGITS:
                    return value_str[:self.MAX_DISPLAY_DIGITS] + "..."
            except (ValueError, OverflowError):
                return value_str[:self.MAX_DISPLAY_DIGITS] + "..."
        
        return value_str
    
    def _add_number(self, number):
        """
        Adiciona um número à expressão atual.
        Valida limite de comprimento.
        
        Args:
            number: Número ou ponto a ser adicionado
        """
        # Evita múltiplos pontos
        if number == '.' and '.' in self.current_expression:
            return
        
        # Verifica limite de comprimento
        if len(self.current_expression) >= self.MAX_EXPRESSION_LENGTH:
            self._update_display("Muito longo!")
            return
        
        self.current_expression += number
        self._update_display(self.current_expression)
    
    def _add_operation(self, operation):
        """
        Adiciona uma operação à expressão atual.
        
        Args:
            operation: Operação (+, -, *, /)
        """
        if self.current_expression and self.current_expression[-1] not in '+-*/.':
            self.current_expression += operation
            self._update_display(self.current_expression)
    
    def _clear(self):
        """Limpa a expressão atual e reseta o display."""
        self.current_expression = ""
        self.result = ""
        self._update_display("0")
    
    def _special_function(self, function):
        """
        Executa funções especiais da calculadora.
        Trata overflow e valores inválidos.
        
        Args:
            function: Tipo de função especial (√, ², !, ←, DEL)
        """
        try:
            if function == '√':  # Raiz quadrada
                if self.current_expression:
                    number = float(self.current_expression)
                    result = self.calculator.square_root(number)
                    self.current_expression = str(result)
                    self._update_display(self.current_expression)
            
            elif function == '²':  # Quadrado
                if self.current_expression:
                    number = float(self.current_expression)
                    result = self.calculator.power(number, 2)
                    self.current_expression = str(result)
                    self._update_display(self.current_expression)
            
            elif function == '!':  # Fatorial
                if self.current_expression:
                    number = int(float(self.current_expression))
                    result = self.calculator.factorial(number)
                    self.current_expression = str(result)
                    self._update_display(self.current_expression)
            
            elif function == '←':  # Desfazer último número
                self.current_expression = self.current_expression[:-1]
                self._update_display(self.current_expression if self.current_expression else "0")
            
            elif function == 'DEL':  # Deletar tudo
                self._clear()
        
        except ValueError as e:
            self._update_display("Erro!")
            self.current_expression = ""
        except OverflowError as e:
            self._update_display("Overflow!")
            self.current_expression = ""
        except (IndexError, TypeError):
            self._update_display("Erro!")
            self.current_expression = ""
    
    def _calculate(self):
        """
        Calcula o resultado da expressão atual.
        Trata overflow numérico e de caracteres.
        """
        try:
            if self.current_expression:
                # Avalia a expressão matemática
                result = eval(self.current_expression)
                
                # Arredonda para evitar muitas casas decimais
                if isinstance(result, float):
                    result = round(result, 10)
                
                result_string = str(result)
                
                # Formata o resultado se for muito longo
                formatted_result = self._format_value_display(result_string)
                
                self.current_expression = formatted_result
                self.result = result
                self._update_display(self.current_expression)
        
        except ZeroDivisionError:
            self._update_display("Divisão por 0!")
            self.current_expression = ""
        except OverflowError:
            self._update_display("Overflow!")
            self.current_expression = ""
        except (SyntaxError, ValueError):
            self._update_display("Erro!")
            self.current_expression = ""
        except Exception as e:
            self._update_display("Erro!")
            self.current_expression = ""


def main():
    """Função principal para executar a aplicação."""
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
