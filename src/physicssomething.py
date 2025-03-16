import pygame
import math
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Slingshot Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

clock = pygame.time.Clock()

SLINGSHOT_ORIGIN = (150, 450)
SLINGSHOT_RADIUS = 10
PROJECTILE_RADIUS = 10
SLINGSHOT_WIDTH = 5

GRAVITY = 0.5
LAUNCH_STRENGTH = 10

projectile = None
projectile_vel = pygame.Vector2(0, 0)

def draw_sling_shot():
    """Draw the slingshot on the screen."""
    pygame.draw.line(screen, BLACK, SLINGSHOT_ORIGIN, (SLINGSHOT_ORIGIN[0], SLINGSHOT_ORIGIN[1] - 60), SLINGSHOT_WIDTH)
    pygame.draw.circle(screen, BLACK, SLINGSHOT_ORIGIN, SLINGSHOT_RADIUS)

def draw_projectile():
    """Draw the projectile."""
    if projectile:
        pygame.draw.circle(screen, RED, (int(projectile.x), int(projectile.y)), PROJECTILE_RADIUS)

def reset_projectile():
    """Reset the projectile to the slingshot origin."""
    global projectile, projectile_vel
    projectile = pygame.Vector2(SLINGSHOT_ORIGIN[0], SLINGSHOT_ORIGIN[1])
    projectile_vel = pygame.Vector2(0, 0)

def game_loop():
    """Main game loop."""
    global projectile, projectile_vel
    reset_projectile()

    is_dragging = False
    drag_start = None

    while True:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    drag_start = pygame.mouse.get_pos()
                    is_dragging = True

            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pressed()[0] == 0 and is_dragging:
                    drag_end = pygame.mouse.get_pos()
                    delta = pygame.Vector2(drag_end[0] - drag_start[0], drag_end[1] - drag_start[1])
                    projectile_vel = delta * LAUNCH_STRENGTH / 50
                    is_dragging = False

        if is_dragging:
            drag_end = pygame.mouse.get_pos()
            projectile = pygame.Vector2(drag_end[0], drag_end[1])

        if projectile:
            projectile += projectile_vel
            projectile_vel.y += GRAVITY

        draw_sling_shot()
        draw_projectile()

        if projectile.y > HEIGHT or projectile.x < 0 or projectile.x > WIDTH:
            reset_projectile()

        pygame.display.update()

        clock.tick(60)

if __name__ == "__main__":
    game_loop()
