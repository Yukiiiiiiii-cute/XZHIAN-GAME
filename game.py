import pygame
import random

# Initialize pygame
pygame.init()

# Screen dimensions
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)
blue = (135, 206, 235)

# Game settings
bird_size = (34, 24)  # Size of the bird
bird_x = 50
bird_y = height // 2
bird_velocity = 0
gravity = 0.5
flap_strength = -10
pipe_width = 70
pipe_gap = 150
pipe_velocity = 5

# Load and scale the bird image
# Make sure to replace this with the actual path to your image file!
bird_image = pygame.image.load('C:/Users/Joy Dayao/Downloads/game ni yukiii/459092232_441907392188623_4553893194067597342_n.jpg')
bird_image = pygame.transform.scale(bird_image, bird_size)

# Create clock object to manage frame rate
clock = pygame.time.Clock()

def draw_bird(x, y):
    # Draw the bird image
    screen.blit(bird_image, (x, y))

def draw_pipe(x, y, width, gap):
    pygame.draw.rect(screen, green, pygame.Rect(x, 0, width, y))
    pygame.draw.rect(screen, green, pygame.Rect(x, y + gap, width, height))

def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, black)
    screen.blit(text, (width // 4, height // 3))
    pygame.display.flip()
    pygame.time.wait(2000)

def main():
    global bird_y, bird_velocity

    pipes = []
    score = 0
    pipe_timer = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = flap_strength

        # Bird physics
        bird_velocity += gravity
        bird_y += bird_velocity

        # Update pipe positions
        pipe_timer += 1
        if pipe_timer > 100:
            pipe_timer = 0
            pipe_height = random.randint(100, height - pipe_gap - 100)
            pipes.append([width, pipe_height])

        for pipe in pipes:
            pipe[0] -= pipe_velocity
            if pipe[0] < -pipe_width:
                pipes.remove(pipe)
                score += 1

        # Collision detection
        bird_rect = pygame.Rect(bird_x, bird_y, *bird_size)
        for pipe in pipes:
            pipe_rect_top = pygame.Rect(pipe[0], 0, pipe_width, pipe[1])
            pipe_rect_bottom = pygame.Rect(pipe[0], pipe[1] + pipe_gap, pipe_width, height)
            if bird_rect.colliderect(pipe_rect_top) or bird_rect.colliderect(pipe_rect_bottom):
                game_over()
                return

        if bird_y > height or bird_y < 0:
            game_over()
            return

        # Draw everything
        screen.fill(blue)
        draw_bird(bird_x, bird_y)
        for pipe in pipes:
            draw_pipe(pipe[0], pipe[1], pipe_width, pipe_gap)
        pygame.display.flip()
        clock.tick(30)

    pygame.quit()

if __name__ == "__main__":
    main()
