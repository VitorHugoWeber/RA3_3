def _classify_token(tok):
    ops = {"+", "-", "*", "|", "/", "%", "^", ">", "<", ">=", "<=", "==", "!=", "if", "while", "RES", "MEM"}
    if tok in ops:
        return "OP"
    if tok == "(":
        return "LPAREN"
    if tok == ")":
        return "RPAREN"
    if tok.isdigit():
        return "INT"
    try:
        float(tok)
        return "REAL"
    except ValueError:
        return "ID"

def _split_multi(tok_list):
    res = []
    i = 0
    while i < len(tok_list):
        t = tok_list[i]
        if t in {">", "<"} and i + 1 < len(tok_list) and tok_list[i + 1] == "=":
            res.append(t + "=")
            i += 2
        elif t == "=" and i + 1 < len(tok_list) and tok_list[i + 1] == "=":
            res.append("==")
            i += 2
        elif t == "!" and i + 1 < len(tok_list) and tok_list[i + 1] == "=":
            res.append("!=")
            i += 2
        else:
            res.append(t)
            i += 1
    return res

def tokenize_line(line, lineno):
    line = line.replace("(", " ( ").replace(")", " ) ")
    parts = line.strip().split()
    parts = _split_multi(parts)
    tokens = []
    for p in parts:
        tokens.append({
            "lexema": p,
            "tipo": _classify_token(p),
            "linha": lineno
        })
    return tokens

def tokenize_file(path):
    all_lines = []
    with open(path, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                all_lines.append([])
            else:
                all_lines.append(tokenize_line(line, i))
    return all_lines