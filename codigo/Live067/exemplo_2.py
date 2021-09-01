import ezdxf

"""Começa configuração do desenho."""
# Cria um novo desenho
dwg = ezdxf.new(dxfversion='AC1032')

# Configura diferentes camadas com diferentes cores
dwg.layers.new(name='CUT', dxfattribs={'color': 7})
dwg.layers.new(name='SCAN', dxfattribs={'color': 5})

# Endereçar o layout do desenho
msp = dwg.modelspace()

"""Adiciona elementos ao layout."""
def desenha_circulos_recursivos(x, y, raio):
    msp.add_circle(
        center=(x, y),
        radius=raio,
        dxfattribs={'layer': 'SCAN'}
    )
    if raio > 2:
        desenha_circulos_recursivos(
            x + raio/2, y, raio/2
        )
        desenha_circulos_recursivos(
            x - raio/2, y, raio/2
        )
        desenha_circulos_recursivos(
            x, y + raio/2, raio/2
        )
        desenha_circulos_recursivos(
            x, y - raio/2, raio/2
        )

def desenha_circulo(x, y, raio):
    msp.add_circle(
        center=(x, y),
        radius=raio,
        dxfattribs={'layer': 'CUT'}
    )
    desenha_circulos_recursivos(x, y, raio)

diametro = int(input("Entre com o diâmetro: "))
desenha_circulo(0, 0, diametro/2)

"""Finaliza e salva o desenho."""
# Salva o desenho em arquivo
dwg.saveas(filename='exemplo_2.dxf')
