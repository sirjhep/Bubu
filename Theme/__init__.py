#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Theme Module for Tkinter
Copyright 2015 Jephthah M. Orobia

This module simplify duplication of work with configuring style for each Tk Widget in an app even of the same type of Widget. The main objective of this module is to separate layout from coding. Much like what a css do.

All widgets in Tkinter are basically copied here. Except that in this module. You can modify those widgets' style and will be the global style for the respective widget that was modified. In that way, this will look work as if it's a CSS of an HTML.

To create specific styles, or special style, create another class which inherits this module's class of that widget type. Let's say for example you want to create 2 types of button, a red and a green:
    class RedButton(Button):
        ...some modification that turns the button to Red...
    
    class GreenButton(Button):
        ...some modification that turns the button to Green...
    
"""


import Tkinter

#### CONSTANTS ####
LEFT = Tkinter.LEFT
RIGHT = Tkinter.RIGHT
TOP = Tkinter.TOP
BOTTOM = Tkinter.BOTTOM
FLAT = Tkinter.FLAT
RAISED = Tkinter.RAISED
SUNKEN = Tkinter.SUNKEN
GROOVE = Tkinter.GROOVE
RIDGE = Tkinter.RIDGE
X = Tkinter.X
Y = Tkinter.Y
NW = Tkinter.NW
N = Tkinter.N
NE = Tkinter.NE
W = Tkinter.W
CENTER = Tkinter.CENTER
E = Tkinter.E
SW = Tkinter.SW
S = Tkinter.S
SE = Tkinter.SE



class Tk(Tkinter.Tk):
    pass

class Button(Tkinter.Button):
	#The Button widget is used to display buttons in your application.
    pass

class Canvas(Tkinter.Canvas):
	#The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.
    pass

class Checkbutton(Tkinter.Checkbutton):
	#The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.
    pass

class Entry(Tkinter.Entry):
	#The Entry widget is used to display a single-line text field for accepting values from a user.
    pass

class Frame(Tkinter.Frame):
	#The Frame widget is used as a container widget to organize other widgets.
    pass

class Label(Tkinter.Label):
	#The Label widget is used to provide a single-line caption for other widgets. It can also contain images.
    pass

class Listbox(Tkinter.Listbox):
	#The Listbox widget is used to provide a list of options to a user.
    pass

class Menubutton(Tkinter.Menubutton):
	#The Menubutton widget is used to display menus in your application.
    pass

class Menu(Tkinter.Menu):
	#The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.
    pass

class Message(Tkinter.Message):
	#The Message widget is used to display multiline text fields for accepting values from a user.
    pass

class Radiobutton(Tkinter.Radiobutton):
	#The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one    option at a time.
    pass

class Scale(Tkinter.Scale):
	#The Scale widget is used to provide a slider widget.
    pass

class Scrollbar(Tkinter.Scrollbar):
	#The Scrollbar widget is used to add scrolling capability to various widgets, such as list boxes.
    pass

class Text(Tkinter.Text):
	#The Text widget is used to display text in multiple lines.
    pass

class Toplevel(Tkinter.Toplevel):
	#The Toplevel widget is used to provide a separate window container.
    pass

class Spinbox(Tkinter.Spinbox):
	#The Spinbox widget is a variant of the standard Tkinter Entry widget, which can be used to select from a fixed number of values.
    pass

class PanedWindow(Tkinter.PanedWindow):
	#A PanedWindow is a container widget that may contain any number of panes, arranged horizontally or vertically.
    pass

class LabelFrame(Tkinter.LabelFrame):
	#A labelframe is a simple container widget. Its primary purpose is to act as a spacer or container for complex window layouts.
    pass