# courses = ['History', 'Math', 'Literature', 'Physics', 'Programming', 'Math']
# numbers = {1, 5, 6, 8, 3, 4, 2}
#
# for subject in courses:
#     print(subject)
#
#
# for .index, subject in enumerate

from turtle import *
setup(300, 200) # akna mõõtmed
bgcolor("lightblue") # akna põhja värv
# auto kere (kolmnurga) joonistamine
penup(); setpos(-100,0); pensize(3)
pencolor("black"); fillcolor("red")
begin_fill() # alusta täitmist
pendown(); forward(200); left(90)
forward(60) ; setpos(-100, 0)
end_fill() # lõpeta täitmine
# ratta (täidetud ringi) joonistamine
setpos(-60, 0) # pliiats ringi algpunkti
color('black', 'yellow'); pensize(15)
begin_fill(); circle(10); end_fill()
# teise ratta joonistamine
penup(); setpos(120,0); pendown()
begin_fill(); circle(25); end_fill()
# teksti kirjutamine graafikaaknasse
penup(); setpos(-70, -50) # teksti algus
pencolor('black')
write ("My super car", font = ('Arial', 14) )
home() # koju – akna keskpunkti (0, 0)
left(90); backward(13) # vasakule, alla
mainloop() # graafikaaken ooteseisu
