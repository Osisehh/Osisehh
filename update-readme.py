import re
import random
import chess
import chess.svg
import os

# Define the animation styles
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

# Update README with animations
def update_readme():
    try:
        with open("README.md", "r") as file:
            content = file.read()
        content = re.sub(r"(<!-- Start of the animated section -->)",
                         r"\1\n" + animation_styles, content)
        with open("README.md", "w") as file:
            file.write(content)
    except Exception as e:
        print(f"Error updating README: {e}")

# Generate chess animations
def generate_chess_game():
    board = chess.Board()
    moves = []
    while not board.is_game_over():
        move = random.choice(list(board.legal_moves))
        board.push(move)
        moves.append(board.fen())
    return moves

def create_svg_animation():
    moves = generate_chess_game()
    os.makedirs("dist", exist_ok=True)
    svg_content = '<svg xmlns="http://www.w3.org/2000/svg" width="800" height="800">'
    for i, fen in enumerate(moves):
        board = chess.Board(fen)
        svg_content += f'<g id="frame{i}" style="display:none;">{chess.svg.board(board)}</g>'
    svg_content += "</svg>"
    with open("dist/github-contribution-chess-game.svg", "w") as f:
        f.write(svg_content)

update_readme()
create_svg_animation()
