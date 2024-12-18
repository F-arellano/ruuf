from objects import Roof

def get_greedy_solution(
        roof_size: tuple[int, int],
        panel_size: tuple[int, int],
        plot: bool = False
        ) -> int:
    """
    Calcula la solución mediante un algoritmo greedy para maximizar el número de paneles.

    Args:
        roof_size (tuple[int, int]): Tamaño del techo (filas, columnas).
        panel_size (tuple[int, int]): Tamaño de los paneles (ancho, alto).
        plot (bool): Si es True, imprime las rejillas resultantes.

    Returns:
        int: El máximo número de paneles que se pueden colocar.
    """

    # en roof 1 colocaremos primero los paneles de forma horizontal, luego vertical
    # en roof 2 haremos lo contrario, primero vertical.
    roof1 = Roof(roof_size)
    roof2 = Roof(roof_size)
    for x in range(roof1.size[0]):
        for y in range(roof1.size[1]):
            pos = (x, y)
            inverted_size = (panel_size[1], panel_size[0])

            roof1.add_panel(pos, panel_size)
            roof1.add_panel(pos, inverted_size)

            roof2.add_panel(pos, inverted_size)
            roof2.add_panel(pos, panel_size)

    n_panels = max(len(roof1.panels), len(roof2.panels))

    if plot:
        print("panels horizontal first: ", len(roof1.panels))
        print(roof1.grid)
        print("panels vertical first: ", len(roof2.panels))
        print(roof2.grid)

    return n_panels
