# gran.py

def gran(num1, num2):
    """Retorna el major dels dos números proporcionats."""
    if num1 > num2:
        return num1
    else:
        return num2

# Proves de la funció
if __name__ == "__main__":
    # Exemples de prova
    print(f"El major entre 5 i 10 és: {gran(5, 10)}")
    print(f"El major entre -1 i 1 és: {gran(-1, 1)}")
    print(f"El major entre 3.5 i 3.5 és: {gran(3.5, 3.5)}")
    print(f"El major entre 100 i 99 és: {gran(100, 99)}")
    print(f"El major entre 0 i -10 és: {gran(0, -10)}")