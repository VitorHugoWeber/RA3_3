from .gramatica_atributos import T_BOOL, T_INT

def analisar_memoria_controle(program, tabela):
    erros = []
    for node in program:
        _visitar(node, tabela, erros)
    return erros, tabela

def _visitar(node, tabela, erros):
    if node["node"] == "op":
        op = node["op"]
        if op == "MEM":
            if len(node["args"]) == 1:
                nome = node["args"][0]["name"]
                if nome not in tabela or not tabela[nome].get("initialized", False):
                    erros.append({"linha": node["line"], "mensagem": "memória {} não inicializada".format(nome)})
        if op == "RES":
            arg = node["args"][0]
            if arg["node"] == "literal":
                if not isinstance(arg["value"], int) or arg["value"] < 0:
                    erros.append({"linha": node["line"], "mensagem": "RES requer inteiro não negativo"})
        if op == "if":
            cond = node["args"][0]
            if cond.get("inferred_type") != T_BOOL:
                erros.append({"linha": node["line"], "mensagem": "condição de if deve ser booleana"})
        if op == "while":
            cond = node["args"][0]
            if cond.get("inferred_type") != T_BOOL:
                erros.append({"linha": node["line"], "mensagem": "condição de while deve ser booleana"})
        for a in node["args"]:
            _visitar(a, tabela, erros)
    else:
        return