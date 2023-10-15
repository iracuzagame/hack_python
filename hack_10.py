"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    resultado = result.upper()
    lista = []
    for letter in resultado:
        lista.append(letter)
    lista[1:3] = ["0", "0"]
    lista[4] = "1"
    lista[6] = "@"
    return lista  