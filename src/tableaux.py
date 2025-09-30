from dataclasses import dataclass
from typing import List, Union, Tuple

# Criação de classes para representação da estrutura das fórmulas 
@dataclass(frozen=True, eq=True)
class Atomica:
    nome: str
    def __repr__(self):
        return self.nome

@dataclass(frozen=True, eq=True)
class Nao:
    operando: 'Formula'
    def __repr__(self):
        return f"¬{self.operando}"

@dataclass(frozen=True, eq=True)
class E:
    esquerda: 'Formula'
    direita: 'Formula'
    def __repr__(self):
        return f"({self.esquerda} ∧ {self.direita})"

@dataclass(frozen=True, eq=True)
class Ou:
    esquerda: 'Formula'
    direita: 'Formula'
    def __repr__(self):
        return f"({self.esquerda} ∨ {self.direita})"

@dataclass(frozen=True, eq=True)
class Implica:
    esquerda: 'Formula'
    direita: 'Formula'
    def __repr__(self):
        return f"({self.esquerda} → {self.direita})"


# Tipo para representar qualquer uma das classes de fórmula acima
Formula = Union[Atomica, Nao, E, Ou, Implica]


# Criação de classe que representa as fórmulas assinadas
@dataclass
class FormulaAssinalada:
    valoracao: bool  # True para T, False para F
    formula: Formula
    expandida: bool = False
    def __repr__(self):
        prefixo = "T" if self.varolacao else "F"
        return f"{prefixo}({self.formula})"


# --- Funções Auxiliares para Classificar e Expandir Fórmulas ---

def formula_alfa(sf: FormulaAssinalada) -> bool:
    # Fórmulas que não causam ramificação
    return (sf.valoracao and isinstance(sf.formula, E)) or \
           (not sf.valoracao and isinstance(sf.formula, Ou)) or \
           (not sf.valoracao and isinstance(sf.formula, Implica)) or \
           (isinstance(sf.formula, Nao)) # T(¬A) ou F(¬A)

def formula_beta(sf: FormulaAssinalada) -> bool:
    # Fórmulas que causam ramificação
    return (sf.valoracao and isinstance(sf.formula, Ou)) or \
           (not sf.valoracao and isinstance(sf.formula, E)) or \
           (sf.valoracao and isinstance(sf.formula, Implica))

def expansao_da_formula(sf: FormulaAssinalada) -> Tuple[FormulaAssinalada, Union[FormulaAssinalada, None]]:
    f = sf.formula
    s = sf.valoracao

    # Regras α (não ramificam)
    if s and isinstance(f, E): return FormulaAssinalada(True, f.esquerda), FormulaAssinalada(True, f.direita)
    if not s and isinstance(f, Ou): return FormulaAssinalada(False, f.esquerda), FormulaAssinalada(False, f.direita)
    if not s and isinstance(f, Implica): return FormulaAssinalada(True, f.esquerda), FormulaAssinalada(False, f.direita)
    if isinstance(f, Nao): return FormulaAssinalada(not s, f.operando), None
    
    # Regras β (ramificam)
    if s and isinstance(f, Ou): return FormulaAssinalada(True, f.esquerda), FormulaAssinalada(True, f.direita)
    if not s and isinstance(f, E): return FormulaAssinalada(False, f.esquerda), FormulaAssinalada(False, f.direita)
    if s and isinstance(f, Implica): return FormulaAssinalada(False, f.esquerda), FormulaAssinalada(True, f.direita)
    
    raise TypeError(f"Fórmula não é do tipo alfa ou beta: {sf}")


#--- Algoritmo Principal de Tableaux ---
def tableaux(premissas: List[Formula], conclusoes: List[Formula]):
    
    # Inicialização:
        # p/ cada formula na lista de premissas assinalamos com T
        # p/ cada formula na lista de conclusões assinalamos com F
    ramo_inicial = [FormulaAssinalada(True, p) for p in premissas] + [FormulaAssinalada(False, c) for c in conclusoes] 
    pilha_de_ramos = []  # Criação da pilha que guardará o caminho até uma bifurcação
    ramo_atual = ramo_inicial

    while True:
        # Verifica se o ramo atual contém uma contradição
        true_atoms = {sf.formula for sf in ramo_atual if isinstance(sf.formula, Atomica) and sf.valoracao}
        false_atoms = {sf.formula for sf in ramo_atual if isinstance(sf.formula, Atomica) and not sf.valoracao}

        # Se houver um elemento atômico presente em ambos os conjuntos,temos uma contradição
        tem_contradicao = not true_atoms.isdisjoint(false_atoms)

        if tem_contradicao:
            if not pilha_de_ramos:
                # Todos os ramos foram explorados e fecharam
                return "VÁLIDO", None
            else:
                # Restaura o estado anterior para explorar o ramo alternativo
                ramo_atual = pilha_de_ramos.pop()
                continue # Volta para o início do loop com o novo ramo

        # Encontra a próxima fórmula não expandida para aplicar uma regra
        proxima_formula_para_expandir = None
        # Prioriza regras alfa para evitar ramificações desnecessárias
        for sf in ramo_atual:
            if not sf.expandida and formula_alfa(sf):
                proxima_formula_para_expandir = sf
                break
        
        if not proxima_formula_para_expandir:
            for sf in ramo_atual:
                 if not sf.expandida and formula_beta(sf):
                    proxima_formula_para_expandir = sf
                    break
        
        # Se encontrou uma fórmula para expandir
        if proxima_formula_para_expandir:
            proxima_formula_para_expandir.expandida = True
            
            # 4. Aplica regra alfa (sem ramificação)
            if formula_alfa(proxima_formula_para_expandir):
                res1, res2 = expansao_da_formula(proxima_formula_para_expandir)
                ramo_atual.append(res1)
                if res2:
                    ramo_atual.append(res2)
            
            # 5. Aplica regra beta (com ramificação)
            elif formula_beta(proxima_formula_para_expandir):
                beta1, beta2 = expansao_da_formula(proxima_formula_para_expandir)
                
                # Cria uma cópia do ramo atual para o backtracking
                # A fórmula expandida não precisa ir na cópia
                copia_ramo_para_pilha = [sf for sf in ramo_atual if sf is not proxima_formula_para_expandir]
                copia_ramo_para_pilha.append(beta2) # Adiciona o segundo caminho
                pilha_de_ramos.append(copia_ramo_para_pilha)

                # Continua a exploração com o primeiro caminho
                ramo_atual.append(beta1)
        
        # 6. Se não há mais regras, o ramo está aberto e saturado
        else:
            # Extrai o contra-exemplo dos átomos no ramo
            contra_exemplo = {
                sf.formula.nome: sf.valoracao
                for sf in ramo_atual if isinstance(sf.formula, Atomica)
            }
            return "INVÁLIDO", contra_exemplo
