#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Dec 01, 2019 02:33:07 AM IST  platform: Windows NT

import sys
import sqlite3 as sq
from tkinter import messagebox

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

import merge_cat_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = merge_window(root)
    merge_cat_support.init(root, top)
    root.mainloop()


w = None


def create_merge_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel(root)
    top = merge_window(w)
    merge_cat_support.init(w, top, *args, **kwargs)
    return (w, top)


def destroy_merge_window():
    global w
    w.destroy()
    w = None


class merge_window:
    def mergecategory(self):
        cat1 = str(self.cat1_entry.get())
        cat2 = str(self.cat2_entry.get())
        new_cat = str(self.new_cat_entry.get())
        conn = sq.connect('accounts.db')
        query1 = conn.execute("SELECT * FROM CATEGORIES WHERE category=(?)", (cat1,)).fetchone()[0]
        query2 = conn.execute("SELECT * FROM CATEGORIES WHERE category=(?)", (cat2,)).fetchone()[0]
        if query1 is not None and query2 is not None:
            conn.execute("DELETE FROM CATEGORIES WHERE category = (?)", (cat1,))
            conn.execute("DELETE FROM CATEGORIES WHERE category = (?)", (cat2,))
            conn.execute("INSERT INTO CATEGORIES (category) \
                                          VALUES (?)", (new_cat,))
            conn.commit()
            messagebox.showinfo("Message", "Merging done successfully")
        else:
            messagebox.showerror("Message", "One of the categories is not a valid category")

    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'

        top.geometry("600x450+594+147")
        top.minsize(148, 1)
        top.maxsize(1924, 1055)
        top.resizable(1, 1)
        top.title("Merge Category")
        top.configure(background="#d9d9d9")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.383, rely=0.178, height=26, width=142)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''Categories to Merge''')

        self.cat1_entry = tk.Entry(top)
        self.cat1_entry.place(relx=0.133, rely=0.333, height=24, relwidth=0.34)
        self.cat1_entry.configure(background="white")
        self.cat1_entry.configure(disabledforeground="#a3a3a3")
        self.cat1_entry.configure(font="TkFixedFont")
        self.cat1_entry.configure(foreground="#000000")
        self.cat1_entry.configure(insertbackground="black")

        self.cat2_entry = tk.Entry(top)
        self.cat2_entry.place(relx=0.533, rely=0.333, height=24, relwidth=0.34)
        self.cat2_entry.configure(background="white")
        self.cat2_entry.configure(disabledforeground="#a3a3a3")
        self.cat2_entry.configure(font="TkFixedFont")
        self.cat2_entry.configure(foreground="#000000")
        self.cat2_entry.configure(highlightbackground="#d9d9d9")
        self.cat2_entry.configure(highlightcolor="black")
        self.cat2_entry.configure(insertbackground="black")
        self.cat2_entry.configure(selectbackground="#c4c4c4")
        self.cat2_entry.configure(selectforeground="black")

        self.new_cat_entry = tk.Entry(top)
        self.new_cat_entry.place(relx=0.333, rely=0.6, height=24, relwidth=0.34)
        self.new_cat_entry.configure(background="white")
        self.new_cat_entry.configure(disabledforeground="#a3a3a3")
        self.new_cat_entry.configure(font="TkFixedFont")
        self.new_cat_entry.configure(foreground="#000000")
        self.new_cat_entry.configure(insertbackground="black")

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(relx=0.383, rely=0.467, height=26, width=142)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text='''New Category name''')

        self.submit_button = tk.Button(top)
        self.submit_button.place(relx=0.45, rely=0.711, height=33, width=59)
        self.submit_button.configure(activebackground="#ececec")
        self.submit_button.configure(activeforeground="#000000")
        self.submit_button.configure(background="#d9d9d9")
        self.submit_button.configure(disabledforeground="#a3a3a3")
        self.submit_button.configure(foreground="#000000")
        self.submit_button.configure(highlightbackground="#d9d9d9")
        self.submit_button.configure(highlightcolor="black")
        self.submit_button.configure(pady="0")
        self.submit_button.configure(text='''Submit''')
        self.submit_button.configure(command=self.mergecategory)


if __name__ == '__main__':
    vp_start_gui()
