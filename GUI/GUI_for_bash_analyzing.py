# encoding: utf-8
import Tkinter
import ScrolledText
import json
initial_directory = 'materials'
result_directory = 'results'
my_tk = Tkinter.Tk()

# реакция на кнопку


def event_info1(event):
    my_txt1.delete("1.0", Tkinter.END)
    my_txt_small.delete("1.0", Tkinter.END)
    with open(initial_directory + '/' + str(my_Entry1.get())) as data_file1:
        data1 = json.load(data_file1)
    my_txt1.insert(Tkinter.END, data1['text'])
    my_txt_small.insert(Tkinter.END, 'id:' + str(data1['id']) + '\n' + 'positive:' + str(data1['positive']) + '\n' + 'sarcasm:' + str(data1['sarcasm']))

    my_txt2.delete("1.0", Tkinter.END)
    with open(result_directory + '/' + str(my_Entry1.get()) + '_tf-idf') as data_file2:
        data2 = json.load(data_file2)
    for term, info in data2['terms'].items():
        my_txt2.insert(Tkinter.END, 'term' + ':' + term + '\n' + 'tf' + ':' + str(info['tf']) + '\n' + 'idf' + ':' + str(info['idf']) + '\n')


def event_info3(event):
    my_Entry1.focus_force()



my_frame_1 = Tkinter.Frame(my_tk, width=70, height=30)
my_frame_1.pack(side=Tkinter.TOP, fill=Tkinter.BOTH)

my_frame_2 = Tkinter.Frame(my_tk, width=70, height=30)
my_frame_2.pack(side=Tkinter.TOP, fill=Tkinter.BOTH)

my_txt1 = ScrolledText.ScrolledText(my_frame_1, width=35, height=30)
my_txt1.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)

my_txt2 = ScrolledText.ScrolledText(my_frame_1, width=35, height=30)
my_txt2.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)

my_Entry1 = Tkinter.Entry(my_frame_2)
my_txt_small = ScrolledText.ScrolledText(my_frame_2, width=40, height=5)

my_Entry1.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)
my_txt_small.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)

my_Entry1.bind("<Return>", event_info1)
my_tk.bind("<Down>", event_info3)

my_tk.mainloop()


