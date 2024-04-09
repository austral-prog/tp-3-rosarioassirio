def check_vowels():
    name = input("Ingresa tu nombre: ")
    a = "a" in name.lower()
    b = "e" in name.lower()
    c = "i" in name.lower()
    d = "o" in name.lower()
    e = "u" in name.lower()
    print (f"Contiene a: {a}")
    print (f"Contiene e: {b}")
    print (f"Contiene i: {c}")
    print (f"Contiene o: {d}")
    print (f"Contiene u: {e}")
check_vowels()
    # Código a implementar utilizando input.


# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
