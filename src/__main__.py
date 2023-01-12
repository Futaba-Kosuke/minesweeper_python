from typing import List, TypedDict, Any
import random
import pprint

CellType = TypedDict("CellType", {
    "is_open": bool,
    "is_mine": bool
})


def init_board(cell_quantity: int, mine_quantity: int) -> List[List[CellType]]:
    board: List[List[CellType]] = []
    for i in range(0, cell_quantity):
        board.append([])
        for j in range(0, cell_quantity):
            board[i].append({
                "is_open": False,
                "is_mine": False
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

def main() -> None:
    cell_quantity = int(input("マス数 >> "))
    mine_quantity = int(input("爆弾の個数 >> "))

    board = init_board(cell_quantity=cell_quantity, mine_quantity=mine_quantity)
    
    pprint.pprint(board)


if __name__ == "__main__":
    main()
