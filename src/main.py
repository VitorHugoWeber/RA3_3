import sys
from pathlib import Path
from lexer import tokenize_file
from parser import parse_program, ParseError
from semantico.gramatica_atributos import get_gramatica_markdown
from semantico.analisador_tipos import analisar_tipos
from semantico.memoria_controle import analisar_memoria_controle
from semantico.gerar_arvore import gerar_arquivos

def executar(caminho):
    base_dir = Path(__file__).resolve().parent.parent
    docs_dir = base_dir / "docs"
    gramatica_md = get_gramatica_markdown()
    erros_coletados = []
    try:
        linhas_tokens = tokenize_file(caminho)
    except Exception as e:
        erros_coletados.append({"linha": 0, "mensagem": "erro léxico: {}".format(str(e))})
        gerar_arquivos([], erros_coletados, [], gramatica_md, docs_dir)
        return
    try:
        programa = parse_program(linhas_tokens)
    except ParseError as e:
        erros_coletados.append({"linha": 0, "mensagem": "erro sintático: {}".format(str(e))})
        gerar_arquivos([], erros_coletados, [], gramatica_md, docs_dir)
        return
    programa, tabela, erros_tipos, linhas_resultado = analisar_tipos(programa)
    erros_mem, tabela = analisar_memoria_controle(programa, tabela)
    gerar_arquivos(programa, erros_tipos + erros_coletados, erros_mem, gramatica_md, docs_dir)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        caminho = str(Path(__file__).resolve().parent.parent / "tests" / "teste1.txt")
    else:
        caminho = sys.argv[1]
    executar(caminho)