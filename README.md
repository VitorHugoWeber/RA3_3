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
```

## 3. Execução do projeto pelo terminal


Para executar o projeto é necessário utilizar o terminal (PowerShell ou CMD no Windows) e navegar até a pasta onde está o arquivo principal (`src/main.py`). Partindo da raiz do projeto (pasta onde está o `README.md`), acesse a pasta `src` com `cd src` e, já dentro dela, rode o analisador informando o arquivo de teste que está na pasta `tests`, que fica uma pasta acima; o comando completo fica assim: `python .\main.py ..\tests\teste1.txt`. Nesse comando, `python` chama o interpretador, `.\main.py` executa o arquivo principal e `..\tests\teste1.txt` é o caminho relativo até o arquivo de teste (o `..` volta da pasta `src` para a raiz e depois entra em `tests`). Após a execução, os arquivos de saída serão gerados ou atualizados na pasta `docs` da raiz do projeto, e você pode repetir o processo mudando apenas o nome do arquivo de teste, por exemplo `python .\main.py ..\tests\com_erros.txt`.
