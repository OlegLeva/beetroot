def val_conv(s):
    """validation and immediate conversion"""
    s = s.strip()
    if not s:
        return
    tmp = s
    if s[0] in "+-":
        tmp = s[1:]
    pieces = tmp.split(".")
    if len(pieces) > 2:
        return
    for p in pieces:
        if not p or not p.isdigit():
            return
    return float(s)
