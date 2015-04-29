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
ACTIVE = 'active'
ALL = 'all'
ANCHOR = 'anchor'
ARC = 'arc'
BASELINE = 'baseline'
BEVEL = 'bevel'
BOTH = 'both'
BOTTOM = 'bottom'
BROWSE = 'browse'
BUTT = 'butt'
CASCADE = 'cascade'
CENTER = 'center'
CHAR = 'char'
CHECKBUTTON = 'checkbutton'
CHORD = 'chord'
COMMAND = 'command'
CURRENT = 'current'
DISABLED = 'disabled'
DOTBOX = 'dotbox'
E = 'e'
END = 'end'
EW = 'ew'
EXCEPTION = 8
EXTENDED = 'extended'
FALSE = 0
FIRST = 'first'
FLAT = 'flat'
GROOVE = 'groove'
HIDDEN = 'hidden'
HORIZONTAL = 'horizontal'
INSERT = 'insert'
INSIDE = 'inside'
LAST = 'last'
LEFT = 'left'
MITER = 'miter'
MOVETO = 'moveto'
MULTIPLE = 'multiple'
N = 'n'
NE = 'ne'
NO = 0
NONE = 'none'
NORMAL = 'normal'
NS = 'ns'
NSEW = 'nsew'
NUMERIC = 'numeric'
NW = 'nw'
OFF = 0
ON = 1
OUTSIDE = 'outside'
PAGES = 'pages'
PIESLICE = 'pieslice'
PROJECTING = 'projecting'
RADIOBUTTON = 'radiobutton'
RAISED = 'raised'
READABLE = 2
RIDGE = 'ridge'
RIGHT = 'right'
ROUND = 'round'
S = 's'
SCROLL = 'scroll'
SE = 'se'
SEL = 'sel'
SEL_FIRST = 'sel.first'
SEL_LAST = 'sel.last'
SEPARATOR = 'separator'
SINGLE = 'single'
SOLID = 'solid'
SUNKEN = 'sunken'
SW = 'sw'
StringTypes = (<type 'str'>, <type 'unicode'>)
TOP = 'top'
TRUE = 1
TclVersion = 8.5
TkVersion = 8.5
UNDERLINE = 'underline'
UNITS = 'units'
VERTICAL = 'vertical'
W = 'w'
WORD = 'word'
WRITABLE = 4
X = 'x'
Y = 'y'
YES = 1
__version__ = '$Revision: 81008 $'
wantobjects = 1



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