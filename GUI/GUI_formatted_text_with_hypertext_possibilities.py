import Tkinter
import json
import urllib
file_with_hypertext = 'diff.txt'
initial_directory = 'materials'
result_directory = 'results'
tk = Tkinter.Tk()
txt = Tkinter.Text(tk, width=64, font='18')
txt.place(relx=0, rely=0, relwidth=0.5, relheight=1)

addr = Tkinter.Text(tk, background="White", width=64, height=1, font='18')
addr.place(relx=0.5, rely=0, relwidth=0.5, relheight=0.1)

initial_page = Tkinter.Text(tk, background="White", width=64, font='18')
initial_page.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.4)

result_page = Tkinter.Text(tk, background="White", width=64, font='18')
result_page.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)

def fetch_url(event):
    click_point = "@%s,%s" % (event.x, event.y)
    trs = txt.tag_ranges("href")
    url = ""
    for i in range(0, len(trs), 2):
        if txt.compare(trs[i], "<=", click_point) and txt.compare(click_point, "<=", trs[i+1]):
            url = txt.get(trs[i], trs[i+1])
    url = url[1:len(url) - 1]
    addr.delete("1.0", Tkinter.END)
    addr.insert("1.0", url)
    place = url.find('_tf-idf')

    with open(initial_directory + '/' + url[0:place]) as data_file1:
        initial_data = json.load(data_file1)
    initial_page.delete("1.0", Tkinter.END)
    initial_page.insert("1.0", initial_data['text'])

    with open(result_directory + '/' + url) as data_file2:
        result_data = json.load(data_file2)
    result_page.delete("1.0", Tkinter.END)
    for term, info in result_data['terms'].items():
        result_page.insert(Tkinter.END, 'term' + ':' + term + '\n' + 'tf' + ':' + str(info['tf']) + '\n' + 'idf' + ':' + str(info['idf']) + '\n')

with open(file_with_hypertext) as data_file:
    text = data_file.read()
text_frags = text.split()
prev_frag = ''
for frag in text_frags:
    if frag.startswith("@"):
        txt.insert(Tkinter.END, frag, "href")
    else:
        txt.insert(Tkinter.END, frag)
    if prev_frag == 'really:':
        txt.insert(Tkinter.END, '\n')
    prev_frag = frag

txt.tag_config("href", foreground="Blue", underline=1)
txt.tag_bind("href", "<1>", fetch_url)
tk.mainloop()
