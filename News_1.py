# import modules
from tkinter import *
from gnewsclient import gnewsclient
import webbrowser
from urllib.request import urlopen
import requests
#import wget
from bs4 import BeautifulSoup
from PIL import ImageTk, Image
import io
import base64
import shutil

# tkinter object
master = Tk()
master.title("NEWS")

# defined funtions


def Open(url, n):
    webbrowser.open(url)
    window3 = Toplevel()

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    page_title = soup.title.text
    print(page_title)
    label = Label(window3, text=page_title)
    label.pack()
    images = soup.find_all('img', {'src': re.compile('.jpg')})
    for image in images:
        print(image['src']+'\n')
        #filename = wget.download(image['src'])
        img_url = image['src']
        image_bytes = urlopen(img_url).read()
        data_stream = io.BytesIO(image_bytes)
        pil_image = Image.open(data_stream)
        w, h = pil_image.size
        fname = img_url.split('/')[-1]
        sf = "{} ({}x{})".format(fname, w, h)
        window3.title(sf)
        img = ImageTk.PhotoImage(pil_image)
        #canvas = Canvas(window3, width = 300, height = 300)
        #canvas.grid(row = 1, column = 0)
        #img = ImageTk.PhotoImage(Image.open(str(filename)))
        #response = requests.get(image['src'])
        #image_data = response.content
        #img = ImageTk.PhotoImage(Image.open(BytesIO(image_data)))
        #panel = tk.Label(window3, image=img)
        #panel.pack(side="bottom", fill="both", expand="yes")
        img_label = Label(window3, image=img, cursor="hand2")
        img_label.pack(padx=5, pady=5)
        #canvas.create_image(20, 20, anchor=NW, image=img)
    #html = page.read().decode("utf-8")
    # print(html)


def news():
    window2 = Toplevel()
    window2.title("NEWS List")
    client = gnewsclient.NewsClient(
        language=lang.get(), location=loc.get(), topic=top.get(), max_results=5)
    news_list = client.get_news()
    result_title_1.set(news_list[0]["title"])
    result_title_2.set(news_list[1]["title"])
    result_title_3.set(news_list[2]["title"])
    result_title_4.set(news_list[3]["title"])
    result_title_5.set(news_list[4]["title"])
    link1 = Label(window2, textvariable=result_title_1,
                  foreground="blue", cursor="hand2")
    link2 = Label(window2, textvariable=result_title_2,
                  foreground="blue", cursor="hand2")
    link3 = Label(window2, textvariable=result_title_3,
                  foreground="blue", cursor="hand2")
    link4 = Label(window2, textvariable=result_title_4,
                  foreground="blue", cursor="hand2")
    link5 = Label(window2, textvariable=result_title_5,
                  foreground="blue", cursor="hand2")
    link1.grid(row=0, column=1)
    link2.grid(row=1, column=1)
    link3.grid(row=2, column=1)
    link4.grid(row=3, column=1)
    link5.grid(row=4, column=1)
    link1.bind("<Button-1>", lambda event: Open(str(news_list[0]["link"]), 1))
    link2.bind("<Button-1>", lambda event: Open(str(news_list[1]["link"]), 2))
    link3.bind("<Button-1>", lambda event: Open(str(news_list[2]["link"]), 3))
    link4.bind("<Button-1>", lambda event: Open(str(news_list[3]["link"]), 4))
    link5.bind("<Button-1>", lambda event: Open(str(news_list[4]["link"]), 5))


def abort():
    master.destroy()


# background set to grey
master.configure(bg='light grey')

# Variable Classes in tkinter
result_title_1 = StringVar()
result_title_2 = StringVar()
result_title_3 = StringVar()
result_title_4 = StringVar()
result_title_5 = StringVar()

# Creating label for each information
# name using widget Label
Label(master, text="Choose language :", bg="light grey",
      pady="5", padx="2").grid(row=0, sticky=W)
Label(master, text="Choose Location :", bg="light grey",
      pady="5", padx="2").grid(row=1, sticky=W)
Label(master, text="Choose Topic :", bg="light grey",
      pady="5", padx="2").grid(row=2, sticky=W)


lang = Entry(master)
lang.grid(row=0, column=1)

loc = Entry(master)
loc.grid(row=1, column=1)

top = Entry(master)
top.grid(row=2, column=1)


# Creating lebel for class variable
# name using widget Entry
#Label(master, text="", textvariable=result_title, bg="light grey").grid(row=3, column=1, sticky=W)

# White space
#Label(master, text="         ", textvariable=result_title, bg="light grey").grid(row=2, column=2, rowspan=3, sticky=W)
#Label(master, text="         ", textvariable=result_title, bg="light grey").grid(row=2, column=4, rowspan=3, sticky=W)
# Label(master, text=" ", textvariable=result_title, bg="light
# grey").grid(row=2, column=5, rowspan=3, sticky=W)

# creating a button using the widget
# Button to call the submit function
Button(master, text="Search", command=news,
       bg="white", padx="3").grid(row=1, column=3)
Button(master, text="Exit", command=abort, bg="white",
       padx="9", pady="1").grid(row=1, column=5)


mainloop()
