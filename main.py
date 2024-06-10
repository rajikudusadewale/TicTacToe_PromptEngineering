import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_size = (400, 500)
window = pygame.display.set_mode(window_size)
pygame.display.set_caption("Tic Tac Toe")

# Set up colors
deep_blue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Set up fonts
font_large = pygame.font.Font(None, 72)
font_medium = pygame.font.Font(None, 36)

# Initialize an empty grid
grid = [' '] * 9

#


# Function to display the grid
def display_grid():
    # Clear the window
    window.fill(deep_blue)

    # Draw the grid lines
    pygame.draw.line(window, white, (133, 100), (133, 400), 2)
    pygame.draw.line(window, white, (266, 100), (266, 400), 2)
    pygame.draw.line(window, white, (0, 200), (400, 200), 2)
    pygame.draw.line(window, white, (0, 300), (400, 300), 2)

    # Draw the symbols
    for i in range(9):
        row = i // 3
        col = i % 3
        symbol = grid[i]
        text = font_large.render(symbol, True, white)
        text_rect = text.get_rect(center=(col * 133 + 67, row * 100 + 150))
        window.blit(text, text_rect)

    # Draw the restart text
    restart_text = font_medium.render("Press 'R' to restart", True, white)
    restart_rect = restart_text.get_rect(center=(200, 450))
    window.blit(restart_text, restart_rect)

    pygame.display.update()


# Function to check if a player has won
def check_win(player):
    # Check rows, columns, and diagonals
    return ((grid[0] == grid[1] == grid[2] == player)
            or (grid[3] == grid[4] == grid[5] == player)
            or (grid[6] == grid[7] == grid[8] == player)
            or (grid[0] == grid[3] == grid[6] == player)
            or (grid[1] == grid[4] == grid[7] == player)
            or (grid[2] == grid[5] == grid[8] == player)
            or (grid[0] == grid[4] == grid[8] == player)
            or (grid[2] == grid[4] == grid[6] == player))


# Function to get the AI's move
def get_ai_move():
    # Implement the Minimax algorithm or any other AI strategy
    # For simplicity, this example uses a random move
    empty_spots = [i for i in range(9) if grid[i] == ' ']
    return random.choice(empty_spots)


# Function to display the game result
def display_result(result):
    text = font_large.render(result, True, white)
    text_rect = text.get_rect(center=(200, 50))
    window.blit(text, text_rect)
    pygame.display.update()
    pygame.time.delay(2000)


# Function to play the game
def play_game():
    player = 'X'
    while True:
        display_grid()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and player == 'X':
                x, y = pygame.mouse.get_pos()
                col = x // 133
                row = (y - 100) // 100
                move = row * 3 + col
                if grid[move] == ' ':
                    grid[move] = player
                    if check_win(player):
                        display_grid()
                        display_result("You win!")
                        return
                    if ' ' not in grid:
                        display_grid()
                        display_result("It's a draw!")
                        return
                    player = 'O'
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    # Reset the game
                    grid[:] = [' '] * 9
                    player = 'X'
                    continue

        if player == 'O':
            pygame.time.delay(
                500)  # Delay for 0.5 sec seconds before AI's move
            move = get_ai_move()
            grid[move] = player
            if check_win(player):
                display_grid()
                display_result("AI wins!")
                return
            if ' ' not in grid:
                display_grid()
                display_result("It's a draw!")
                return
            player = 'X'

        pygame.time.delay(100)


# Start the game
while True:
    play_game()
    # Reset the game
    grid[:] = [' '] * 9
