def soma(a, b):
    """
    Calcula e retorna a soma de dois números.
    
    Args:
        a: Primeiro número
        b: Segundo número
    
    Returns:
        A soma de a e b
    """
    return a + b


# Exemplo de uso
if __name__ == "__main__":
    resultado = soma(5, 3)
    print(f"5 + 3 = {resultado}")
    
    resultado2 = soma(10.5, 7.2)
    print(f"10.5 + 7.2 = {resultado2}")
