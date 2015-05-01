# encoding: utf-8
import Tkinter
import ScrolledText
import json
directory = 'materials'
my_tk = Tkinter.Tk()
# реакция на кнопку
def button_clicked():
    my_txt.delete("1.0", Tkinter.END)
    my_txt_small.delete("1.0", Tkinter.END)
    with open(directory + '/' + str(my_Entry.get())) as data_file:
        data = json.load(data_file)
    my_txt.insert(Tkinter.END, data['text'])
    my_txt_small.insert(Tkinter.END, 'id:' + str(data['id']) + '\n' + 'positive:' + str(data['positive']) + '\n' + 'sarcasm:' + str(data['sarcasm']))


def event_info1(event):
    my_txt.delete("1.0", Tkinter.END)
    my_txt_small.delete("1.0", Tkinter.END)
    with open(directory + '/' + str(my_Entry.get())) as data_file:
        data = json.load(data_file)
    my_txt.insert(Tkinter.END, data['text'])
    my_txt_small.insert(Tkinter.END, 'id:' + str(data['id']) + '\n' + 'positive:' + str(data['positive']) + '\n' + 'sarcasm:' + str(data['sarcasm']))

def event_info2(event):
    my_Entry.focus_force()



my_frame_1 = Tkinter.Frame(my_tk, width=300, height=50)
my_frame_1.pack(side=Tkinter.TOP, fill=Tkinter.BOTH)

my_frame_2 = Tkinter.Frame(my_tk, width=300, height=50)
my_frame_2.pack(side=Tkinter.TOP, fill=Tkinter.BOTH)

my_txt = ScrolledText.ScrolledText(my_frame_1, )
my_txt.pack(fill=Tkinter.BOTH)

my_Entry = Tkinter.Entry(my_frame_2)
my_Button = Tkinter.Button(my_frame_2, text="Посмотреть", width=25, height=25, command=button_clicked)
my_txt_small = ScrolledText.ScrolledText(my_frame_2, width=50, height=25)

my_Entry.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
my_Button.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
my_txt_small.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)

my_Entry.bind("<Return>", event_info1)
my_tk.bind("<Down>", event_info2)

my_tk.mainloop()


