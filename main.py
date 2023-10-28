from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from scoreboard import scoreboard
scr= Screen()
scr.setup(width=600,height=600)
scr.bgcolor("black")
scr.title("SNAKE GAME")
scr.tracer(0)

snake = Snake()
food = Food()
scoreboard = scoreboard()


scr.listen()
scr.onkey(key="Up", fun=snake.up)
scr.onkey(key="Down", fun=snake.down)
scr.onkey(key="Left", fun=snake.left)
scr.onkey(key="Right", fun=snake.right)
game_is_on = True

while game_is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()


    #COLLISION WITH FOOD

    if snake.head.distance(food) < 15:
        scoreboard.increase_Score()
        snake.extend()
        food.refresh()

    #BORDER COLLISION
    if snake.head.xcor() > 290 or snake.head.xcor() <-290 or snake.head.ycor() > 290 or snake.head.ycor() <-290 :
        game_is_on = False


    #TAIL COLLISION
    k = len(snake.segments)
    for segment in range(1,k):
        if snake.head.distance(snake.segments[segment]) < 10:
          game_is_on = False
    '''for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
'''
scoreboard.game_over()
scr.exitonclick()