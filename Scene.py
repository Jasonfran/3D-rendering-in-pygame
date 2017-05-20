from abc import ABCMeta, abstractmethod


class Scene(metaclass=ABCMeta):

    @abstractmethod
    def update(self, delta):
        pass

    @abstractmethod
    def render(self, screen):
        pass

    @abstractmethod
    def handle_input(self, event, pressed_keys):
        pass

