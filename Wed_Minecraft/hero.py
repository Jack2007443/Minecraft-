class Hero:
    """ Управління гравцем """
    def __init__(self, pos, land):

        self.start_pos = pos

        base.camera.SetPos(self.start_pos)
        base.camera.setZ(180)
        