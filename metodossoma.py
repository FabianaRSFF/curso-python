def soma(x: float, y: float) -> float:
    return x+y
 

def main() -> None:
    print(soma(34, 20))
    print(soma(49, 34))


# Caso eu importasse este modulo, o '__name__ seria o nome do modulo, não'__main__
# No caso aula129
# se eu não quiser que o módulo principal(testes) não seja executado
# é só colocar:

if __name__ == '__main__':
    print(20, 30)

if __name__ == '__main__':
    main()
    
