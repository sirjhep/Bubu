from Theme import *
from Utopia import Utopia

class MyApp:
  def __init__(self, title, icon=False, geometry=False):
    
    # configure main window
    self.root = Tk()
    self.root.title(title)
    self.root.config()
    
    if icon:
      self.root.iconbitmap(icon)
    
    if geometry:
      self.root.geometry(geometry)
    else:
      self.root.geometry("350x250+{0}+{1}".format(
                                    self.root.winfo_screenwidth()/2 - 200,
                                    self.root.winfo_screenheight()/2 - 150))
    
    # loads the login page
    self.load_login(self.root)

  def init(self):
    self.root.mainloop()
  
  def report(self, message):
    pass
  
  def alert(self, message):
    pass

  def load_login(self, tobeparent):
    self.login_form = Frame(tobeparent)
    self.login_form.pack()
    self.login_header = Label(self.login_form, font=("Consolas", 20, 'bold'), text="Bubu", pady=20)
    self.login_header.grid(columnspan=2, pady=5)
    self.username_label = Label(self.login_form, text="Username:")
    self.username_label.grid(row=1, pady=5)
    self.username_form = Entry(self.login_form)
    self.username_form.grid(row=1,column=1, pady=5)
    self.username_form.bind("<Return>", self.login)
    self.password_label = Label(self.login_form, text="Password:")
    self.password_label.grid(row=2, pady=5)
    self.password_form = Entry(self.login_form, show="*")
    self.password_form.grid(row=2, column=1, pady=5)
    self.password_form.bind("<Return>", self.login)
    self.login_button = Button(self.login_form, text="Log In", command=self.login)
    self.login_button.grid(row=3, columnspan=2, pady=5)
    self.login_button.bind("<Return>", self.login)
    self.login_message = Label(self.login_form)
    self.login_message.grid(row=4, columnspan=2, pady=5)

  def login(self, event=None):
    
    usr = self.username_form.get()
    pwd = self.password_form.get()
    
    if(usr != "" and pwd != ""):
      self.uto = Utopia(usr, pwd)
      res = self.uto.login()
      if res:
        self.login_form.destroy()
        self.load_main()
      else:
        self.login_message.config(bg='pink', fg='white', text="Failed to Log-In, possible reasons:\n- Incorrect Username or Password.\n- No Internet Connection.")
    else:
      self.login_message.config(bg='pink', fg='white', text="You must provide your\nusername and password first!")
  
  def load_main(self):
    
    #maximize the window
    self.root.wm_state('zoomed')
    
    #load menu
    self.load_menu()
    
    # Frames to hold columns.
    self.col1 = Frame(self.root, borderwidth=2, pady=5, padx=5, bg="white")
    self.col1.pack(side=LEFT, fill=Y)
    self.col2 = Frame(self.root, borderwidth=2, pady=5, padx=5, bg="white")
    self.col2.pack(side=LEFT, fill=Y)
    self.col3 = Frame(self.root, borderwidth=2, pady=5, padx=5, bg="white")
    self.col3.pack(side=LEFT, fill=Y)
    self.col4 = Frame(self.root, borderwidth=2, pady=5, padx=5, bg="white")
    self.col4.pack(side=LEFT, fill=Y)
    
    #From left to right
    Label(self.col1, text="Scheduled Task", font=("Consolas", 14, "bold")).pack()
    Label(self.col2, text="News", font=("Consolas", 14, "bold")).pack()
    Label(self.col3, text="Build Presets", font=("Consolas", 14, "bold")).pack()
    Label(self.col4, text="Province Info", font=("Consolas", 14, "bold")).pack()
    
    #col4 content
    self.uto.update_sot();
    for info in self.uto.sot:
      Label(self.col4, text=info + ": "+ str(self.uto.sot[info]), font=("Consolas", 11, "bold")).pack()
    
  
  def load_menu(self):
    #Set Up Menu
    self.menu = Menu(self.root)
    
    # First Level Menu
    self.user_menu = Menu(self.menu)
    self.sch_menu = Menu(self.menu)
    self.coun_menu = Menu(self.menu)
    self.win_menu = Menu(self.menu)
    self.help_menu = Menu(self.menu)
    
    # User Menu
    self.user_menu.add_command(label="Prov News")
    self.user_menu.add_command(label="KD News")
    self.user_menu.add_command(label="Log-Out", command=self.logout)
    self.user_menu.add_separator()
    self.user_menu.add_command(label="Exit", command=self.root.quit)
    
    # Schedule Menu
    self.coun_menu.add_command(label="Add...")
    
    # Council Menu
    self.coun_menu.add_command(label="State")
    self.coun_menu.add_command(label="Military")
    self.coun_menu.add_command(label="Buildings")
    self.coun_menu.add_command(label="Science")
    self.coun_menu.add_command(label="Mystics")
    
    # Windows
    self.win_menu.add_command(label="Automation")
    
    # Help
    self.help_menu.add_command(label="About")
    
    
    # Attaches menu to menu to root
    self.root.config(menu=self.menu)
    self.menu.add_cascade(label="Account["+self.uto.user+"]", menu=self.user_menu)
    self.menu.add_cascade(label="Council", menu=self.coun_menu)
    self.menu.add_cascade(label="Schedule", menu=self.sch_menu)
    self.menu.add_cascade(label="Windows", menu=self.win_menu)
    self.menu.add_cascade(label="Help", menu=self.help_menu)
    
  def logout(self):
    res = self.uto.logout()
    if res:
      self.menu.destroy()
      self.col1.destroy()
      self.col2.destroy()
      self.col3.destroy()
      self.col4.destroy()
      self.load_login(self.root)
      self.login_message.config(bg="green", fg="white", text="You have log-out...")
    else:
      self.alert("Failed to Log-out, check Internete connection")
