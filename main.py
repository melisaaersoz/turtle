import turtle
import random


turtle_board = turtle.Screen()
turtle_board.bgcolor("Light Blue")
turtle_board.title("Python Turtle Graphics")


FONT=("Arial", 12, "normal")

score=0

game_over=False

score_turtle = turtle.Turtle()
def score_turtle_start():
    score_turtle.hideturtle()
    score_turtle.penup()
    top_height = turtle_board.window_height() / 2
    y = top_height * 0.9
    score_turtle.setposition(0,y)
    score_turtle.write(arg="Score:0", move=False, align="center", font=FONT)

grid_size=10
turtle_list=[]

def make_turtle(x,y):
    turtle_instance = turtle.Turtle()

    def handle_click(x,y):
        global score
        #print(x,y)
        score+=1
        score_turtle.clear()  #skorları yazdırırken hepsinin ekranda görünmemesi için score arttıkça önceki skor silinir yenii yazılır
        score_turtle.write(arg=f"Score:{score}", move=False, align="center", font=FONT)

    turtle_instance.onclick(handle_click)

    turtle_instance.penup()
    turtle_instance.shapesize(3,3)
    turtle_instance.color("green")
    turtle_instance.shape("turtle")
    turtle_instance.goto(x*grid_size,y*grid_size)
    turtle_list.append(turtle_instance)


turtle_x_coordinates=[20,10,0,-10,-20]
turtle_y_coordinates=[20,10,0,-10,-20]

def turtle_setup():
    for x in turtle_x_coordinates:
        for y in turtle_y_coordinates:
            make_turtle(x,y)

def hide_turtle():
     for turtle_instance in turtle_list:
        turtle_instance.hideturtle()


#recursive func
def show_random_turtles():
    if not game_over:
        hide_turtle()
        random.choice(turtle_list).showturtle()
        turtle_board.ontimer(show_random_turtles,500)


countdown_turtle = turtle.Turtle()
def countdown(time):
    global game_over
    countdown_turtle.hideturtle()
    countdown_turtle.penup()
    top_height = turtle_board.window_height() / 2
    y = top_height * 0.9
    countdown_turtle.setposition(0,y-30)
    countdown_turtle.clear()
    if time>0:
        countdown_turtle.clear()
        countdown_turtle.write(arg=f"Game Time: {time}", move=False, align="center", font=FONT)
        turtle_board.ontimer(lambda : countdown(time-1),1000)

    else:
        game_over=True
        countdown_turtle.clear()
        hide_turtle()
        countdown_turtle.write(arg="Game Over!", move=False, align="center", font=FONT)



def game_start_def():
    turtle.tracer(0)
    turtle_setup()
    score_turtle_start()
    countdown(10)
    hide_turtle()
    show_random_turtles()
    turtle.tracer(1)

game_start_def()
turtle.mainloop()
#tracer 0 yapıp işlemler bittikten sonra 1 yaparsak açtığımız anda turtlelar istediğimiz konumda olurlar.