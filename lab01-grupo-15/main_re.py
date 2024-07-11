import re

pat01 = '[0-9]+|[a-b]|\b'
lista_cadeias = ['aa', '0001', 'b', '\b', '0', '0a']
for c in lista_cadeias:
    mat01 = re.fullmatch(pat01,c)
    print(f"Cadeia {c}", end=" ")
    print(f"é gerada" if mat01 is not None else "não é gerada")