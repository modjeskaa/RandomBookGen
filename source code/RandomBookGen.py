from io import BytesIO
import tkinter as tk
from tkinter import Text
from PIL import Image, ImageTk
import webbrowser
from scraper_AuthorTitlePic import random_book_url, author_and_title_and_image, getAuthorTitlePic
from scraper_Gatunek import random_book_by_genre_url, getRandomBook, gatunek_URL
import requests

text_background_color = "#613717"
genre_var = None
bg_image = None

def open_url(event):
    webbrowser.open(random_book_url)


def load_frame1():
    global genre_var, bg_image

    for widget in root.winfo_children():
        widget.destroy()

    bg_image = ImageTk.PhotoImage(file="assets/frame1_rsz.png")
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    tk.Label(root, text="Gatunek: ", font=("Courier", 20), bg=text_background_color, fg="white").place(x=100, y=320)


    #                               Dropdown list with choices
    genres = [
        "Literatura piękna",
        "Klasyka",
        "Kryminał, sensacja, thriller",
        "Reportaż",
        "Biografia, autobiografia, pamiętnik",
        "Literatura popularnonaukowa",
        "Fantasy, science-fiction",
        "Literatura dziecięca",
        "Komiksy",
        "Poezja, dramat, satyra",
        "Sztuka",
        "Pozostałe"
    ]
    genre_var = tk.StringVar(root)
    genre_var.set(genres[0]) 

    genre_dropdown = tk.OptionMenu(root, genre_var, *genres)
    genre_dropdown.config(width=25)
    genre_dropdown_width = genre_dropdown.winfo_reqwidth()
    genre_dropdown_x_coordinate = (app_width - genre_dropdown_width) // 2
    genre_dropdown.place(x=genre_dropdown_x_coordinate, y=360)

    #                               "Let's go!" button
    lets_go_button = tk.Button(root, text="Let's go!", font=("Courier", 16), bg="#995344", fg="white", cursor="hand2",
                            activebackground="#badee2", activeforeground="black", command=load_frame2)
    button_width = lets_go_button.winfo_reqwidth()
    x_coordinate = (app_width - button_width) // 2
    lets_go_button.place(x=x_coordinate, y=400)

    #                                   "lub"
    tk.Label(root, text="lub", font=("Courier", 20), bg=text_background_color, fg="white").place(x=x_coordinate + 45, y=450)

    #                               Random TOP100 button 
    TOP100_button = tk.Button(root, text="Random TOP100", font=("Courier", 16), bg="#995344", fg="white", cursor="hand2",
                        activebackground="#badee2", activeforeground="black", command=load_frame3)
    TOP100_button.place(x=x_coordinate - 20, y=490)

    #                                    Footer
    center_x = app_width // 2
    tk.Label(root, text="created by modjeska", font=("Courier", 10), bg=text_background_color, fg="white").place(x=center_x - 80, y=app_height - 30)


def load_frame2():
    global genre_var, bg_image
    selected_genre = genre_var.get()

    random_book_url = getRandomBook(gatunek_URL[selected_genre])

    for widget in root.winfo_children():
        widget.destroy()

    bg_image = ImageTk.PhotoImage(file="assets/frame2_rsz.png")

    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    title, author_name, image_src = getAuthorTitlePic(random_book_url)

    #                           Link
    link_text = "Link do książki [lubimyczytac]"
    link_label_width = len(link_text) * 7 

    # Calculate the center 
    center_x = (app_width - link_label_width) // 2
    center_y = (app_height - 200) // 2 - 20  

    #                           Bookcover
    response = requests.get(image_src)
    image = Image.open(BytesIO(response.content))

    image = image.resize((170, 243))
    photo = ImageTk.PhotoImage(image)
    image_label = tk.Label(root, image=photo)
    image_label.image = photo

    image_label.place(x=center_x + 15, y=center_y + 30)  

    #                           Tytuł (Label)
    text_widget_title = tk.Label(root, text=f"Tytuł: '{title}'", font=("Courier", 12),
                                 bg=text_background_color, fg="white")
    text_widget_title.place(x=center_x - 70, y=center_y + 300)  

    #                           Autor (Label)
    text_widget_author = tk.Label(root, text=f"Autor(ka): '{author_name}'", font=("Courier", 12),
                                  bg=text_background_color, fg="white")
    text_widget_author.place(x=center_x - 70, y=center_y + 320) 

    #                           Link (Label)
    link_label = tk.Label(root, text=link_text, font=("Courier", 10), bg=text_background_color,
                          fg="white", cursor="hand2")
    link_label.place(x=center_x, y=center_y + 280) 
    link_label.bind("<Button-1>", open_url)

    #                           Back to Main Menu
    back_button = tk.Button(root, text="Powrót do menu", font=("Courier", 12), bg="#995344", fg="white",
                            cursor="hand2", activebackground="#badee2", activeforeground="black", command=load_frame1)
    back_button.place(x=170, y=530)


def load_frame3():
    global genre_var, bg_image
    selected_genre = genre_var.get()

    # Hide frame1 widgets
    for widget in root.winfo_children():
        widget.destroy()

    bg_image = ImageTk.PhotoImage(file="assets/frame3_rsz.png")
    background_label = tk.Label(root, image=bg_image)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)

    #                       Bookcover
    image_url = author_and_title_and_image[2]
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))

    image = image.resize((170, 243))

    photo = ImageTk.PhotoImage(image)

    image_label = tk.Label(root, image=photo)
    image_label.image = photo

    # Calculate the center
    center_x = (app_width - image_label.winfo_reqwidth()) // 2
    center_y = (app_height - image_label.winfo_reqheight()) // 2

    image_label.place(x=center_x, y=center_y + 30)

    #                               Link (Label)
    link_label = tk.Label(root, text="Link do książki [lubimyczytac]", font=("Courier", 10), bg=text_background_color,
                          fg="white", cursor="hand2")
    link_label.place(x=center_x - 10, y=center_y + 290)

    link_label.bind("<Button-1>", open_url)

    #                               Tytuł (Label)
    text_widget_title = tk.Label(root, text=f"Tytuł: '{author_and_title_and_image[0]}'", font=("Courier", 12),
                                 bg=text_background_color, fg="white")
    text_widget_title.place(x=center_x - 90, y=center_y + 310)  

    #                               Autor (Label)
    text_widget_author = tk.Label(root, text=f"Autor(ka): '{author_and_title_and_image[1]}'", font=("Courier", 12),
                                  bg=text_background_color, fg="white")
    text_widget_author.place(x=center_x - 90, y=center_y + 330) 

        #                           Back to Main Menu
    back_button = tk.Button(root, text="Powrót do menu", font=("Courier", 12), bg="#995344", fg="white",
                            cursor="hand2", activebackground="#badee2", activeforeground="black", command=load_frame1)
    back_button.place(x=170, y=530)



root = tk.Tk()
root.title("Random book")

app_width, app_height = 500, 600
root.geometry(f"{app_width}x{app_height}")

load_frame1()
root.mainloop()
