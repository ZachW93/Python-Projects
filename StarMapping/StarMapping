'''Project: Star Mapping

Problem Summary: Create a 2D plot star map using coordinates/magnitude from a 
TXT File. The solution must be graphed in a unit circle, coordinates will work.

Solution Thought Process: Understand the data that is given, the TXT file 
contains XYZ coordinates and magnitude. The Z coordinate can be ignored at position 
3 of the text file. Utilize python data manipulation and dictionaries to parse the data 
and seperate by coordinate and magnitude. Once coordinates are found, use
turtle graphics to plot the graph using x,y coordinates. Also, at the time of 
plotting, round the magnitude and test whether magnitude will be greater than 8
(or graph will be a large blob) and use the magnitude to graph a circle of the
same diameter as the magnitude.

@Author: Zach W
Last Date Modified: January 3rd, 2020 
'''



import turtle


def read_coords(filehandle):
    HDnumXY = {}  # Creating dictionaries for the tuple that we will set-up
    HDnumMag = {}
    NamesHDnum = {}
    input_filehandle = open(filehandle, "r")
    for line in input_filehandle:  # Going through eachline of code splitting
        split_line = line.split(" ")  # up the components of the file
        x = split_line[0]
        y = split_line[1]
        magnitude = split_line[4]
        HDnum = split_line[3]
        if len(split_line) >= 7:  # Checking which stars have names and saving
            names = split_line[6:]  # the names
            for i in names:  # stripping the /n off the names
                i = i.strip(" \n")
                NamesHDnum[i] = HDnum
        HDnumXY[HDnum] = [x, y]  # Creating the dicitonaries and the tuple
        HDnumMag[HDnum] = [magnitude]  # at the end
    return HDnumXY, HDnumMag, NamesHDnum
dict_tuple = read_coords('stars.txt')


def plot_plain_stars(picture_size, coordinates_dict):
    turtle.screensize(picture_size, picture_size)  # Creating the turtle
    turtle.bgcolor("black")
    for i in coordinates_dict:
        coords = coordinates_dict[i]  # taking the coordinates
        turtle.tracer(0)
        xcord = picture_size*float(coords[0])  # x-coordinate times size
        ycord = picture_size*float(coords[1])  # y-coordinate times size
        turtle.penup()
        turtle.setpos(xcord, ycord)
        turtle.pendown()
        turtle.pencolor("white")  # Creating the stars and position
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(1)
        turtle.right(90)
        turtle.forward(1)
        turtle.end_fill()

    turtle.exitonclick()

plot_plain_stars(400, dict_tuple[0])


def plot_by_magnitude(picture_size, coordinates_dict, magnitudes_dict):
    turtle.screensize(picture_size, picture_size)
    turtle.bgcolor("black")
    for i in magnitudes_dict:
        magns = magnitudes_dict[i][0]
        magns = float(magns)
        star_size = round(10.0/(magns+2))  # find the size of each star
        if star_size > 8:  # creating max size of 8 pixels
            star_size = 8
        else:
            star_size = star_size
        magnitudes_dict[i] = star_size
        coords = coordinates_dict[i]
        turtle.tracer(0)  # Using same arguments at previous function
        xcord = picture_size*float(coords[0])
        ycord = picture_size*float(coords[1])
        turtle.penup()
        turtle.setpos(xcord, ycord)
        turtle.pendown()
        turtle.pencolor("white")
        turtle.fillcolor("white")
        turtle.begin_fill()
        turtle.forward(magnitudes_dict[i])
        turtle.right(90)
        turtle.forward(magnitudes_dict[i])
        turtle.right(90)
        turtle.forward(magnitudes_dict[i])
        turtle.right(90)
        turtle.forward(magnitudes_dict[i])
        turtle.end_fill()
    turtle.exitonclick()

plot_by_magnitude(400, dict_tuple[0], dict_tuple[1])
