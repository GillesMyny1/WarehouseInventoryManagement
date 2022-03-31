import sys
import platform
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *

import sqlite3
from sqlite3 import Error

import main

class MainFrame:
    def showWarehouseStock(self):
        cursorOne = self.conn.cursor()
        cursorOne.execute("SELECT * FROM warehouse")
        stockRows = cursorOne.fetchall()
        self.WarehouseList.insert(0, "Bin | Product ID | Quantity")
        for i in range(0, len(stockRows)):
            data = str(stockRows[i][0]) + "    " + str(stockRows[i][1]) + "    " + str(stockRows[i][2])
            self.WarehouseList.insert(i + 1, data)
            
    def selectedItem(self, event):
        w = event.widget
        for i in w.curselection():
            if i < 1:
                return
            text = w.get(i)
        data = text.split("    ")
        cursorTwo = self.conn.cursor()
        cursorTwo.execute("SELECT * FROM product WHERE product_id = " + str(data[1]))
        productInfo = cursorTwo.fetchall()
        self.ProdIDRead.configure(state='normal')
        self.ProdIDRead.delete('1.0', END)
        self.ProdIDRead.insert(INSERT, productInfo[0][0])
        self.ProdIDRead.configure(state='disabled')
        self.DescRead.configure(state='normal')
        self.DescRead.delete('1.0', END)
        self.DescRead.insert(INSERT, productInfo[0][1])
        self.DescRead.configure(state='disabled')
        
    def enterHandlerSellOrderDate(self, event):
        self.BuyOrderDateText.delete(0, END)
        self.ProdIDSearchText.delete(0, END)
        self.OrderNumText.delete(0, END)
        w = event.widget
        sellDate = w.get()
        cursorThree = self.conn.cursor()
        cursorThree.execute("SELECT sell_order_num, destination_addr FROM sell_order_sheet WHERE soldby_date = '" + sellDate + "'")
        sellOrderSheet = cursorThree.fetchall()
        self.DisplayResultQuery.delete(0, END)
        self.DisplayResultQuery.insert(0, "Sell Order Sheet Num | Destination Address")
        for i in range(0, len(sellOrderSheet)):
            num = 23 - len(str(sellOrderSheet[i][0]))
            filler = ' ' * num
            data = str(sellOrderSheet[i][0]) + filler + sellOrderSheet[i][1]
            self.DisplayResultQuery.insert(i + 1, data)

    def enterHandlerBuyOrderDate(self, event):
        self.SellOrderDateText.delete(0, END)
        self.ProdIDSearchText.delete(0, END)
        self.OrderNumText.delete(0, END)
        w = event.widget
        buyDate = w.get()
        cursorFour = self.conn.cursor()
        cursorFour.execute("SELECT buy_order_num, origin_adrr FROM buy_order_sheet WHERE arrival_date = '" + buyDate + "'")
        buyOrderSheets = cursorFour.fetchall()
        self.DisplayResultQuery.delete(0, END)
        self.DisplayResultQuery.insert(0, "Buy Order Sheet Num | Origin Address")
        for i in range(0, len(buyOrderSheets)):
            num = 22 - len(str(buyOrderSheets[i][0]))
            filler = ' ' * num
            data = str(buyOrderSheets[i][0]) + filler + buyOrderSheets[i][1]
            self.DisplayResultQuery.insert(i + 1, data)
            
    def enterHandlerProdSearch(self, event):
        self.BuyOrderDateText.delete(0, END)
        self.SellOrderDateText.delete(0, END)
        self.OrderNumText.delete(0, END)
        w = event.widget
        prodID = w.get()
        cursorFive = self.conn.cursor()
        cursorFive.execute("SELECT warehouse_bin, bin_quantity FROM warehouse WHERE product_id = " + prodID)
        products = cursorFive.fetchall()
        self.DisplayResultQuery.delete(0, END)
        self.DisplayResultQuery.insert(0, "Warehouse Bin | Bin Quantity")
        for i in range(0, len(products)):
            num = 16 - len(str(products[i][0]))
            filler = ' ' * num
            data = str(products[i][0]) + filler + str(products[i][1])
            self.DisplayResultQuery.insert(i + 1, data)

    def enterHandlerOrderSearch(self, event):
        self.BuyOrderDateText.delete(0, END)
        self.SellOrderDateText.delete(0, END)
        self.ProdIDSearchText.delete(0, END)
        w = event.widget
        orderNum = w.get()
        cursorSix = self.conn.cursor()
        cursorSix.execute("SELECT warehouse_bin, buy_prod_quantity FROM buy_order WHERE buy_order_num = " + orderNum)
        buyOrders = cursorSix.fetchall()
        self.DisplayResultQuery.delete(0, END)
        self.DisplayResultQuery.insert(0, "Warehouse Bin Added To | Quantity Added to Bin")
        for i in range(0, len(buyOrders)):
            num = 25 - len(str(buyOrders[i][0]))
            filler = ' ' * num
            data = str(buyOrders[i][0]) + filler + str(buyOrders[i][1])
            self.DisplayResultQuery.insert(i + 1, data)
    def __init__(self, top=None):
        self.conn = None
        try:
            self.conn = sqlite3.connect(r"C:\Users\Gilles Myny\Desktop\COMP 3005 A\Project\project_database.db")
        except Error as e:
            print(e)

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("750x850+559+74")
        top.minsize(750, 850)
        top.maxsize(750, 850)
        top.resizable(1,  1)
        top.title("Warehouse Inventory Management")
        top.configure(background="#d9d9d9")

        self.top = top

        self.PrimaryFrame = tk.Frame(self.top)
        self.PrimaryFrame.place(relx=0.2, rely=0.08, relheight=0.333, relwidth=0.6)
        self.PrimaryFrame.configure(relief='raised')
        self.PrimaryFrame.configure(borderwidth="2")
        self.PrimaryFrame.configure(relief="raised")
        self.PrimaryFrame.configure(background="#d9d9d9")
        self.PrimaryFrame.configure(cursor="fleur")

        self.ProdIDSearchText = tk.Entry(self.PrimaryFrame)
        self.ProdIDSearchText.place(relx=0.578, rely=0.76, relheight=0.141, relwidth=0.311)
        self.ProdIDSearchText.configure(background="white")
        self.ProdIDSearchText.configure(font="-family {Segoe UI} -size 10")
        self.ProdIDSearchText.configure(foreground="black")
        self.ProdIDSearchText.configure(highlightbackground="#d9d9d9")
        self.ProdIDSearchText.configure(highlightcolor="black")
        self.ProdIDSearchText.configure(insertbackground="black")
        self.ProdIDSearchText.configure(selectbackground="blue")
        self.ProdIDSearchText.configure(selectforeground="white")
        self.ProdIDSearchText.bind('<Return>', self.enterHandlerProdSearch)

        self.SellOrderDateLabel = tk.Label(self.PrimaryFrame)
        self.SellOrderDateLabel.place(relx=0.156, rely=0.558, height=37, width=179)
        self.SellOrderDateLabel.configure(anchor='w')
        self.SellOrderDateLabel.configure(background="#d9d9d9")
        self.SellOrderDateLabel.configure(compound='left')
        self.SellOrderDateLabel.configure(disabledforeground="#a3a3a3")
        self.SellOrderDateLabel.configure(font="-family {Segoe UI} -size 10")
        self.SellOrderDateLabel.configure(foreground="#000000")
        self.SellOrderDateLabel.configure(text='''Display Sell Orders Dated on:''')

        self.SellOrderDateText = tk.Entry(self.PrimaryFrame)
        self.SellOrderDateText.place(relx=0.578, rely=0.558, relheight=0.141, relwidth=0.311)
        self.SellOrderDateText.configure(background="white")
        self.SellOrderDateText.configure(font="-family {Segoe UI} -size 10")
        self.SellOrderDateText.configure(foreground="black")
        self.SellOrderDateText.configure(highlightbackground="#d9d9d9")
        self.SellOrderDateText.configure(highlightcolor="black")
        self.SellOrderDateText.configure(insertbackground="black")
        self.SellOrderDateText.configure(selectbackground="blue")
        self.SellOrderDateText.configure(selectforeground="white")
        self.SellOrderDateText.bind('<Return>', self.enterHandlerSellOrderDate)

        self.BuyOrderDateText = tk.Entry(self.PrimaryFrame)
        self.BuyOrderDateText.place(relx=0.578, rely=0.36, relheight=0.141, relwidth=0.311)
        self.BuyOrderDateText.configure(background="white")
        self.BuyOrderDateText.configure(font="-family {Segoe UI} -size 10")
        self.BuyOrderDateText.configure(foreground="black")
        self.BuyOrderDateText.configure(highlightbackground="#d9d9d9")
        self.BuyOrderDateText.configure(highlightcolor="black")
        self.BuyOrderDateText.configure(insertbackground="black")
        self.BuyOrderDateText.configure(selectbackground="blue")
        self.BuyOrderDateText.configure(selectforeground="white")
        self.BuyOrderDateText.bind('<Return>', self.enterHandlerBuyOrderDate)

        self.BuyOrderDateLabel = tk.Label(self.top)
        self.BuyOrderDateLabel.place(relx=0.293, rely=0.2, height=37, width=180)
        self.BuyOrderDateLabel.configure(activebackground="#f9f9f9")
        self.BuyOrderDateLabel.configure(activeforeground="black")
        self.BuyOrderDateLabel.configure(anchor='w')
        self.BuyOrderDateLabel.configure(background="#d9d9d9")
        self.BuyOrderDateLabel.configure(compound='left')
        self.BuyOrderDateLabel.configure(disabledforeground="#a3a3a3")
        self.BuyOrderDateLabel.configure(font="-family {Segoe UI} -size 10")
        self.BuyOrderDateLabel.configure(foreground="#000000")
        self.BuyOrderDateLabel.configure(highlightbackground="#d9d9d9")
        self.BuyOrderDateLabel.configure(highlightcolor="black")
        self.BuyOrderDateLabel.configure(text='''Display Buy Orders Dated on:''')

        self.ProdIDSearchLabel = tk.Label(self.top)
        self.ProdIDSearchLabel.place(relx=0.24, rely=0.333, height=37, width=220)

        self.ProdIDSearchLabel.configure(activebackground="#f9f9f9")
        self.ProdIDSearchLabel.configure(activeforeground="black")
        self.ProdIDSearchLabel.configure(anchor='w')
        self.ProdIDSearchLabel.configure(background="#d9d9d9")
        self.ProdIDSearchLabel.configure(compound='left')
        self.ProdIDSearchLabel.configure(disabledforeground="#a3a3a3")
        self.ProdIDSearchLabel.configure(font="-family {Segoe UI} -size 10")
        self.ProdIDSearchLabel.configure(foreground="#000000")
        self.ProdIDSearchLabel.configure(highlightbackground="#d9d9d9")
        self.ProdIDSearchLabel.configure(highlightcolor="black")
        self.ProdIDSearchLabel.configure(text='''Search for Product ID in Warehouse:''')

        self.OrderNumFindLabel = tk.Label(self.top)
        self.OrderNumFindLabel.place(relx=0.270, rely=0.107, height=24, width=364)
        self.OrderNumFindLabel.configure(anchor='w')
        self.OrderNumFindLabel.configure(background="#d9d9d9")
        self.OrderNumFindLabel.configure(compound='left')
        self.OrderNumFindLabel.configure(disabledforeground="#a3a3a3")
        self.OrderNumFindLabel.configure(foreground="#000000")
        self.OrderNumFindLabel.configure(text='''Enter Buy Order Num to Find Bin Number & Quantity Added:''')

        self.OrderNumText = tk.Entry(self.top)
        self.OrderNumText.place(relx=0.4, rely=0.147, relheight=0.04, relwidth=0.2)
        self.OrderNumText.configure(background="white")
        self.OrderNumText.configure(font="TkTextFont")
        self.OrderNumText.configure(foreground="black")
        self.OrderNumText.configure(highlightbackground="#d9d9d9")
        self.OrderNumText.configure(highlightcolor="black")
        self.OrderNumText.configure(insertbackground="black")
        self.OrderNumText.configure(selectbackground="blue")
        self.OrderNumText.configure(selectforeground="white")
        self.OrderNumText.bind('<Return>', self.enterHandlerOrderSearch)

        self.SpecificInfoLabel = tk.Label(self.top)
        self.SpecificInfoLabel.place(relx=0.213, rely=0.027, height=35, width=435)
        self.SpecificInfoLabel.configure(anchor='w')
        self.SpecificInfoLabel.configure(background="#d9d9d9")
        self.SpecificInfoLabel.configure(compound='left')
        self.SpecificInfoLabel.configure(disabledforeground="#a3a3a3")
        self.SpecificInfoLabel.configure(font="-family {Cambria} -size 16 -weight bold")
        self.SpecificInfoLabel.configure(foreground="#000000")
        self.SpecificInfoLabel.configure(text='''Find Information Given Specific Parameters''')

        self.DisplayResultQuery = ScrolledListBox(self.top)
        self.DisplayResultQuery.place(relx=0.2, rely=0.44, relheight=0.132, relwidth=0.6)
        self.DisplayResultQuery.configure(background="white")
        self.DisplayResultQuery.configure(cursor="xterm")
        self.DisplayResultQuery.configure(disabledforeground="#a3a3a3")
        self.DisplayResultQuery.configure(font="TkFixedFont")
        self.DisplayResultQuery.configure(foreground="black")
        self.DisplayResultQuery.configure(highlightbackground="#d9d9d9")
        self.DisplayResultQuery.configure(highlightcolor="#d9d9d9")
        self.DisplayResultQuery.configure(selectbackground="blue")
        self.DisplayResultQuery.configure(selectforeground="white")

        self.StockListLabel = tk.Label(self.top)
        self.StockListLabel.place(relx=0.36, rely=0.598, height=34, width=225)
        self.StockListLabel.configure(activebackground="#f9f9f9")
        self.StockListLabel.configure(activeforeground="black")
        self.StockListLabel.configure(anchor='w')
        self.StockListLabel.configure(background="#d9d9d9")
        self.StockListLabel.configure(compound='left')
        self.StockListLabel.configure(disabledforeground="#a3a3a3")
        self.StockListLabel.configure(font="-family {Cambria} -size 16 -weight bold")
        self.StockListLabel.configure(foreground="#000000")
        self.StockListLabel.configure(highlightbackground="#d9d9d9")
        self.StockListLabel.configure(highlightcolor="black")
        self.StockListLabel.configure(text='''Warehouse Stock List''')

        self.FirstSeperator = ttk.Separator(self.top)
        self.FirstSeperator.place(relx=0.173, rely=0.592,  relwidth=0.667)

        self.WarehouseList = ScrolledListBox(self.top)
        self.WarehouseList.place(relx=0.2, rely=0.644, relheight=0.133, relwidth=0.6)
        self.WarehouseList.configure(background="white")
        self.WarehouseList.configure(cursor="xterm")
        self.WarehouseList.configure(disabledforeground="#a3a3a3")
        self.WarehouseList.configure(font="TkFixedFont")
        self.WarehouseList.configure(foreground="black")
        self.WarehouseList.configure(highlightbackground="#d9d9d9")
        self.WarehouseList.configure(highlightcolor="#d9d9d9")
        self.WarehouseList.configure(selectbackground="blue")
        self.WarehouseList.configure(selectforeground="white")
        self.showWarehouseStock()
        self.WarehouseList.bind('<<ListboxSelect>>', self.selectedItem)

        self.SecondSeperator=ttk.Separator(self.top)
        self.SecondSeperator.place(relx=0.16, rely=0.793, relwidth=0.687)

        self.ProdInfoLabel=tk.Label(self.top)
        self.ProdInfoLabel.place(relx=0.413, rely=0.805, height=34, width=135)
        self.ProdInfoLabel.configure(activebackground="#f9f9f9")
        self.ProdInfoLabel.configure(activeforeground="black")
        self.ProdInfoLabel.configure(anchor='w')
        self.ProdInfoLabel.configure(background="#d9d9d9")
        self.ProdInfoLabel.configure(compound='left')
        self.ProdInfoLabel.configure(disabledforeground="#a3a3a3")
        self.ProdInfoLabel.configure(font="-family {Cambria} -size 16 -weight bold")
        self.ProdInfoLabel.configure(foreground="#000000")
        self.ProdInfoLabel.configure(highlightbackground="#d9d9d9")
        self.ProdInfoLabel.configure(highlightcolor="black")
        self.ProdInfoLabel.configure(text='''Product Info''')

        self.SecondaryFrame=tk.Frame(self.top)
        self.SecondaryFrame.place(relx=0.2, rely=0.851, relheight=0.133, relwidth=0.6)
        self.SecondaryFrame.configure(relief='raised')
        self.SecondaryFrame.configure(borderwidth="2")
        self.SecondaryFrame.configure(relief="raised")
        self.SecondaryFrame.configure(background="#d9d9d9")

        self.ProdIDLabel=tk.Label(self.SecondaryFrame)
        self.ProdIDLabel.place(relx=0.222, rely=0.257, height=21, width=74)
        self.ProdIDLabel.configure(anchor='w')
        self.ProdIDLabel.configure(background="#d9d9d9")
        self.ProdIDLabel.configure(compound='left')
        self.ProdIDLabel.configure(disabledforeground="#a3a3a3")
        self.ProdIDLabel.configure(font="-family {Segoe UI} -size 10")
        self.ProdIDLabel.configure(foreground="#000000")
        self.ProdIDLabel.configure(text='''Product ID:''')

        self.DescriptionLabel=tk.Label(self.SecondaryFrame)
        self.DescriptionLabel.place(relx=0.222, rely=0.611, height=20, width=84)
        self.DescriptionLabel.configure(anchor='w')
        self.DescriptionLabel.configure(background="#d9d9d9")
        self.DescriptionLabel.configure(compound='left')
        self.DescriptionLabel.configure(disabledforeground="#a3a3a3")
        self.DescriptionLabel.configure(font="-family {Segoe UI} -size 10")
        self.DescriptionLabel.configure(foreground="#000000")
        self.DescriptionLabel.configure(text='''Description:''')

        self.ProdIDRead=tk.Text(self.SecondaryFrame)
        self.ProdIDRead.place(relx=0.4, rely=0.265, relheight=0.221, relwidth=0.544)
        self.ProdIDRead.configure(background="white")
        self.ProdIDRead.configure(font="TkTextFont")
        self.ProdIDRead.configure(foreground="black")
        self.ProdIDRead.configure(highlightbackground="#d9d9d9")
        self.ProdIDRead.configure(highlightcolor="black")
        self.ProdIDRead.configure(insertbackground="black")
        self.ProdIDRead.configure(selectbackground="blue")
        self.ProdIDRead.configure(selectforeground="white")
        self.ProdIDRead.configure(state='disabled')
        self.ProdIDRead.configure(wrap="word")

        self.DescRead=tk.Text(self.SecondaryFrame)
        self.DescRead.place(relx=0.4, rely=0.619, relheight=0.221, relwidth=0.544)
        self.DescRead.configure(background="white")
        self.DescRead.configure(font="TkTextFont")
        self.DescRead.configure(foreground="black")
        self.DescRead.configure(highlightbackground="#d9d9d9")
        self.DescRead.configure(highlightcolor="black")
        self.DescRead.configure(insertbackground="black")
        self.DescRead.configure(selectbackground="blue")
        self.DescRead.configure(selectforeground="white")
        self.DescRead.configure(state='disabled')
        self.DescRead.configure(wrap="word")

class AutoScroll(object):
    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz

def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

def start_up():
    main.main()

if __name__ == '__main__':
    main.main()
    