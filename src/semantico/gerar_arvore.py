import json
from pathlib import Path

def _serializar(node):
    if node["node"] == "literal":
        return {
            "node": "literal",
            "value": node["value"],
            "type": node.get("inferred_type"),
            "line": node["line"]
        }
    if node["node"] == "id":
        return {
            "node": "id",
            "name": node["name"],
            "type": node.get("inferred_type"),
            "line": node["line"]
        }
    return {
        "node": "op",
        "op": node["op"],
        "args": [_serializar(a) for a in node["args"]],
        "type": node.get("inferred_type"),
        "line": node["line"]
    }

def gerar_arquivos(program, erros_tipos, erros_mem, gramatica_md, docs_dir):
    p = Path(docs_dir)
    p.mkdir(parents=True, exist_ok=True)
    arvore = [_serializar(n) for n in program]
    with (p / "arvore_atribuida.md").open("w", encoding="utf-8") as f:
        f.write("# Árvore Sintática Atribuída\n\n")
        f.write("```json\n")
        f.write(json.dumps(arvore, ensure_ascii=False, indent=2))
        f.write("\n```\n")
    with (p / "erros_semanticos.md").open("w", encoding="utf-8") as f:
        f.write("# Erros Semânticos\n\n")
        if not erros_tipos and not erros_mem:
            f.write("Nenhum erro.\n")
        else:
            for e in erros_tipos + erros_mem:
                f.write("- Linha {}: {}\n".format(e["linha"], e["mensagem"]))
    with (p / "julgamento_tipos.md").open("w", encoding="utf-8") as f:
        f.write("# Julgamento de Tipos\n\n")
        for n in arvore:
            _listar_tipos(n, f)
    with (p / "gramatica_atributos.md").open("w", encoding="utf-8") as f:
        f.write(gramatica_md)

def _listar_tipos(node, f):
    if node["node"] == "literal":
        f.write("- Linha {} literal -> {}\n".format(node["line"], node.get("type")))
        return
    if node["node"] == "id":
        f.write("- Linha {} id {} -> {}\n".format(node["line"], node["name"], node.get("type")))
        return
    f.write("- Linha {} op {} -> {}\n".format(node["line"], node["op"], node.get("type")))
    for a in node["args"]:
        _listar_tipos(a, f)