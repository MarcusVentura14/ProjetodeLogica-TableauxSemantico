from tableaux import *

if __name__ == '__main__':
    # Definindo os átomos
    p = Atomica("p")
    q = Atomica("q")
    r = Atomica("r")

    # Exemplo 1: p → q, q → r ⊢ p → r  (Deve ser VÁLIDO)
    premissas1 = [Implica(p, q), Implica(q, r)]
    conclusao1 = [Implica(p, r)]
    resultado, modelo = tableaux(premissas1, conclusao1)
    print(f"Teste 1 (p → q, q → r ⊢ p → r): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("-" * 20)

    # Exemplo 2: p ∨ q ⊢ p ∧ q (Deve ser INVÁLIDO)
    premissas2 = [Ou(p, q)]
    conclusao2 = [E(p, q)]
    resultado, modelo = tableaux(premissas2, conclusao2)
    print(f"Teste 2 (p ∨ q ⊢ p ∧ q): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("-" * 20)

    # Exemplo 3: ⊢ (p ∧ q) → p (Deve ser VÁLIDO - Tautologia)
    premissas3 = []
    conclusao3 = [Implica(E(p, q), p)]
    resultado, modelo = tableaux(premissas3, conclusao3)
    print(f"Teste 3 (⊢ (p ∧ q) → p): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")