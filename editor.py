import tkinter as tk
from tkinter import ttk
from tkinter import messagebox , filedialog , colorchooser , font
import os

main_app = tk.Tk()
main_app.geometry('1920x1080')
main_app.title("New Editor")
main_app.wm_iconbitmap('icons/icon.ico')

main_menu = tk.Menu()
# File icons
new_icon = tk.PhotoImage(file="icons/new.png")
open_icon = tk.PhotoImage(file="icons/open.png")
save_icon = tk.PhotoImage(file="icons/save.png")
saveas_icon = tk.PhotoImage(file="icons/save_as.png")
exit_icon = tk.PhotoImage(file="icons/exit.png")

file = tk.Menu(main_menu , tearoff=False)

# Edit icons
copy_icon = tk.PhotoImage(file='icons/copy.png')
paste_icon = tk.PhotoImage(file='icons/paste.png')
cut_icon = tk.PhotoImage(file='icons/cut.png')
clearall_icon = tk.PhotoImage(file='icons/clear_all.png')
find_icon = tk.PhotoImage(file='icons/find.png')

Edit = tk.Menu(main_menu , tearoff=False)

# view icons
tool_bar_icon = tk.PhotoImage(file='icons/tool.png')
status_bar_icon = tk.PhotoImage(file='icons/status.png')

View = tk.Menu(main_menu , tearoff=False)

# color icons
white = tk.PhotoImage(file='icons/light_default.png')
white_plus = tk.PhotoImage(file='icons/light_plus.png')
dark = tk.PhotoImage(file='icons/dark.png')
red = tk.PhotoImage(file='icons/red.png')
monokai = tk.PhotoImage(file='icons/monokai.png')
blue = tk.PhotoImage(file='icons/night_blue.png')

# bold icon
bold_icon = tk.PhotoImage(file='icons/bold.png')

# italic icon
italic_icon = tk.PhotoImage(file='icons/italic.png')

# underline icon
underline_icon = tk.PhotoImage(file='icons/underline.png')

# font icon
font_icon = tk.PhotoImage(file='icons/font.png')

# align left icon
align_left_icon = tk.PhotoImage(file='icons/align_left.png')

# align right icon
align_right_icon = tk.PhotoImage(file='icons/align_right.png')

# align center icon
align_center_icon = tk.PhotoImage(file='icons/align_center.png')

Color = tk.Menu(main_menu , tearoff=False)
colors = ['#FCFBFB' , '#A19797' , '#070707' , '#E00D0D' , '#E0900D' , '#110DE0']

main_menu.add_cascade(label='File' , menu=file)
main_menu.add_cascade(label='Edit' , menu=Edit)
main_menu.add_cascade(label='View' , menu=View)
main_menu.add_cascade(label='Style' , menu=Color)

tool_bar = ttk.Label(main_app , background='#9D9DA4')
tool_bar.pack(side=tk.TOP , fill=tk.X)

fonts = tk.font.families()
font_family = tk.StringVar()
font_box = ttk.Combobox(tool_bar , width=30 , textvariable=font_family , state='readonly')
font_box['values'] = fonts
font_box.grid(row=0 , column=0 , padx=5)
font_box.current(fonts.index('Arial'))

size_var = tk.IntVar()
font_size = ttk.Combobox(tool_bar , width=6 , textvariable=size_var , state='readonly')
font_size['values'] = tuple(range(6 , 80 , 2))
font_size.grid(row=0 , column=1 , padx=5)
font_size.current(font_size.index(6))

bold_button = ttk.Button(tool_bar , image=bold_icon)
bold_button.grid(row=0 , column=2 , padx=5)

italic_button = ttk.Button(tool_bar , image=italic_icon)
italic_button.grid(row=0 , column=3 , padx=5)

underline_button = ttk.Button(tool_bar , image=underline_icon)
underline_button.grid(row=0 , column=4 , padx=5)

font_button = ttk.Button(tool_bar , image=font_icon)
font_button.grid(row=0 , column=5 , padx=5)

align_left_button = ttk.Button(tool_bar , image=align_left_icon)
align_left_button.grid(row=0 , column=6 , padx=5)

align_right_button = ttk.Button(tool_bar , image=align_right_icon)
align_right_button.grid(row=0 , column=7 , padx=5)

align_center_button = ttk.Button(tool_bar , image=align_center_icon)
align_center_button.grid(row=0 , column=8 , padx=5)

text_editor = tk.Text(main_app)
text_editor.config(wrap='word' , relief=tk.FLAT)
text_editor.pack(fill=tk.BOTH , expand=True)
text_editor.focus_set()
# scr_bar = tk.Scrollbar(main_app)
# scr_bar.pack(side=tk.RIGHT,fill=tk.Y)
# scr_bar.config(command=text_editor.yview)
# text_editor.config(yscrollcommand = scr_bar.set)

current_font_family = font_family.get()
current_font_size = size_var.get()


def change_font (event=None):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family , current_font_size))


def change_font_size (event=None):
    global current_font_family
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family , current_font_size))


font_box.bind("<<ComboboxSelected>>" , change_font)
font_size.bind("<<ComboboxSelected>>" , change_font_size)


def change_bold ():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family , size_var.get() , 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family , size_var.get() , 'normal'))


bold_button.configure(command=change_bold)


def change_italic ():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(font_family.get() , size_var.get() , 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(font_family.get() , size_var.get() , 'normal'))


italic_button.configure(command=change_italic)


def change_underline ():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(font_family.get() , size_var.get() , 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(font_family.get() , size_var.get() , 'normal'))


underline_button.configure(command=change_underline)


def change_fontcolor ():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])


font_button.configure(command=change_fontcolor)


def align_left ():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_configure('left' , justify=tk.LEFT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'left')


align_left_button.configure(command=align_left)


def align_center ():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_configure('center' , justify=tk.CENTER)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , tk.CENTER)


align_center_button.configure(command=align_center)


def align_right ():
    text_content = text_editor.get(1.0 , 'end')
    text_editor.tag_configure('right' , justify=tk.RIGHT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'right')


align_right_button.configure(command=align_right)

status_bar = ttk.Label(main_app , text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

text_changed = False


def changed (event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed = True
        words = len(text_editor.get(1.0 , 'end-1c').split())
        characters = len(text_editor.get(1.0 , 'end-1c').replace(' ' , ''))
        status_bar.config(text=f"characters:{characters}  Words:{words}")
    text_editor.edit_modified(False)


text_editor.bind("<<Modified>>" , changed)

url = ''


def new_file (event=None):
    global url
    url = ''
    text_editor.delete(1.0 , 'end')


file.add_command(label="New" , image=new_icon , compound=tk.LEFT , accelerator='Ctrl+N' , command=new_file)


def open_file (event=None):
    global url
    url = filedialog.askopenfilename(initialdir=os.getcwd() , title="Open file" ,
                                     filetypes=(('Text File' , '*.txt') , ('All Files' , '*.*')))
    try:
        with open(url , 'r') as fr:
            text_editor.delete(1.0 , 'end')
            text_editor.insert(1.0 , fr.read())
    except FileNotFoundError:
        return
    except:
        return
    main_app.title = os.path.basename(url)


file.add_command(label="Open" , image=open_icon , compound=tk.LEFT , accelerator='Ctrl+O' , command=open_file)


def save_file (event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0 , 'end'))
            with open(url , 'w' , encoding='UTF-8') as fw:
                fw.write(content)
        else:
            url = filedialog.asksaveasfile(mode='w' , defaultextension='.txt' ,
                                           filetypes=(('Text File' , '*.txt') , ('All files' , '*.*')))
            content2 = text_editor.get(1.0 , 'end')
            url.write(content2)
            url.close()
    except:
        return


file.add_command(label="Save" , image=save_icon , compound=tk.LEFT , accelerator='Ctrl+S' , command=save_file)


def save_as_file (event=None):
    global url
    try:
        content = text_editor.get(1.0 , 'end')
        url = filedialog.asksaveasfile(mode='w' , defaultextension='.txt' ,
                                       filetypes=(('Text File' , '*.txt') , ('All files' , '*.*')))
        url.write(content)
        url.close()
    except:
        return


file.add_command(label="Save As" , image=saveas_icon , compound=tk.LEFT , accelerator='Ctrl+Alt+S' ,
                 command=save_as_file)


def exit_file (event=None):
    global url , text_changed
    try:
        if text_changed:
            mbox = messagebox.askyesnocancel('Warning' , 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content = text_editor.get(1.0 , 'end')
                    with open(url , 'w') as fw:
                        fw.write(content)
                        main_app.destroy()
                else:
                    content2 = text_editor.get(1.0 , 'end')
                    url = filedialog.asksaveasfile(mode='w' , defaultextension='.txt' ,
                                                   filetypes=(('Text File' , '*.txt') , ('All files' , '*.*')))
                    url.write(content2)
                    url.close()
            elif mbox is False:
                main_app.destroy()
        else:
            main_app.destroy()
    except:
        return


def find_box (event=None):
    def find ():
        word = text_find_entry.get()
        text_editor.tag_remove('match' , 1.0 , 'end')
        matches = 0
        if word:
            start_pos = 1.0
            while True:
                start_pos = text_editor.search(word , start_pos , stopindex=tk.END)
                if not start_pos:
                    break
                end_pos = f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match' , start_pos , end_pos)
                matches += 1
                start_pos = end_pos
                text_editor.tag_config('match' , foreground='yellow' , background='#000000')

    def replace ():
        word = text_find_entry.get()
        replace_text = text_replace_entry.get()
        content = text_editor.get(1.0 , tk.END)
        new_content = content.replace(word , replace_text)
        text_editor.delete(1.0 , tk.END)
        text_editor.insert(1.0 , new_content)

    find_dialog = tk.Toplevel()
    find_dialog.configure(background="blue")
    find_dialog.geometry('450x250+500+200')
    find_dialog.title('Find')
    find_dialog.resizable(0 , 0)
    find_frame = ttk.Labelframe(find_dialog , text='Find/Replace')
    find_frame.pack(pady=20)

    text_find_label = ttk.Label(find_frame , text='Find: ')
    text_replace_label = ttk.Label(find_frame , text='Replace: ')
    text_find_label.grid(row=0 , column=0 , padx=20 , pady=20)
    text_replace_label.grid(row=1 , column=0 , padx=20 , pady=20)

    text_find_entry = ttk.Entry(find_frame , width=30)
    text_replace_entry = ttk.Entry(find_frame , width=30)
    text_find_entry.grid(row=0 , column=1)
    text_replace_entry.grid(row=1 , column=1)

    find_button = ttk.Button(find_frame , text='Find' , width=12 , command=find)
    find_button.grid(row=2 , column=0 , padx=20)

    replace_button = ttk.Button(find_frame , text='Replace' , width=12 , command=replace)
    replace_button.grid(row=2 , column=1 , padx=20)

    find_dialog.mainloop()


file.add_command(label="Exit" , image=exit_icon , compound=tk.LEFT , accelerator='Ctrl+Q' , command=exit_file)

Edit.add_command(label="Copy" , image=copy_icon , compound=tk.LEFT , accelerator='Ctrl+C' ,
                 command=lambda: text_editor.event_generate("<Control c>"))
Edit.add_command(label="Paste" , image=paste_icon , compound=tk.LEFT , accelerator='Ctrl+V' ,
                 command=lambda: text_editor.event_generate("<Control v>"))
Edit.add_command(label="Cut" , image=cut_icon , compound=tk.LEFT , accelerator='Ctrl+X' ,
                 command=lambda: text_editor.event_generate("<Control x>"))
Edit.add_command(label="Clear All" , image=clearall_icon , compound=tk.LEFT , accelerator='Ctrl+Alt+C' ,
                 command=lambda: text_editor.delete(1.0 , 'end'))

Edit.add_command(label="Find" , image=find_icon , compound=tk.LEFT , accelerator='Ctrl+F' , command=find_box)

show_tool = tk.BooleanVar()
show_tool.set(True)
show_status = tk.BooleanVar()
show_status.set(True)


def hide_toolbar (event=None):
    global show_tool
    if show_tool is True:
        tool_bar.pack_forget()
        show_tool = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP , fill=tk.X)
        text_editor.pack(fill=tk.BOTH , expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool = True


def hide_statusbar (event=None):
    global show_status
    if show_status:
        status_bar.pack_forget()
        show_status = False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status = True


View.add_checkbutton(label='Tool Bar' , image=tool_bar_icon , variable=show_tool , compound=tk.LEFT ,
                     command=hide_toolbar)
View.add_checkbutton(label='Status Bar' , image=status_bar_icon , variable=show_status , compound=tk.LEFT ,
                     command=hide_statusbar)

Color.add_command(label='White' , image=white , compound=tk.LEFT , command=lambda: text_editor.configure(bg=colors[0]))
Color.add_command(label='Grey' , image=white_plus , compound=tk.LEFT ,
                  command=lambda: text_editor.configure(bg=colors[1]))
Color.add_command(label='Dark' , image=dark , compound=tk.LEFT ,
                  command=lambda: text_editor.configure(bg=colors[2] , fg='white'))
Color.add_command(label='Red' , image=red , compound=tk.LEFT , command=lambda: text_editor.configure(bg=colors[3]))
Color.add_command(label='Orange' , image=monokai , compound=tk.LEFT ,
                  command=lambda: text_editor.configure(bg=colors[4]))
Color.add_command(label='Night Blue' , image=blue , compound=tk.LEFT ,
                  command=lambda: text_editor.configure(bg=colors[5] , fg='white'))

main_app.config(menu=main_menu)
main_app.bind("<Control-n>",new_file)
main_app.bind("<Control-o>",open_file)
main_app.bind("<Control-s>",save_file)
main_app.bind("<Control-Alt-s>",save_as_file)
main_app.bind("<Control-q>",exit_file)
main_app.mainloop()
