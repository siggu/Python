def solution(keyinput, board):
    width = int(board[0]//2)
    height = int(board[1]//2)
    x = 0
    y = 0
    
    for i in keyinput:
        if i == "left":
            x -= 1
        elif i == "right":
            x += 1
        elif i == "up":
            y += 1
        elif i == "down":
            y -= 1
    
        if x > width:
            x = width
        elif x < -width:
            x = -width

        if y > height:
            y = height
        elif y < -height:
            y = -height
    
    return [x, y]