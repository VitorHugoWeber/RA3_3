T_INT = "int"
T_REAL = "real"
T_BOOL = "bool"
T_UNKNOWN = "unknown"

ARIT_FLOAT = {"+", "-", "*", "|"}
ARIT_INT_ONLY = {"/", "%"}
REL = {">", "<", ">=", "<=", "==", "!="}

def promover(a, b):
    if a == b:
        return a
    if a in {T_INT, T_REAL} and b in {T_INT, T_REAL}:
        return T_REAL
    return T_UNKNOWN

def tipo_binario(op, t1, t2):
    if op in ARIT_FLOAT:
        if t1 in {T_INT, T_REAL} and t2 in {T_INT, T_REAL}:
            return promover(t1, t2)
        return T_UNKNOWN
    if op in ARIT_INT_ONLY:
        if t1 == T_INT and t2 == T_INT:
            return T_INT
        return T_UNKNOWN
    if op == "^":
        if t1 in {T_INT, T_REAL} and t2 == T_INT:
            return t1
        return T_UNKNOWN
    if op in REL:
        if t1 in {T_INT, T_REAL} and t2 in {T_INT, T_REAL}:
            return T_BOOL
        return T_UNKNOWN
    return T_UNKNOWN

def get_gramatica_markdown():
    texto = []
    texto.append("# Gramática de Atributos")
    texto.append("")
    texto.append("Símbolos terminais e operações seguem a Fase 2.")
    texto.append("")
    texto.append("Regras de tipos principais:")
    texto.append("- +, -, *, | : promovem para real se houver real; senão int")
    texto.append("- /, % : apenas entre int, retornam int")
    texto.append("- ^ : base numérica, expoente int, retorna tipo da base")
    texto.append("- >, <, >=, <=, ==, != : aceitam int ou real e retornam bool")
    texto.append("- (N RES) : N int, retorna tipo da linha recuperada; se a linha não existir gera erro")
    texto.append("- (V MEM) : armazena tipo de V em MEM; booleano não pode ser armazenado")
    texto.append("- (MEM) : retorna tipo associado a MEM")
    texto.append("- if e while : expressão condicional deve ser bool")
    return "\n".join(texto)