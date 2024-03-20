class Colors:
    """
    black = (0, 0, 0)
    i_block = (64, 193, 146)
    j_block = (84, 67, 167)
    t_block = (167, 67, 157)
    z_block = (184, 57, 64)
    o_block = (192, 167, 62)
    l_block = (184, 104, 56)
    s_block = (135, 183, 55)
    """
    black = (0, 0, 0)
    i_block = (71, 193, 149) #
    j_block = (94, 76, 176) #
    t_block = (176, 76, 167) #
    z_block = (196, 65, 72)#
    o_block = (185, 160, 58) #
    l_block = (194, 114, 65) #
    s_block = (145, 193, 65) #

    @classmethod
    def get_cell_colors(cls):
        return [cls.black, cls.i_block, cls.j_block, cls.t_block, cls.z_block, cls.o_block, cls.l_block, cls.s_block]