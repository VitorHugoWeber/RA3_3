# RA3 – Analisador Semântico
Disciplina: Linguagens Formais e Compiladores  
Professor: Frank Alcântara  
Aluno: Vitor Hugo Behlau Weber  
Fase 3 – Análise Semântica da linguagem em notação pós-fixa com comandos especiais

## 1. Objetivo
Esta fase tem como objetivo receber o programa de entrada (mesmo formato usado no RA1 e RA2), analisar a árvore sintática gerada na fase anterior e aplicar as regras semânticas da linguagem, produzindo:
- verificação de tipos;
- verificação de uso de memória (`MEM`);
- verificação de comandos especiais (`RES`);
- verificação de estruturas de controle (`if` e `while`);
- geração da **árvore sintática atribuída**;
- geração de arquivos de relatório em `docs/`.

Tudo o que for encontrado deve ser registrado em arquivos `.md` para ser usado na Fase 4.

## 2. Requisitos
- Python 3.10+ instalado
- Terminal com acesso à pasta do projeto

Opcional:
```bash
pip install -r requirements.txt