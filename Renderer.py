import pygame
from MainScene import MainScene


class Renderer:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.main_screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.running = True
        self.clock = pygame.time.Clock()
        self.current_scene = MainScene(self)

        pygame.init()
        pygame.font.init()
        self.font = pygame.font.SysFont("Arial", 15)
        pygame.display.set_caption("Pygame 3D Renderer")
        self.main_screen.fill((255, 255, 255))

    def run(self):
        while self.running:
            pressed_keys = pygame.key.get_pressed()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
            self.current_scene.handle_input(events, pressed_keys)

            self.main_screen.fill((0, 0, 0))
            dt = self.clock.tick(60)/1000.0
            # update current scene
            self.current_scene.update(dt)
            # render current scene
            self.current_scene.render(self.main_screen)

            fps = self.font.render(str(int(self.clock.get_fps())), 1, (0, 0, 0))
            self.main_screen.blit(fps, (0, 0))

            pygame.display.flip()

if __name__ == '__main__':
    renderer = Renderer()
    renderer.run()

