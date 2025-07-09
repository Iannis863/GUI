import pygame
import random

pygame.init()

width, height = 670, 600
rows, cols = 10, 4
radius = 20
spacing = 10
colors = ["red", "blue", "yellow", "white", "black", "purple", "pink", "orange"]
color_map = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "yellow": (255, 255, 0),
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "purple": (128, 0, 128),
    "pink": (252, 3, 152),
    "orange": (255, 165, 0)
}

color_key = {
    "red": "r",
    "blue": "b",
    "yellow": "y",
    "white": "w",
    "black": "k",
    "purple": "p",
    "pink": "i",
    "orange": "o"
}

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Color Guessing Game")

font = pygame.font.SysFont(None, 24)

def generate_colors():
    return random.choices(colors, k=4)

def check_guess(guess, code):
    check = [""] * 4
    for i in range(4):
        if guess[i] == code[i]:
            check[i] = "red"
        elif guess[i] in code:
            check[i] = "yellow"
    return check

def draw_board(guesses, feedback, message=""):
    screen.fill((2, 5, 48))
    for row in range(rows):
        for col in range(cols):
            x = col * (2 * radius + spacing) + 50
            y = row * (2 * radius + spacing) + 50
            color = color_map.get(guesses[row][col], (186, 194, 183))
            pygame.draw.circle(screen, color, (x, y), radius)
        for col in range(cols):
            x = col * (2 * radius + spacing) + 300
            y = row * (2 * radius + spacing) + 50
            color = color_map.get(feedback[row][col], (0, 0, 0))
            pygame.draw.circle(screen, color, (x, y), radius // 2)

        row_number_surface = font.render(str(rows - row), True, (255, 255, 255))
        row_number_rect = row_number_surface.get_rect(center=(15, row * (2 * radius + spacing) + 50))
        screen.blit(row_number_surface, row_number_rect)

    for row, color in enumerate(color_map.values()):
        x = width - 140
        y = row * (2 * radius + spacing) + 100
        pygame.draw.circle(screen, color, (x, y), radius)
        legend_surface = font.render(f"Press \"{list(color_key.values())[row]}\"", True, (255, 255, 255))
        legend_rect = legend_surface.get_rect(center=(x + 70, y))
        screen.blit(legend_surface, legend_rect)

    if message:
        text_surface = font.render(message, True, (255, 255, 255))
        text_rect = text_surface.get_rect(center=(width / 2, height - 30))
        screen.blit(text_surface, text_rect)

    pygame.display.flip()

def main():
    code = generate_colors()
    guesses = [[""] * 4 for _ in range(rows)]
    feedback = [[""] * 4 for _ in range(rows)]
    current_row = 9
    running = True
    message = ""
    while running:
        if current_row < 0:
            message = f"Game over! The correct colors were: {', '.join(code)}"
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and current_row < rows:
                    for col in range(cols):
                        if guesses[current_row][col] == "":
                            break
                    else:
                        guess = guesses[current_row]
                        feedback[current_row] = check_guess(guess, code)
                        if feedback[current_row] == ["red"] * 4:
                            message = f"Congratulations! You guessed the correct colors! You won in {rows - current_row} turns!"
                        current_row -= 1
                elif event.key == pygame.K_BACKSPACE:
                    if current_row < rows:
                        for col in reversed(range(cols)):
                            if guesses[current_row][col] != "":
                                guesses[current_row][col] = ""
                                break
                elif event.key in [pygame.K_r, pygame.K_b, pygame.K_y, pygame.K_w, pygame.K_k, pygame.K_p, pygame.K_i, pygame.K_o]:
                    color_key_map = {
                        pygame.K_r: "red",
                        pygame.K_b: "blue",
                        pygame.K_y: "yellow",
                        pygame.K_w: "white",
                        pygame.K_k: "black",
                        pygame.K_p: "purple",
                        pygame.K_i: "pink",
                        pygame.K_o: "orange"
                    }
                    color = color_key_map[event.key]
                    for col in range(cols):
                        if guesses[current_row][col] == "":
                            guesses[current_row][col] = color
                            break
        draw_board(guesses, feedback, message)
    pygame.quit()

if __name__ == "__main__":
    main()