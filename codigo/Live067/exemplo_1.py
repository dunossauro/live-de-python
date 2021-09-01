import ezdxf

"""Começa configuração do desenho."""
# Cria um novo desenho
dwg = ezdxf.new(dxfversion='AC1032')

# Endereçar o layout do desenho
msp = dwg.modelspace()

"""Adiciona elementos ao layout."""
# Adiciona um traço no layout
msp.add_line(start=(5, 0), end=(5, 10))

# Adiciona um retângulo
retangulo = [(-20, 0), (0, 0), (0, 10), (-20, 10)]
msp.add_lwpolyline(
    points=retangulo,
    dxfattribs={'closed': True}
)

# Adiciona um triângulo
triangulo = [(50, -20), (90, -20), (70, 0)]
msp.add_lwpolyline(points=triangulo)

# Adiciona um círculo
msp.add_circle(center=(-10, -50), radius=20.5)

# Adiciona um texto
msp.add_text(
    text="Live de Python",
    dxfattribs={'height': 5, 'color': 5}
).set_pos((0, -10))

"""Finaliza e salva o desenho."""
# Salva o desenho em arquivo
dwg.saveas(filename='exemplo_1.dxf')
