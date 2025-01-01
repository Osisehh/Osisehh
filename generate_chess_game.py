import random
import chess
import chess.svg

# Example function to generate a random chess game
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

# Write the SVG file
with open('dist/github-contribution-chess-game.svg', 'w') as f:
    f.write(svg_content)
