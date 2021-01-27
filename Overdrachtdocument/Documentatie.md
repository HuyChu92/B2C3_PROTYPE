CLASSES
    tkinter.Tk(tkinter.Misc, tkinter.Wm)
        Mainframe

    class Mainframe(tkinter.Tk)
     |  Een 'MainFrame' object dat geinstantieerd wordt met tk.TK.
     |  Dit dient als venster van het programma en vanuit dit venster
     |  kan er genavigeerd worden
     |
     |  Method resolution order:
     |      Mainframe
     |      tkinter.Tk
     |      tkinter.Misc
     |      tkinter.Wm
     |      builtins.object
     |
     |  Methods defined here:
     |
     |  __init__(self)
     |      Return a new Toplevel widget on screen SCREENNAME. A new Tcl interpreter will
     |      be created. BASENAME will be used for the identification of the profile file (see
     |      readprofile).
     |      It is constructed from sys.argv[0] without extensions if None is given. CLASSNAME
     |      is the name of the widget class.
     |
     |  change(self, frame)
     |      Verandert frame o.b.v. ingevoerde frame
     |
     |  start(self)
     |      Keert terug naar startscherm als er op start gedrukt wordt
     |
     |  ----------------------------------------------------------------------