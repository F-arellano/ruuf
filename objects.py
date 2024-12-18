import numpy as np

class Panel:
    """
    Representa un panel solar con un tamaño y una posición en un techo.

    Attributes:
        size (tuple[int, int]): Tamaño del panel (ancho, alto).
        pos (tuple[int, int] | None): Posición del panel en la rejilla del techo.
        id (int | None): Identificador único del panel.
    """
    id_counter = 0

    def __init__(self, size: tuple[int, int]):
        self.size = size

        self.pos = None
        self.id = None

    def set_pos(self, pos: tuple[int, int]):
        """
        Establece la posición del panel en la rejilla y asigna un ID único.

        Args:
            pos (tuple[int, int]): Posición (fila, columna) en la rejilla.
        """
        self.pos = pos
        Panel.id_counter += 1
        self.id = Panel.id_counter



class Roof:
    """
    Representa un techo donde se pueden colocar paneles solares.

    Attributes:
        size (tuple[int, int]): Tamaño del techo (filas, columnas).
        grid (np.ndarray): Rejilla que representa el techo (0 indica espacio vacío).
        panels (list[Panel]): Lista de paneles colocados en el techo.
    """
    def __init__(self, size: tuple[int, int]):
        self.size = size
        self.grid = np.zeros(size, dtype=int)
        self.panels = []

    def is_space_available(self, pos: tuple[int, int], size: tuple[int, int]) -> bool:
        """
        Verifica si hay espacio disponible para colocar un panel.

        Args:
            pos (tuple[int, int]): Posición inicial (fila, columna).
            size (tuple[int, int]): Tamaño del panel (alto, ancho).

        Returns:
            bool: True si el espacio está disponible, False de lo contrario.
        """
        x, y = pos
        for i in range(size[0]):
            for j in range(size[1]):
                if x + i >= self.size[0] or y + j >= self.size[1] or self.grid[x + i, y + j] != 0:
                    return False
        return True


    def place_panel(self, pos: tuple[int, int], panel: Panel):
        """
        Coloca un panel en la rejilla y actualiza la información.

        Args:
            pos (tuple[int, int]): Posición inicial (fila, columna).
            panel (Panel): Panel a colocar.
        """
        panel.set_pos(pos)
        self.panels.append(panel)
        x, y = pos
        for i in range(panel.size[0]):
            for j in range(panel.size[1]):
                self.grid[x + i, y + j] = panel.id


    def add_panel(self, pos: tuple[int, int], size: tuple[int, int]) -> bool:
        """
        Intenta agregar un panel al techo.

        Args:
            pos (tuple[int, int]): Posición inicial (fila, columna).
            size (tuple[int, int]): Tamaño del panel (alto, ancho).

        Returns:
            bool: True si el panel fue agregado, False de lo contrario.
        """
        if self.is_space_available(pos, size):
            panel = Panel(size)
            self.place_panel(pos, panel)
            return True
        return False
