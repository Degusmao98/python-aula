
__version__ = '0.0.1'
__author__ = 'Douglas Gusmao'
__license__ = 'Unlicense'

import os
# dunder (__)

# este imprime 'hello world'
current_language = 'it_IT'
msg = 'hello word'

if current_language == 'pt_BR':  # condição SE
    msg = 'olá mundo'
elif current_language == 'it_IT':  # condição SE NÃO SER
    msg = 'ciano, Mondo!'
print(msg)
