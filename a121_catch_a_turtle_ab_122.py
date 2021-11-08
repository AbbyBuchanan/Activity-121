# a121_catch_a_turtle_customized.py
#-----import statements-----
import turtle as trtl
import random as rand
import leaderboard as lb

#-----game configuration----
spot_shape = "circle"
font_setup = ("comic sans MS", 20, "normal")
score = 0
timer = 5
counter_interval = 1000   
timer_up = False
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "pink", "grey"]
sizes = [1.5, 1.75, 2, 2.25, 2.5, 2.75, 3]
leaderboard_file_name = "a122_leaderboard.y=txt"
leader_names_list = []
leader_scores_list = []
player_name = input("give name now: ")


#-----initialize turtle-----
spot = trtl.Turtle()
score_writer = trtl.Turtle()
counter =  trtl.Turtle()
spot.shape(spot_shape)
score_writer.penup()
score_writer.goto(250,275)
counter.penup()
counter.goto(-275,275)

#-----game functions--------
spot.penup()
def update_score():
  global score
  score += 1
  score_writer.clear()
  score_writer.write(score, font=font_setup)
def spot_clicked(x,y):
  global timer_up
  if (not timer_up):
    update_score()
    change_position()
    change_color()
    change_size()
  else:
    spot.hideturtle
def change_position():
  new_xpos = rand.randint(-200,200)
  new_ypos = rand.randint(-150,150)
  spot.goto(new_xpos,new_ypos)
def change_color():
  the_color = rand.choice(colors)
  spot.fillcolor(the_color)
  spot.stamp
def change_size():
  new_size = rand.choice(sizes)
  spot.shapesize(new_size)
def countdown():
  global timer, timer_up
  counter.clear()
  if timer <= 0:
    counter.write("Time's Up", font=font_setup)
    timer_up = True
    manage_leaderboard()
  else:
    counter.write("Timer: " + str(timer), font=font_setup)
    timer -= 1
    counter.getscreen().ontimer(countdown, counter_interval)

# manages the leaderboard for top 5 scorers
def manage_leaderboard():
  
  global leader_scores_list
  global leader_names_list
  global score
  global spot

  # load all the leaderboard records into the lists
  lb.load_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list)

  # TODO
  if (len(leader_scores_list) < 5 or score > leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(leader_names_list, leader_scores_list, True, spot, score)

  else:
    lb.draw_leaderboard(leader_names_list, leader_scores_list, False, spot, score)

#-----events----------------
wn = trtl.Screen()
spot.onclick(spot_clicked)
wn.ontimer(countdown, counter_interval)
wn.bgcolor("grey")
wn.mainloop()