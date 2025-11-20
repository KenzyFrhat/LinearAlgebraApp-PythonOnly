def format_fraction_matrix(M):
    lines = []
    for r in M:
        cells = []
        for x in r:
            try:
                num = x.numerator; den = x.denominator
                if den == 1:
                    cells.append(str(num))
                else:
                    cells.append(f"{num}/{den}")
            except:
                cells.append(str(x))
        lines.append('\t'.join(cells))
    return '\n'.join(lines)
