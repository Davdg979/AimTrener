import pygame
import random
import time
import math
import sys

class AimTrainer:
    def __init__(self, x=100, y=100, w=800, h=600, outer_rgb=(255,255,0), center_rgb=(255,0,0), radius=25):
        pygame.init()
        self.outer_rgb = outer_rgb
        self.center_rgb = center_rgb
        self.radius = radius
        self.hits = 0
        self.running = True
        self.target_pos = (0,0)
        self.spawn_time = 0

        # Tela em janela (não fullscreen)
        self.screen = pygame.display.set_mode((w,h))
        pygame.display.set_caption("Aim Trainer")
        self.width, self.height = self.screen.get_size()
        self.spawn_target()

    def spawn_target(self):
        x = random.randint(self.radius, self.width - self.radius)
        y = random.randint(self.radius, self.height - self.radius)
        self.target_pos = (x,y)
        self.spawn_time = time.time()

    def draw(self):
        self.screen.fill((0,0,0))
        pygame.draw.circle(self.screen, self.outer_rgb, self.target_pos, self.radius)
        pygame.draw.circle(self.screen, self.center_rgb, self.target_pos, self.radius//2)
        pygame.display.flip()

    def handle_click(self, pos):
        x,y = pos
        tx,ty = self.target_pos
        dist = math.hypot(x-tx, y-ty)
        if dist <= self.radius:
            self.hits += 1
            self.spawn_target()

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.handle_click(event.pos)
            self.draw()
            clock.tick(60)
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = AimTrainer(x=100, y=100, w=800, h=600, outer_rgb=(255,255,0), center_rgb=(255,0,0), radius=25)
    app.run()
