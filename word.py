from guizero import App, TextBox, PushButton, Box, Combo, Slider, Waffle, CheckBox, MenuBar

# all deffs there
def save_file():
    global text_ent
    save_dir = app.select_file(save=True)
    if len(save_dir) > 0:
        save = open(save_dir, "wt", encoding="UTF-8", )
        save.write(editor.value)
        save.close()
#    save_button.disable()
def open_file():
    global text_ent
    open_dir = app.select_file(filetypes=[["TXT", "txt"]])
    if len(open_dir) > 0:
        fil = open(open_dir, encoding="UTF-8")
        editor.value = fil.read()
        fil.close()

def exit_app():
    app.destroy()

def font_visible():
    font.visible = True

def size_visible():
    size.visible = True

def change_font():
    editor.font = font.value
    #font.show

def change_text_size():
    editor.text_size = size.value
    # resize the widget because if the text is made bigger, this might affect the size of the TextBox so guizero needs to know how to maintain the intended layout
    editor.resize(1, 1)
    editor.resize("fill", "fill")

def text_color_black():
    editor.text_color = "black"

def text_color_green():
    editor.text_color = "green"

def text_color_blue():
    editor.text_color = "blue"

def text_color_yellow():
    editor.text_color = "yellow"

def text_color_red():
    editor.text_color = "red"

def text_color_purple():
    editor.text_color = "purple"



app = App(title="texteditor")
app.font="Futura"




menubar = MenuBar(app,
                    toplevel=["File","Options"],
                    options=[[["open",open_file],["save",save_file],["close editor",exit_app]],
                    [["font",font_visible], ["size", size_visible]]])



preferences_controls = Box(app, align="top", width="fill", border=True)

font = Combo(preferences_controls, options=["courier", "times new roman", "verdana", "futura"], align="left", command=change_font)
font.hide()

size = Slider(preferences_controls,  align="left", command=change_text_size, start=10, end=40)
size.hide()
#Colors

color_txt = PushButton(preferences_controls,  align="left", command=change_text_size, text=" ")
color_txt.bg = "black"

color_txt1 = PushButton(preferences_controls,  align="left", command=change_text_size, text=" ")
color_txt1.bg = "green"

color_txt2 = PushButton(preferences_controls,  align="left", command=change_text_size, text=" ")
color_txt2.bg = "blue"

color_txt3 = PushButton(preferences_controls,  align="left", command=change_text_size, text=" ")
color_txt3.bg = "yellow"

color_txt4 = PushButton(preferences_controls,  align="left", command=change_text_size, text=" ")
color_txt4.bg = "red"

color_txt5 = PushButton(preferences_controls,  align="left", command=text_color_purple, text=" ")
color_txt5.bg = "purple"



# create a box to house the controls, we want the box to span the entire width of the app###################################
file_controls = Box(app, align="top", width="fill")

# create a TextBox for the file name
file_name = TextBox(file_controls, text="text_file.txt", width=50, align="left")

# create a save button which uses the save_file function###################################
#save_button = PushButton(file_controls, text="Save", command=save_file,  align="right")

# create an open button which uses the open_file function###################################
#open_button = PushButton(file_controls, text="Open", command=open_file,  align="right")

# create a TextBox which is not in the box and fills the rest of the GUI###################################
box1 = Box(app, height="fill", width="fill")
editor = TextBox(box1, multiline=True, height="fill", width="fill")


def Dark_Th():
    running = True
    box1.bg = "black"
    while running == True:

        if Dark_mode.value == 1:
            box1.bg = "black"
            box1.text_color = "white"
            running = False

        else:
            box1.bg = "white"
            box1.text_color = "black"
            running = False

    return box1.bg

Dark_mode = CheckBox(preferences_controls, align="right", text="Dark mode", command=Dark_Th)


#Dark_mode.when_left_button_pressed = color_txt.hide
#Dark_mode.when_right_button_pressed = color_txt.show


color_txt.when_left_button_pressed = text_color_black
color_txt1.when_left_button_pressed = text_color_green
color_txt2.when_left_button_pressed = text_color_blue
color_txt3.when_left_button_pressed = text_color_yellow
color_txt4.when_left_button_pressed = text_color_red
color_txt5.when_left_button_pressed = text_color_purple

app.display()
