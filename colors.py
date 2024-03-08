class Colors:
    black = (0, 0, 0)
    bloque_barra = (64, 193, 146)
    bloque_l_invertida = (84, 67, 167)
    bloque_t = (167, 67, 157)
    bloque_s_invertida = (184, 57, 64)
    bloque_cuadrado = (192, 167, 62)
    bloque_l = (184, 104, 56)
    bloque_s = (135, 183, 55)

    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.bloque_barra, cls.bloque_l_invertida, cls.bloque_t, cls.bloque_s_invertida, cls.bloque_cuadrado, cls.bloque_l, cls.bloque_s]