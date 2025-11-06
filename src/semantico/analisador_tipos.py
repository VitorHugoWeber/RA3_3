from .gramatica_atributos import T_INT, T_REAL, T_BOOL, T_UNKNOWN, tipo_binario

def analisar_tipos(program):
    tabela = {}
    erros = []
    linhas_resultado = []
    for idx, node in enumerate(program):
        t = inferir_tipo(node, tabela, erros, idx, linhas_resultado)
        linhas_resultado.append(t)
    return program, tabela, erros, linhas_resultado

def inferir_tipo(node, tabela, erros, idx_linha_prog, linhas_resultado):
    if node["node"] == "literal":
        node["inferred_type"] = node["literal_type"]
        return node["literal_type"]
    if node["node"] == "id":
        nome = node["name"]
        if nome.isdigit():
            node["inferred_type"] = T_INT
            return T_INT
        if nome in tabela:
            node["inferred_type"] = tabela[nome]["type"]
            return tabela[nome]["type"]
        node["inferred_type"] = T_UNKNOWN
        return T_UNKNOWN
    op = node["op"]
    args = node["args"]
    tipos_args = []
    for a in args:
        t = inferir_tipo(a, tabela, erros, idx_linha_prog, linhas_resultado)
        tipos_args.append(t)
    if op == "MEM":
        if len(args) == 2:
            val_type = tipos_args[0]
            mem_name = args[1]["name"]
            if val_type == T_BOOL:
                erros.append({"linha": node["line"], "mensagem": "não é permitido armazenar booleano em MEM"})
                node["inferred_type"] = T_UNKNOWN
                return T_UNKNOWN
            tabela[mem_name] = {"initialized": True, "type": val_type}
            node["inferred_type"] = val_type
            return val_type
        if len(args) == 1:
            mem_name = args[0]["name"]
            if mem_name in tabela:
                node["inferred_type"] = tabela[mem_name]["type"]
                return tabela[mem_name]["type"]
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
    if op == "RES":
        if len(args) != 1 or args[0]["node"] != "literal":
            erros.append({"linha": node["line"], "mensagem": "RES requer inteiro não negativo"})
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
        n = args[0]["value"]
        if not isinstance(n, int) or n < 0:
            erros.append({"linha": node["line"], "mensagem": "RES requer inteiro não negativo"})
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
        alvo = idx_linha_prog - (n + 1)
        if alvo < 0 or alvo >= len(linhas_resultado):
            erros.append({"linha": node["line"], "mensagem": "linha referenciada por RES não existe"})
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
        tipo_alvo = linhas_resultado[alvo]
        node["inferred_type"] = tipo_alvo
        return tipo_alvo
    if op == "if":
        if len(tipos_args) != 3:
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
        node["inferred_type"] = tipos_args[1]
        return tipos_args[1]
    if op == "while":
        if len(tipos_args) != 2:
            node["inferred_type"] = T_UNKNOWN
            return T_UNKNOWN
        node["inferred_type"] = tipos_args[1]
        return tipos_args[1]
    if len(tipos_args) == 2:
        t = tipo_binario(op, tipos_args[0], tipos_args[1])
        if t == T_UNKNOWN:
            erros.append({"linha": node["line"], "mensagem": "incompatibilidade de tipos em operador {}".format(op)})
        node["inferred_type"] = t
        return t
    if len(tipos_args) == 1:
        node["inferred_type"] = tipos_args[0]
        return tipos_args[0]
    node["inferred_type"] = T_UNKNOWN
    return T_UNKNOWN