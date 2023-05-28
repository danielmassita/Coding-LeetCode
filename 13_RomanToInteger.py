"""
13. Roman to Integer
Easy
10.5K
605
Companies
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""



"""
Vamos resolver o problema de conversão de números romanos para inteiros.

Para converter um número romano para inteiro, podemos seguir o seguinte algoritmo:

Inicialize uma variável resultado com o valor zero para armazenar o valor inteiro final.
Crie um dicionário para mapear os símbolos romanos aos seus respectivos valores: 'I' = 1, 'V' = 5, 'X' = 10, 'L' = 50, 'C' = 100, 'D' = 500, 'M' = 1000.
Itere através da string do número romano:
Se o símbolo atual tiver um valor maior que o valor do símbolo anterior, subtraia duas vezes o valor do símbolo anterior do resultado (já que o símbolo anterior foi adicionado na iteração anterior).
Caso contrário, adicione o valor do símbolo atual ao resultado.
Retorne o valor final do resultado.
Aqui está o código em Python que implementa esse algoritmo:
"""
def romanToInt(s):
    valores_romanos = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    resultado = 0
    valor_anterior = 0

    for simbolo in s:
        valor = valores_romanos[simbolo]
        if valor > valor_anterior:
            resultado -= 2 * valor_anterior
        resultado += valor
        valor_anterior = valor

    return resultado
"""
Agora você pode usar essa função para converter números romanos em inteiros. Por exemplo:

python
Copy code
print(romanToInt("III"))      # Saída: 3
print(romanToInt("LVIII"))    # Saída: 58
print(romanToInt("MCMXCIV"))  # Saída: 1994
A função retornará os valores inteiros esperados para os números romanos fornecidos.

"""
# Exemplo 1:
s = "III"
# Passo a passo da depuração:
# symbol = 'I', value = 1, prev_value = 0, result = 0
# value > prev_value: 1 > 0
# result -= 2 * prev_value = 0 - 2 * 0 = 0
# result += value = 0 + 1 = 1
# prev_value = value = 1
# ------------------------------
# symbol = 'I', value = 1, prev_value = 1, result = 1
# value <= prev_value: 1 <= 1
# result += value = 1 + 1 = 2
# prev_value = value = 1
# ------------------------------
# symbol = 'I', value = 1, prev_value = 1, result = 2
# value <= prev_value: 1 <= 1
# result += value = 2 + 1 = 3
# prev_value = value = 1
# ------------------------------
# Fim da iteração
# Resultado final: 3
print(romanToInt(s))  # Saída: 3


# Exemplo 2:
s = "LVIII"
# Passo a passo da depuração:
# symbol = 'L', value = 50, prev_value = 0, result = 0
# value > prev_value: 50 > 0
# result -= 2 * prev_value = 0 - 2 * 0 = 0
# result += value = 0 + 50 = 50
# prev_value = value = 50
# ------------------------------
# symbol = 'V', value = 5, prev_value = 50, result = 50
# value <= prev_value: 5 <= 50
# result += value = 50 + 5 = 55
# prev_value = value = 5
# ------------------------------
# symbol = 'I', value = 1, prev_value = 5, result = 55
# value <= prev_value: 1 <= 5
# result += value = 55 + 1 = 56
# prev_value = value = 1
# ------------------------------
# symbol = 'I', value = 1, prev_value = 1, result = 56
# value <= prev_value: 1 <= 1
# result += value = 56 + 1 = 57
# prev_value = value = 1
# ------------------------------
# symbol = 'I', value = 1, prev_value = 1, result = 57
# value <= prev_value: 1 <= 1
# result += value = 57 + 1 = 58
# prev_value = value = 1
# ------------------------------
# Fim da iteração
# Resultado final: 58
print(romanToInt(s))  # Saída: 58


# Exemplo 3:
s = "MCMXCIV"
# Passo a passo da depuração:
# symbol = 'M', value = 1000, prev_value = 0, result = 0
# value > prev_value: 1000 > 0
# result -= 2 * prev_value = 0 - 2 * 0 = 0
# result += value = 0 + 1000 = 1000
# prev_value = value = 1000
# ------------------------------
# symbol = 'C', value = 100, prev_value = 1000, result = 1000
# value <= prev_value: 100 <= 1000
# result += value = 1000 + 100 = 1100
# prev_value = value = 100
# ------------------------------
# symbol = 'M', value = 1000, prev_value = 100, result = 1100
# value > prev_value: 1000 > 100
# result -= 2 * prev_value = 1100 - 2 * 100 = 900
# result += value = 900 + 1000 = 1900
# prev_value = value = 1000
# ------------------------------
# symbol = 'X', value = 10, prev_value = 1000, result = 1900
# value <= prev_value: 10 <= 1000
# result += value = 1900 + 10 = 1910
# prev_value = value = 10
# ------------------------------
# symbol = 'C', value = 100, prev_value = 10, result = 1910
# value > prev_value: 100 > 10
# result -= 2 * prev_value = 1910 - 2 * 10 = 1890
# result += value = 1890 + 100 = 1990
# prev_value = value = 100
# ------------------------------
# symbol = 'I', value = 1, prev_value = 100, result = 1990
# value <= prev_value: 1 <= 100
# result += value = 1990 + 1 = 1991
# prev_value = value = 1
# ------------------------------
# symbol = 'V', value = 5, prev_value = 1, result = 1991
# value <= prev_value: 5 <= 1
# result += value = 1991 + 5 = 1996
# prev_value = value = 5
# ------------------------------
# symbol = 'I', value = 1, prev_value = 5, result = 1996
# value <= prev_value: 1 <= 5
# result += value = 1996 + 1 = 1997
# prev_value = value = 1
# ------------------------------
# symbol = 'V', value = 5, prev_value = 1, result = 1997
# value <= prev_value: 5 <= 1
# result += value = 1997 + 5 = 2002
# prev_value = value = 5
# ------------------------------
# Fim da iteração
# Resultado final: 1994
print(romanToInt(s))  # Saída: 1994
