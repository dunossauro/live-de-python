import ezdxf

"""Começa configuração do desenho."""
# Cria um novo desenho
dwg = ezdxf.readfile('smartstand.dxf')

# Configura o estilo do texto
dwg.styles.new(
    'estiloso',
    dxfattribs={
        'font': 'arial.ttf',
        'width': 0.8
    }
)

# Endereçar o layout do desenho
msp = dwg.modelspace()

"""Adiciona elementos ao layout."""
nome = input('Entre com o nome: ')

atributos = {
    'height': 5,
    'color': 5,
    'halign': 2,
    'style': 'estiloso'
}
msp.add_text(
    text=nome,
    dxfattribs=atributos
).set_pos(p1=(106, 160))

"""Finaliza e salva o desenho."""
# Salva o desenho em arquivo
dwg.saveas(filename='exemplo_3.dxf')
