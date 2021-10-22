@namespace
class SpriteKind:
    LeftPaddles = SpriteKind.create()
    RightPaddles = SpriteKind.create()

def create_ball(): 
    global ball
    ball = sprites.create(img("""
        . . . . . b b b b b b . . . . .
        . . . b b 9 9 9 9 9 9 b b . . .
        . . b b 9 9 9 9 9 9 9 9 b b . .
        . b b 9 d 9 9 9 9 9 9 9 9 b b .
        . b 9 d 9 9 9 9 9 1 1 1 9 9 b .
        b 9 d d 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 d 9 9 9 9 9 9 1 1 1 9 9 9 b
        b 9 3 9 9 9 9 9 9 9 9 9 1 9 9 b
        b 5 3 d 9 9 9 9 9 9 9 9 9 9 9 b
        b 5 3 3 9 9 9 9 9 9 9 9 9 d 9 b
        b 5 d 3 3 9 9 9 9 9 9 9 d d 9 b
        . b 5 3 3 3 d 9 9 9 9 d d 5 b .
        . b d 5 3 3 3 3 3 3 3 d 5 b b .
        . . b d 5 d 3 3 3 3 5 5 b b . .
        . . . b b 5 5 5 5 5 5 b b . . .
        . . . . . b b b b b b . . . . .
    """), SpriteKind.player)
    ball.set_velocity(100, 100)
    ball.set_bounce_on_wall(True)
    ball.y = Math.random_range(0, 120) 

def create_left_paddle(): 
    global left_paddle
    left_paddle = sprites.create(img("""
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
    """), SpriteKind.LeftPaddles)
    controller.move_sprite(left_paddle, 0, 150)
    left_paddle.set_stay_in_screen(True)
    left_paddle.left = 0  

def create_right_paddle():
    global right_paddle
    right_paddle = sprites.create(img("""
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
        . . . . . . 3 3 3 3 . . . . . .
    """), SpriteKind.RightPaddles)
    controller.player2.move_sprite(right_paddle, 0, 150)
    right_paddle.set_stay_in_screen(True)
    right_paddle.right = 160 

ball: Sprite = None
right_paddle: Sprite = None
left_paddle: Sprite = None

def on_on_overlap():
    ball.vx = ball.vx * -1
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.LeftPaddles, on_on_overlap)

def on_on_overlap_right():
    ball.vx = ball.vx * -1
    info.player2.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.RightPaddles, on_on_overlap_right)

create_ball() 
create_left_paddle() 
create_right_paddle()