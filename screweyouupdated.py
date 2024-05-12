import tkinter as tk
from tkinter import ttk
import webbrowser
import time
import random

root = tk.Tk()
tree = ttk.Treeview(root)

# Set up some dummy data for the tree
tree.insert("", "end", text="Website 1", values=("http://www.google.com",))
tree.insert("", "end", text="Website 2", values=("http://www.amazon.com",))
tree.insert("", "end", text="Website 5", values=("http://www.pornhub.com",))
tree.insert("", "end", text="Website 3", values=("http://www.youtube.com",))
tree.insert("", "end", text="Website 4", values=("http://www.facebook.com",))
tree.insert("", "end", text="Website 5", values=("http://www.gmail.com",))

tree.pack()

# Get all item IDs in the tree
item_ids = tree.get_children()

# Infinite loop to open random websites
while True:
    # Choose a random item ID from the tree
    selected_item = random.choice(item_ids)

    # Get the website URL associated with the selected item
    website_url = tree.item(selected_item, 'values')[0]

    # Open the website in the default web browser
    webbrowser.open(website_url)

    # Sleep for a random duration
    seconds = random.uniform(1, 5)
    time.sleep(seconds)

root.mainloop()
