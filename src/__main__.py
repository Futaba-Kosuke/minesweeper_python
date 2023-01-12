from typing import List, TypedDict, Optional
import random
import pprint

CellType = TypedDict("CellType", {
    "is_open": bool,
    "is_mine": bool,
    "quantity": Optional[int]
})

BoardType = List[List[CellType]]


def init_board(cell_quantity: int, mine_quantity: int) -> BoardType:
    board: BoardType = []
    for i in range(0, cell_quantity):
        board.append([])
        for j in range(0, cell_quantity):
            board[i].append({
                "is_open": False,
                "is_mine": False,
                "quantity": None
            })
    
    i = 0
    while True:
        if i == mine_quantity:
            break
        
        x = random.randint(0, cell_quantity - 1)
        y = random.randint(0, cell_quantity - 1)
        if board[y][x]["is_mine"]:
            continue
        
        board[y][x]["is_mine"] = True
        i += 1

    return board

def is_complete(board: BoardType) -> bool:
    print(len(board[0]))
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if not board[i][j]["is_open"] and not board[i][j]["is_mine"]:
                return False
            
    return True

def count(x: int, y: int, board: BoardType) -> int:
    cnt = 0
    
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if y + i < 0 or y + i == len(board[0]):
                continue
            if x + j < 0 or x + j == len(board[0]):
                continue
            if board[y + i][x + j]["is_mine"]:
                cnt += 1
                
    return cnt

def display(board: BoardType) -> None:
    for i in range(len(board[0])):
        for j in range(len(board[0])):
            if board[i][j]["quantity"] is not None:
                print(board[i][j]["quantity"], end="")
            else:
                print("x", end="")
            print(" ", end="")
        print("\n", end="")
        
def open(x: int, y: int, board: BoardType, is_click: bool) -> BoardType:
    
    if board[y][x]["is_open"]:
        return board
    
    if board[y][x]["is_mine"]:
        return None
    
    cnt = count(x, y, board)
    
    board[y][x]["is_open"] = True
    board[y][x]["quantity"] = cnt

    if cnt == 0:
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                if y + i < 0 or y + i == len(board[0]):
                    continue
                if x + j < 0 or x + j == len(board[0]):
                    continue
                board = open(x + j, y + i, board, False)
    
    if is_click:
        display(board)
        
    return board

def main() -> None:
    cell_quantity = int(input("マス数 >> "))
    mine_quantity = int(input("爆弾の個数 >> "))

    board = init_board(cell_quantity=cell_quantity, mine_quantity=mine_quantity)

    while True:
        x_str, y_str = input("(x y) >> ").split(" ", 2)
        x = int(x_str) - 1
        y = int(y_str) - 1

        if x < 0 or x >= len(board[0]) or y < 0 or y >= len(board[0]):
            print("OUT OF BOARD!")
            continue
                
        board = open(int(x), int(y), board, True)
        if board is None:
            print("====== GAME OVER =====")
            break
        if is_complete(board):
            print("===== CLEAR! =====")
            break
        

if __name__ == "__main__":
    main()
