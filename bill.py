from tkinter import *
import math,random
import os,sys
from tkinter import messagebox
import mysql.connector
class Bill():
    def __init__(self,root):
        self.root = root
        self.root.title = 'Billing Software'
        self.root.geometry('1350x700')
        bg_color= '#074463'
        self.root.title = Label(root,text = "Billing Software", font = ('times new roman',40,'bold'),bd=20,bg=bg_color,fg='white')
        self.root.title.pack(side=TOP,fill=X)
        #==========================================Variable========================================
        #==========================Cosmetics============================
        self.soap = IntVar()
        self.face_cream = IntVar()
        self.face_wash = IntVar()
        self.spray = IntVar()
        self.gell = IntVar()
        self.loshan = IntVar()
        # =================================grocery======================================
        self.rice = IntVar()
        self.food_oil = IntVar()
        self.daal = IntVar()
        self.wheat = IntVar()
        self.sugar = IntVar()
        self.tea = IntVar()
        # =====================================cold drinks=============================
        self.maaza = IntVar()
        self.coke = IntVar()
        self.frooti = IntVar()
        self.thumbsup = IntVar()
        self.limca = IntVar()
        self.sprite = IntVar()
        # ===================================Totalproduct price and tax======================
        self.cosmetic_price = StringVar()
        self.grocery_price = StringVar()
        self.colddrink_price = StringVar()
        self.cosmetic_tax = StringVar()
        self.grocery_tax = StringVar()
        self.colddrink_tax = StringVar()
        # ======================================Customer=============================
        self.cstname = StringVar()
        self.mobile = StringVar()
        x = random.randint(1000, 9999)
        self.bill_no = StringVar()
        self.bill_no.set(str(x))
        self.search_bill = StringVar()

        f1 = LabelFrame(root, text='Customer Details', font=('times new roman', 15, 'bold'), fg='gold', bd=12, bg=bg_color)
        f1.place(x=0, y=80, relwidth=1, relheight=0.1)
        cname_lbl = Label(f1, text='Customer Name:', font=('times new roman', 15, 'bold'), fg='white', bg=bg_color)
        cname_lbl.grid(row=0, column=0, padx=10)
        cname_txt = Entry(f1, font=('times new roman', 15, 'bold'), textvariable=self.cstname, width=15, bd=5)
        cname_txt.grid(row=0, column=1)

        cphn_lbl = Label(f1, text='     Customer Phone Number:', font=('times new roman', 15, 'bold'), fg='white', bg=bg_color)
        cphn_lbl.grid(row=0, column=2, padx=10)
        cphn_txt = Entry(f1, font=('times new roman', 15, 'bold'), textvariable=self.mobile, width=15, bd=5)
        cphn_txt.grid(row=0, column=3)

        cbill_lbl = Label(f1, text='     Bill Number:', font=('times new roman', 15, 'bold'), fg='white', bg=bg_color)
        cbill_lbl.grid(row=0, column=4, padx=10)
        cbill_txt = Entry(f1, font=('times new roman', 15, 'bold'), textvariable=self.search_bill, width=15, bd=5)
        cbill_txt.grid(row=0, column=5)

        srch_btn = Button(f1, text='Search', bd=5, width=20,command=self.find_bill, font=('ariel bold', 10, 'bold'))
        srch_btn.grid(row=0, column=6, sticky='e', padx=20)

        f2 = LabelFrame(root, text='Cosmetics', font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color, bd=5)
        f2.place(x=5, y=150, width=350, height=450)

        bath_lbl = Label(f2, text='Bath Soap:', font=('times new roman', 15, 'bold'), bg=bg_color,
                         fg='white').grid(row=0, column=0, sticky='w', padx=10)
        txt_bath = Entry(f2, width=15, font=('times new roman', 15, 'bold'),textvariable=self.soap, bd=5).grid(row=0, column=1, padx=10, pady=10)

        face_lbl = Label(f2, text='Face Cream:', font=('times new roman', 15, 'bold'),
                         bg=bg_color, fg='white').grid(
            row=1, column=0, sticky='w', padx=10)
        txt_face = Entry(f2, width=15, font=('times new roman', 15, 'bold'), textvariable=self.face_cream, bd=5).grid(row=1, column=1, padx=10, pady=10)

        wash_lbl = Label(f2, text='Face Wash:', font=('times new roman', 15, 'bold'),
                         bg=bg_color, fg='white', bd=5).grid(row=2, column=0, sticky='w', padx=10)
        txt_wash = Entry(f2, width=15, font=('times new roman', 15, 'bold'),textvariable=self.face_wash, bd=5).grid(row=2, column=1, padx=10, pady=10)

        hair_lbl = Label(f2, text='Hair Spray:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white', bd=5).grid(
            row=3, column=0, sticky='w', padx=10)
        txt_hair = Entry(f2, width=15, font=('times new roman', 15, 'bold'),textvariable=self.spray, bd=5).grid(row=3, column=1, padx=10, pady=10)

        gell_lbl = Label(f2, text='Hair Gell:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white', bd=5).grid(
            row=4, column=0, sticky='w', padx=10)
        txt_gell = Entry(f2, width=15, font=('times new roman', 15, 'bold'),textvariable=self.gell, bd=5).grid(row=4, column=1, padx=10, pady=10)

        body_lbl = Label(f2, text='Body Lotion:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white', bd=5).grid(
            row=5, column=0, sticky='w', padx=10)
        txt_body = Entry(f2, width=15, font=('times new roman', 15, 'bold'),textvariable=self.loshan, bd=5).grid(row=5, column=1, padx=10, pady=10)

        f3 = LabelFrame(root, text='Provisions', font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color, bd=5)
        f3.place(x=360, y=150, width=350, height=450)

        rice_lbl = Label(f3, text='Rice:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white').grid(row=0, column=0, sticky='w', padx=10)
        txt_rice = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.rice, bd=5).grid(row=0, column=1, padx=10, pady=10)

        food_lbl = Label(f3, text='Food Oil:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white').grid(
            row=1, column=0, sticky='w', padx=10)
        txt_food = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.food_oil, bd=5).grid(row=1, column=1, padx=10, pady=10)

        daal_lbl = Label(f3, text='Daal:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white', bd=5).grid(row=2, column=0, sticky='w', padx=10)
        txt_daal = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.daal, bd=5).grid(row=2, column=1, padx=10, pady=10)

        wheat_lbl = Label(f3, text='Wheat:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                          fg='white', bd=5).grid(
            row=3, column=0, sticky='w', padx=10)
        txt_wheat = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.wheat, bd=5).grid(row=3, column=1, padx=10, pady=10)

        sugar_lbl = Label(f3, text='Sugar:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                          fg='white', bd=5).grid(
            row=4, column=0, sticky='w', padx=10)
        txt_sugar = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.sugar, bd=5).grid(row=4, column=1, padx=10, pady=10)

        tea_lbl = Label(f3, text='Tea', font=('times new roman', 15, 'bold'),  bg=bg_color, fg='white',
                        bd=5).grid(
            row=5, column=0, sticky='w', padx=10)
        txt_tea = Entry(f3, width=15, font=('times new roman', 15, 'bold'),textvariable=self.tea, bd=5).grid(row=5, column=1, padx=10, pady=10)

        f4 = LabelFrame(root, text='Cool Drinks', font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color, bd=5)
        f4.place(x=715, y=150, width=350, height=450)

        maaza_lbl = Label(f4, text='Maaza:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                          fg='white').grid(row=0, column=0, sticky='w', padx=10)
        txt_maaza = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.maaza, bd=5).grid(row=0, column=1, padx=10, pady=10)

        coke_lbl = Label(f4, text='Coke:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                         fg='white').grid(
            row=1, column=0, sticky='w', padx=10)
        txt_coke = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.coke, bd=5).grid(row=1, column=1, padx=10, pady=10)

        frooty_lbl = Label(f4, text='Frooty', font=('times new roman', 15, 'bold'),  bg=bg_color,
                           fg='white', bd=5).grid(row=2, column=0, sticky='w', padx=10)
        txt_frooty = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.frooti, bd=5).grid(row=2, column=1, padx=10, pady=10)

        thumb_lbl = Label(f4, text='Thumbs up:', font=('times new roman', 15, 'bold'),
                          bg=bg_color, fg='white', bd=5).grid(
            row=3, column=0, sticky='w', padx=10)
        txt_thumb = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.thumbsup, bd=5).grid(row=3, column=1, padx=10, pady=10)

        limca_lbl = Label(f4, text='Limca:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                          fg='white', bd=5).grid(
            row=4, column=0, sticky='w', padx=10)
        txt_limca = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.limca, bd=5).grid(row=4, column=1, padx=10, pady=10)

        sprite_lbl = Label(f4, text='Sprite:', font=('times new roman', 15, 'bold'),  bg=bg_color,
                           fg='white', bd=5).grid(
            row=5, column=0, sticky='w', padx=10)
        txt_sprite = Entry(f4, width=15, font=('times new roman', 15, 'bold'),textvariable=self.sprite, bd=5).grid(row=5, column=1, padx=10, pady=10)

        # =====================Bill area===============================================
        f5 = Frame(root, bd=10, bg='white', relief='groove')
        f5.place(x=1075, y=150, width=450, height=450)

        bill_title = Label(f5, text='Bill Area', font=('times new roman', 15, 'bold'), bg='black', fg='white')
        bill_title.pack(side=TOP, fill=X)

        scroll_y = Scrollbar(f5, orient=VERTICAL)
        self.txtarea = Text(f5, yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.txtarea.yview)
        self.txtarea.pack(expand=1, fill=BOTH)

        # =============================Button Frame=====================================
        f6 = LabelFrame(root, text='Bill Menu', font=('times new roman', 15, 'bold'), fg='gold', bg=bg_color, bd=10)
        f6.place(x=0, y=600, relwidth=1, relheight=1)

        m1 = Label(f6, text='Total Cosmetic Price', font=('times new roman', 15, 'bold'),
                   fg='white', bg=bg_color)
        m1.grid(row=0, column=0, padx=10, pady=10)

        m1_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.cosmetic_price, bd=5)
        m1_txt.grid(row=0, column=1, padx=10, pady=10)

        m2 = Label(f6, text='Cosmetic Tax', font=('times new roman', 15, 'bold'),  fg='white',
                   bg=bg_color)
        m2.grid(row=0, column=2, padx=10, pady=10)

        m2_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.cosmetic_tax, bd=5)
        m2_txt.grid(row=0, column=3, padx=10, pady=10)

        m3 = Label(f6, text='Total Grocery Price', font=('times new roman', 15, 'bold'),
                   fg='white', bg=bg_color)
        m3.grid(row=1, column=0, padx=10, pady=10)

        m3_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.grocery_price, bd=5)
        m3_txt.grid(row=1, column=1, padx=10, pady=10)

        m4 = Label(f6, text='Grocery Tax', font=('times new roman', 15, 'bold'),  fg='white',
                   bg=bg_color)
        m4.grid(row=1, column=2, padx=10, pady=10)

        m4_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.grocery_tax, bd=5)
        m4_txt.grid(row=1, column=3, padx=10, pady=10)

        m5 = Label(f6, text='Total Cold Drinks Price', font=('times new roman', 15, 'bold'),
                    fg='white', bg=bg_color)
        m5.grid(row=2, column=0, padx=10, pady=10)

        m5_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.colddrink_price, bd=5)
        m5_txt.grid(row=2, column=1, padx=10, pady=10)

        m6 = Label(f6, text='Cold Drink Tax', font=('times new roman', 15, 'bold'),
                   fg='white', bg=bg_color)
        m6.grid(row=2, column=2, padx=10, pady=10)

        m6_txt = Entry(f6, font=('times new roman', 15, 'bold'),textvariable=self.colddrink_tax, bd=5)
        m6_txt.grid(row=2, column=3)

        f7 = Frame(f6, bd=10, bg='white', relief='groove')
        f7.place(x=850, y=5, width=600, height=110)

        tot_btn = Button(f7, bd=5, bg=bg_color, command=self.total, fg='white', text='Total',
                              font=('times new roman', 15, 'bold'), width=8)
        tot_btn.grid(row=0, column=0, pady=15, padx=10)

        gen_btn = Button(f7, bd=5, bg=bg_color, fg='white',command=self.bill_area, text='Generate Bill', font=('times new roman', 15, 'bold'),
                         width=10)
        gen_btn.grid(row=0, column=1, pady=15, padx=10)

        clr_btn = Button(f7, bd=5, bg=bg_color, fg='white', text='Clear',command=self.clear_bill, font=('times new roman', 15, 'bold'), width=8)
        clr_btn.grid(row=0, column=2, pady=15, padx=10)

        exit_btn = Button(f7, bd=5, bg=bg_color, fg='white',command=self.exit_app, text='Exit', font=('times new roman', 15, 'bold'), width=8)
        exit_btn.grid(row=0, column=3, pady=15, padx=10)
        self.welcome_bill()



    def total(self):
        self.c_s_p = self.soap.get() * 40
        self.f_c_p = self.face_cream.get()*120
        self.f_w_p = self.face_wash.get()*60
        self.s_p = self.spray.get()*180
        self.gell_price = self.gell.get()*140
        self.loshan_price = self.loshan.get()*140
        self.rice_price = self.rice.get()*40
        self.f_o_p = self.food_oil.get()*20
        self.daal_price = self.daal.get()*30
        self.wheat_price = self.wheat.get()*50
        self.sugar_price = self.sugar.get()*10
        self.tea_price = self.tea.get()*15
        self.coke_price = self.coke.get()*20
        self.sprite_price = self.sprite.get()*40
        self.frooti_price = self.frooti.get()*30
        self.maaza_price = self.maaza.get()*40
        self.limca_price = self.limca.get()*50
        self.thumbsup_price = self.thumbsup.get()*60

        self.total_cosmetic_price = (
                     self.c_s_p+ self.f_c_p + self.f_w_p + self.s_p +
                    self.gell_price + self.loshan_price
            )
        self.c_tax = 0.05*self.total_cosmetic_price
        self.cosmetic_price.set('Rs ' + str(self.total_cosmetic_price))
        self.cosmetic_tax.set('Rs. '+str(0.05 * self.total_cosmetic_price))

        self.total_grocery_price=(
            self.rice_price+self.f_o_p+self.daal_price+self.wheat_price+self.sugar_price+self.tea_price
        )
        self.g_tax = 0.1*self.total_grocery_price
        self.grocery_price.set('Rs '+str(self.total_grocery_price))
        self.grocery_tax.set('Rs.'+str(0.1*self.total_grocery_price))

        self.total_colddrinks_price = (
            self.coke_price+self.sprite_price+self.frooti_price+self.maaza_price+self.limca_price+self.thumbsup_price
        )
        self.Cld_tax = 0.4*self.total_colddrinks_price
        self.colddrink_price.set('Rs '+str(self.total_colddrinks_price))
        self.colddrink_tax.set('Rs.'+str(0.4*self.total_colddrinks_price))

        self.total_bill = float(self.total_cosmetic_price+self.total_grocery_price+self.total_colddrinks_price
                                +self.c_tax+self.g_tax+self.Cld_tax)

    def welcome_bill(self):
        self.txtarea.delete('1.0', END)
        self.txtarea.insert(END,'\t\tWelcome to Billing')
        self.txtarea.insert(END, f'\nBill Number:{self.bill_no.get()}')
        self.txtarea.insert(END, f'\nCustomer Name:{self.cstname.get()}')
        self.txtarea.insert(END, f'\nPhone Number:{self.mobile.get()}')
        self.txtarea.insert(END,"\n===================================================")
        self.txtarea.insert(END,"\n\tProducts\t\tQty\t\tPrice(Rs)")
        self.txtarea.insert(END,"\n===================================================")

    def bill_area(self):
        if self.cstname.get()=="" or self.mobile.get()=="":
            messagebox.showerror("Error", "Please enter customer details.")
        elif self.cosmetic_price.get()=='Rs 0' and self.grocery_price.get()=='Rs 0' and self.colddrink_price=='Rs 0':
            messagebox.showerror("Error", "No product purchased!!")
        else:
            self.welcome_bill()
        if self.soap.get()!=0:
            self.txtarea.insert(END,f"\n\t Bath Soap\t\t{self.soap.get()}\t\t{self.c_s_p}")
        if self.face_cream.get() != 0:
            self.txtarea.insert(END, f"\n\t Face Cream\t\t{self.face_cream.get()}\t\t{self.f_c_p}")
        if self.face_wash.get() != 0:
            self.txtarea.insert(END, f"\n\t Face Wash\t\t{self.face_wash.get()}\t\t{self.f_w_p}")
        if self.spray.get() != 0:
            self.txtarea.insert(END, f"\n\t Hair Spray\t\t{self.spray.get()}\t\t{self.s_p}")
        if self.gell.get() != 0:
            self.txtarea.insert(END, f"\n\t Hair gell\t\t{self.gell.get()}\t\t{self.gell_price}")
        if self.loshan.get() != 0:
            self.txtarea.insert(END, f"\n\t Body Lotion\t\t{self.loshan.get()}\t\t{self.loshan_price}")

        if self.rice.get()!=0:
            self.txtarea.insert(END,f"\n\t Rice\t\t{self.rice.get()}\t\t{self.rice_price}")
        if self.food_oil.get() != 0:
            self.txtarea.insert(END, f"\n\t Food Oil\t\t{self.food_oil.get()}\t\t{self.f_o_p}")
        if self.daal.get() != 0:
            self.txtarea.insert(END, f"\n\t Daal\t\t{self.daal.get()}\t\t{self.daal_price}")
        if self.wheat.get() != 0:
            self.txtarea.insert(END, f"\n\t Wheat\t\t{self.wheat.get()}\t\t{self.wheat_price}")
        if self.sugar.get() != 0:
            self.txtarea.insert(END, f"\n\t Sugar\t\t{self.sugar.get()}\t\t{self.sugar_price}")
        if self.tea.get() != 0:
            self.txtarea.insert(END, f"\n\t Tea\t\t{self.tea.get()}\t\t{self.tea_price}")

        if self.maaza.get()!=0:
            self.txtarea.insert(END,f"\n\t Maaza\t\t{self.maaza.get()}\t\t{self.maaza_price}")
        if self.coke.get() != 0:
            self.txtarea.insert(END, f"\n\t Coke\t\t{self.coke.get()}\t\t{self.coke_price}")
        if self.frooti.get() != 0:
            self.txtarea.insert(END, f"\n\t Frooti\t\t{self.frooti.get()}\t\t{self.frooti_price}")
        if self.thumbsup.get() != 0:
            self.txtarea.insert(END, f"\n\t Thumbs up\t\t{self.thumbsup.get()}\t\t{self.thumbsup_price}")
        if self.limca.get() != 0:
            self.txtarea.insert(END, f"\n\t Limca\t\t{self.limca.get()}\t\t{self.limca_price}")
        if self.sprite.get() != 0:
            self.txtarea.insert(END, f"\n\t Sprite\t\t{self.sprite.get()}\t\t{self.sprite_price}")

        self.txtarea.insert(END, '\n===================================================')
        if self.cosmetic_tax.get()!='Rs. 0.0':
            self.txtarea.insert(END,f"Cosmetic Tax: \t\t\t\t\t{self.cosmetic_tax.get()}\n")
        if self.grocery_tax.get()!='Rs.0.0':
            self.txtarea.insert(END, f"Grocery Tax: \t\t\t\t\t{self.grocery_tax.get()}\n")
        if self.colddrink_tax!='Rs.0.0':
            self.txtarea.insert(END, f"Cold Drink Tax: \t\t\t\t\t{self.colddrink_tax.get()}")
        self.txtarea.insert(END,'\n===================================================')

        self.txtarea.insert(END, f'\nTotal Price: \t\t\t\t\t{self.total_bill}rs')
        self.save_bill()
    def add_data(self):
        con = mysql.connector.connect(host="localhost",user="root",passwd="Rajan@2ks",database="world")
        cur = con.cursor()
        sql = 'insert into bill values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        val = (self.cstname.get(),self.mobile.get(),self.bill_no.get(),self.soap.get(),self.face_cream.get(),self.face_wash.get(),self.spray.get(),self.gell.get(),self.loshan.get(),self.rice.get(),self.food_oil.get(),self.daal.get(),self.wheat.get(),self.sugar.get(),self.tea.get(),self.maaza.get(),self.coke.get(),self.frooti.get(),self.thumbsup.get(),self.limca.get(),self.sprite.get(),self.cosmetic_tax.get(),self.grocery_tax.get(),self.colddrink_tax.get(),(self.cosmetic_price.get()+self.grocery_price.get()+self.colddrink_price.get()))
        cur.execute(sql,val)
        print(cur.rowcount , "record inserted.")
        con.commit()
        con.close()

    def save_bill(self):
        op = messagebox.askyesno("Save Bill", "Do you want to save the bill?")
        if op>0:
            self.bill_data = self.txtarea.get('1.0', END)
            f1 = open("bills/"+str(self.bill_no.get())+".txt","w")
            f1.write(self.bill_data)
            f1.close()
            self.add_data()
            messagebox.showinfo("Saved", f"Bill no.{self.bill_no.get()} saved successfully")
        else:
            return

    def find_bill(self):
        present='no'
        for i in os.listdir("bills/"):
            if i.split('.')[0] == self.search_bill.get():
                f1=open(f"bills/{i}","r")
                self.txtarea.delete('1.0',END)
                for d in f1:
                    self.txtarea.insert(END,d)
                f1.close()
                present='yes'
        if present=='no':
            messagebox.showerror("Error","Invalid Bill No.")

    def clear_bill(self):
        # ========================Cosmetics============================
        self.soap.set(0)
        self.face_cream.set(0)
        self.face_wash.set(0)
        self.spray.set(0)
        self.gell.set(0)
        self.loshan.set(0)
        # =================================grocery======================================
        self.rice.set(0)
        self.food_oil.set(0)
        self.daal.set(0)
        self.wheat.set(0)
        self.sugar.set(0)
        self.tea.set(0)
        # =====================================cold drinks=============================
        self.maaza.set(0)
        self.coke.set(0)
        self.frooti.set(0)
        self.thumbsup.set(0)
        self.limca.set(0)
        self.sprite.set(0)
        # ===================================Totalproduct price and tax======================
        self.cosmetic_price.set("")
        self.grocery_price.set("")
        self.colddrink_price.set("")
        self.cosmetic_tax.set("")
        self.grocery_tax.set("")
        self.colddrink_tax.set("")
        # ======================================Customer=============================
        self.cstname.set("")
        self.mobile.set("")
        x = random.randint(1000, 9999)
        self.bill_no.set("")
        self.bill_no.set(str(x))
        self.search_bill.set("")
        self.welcome_bill()


    def exit_app(self):
        op = messagebox.askyesno("Exit", "Do you really want to exit?")
        if op>1:
            self.root.destroy()

root = Tk()
obj = Bill(root)
root.mainloop()