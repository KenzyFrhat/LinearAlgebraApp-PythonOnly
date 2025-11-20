from fractions import Fraction

def parse_matrix_from_table(table):
    rows = table.rowCount()
    cols = table.columnCount()
    M = []
    for i in range(rows):
        row = []
        for j in range(cols):
            item = table.item(i,j)
            s = item.text().strip() if item else ''
            if s == '': 
                row.append(Fraction(0))
            else:
                # allow fraction string a/b or decimal or int
                if '/' in s:
                    a,b = s.split('/')
                    row.append(Fraction(int(a.strip()), int(b.strip())))
                else:
                    try:
                        row.append(Fraction(int(s)))
                    except ValueError:
                        row.append(Fraction(s))
        M.append(row)
    return M
