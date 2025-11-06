# Vitor Hugo Behlau Weber
class ParseError(Exception):
    pass

def _parse_atom(tokens, pos):
    tok = tokens[pos]
    if tok["tipo"] in {"INT", "REAL"}:
        val = float(tok["lexema"]) if tok["tipo"] == "REAL" else int(tok["lexema"])
        node = {
            "node": "literal",
            "value": val,
            "literal_type": "real" if tok["tipo"] == "REAL" else "int",
            "line": tok["linha"]
        }
        return node, pos + 1
    else:
        node = {
            "node": "id",
            "name": tok["lexema"],
            "line": tok["linha"]
        }
        return node, pos + 1

def _parse_paren(tokens, pos):
    start_tok = tokens[pos]
    if start_tok["lexema"] != "(":
        raise ParseError("esperado (")
    pos += 1
    elements = []
    while pos < len(tokens) and tokens[pos]["lexema"] != ")":
        node, pos = _parse_expr(tokens, pos)
        elements.append(node)
    if pos >= len(tokens) or tokens[pos]["lexema"] != ")":
        raise ParseError("esperado )")
    pos += 1
    if not elements:
        raise ParseError("expressão vazia")
    last = elements[-1]
    if last["node"] == "id":
        op = last["name"]
    else:
        raise ParseError("operador inválido")
    args = elements[:-1]
    node = {
        "node": "op",
        "op": op,
        "args": args,
        "line": start_tok["linha"]
    }
    return node, pos

def _parse_expr(tokens, pos):
    tok = tokens[pos]
    if tok["lexema"] == "(":
        return _parse_paren(tokens, pos)
    return _parse_atom(tokens, pos)

def parse_program(lines_tokens):
    program = []
    for line_tokens in lines_tokens:
        if not line_tokens:
            continue
        node, pos = _parse_expr(line_tokens, 0)
        if pos != len(line_tokens):
            raise ParseError("tokens extras na linha {}".format(line_tokens[0]["linha"]))
        program.append(node)

    return program
