# Gramática de Atributos

Símbolos terminais e operações seguem a Fase 2.

Regras de tipos principais:
- +, -, *, | : promovem para real se houver real; senão int
- /, % : apenas entre int, retornam int
- ^ : base numérica, expoente int, retorna tipo da base
- >, <, >=, <=, ==, != : aceitam int ou real e retornam bool
- (N RES) : N int, retorna tipo da linha recuperada; se a linha não existir gera erro
- (V MEM) : armazena tipo de V em MEM; booleano não pode ser armazenado
- (MEM) : retorna tipo associado a MEM
- if e while : expressão condicional deve ser bool