import re
import random
import chess
import chess.svg
import os

# Define the animation styles for the greetings
animation_styles = """
<style>
@keyframes fadeIn {
  0% { opacity: 0; }
  100% { opacity: 1; }
}

@keyframes slideIn {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(0); }
}

.fadeIn {
  animation: fadeIn 2s ease-in-out infinite alternate;
}

.slideIn {
  animation: slideIn 3s ease-in-out infinite alternate;
}
</style>
"""

# Read the README file
try:
    with open("README.md", "r") as file:
        readme_content = file.read()
except FileNotFoundError:
    print("README.md file not found. Please ensure the file exists in the repository.")
    exit(1)

# Insert the animation styles into the README content
updated_readme_content = re.sub(
    r"(<!-- Start of the animated section -->)",
    r"\1\n" + animation_styles,
    readme_content
)

# Update the HTML elements with the animation classes
updated_readme_content = re.sub(
    r'(<div id="greeting".*?>)',
    r'\1<span class="fadeIn">',
    updated_readme_content
)
updated_readme_content = re.sub(
    r'(<div id="name".*?>)',
    r'\1<span class="slideIn">',
    updated_readme_content
)
updated_readme_content = re.sub(
    r'(</div>)(?!\n<!-- End of the animated section -->)',
    r'</span>\1',
    updated_readme_content
)

# Write the updated content back to the README file
try:
    with open("README.md", "w") as file:
        file.write(updated_readme_content)
except IOError:
    print("An error occurred while writing to README.md.")
    exit(1)

# Generate a chess game animation
def generate_chess_game():
    board = chess.Board()
    moves = []

    while not board.is_game_over():
        move = random.choice(list(board.legal_moves))
        board.push(move)
        moves.append(board.fen())

    return moves

# Generate the chess game
moves = generate_chess_game()

# Create an SVG animation
svg_content = '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">'
svg_content += '<rect width="800" height="800" fill="white"/>'

for i, fen in enumerate(moves):
    board = chess.Board(fen)
    svg_board = chess.svg.board(board)
    svg_content += f'<g id="frame{i}" style="display:none;">{svg_board}</g>'

svg_content += '</svg>'

# Ensure the dist directory exists
os.makedirs('dist', exist_ok=True)

# Write the SVG file
try:
    with open('dist/github-contribution-chess-game.svg', 'w') as f:
        f.write(svg_content)
except IOError:
    print("An error occurred while writing the SVG file.")
    exit(1)
