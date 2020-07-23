import pymunk


class Boxes:
    def __init__(self, size_x: int, size_y: int, space=None):
        """
        Class to generate "boxes" (sub-windows) where the simulation takes place.
        It divides the main window in 3: 
        Right box - visualisation
        Top left box - UI
        Bottom left box - Parameters presentation
        :param size_x: [Main window's width]
        :type size_x: int
        :param size_y: [Main window's height]
        :type size_y: int
        """
        self.space = space
        self.size_x = size_x
        self.size_y = size_y
        self.box_x_boundary = self.size_x / 2
        self.box_y_boundary = self.size_y / 2

    def set_visual_window_limits(self) -> list:
        """
        Sets visualisation window limits in accordance to main window's size
        
        :return: [list of tuples indicating window's frame/boundaries]
        :rtype: list
        """
        box_points = [
            (self.size_x - 10, 10),
            (self.size_x - 10, self.size_y - 10),
            (self.box_x_boundary + 5, self.size_y - 10),
            (self.box_x_boundary + 5, 10),
        ]
        return box_points

    def set_ui_window_limits(self) -> list:
        """
        Sets UI window limits in accordance to main window's size

        :return: [list of tuples indicating window's frame/boundaries]
        :rtype: list
        """
        box_points = [
            (10, self.size_y - 140),
            (10, self.size_y - 10),
            (self.box_x_boundary - 5, self.size_y - 10),
            (self.box_x_boundary - 5, self.size_y - 140),
        ]
        return box_points

    def set_param_window_limits(self) -> list:
        """
        Sets parameters window limits in accordance to main window's size

        :return: [list of tuples indicating window's frame/boundaries]
        :rtype: list
        """
        box_points = [
            (10, 10),
            (10, self.size_y - 150),
            (self.box_x_boundary - 5, self.size_y - 150),
            (self.box_x_boundary - 5, 10),
        ]
        return box_points

    def add_window(self, box_boundaries: list):
        """
        Adds a windows to pymunk's space, as defined by it's boundaries.

        :param box_boundaries: [list of tuples indicating window's frame/boundaries]
        :type box_boundaries: list
        """
        for i in range(len(box_boundaries)):
            seg = pymunk.Segment(
                self.space.static_body,
                box_boundaries[i],
                box_boundaries[(i + 1) % 4],
                2,
            )
            seg.elasticity = 0.999
            seg.color = (255, 255, 255, 0)
            self.space.add(seg)

    @property
    def ui_shape(self):
        ui_box = self.set_ui_window_limits()
        width = ui_box[2][0] - ui_box[0][0]
        height = ui_box[1][1] - ui_box[0][1]
        return width, height

    def create(self):
        """
        Sets all windows' boundaries and add them to pymunk's space
        """
        for box_boundaries in [
            self.set_param_window_limits(),
            self.set_ui_window_limits(),
            self.set_visual_window_limits(),
        ]:
            self.add_window(box_boundaries)
