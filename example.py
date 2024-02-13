# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0


class Player:

    def __init__(self):
        self.pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

    def update(self):

        pygame.draw.circle(screen, "red", player.pos, 40)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            player.pos.y -= 300 * dt
        if keys[pygame.K_s]:
            player.pos.y += 300 * dt
        if keys[pygame.K_a]:
            player.pos.x -= 300 * dt
        if keys[pygame.K_d]:
            player.pos.x += 300 * dt



player = Player()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    player.update()

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
