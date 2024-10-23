#sky
size (700, 700)
background (123, 186, 240)


#water
strokeWeight (300)
stroke (199, 235, 252)
line (0, 450, 900, 450)


#sand
strokeWeight (900)
stroke (242, 233, 179)
line (0, 900, 900, 900)

strokeWeight (10)
stroke (222, 239, 247)
line (0, 450, 7000, 450)


#beachtowels
# first two numbers are position, second two are size
# must be positioned less than 480
stroke (240, 119, 232)
fill (240, 119, 232)
rect (550, 500, 90, 150)

stroke (51, 121, 24)
fill (122, 209, 112)
rect (400, 550, 70, 140)

stroke (209, 112, 142)
fill (209, 112, 142)
rect (300, 480, 70, 100)

stroke (150, 103, 255)
fill (186, 156, 250)
rect (50, 500, 70, 150)

stroke (203, 126, 74)
fill (222, 167, 130)
rect (130, 500, 70, 150)


#sun
stroke (252, 252, 36)
fill (252, 252, 36)
circle (0, 0, 300)


#sunrays
strokeWeight (10)
stroke (252, 252, 36)
line (0, 0, 10, 200)
line (0, 0, 30, 200)
line (0, 0, 50, 200)
line (0, 0, 70, 200)
line (0, 10, 90, 200)
line (0, 10, 110, 200)
line (0, 20, 150, 150)
line (0, 10, 160, 100)
line (0, 10, 190, 150)
line (0, 0, 110, 150)
line (0, 10, 150, 150)
line (0, 0, 230, 100)
#line (0, 10, 160, 180)
line (0, 0, 250, 130)
line (0, 10, 215, 60)
line (0, 10, 250, 0)
line (0, 10, 250, 30)


#umbrella
#arc(x, y width, height, radians (startangle), radians (end angle));
strokeWeight (10)
stroke (0, 0, 0)
line (500, 600, 500, 450)
stroke (255, 194, 72)
fill (255, 194, 72)
#circle (500, 450, 70)
arc(500, 450, 150, 150, radians(180), radians(360));

strokeWeight (10)
stroke (0, 0, 0)
line (125, 450, 125, 550)
stroke (255, 194, 72)
fill (255, 194, 72)
#circle (125, 450, 70)
arc(125, 450, 150, 150, radians(180), radians(360));


#esky
stroke (0, 0, 0)
strokeWeight (5)
fill (66, 48, 240)
rect (230, 610, 70, 60)

stroke (0, 0, 0)
strokeWeight (4)
fill (245, 245, 245)
rect (230, 610, 70, 10)

stroke (0, 0, 0)
fill (245, 245, 245)
strokeWeight (4)
rect (229, 580, 10, 30)

stroke (0, 0, 0)
fill (245, 245, 245)
strokeWeight (4)
rect (290, 580, 10, 30)

stroke (0, 0, 0)
fill (245, 245, 245)
strokeWeight (4)
rect (240, 580, 50, 9)


#beer
stroke (74,43,3)
fill (74,43,3)
strokeWeight (1)
rect (240, 630, 8, 30)

stroke (74,43,3)
fill (74,43,3)
strokeWeight (1)
rect (260, 630, 8, 30)

stroke (74,43,3)
fill (74,43,3)
strokeWeight (1)
rect (280, 630, 8, 30)


#clouds
stroke (255, 255, 255)
fill (255, 255, 255)

circle (300, 100, 70)
circle (330, 90, 80)
circle (350, 80, 70)
circle (370, 110, 80)

circle (500, 100, 70)
circle (530, 90, 80)
circle (550, 80, 70)
circle (570, 110, 80)


#shark
fill (113, 113, 117)
stroke (113, 113, 117)
#first two = bottom left, next 2= top, last 2 = bottom right
triangle(399, 370, 300, 370, 420, 330)


#BOAT
#arc(x, y width, height, radians (startangle), radians (end angle));
strokeWeight (10)
stroke (126, 120, 85)
fill (126, 120, 85)
arc(200, 310, 150, 100, radians(0), radians(180));
strokeWeight (10); stroke (0, 0, 0); line (200, 310, 200, 210)
fill (255,0,0); stroke (255,0,0); rect (200, 200, 80, 40)
#strokeWeight (5), stroke (0, 0, 0), line (150, 150, 170, 170)
