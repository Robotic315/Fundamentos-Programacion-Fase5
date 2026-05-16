# ==============================================================================
# Curso: Fundamentos de Programación
# Fase 5 - Evaluación Final POA
# Problema Elegido: Problema 3 (Inventario)
# ==============================================================================

def calcular_cantidad_pedido(stock_actual, stock_minimo):
    """
    Evalúa si se necesita reabastecer el artículo.
    Retorna la diferencia si falta stock, o 0 si el stock es suficiente.
    """
    if stock_actual < stock_minimo:
        cantidad_a_pedir = stock_minimo - stock_actual
        return cantidad_a_pedir
    else:
        return 0


def main():

    inventario = [
        ["ART-01", "Teclado Inalámbrico", 15, 20],  
        ["ART-02", "Mouse Óptico", 30, 15],         
        ["ART-03", "Monitor 24 pulgadas", 5, 10],   
        ["ART-04", "Cable HDMI 2m", 50, 50],        
        ["ART-05", "Disco Duro 1TB", 3, 12]         
    ]

    print("="*45)
    print("   REPORTE DE REABASTECIMIENTO DE INVENTARIO   ")
    print("="*45)


    for articulo in inventario:

        nombre = articulo[1]
        stock_actual = articulo[2]
        stock_minimo = articulo[3]

        cantidad_pedir = calcular_cantidad_pedido(stock_actual, stock_minimo)

        if cantidad_pedir > 0:
            print(f"-> {nombre}: Se deben solicitar {cantidad_pedir} unidades.")
        else:
            print(f"-> {nombre}: Stock suficiente (0 unidades a solicitar).")
            
    print("="*45)

if __name__ == "__main__":
    main()