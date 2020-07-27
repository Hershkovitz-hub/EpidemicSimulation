import thorpy
import pygame
from epidemic_simulation.GUI.features.world import World
from epidemic_simulation.GUI.features.utils.screen_divider import ScreenDivider
from epidemic_simulation.GUI.features.utils.sliders import Sliders


class UserInterface:
    def __init__(self, world: World, ui_limits: list):
        """
        A class to create and update all UI-related components of the simulation
        :param world: [The simulation World instance, conatining all window-related properties]
        :type world: World
        :param ui_limits: [List of 4 tuples, indicating UI part of the window]
        :type ui_limits: list
        """
        self.world = world
        self.screen = self.world.screen
        self.calculate_window_dimension(ui_limits)
        self.set_initial_parameters()

    def set_initial_parameters(self):
        """
        Initiate the "starting point" of the world-related parameters
        """
        self.parameters = {}
        for parameter in Sliders:
            self.parameters[parameter.name] = parameter.value["initial_value"]

    def calculate_window_dimension(self, ui_limits: list):
        """
        Calculates the area designated for UI from a list of 4 tuples indicating it's corners' coordinates
        :param ui_limits: [List of 4 tuples]
        :type ui_limits: list
        """
        self.height = ui_limits[1][1] - ui_limits[0][1]
        self.width = ui_limits[2][0] - ui_limits[0][0]

    def initiate_ui_box(self, elements: list):
        """
        Initiates a thorpy box where sliders and buttons take place
        :param elements: [List of all thorpy elements that will be integrated into the UI box]
        :type elements: list
        """
        self.ui_box = thorpy.Box(
            size=(self.width, self.height), elements=elements
        )

    def generate_quit_button(self):
        """
        Creates a quit button
        """
        return thorpy.make_button("Quit", func=thorpy.functions.quit_func)

    def initiate_slider(
        self,
        title: str,
        values_range: tuple,
        initial_value: float,
        values_type: type,
    ):
        """
        Initiate thorpy.SliderX slider for GUI usage
        :param title: [Slider's title]
        :type title: str
        :param value_range: [Slider's values range]
        :type value_range: tuple
        :param initial_value: [Slider's initial value]
        :type initial_value: float
        """
        return thorpy.SliderX(
            length=300,
            limvals=values_range,
            text=title,
            initial_value=initial_value,
            type_=values_type,
        )

    def initiate_ui_selections(self):
        """
        Sets the relevant elements into the UI box and defines it's reaction
        """
        self.initiate_ui_box(self.elements)
        self.ui_box.add_reaction(self.reaction)
        self.menu = thorpy.Menu(self.ui_box)
        for element in self.menu.get_population():
            element.surface = self.world.screen
        self.ui_box.set_topleft((10, 10))
        self.ui_box.blit()
        self.ui_box.update()

    @property
    def reaction(self):
        """
        Sets the reaction to slider-related user event
        :return: [The value of the slider after user's choice]
        :rtype: [int or float]
        """
        return thorpy.Reaction(
            reacts_to=pygame.USEREVENT,
            reac_func=self.sliders_reaction,
            event_args={"id": thorpy.constants.EVENT_SLIDE},
            params={
                "people_n": self.ui_box.get_elements()[0],
                "infection_p": self.ui_box.get_elements()[1],
                "infection_r": self.ui_box.get_elements()[2],
                "carriers": self.ui_box.get_elements()[3],
                "duration": self.ui_box.get_elements()[4],
            },
        )

    def sliders_reaction(
        self, event, people_n, infection_p, infection_r, carriers, duration
    ):
        """
        Adds the value to it's designated target, by comparing the user event to those added to UI box.
        """
        if event.el == people_n:
            self.parameters["subjects_n"] = people_n.get_value()
        if event.el == infection_p:
            self.parameters["infection_p"] = infection_p.get_value()
        if event.el == infection_r:
            self.parameters["infection_r"] = infection_r.get_value()
        if event.el == carriers:
            self.parameters["initial_carriers_p"] = carriers.get_value()
        if event.el == duration:
            self.parameters["sickness_duration"] = duration.get_value()

    @property
    def elements(self) -> list:
        """
        All UI elements generated
        :return: [List of thorpy's elements]
        :rtype: list
        """
        elements = []
        for slider in Sliders:
            slider_dict = slider.value
            (
                title,
                values_range,
                initial_value,
                values_type,
            ) = slider_dict.values()
            elements.append(
                self.initiate_slider(
                    title, values_range, initial_value, values_type
                )
            )
        elements.append(self.generate_quit_button())
        return elements
