namespace SpriteKind {
    export const LeftPaddles = SpriteKind.create()
    export const RightPaddles = SpriteKind.create()
}

function create_ball() {
    
    ball = sprites.create(img`
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
    `, SpriteKind.Player)
    ball.setVelocity(100, 100)
    ball.setBounceOnWall(true)
    ball.y = Math.randomRange(0, 120)
}

function create_left_paddle() {
    
    left_paddle = sprites.create(img`
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
    `, SpriteKind.LeftPaddles)
    controller.moveSprite(left_paddle, 0, 150)
    left_paddle.setStayInScreen(true)
    left_paddle.left = 0
}

function create_right_paddle() {
    
    right_paddle = sprites.create(img`
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
    `, SpriteKind.RightPaddles)
    controller.player2.moveSprite(right_paddle, 0, 150)
    right_paddle.setStayInScreen(true)
    right_paddle.right = 160
}

let ball : Sprite = null
let right_paddle : Sprite = null
let left_paddle : Sprite = null
sprites.onOverlap(SpriteKind.Player, SpriteKind.LeftPaddles, function on_on_overlap() {
    ball.vx = ball.vx * -1
    info.changeScoreBy(1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.RightPaddles, function on_on_overlap_right() {
    ball.vx = ball.vx * -1
    info.player2.changeScoreBy(1)
})
create_ball()
create_left_paddle()
create_right_paddle()
