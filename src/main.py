from tableaux import *

if __name__ == '__main__':
    # Definindo os átomos
    p = Atomica("p")
    q = Atomica("q")
    r = Atomica("r")
    s = Atomica("s")

    print ("\n")
    print("=" * 50)
    print (f"    Exemplos de prova com Taubleaux Semântico   ")
    print("=" * 50)

    # Exemplo 1: p → q, q → r ⊢ p → r  (Deve ser VÁLIDO)
    premissas1 = [Implica(p, q), Implica(q, r)]
    conclusao1 = [Implica(p, r)]
    resultado, modelo = tableaux(premissas1, conclusao1)
    print(f"Exemplo 1 (p → q, q → r ⊢ p → r): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("=" * 50)

    # Exemplo 2: p ∨ q ⊢ p ∧ q (Deve ser INVÁLIDO)
    premissas2 = [Ou(p, q)]
    conclusao2 = [E(p, q)]
    resultado, modelo = tableaux(premissas2, conclusao2)
    print(f"Exemplo 2 (p ∨ q ⊢ p ∧ q): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("=" * 50)

    # Exemplo 3: ⊢ (p ∧ q) → p (Deve ser VÁLIDO - Tautologia)
    premissas3 = []
    conclusao3 = [Implica(E(p, q), p)]
    resultado, modelo = tableaux(premissas3, conclusao3)
    print(f"Exemplo 3 (⊢ (p ∧ q) → p): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("=" * 50)
    
    # Exemplo 4: p ∨ q, p → r, q → r ⊢ r (Deve ser VÁLIDO)
    premissas4 = [Ou(p, q), Implica(p, r), Implica(q, r)]
    conclusao4 = [r]
    resultado, modelo = tableaux(premissas4, conclusao4)
    print(f"Exemplo 4 (p ∨ q, p → r, q → r ⊢ r): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}") 

    print("=" * 50)       
    
    # Exemplo 5: ⊢ p ∨ ¬p (Deve ser VÁLIDO)
    premissas5 = []
    conclusao5 = [Ou(p, Nao(p))]
    resultado, modelo = tableaux(premissas5, conclusao5)
    print(f"Exemplo 5: (⊢ p ∨ ¬p): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")    
    
    print("=" * 50)  

    # Exemplo 6: p ∨ q, p → r, q → r ∨ s ⊢ r (Deve ser INVÁLIDO)
    premissas6 = [Ou(p, q), Implica(p, r), Implica(q, Ou(r, s))]
    conclusao6 = [r]
    resultado, modelo = tableaux(premissas6, conclusao6)
    print(f"Exemplo 6: (p ∨ q, p → r, q → r ∨ s ⊢ r): {resultado}")
    if modelo:
        print(f"  Contra-exemplo: {modelo}")

    print("=" * 50)
    print ("\n")