from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox



class Dashboard_Page(Frame):
    def __init__(self, *args):
        Frame.__init__(self, *args)

    def show(self):
        self.lift()


#Creating main frame class
class Student_Page(Dashboard_Page):
    def __init__(self, *args):
        Dashboard_Page.__init__(self, *args)
        #============================styling================================================

        #defining font
        fonts = "helvetica"
        #font size
        fs=10
        #font color
        fc="#FFCE00"

        #window background color
        b_color = "#1A1A1D"
        #inside frame color
        b2_color="#343439"

        #defining button color
        button_color = "#FFCE00"
        button_font_color=b_color
        button_size=10

        # CREATING Style variable
        style = ttk.Style()

        #creating comobox styling
        style.theme_create('combostyle', parent='alt',
                                settings={'TCombobox':
                                              {'configure':
                                                   {'selectbackground': '#5783B3',
                                                    'fieldbackground': b2_color,
                                                    'background': button_color,
                                                    "foreground": fc,

                                                    }}})
        style.theme_use('combostyle')
        #Combobox end


        #creating tree view styling
        style.configure("Treeview",bg="red",activefrontground="red",fieldbackground=b2_color,font=(fonts,fs),activeforground="red")
        style.configure("Treeview.Heading", background=button_color, foreground=b_color,font=(fonts,fs,"bold"))
        #Tree view end

        #===============================styling end======================================

        # ====================creating main_frame===========================================
        main_frame = Frame(self, bg=b_color)
        main_frame.pack(fill=BOTH,expand=True)
        # =======================frame end==================================================

        # =============creating detail_frame================================================
        detail_frame = Frame(main_frame, bg=b_color)
        detail_frame.pack(side=TOP,fill=BOTH,expand=True)
        # frame end

        # ============defing variables all text variable==================
        self.first_name = StringVar()
        self.last_name = StringVar()
        self.father_name = StringVar()
        self.roll_no = StringVar()
        self.contact_no = StringVar()
        self.cnic_no = StringVar()
        self.dob = StringVar()
        self.email = StringVar()
        self.gender_var = StringVar()
        self.clas_var = StringVar()
        self.sec_var = StringVar()
        self.address = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        #==========================creating button frame=========================
        detail_button_frame= Frame(detail_frame, bg=b_color)
        detail_button_frame.pack(side=TOP,fill=X)

        # creating search by lable
        searchby_label = Label(detail_button_frame, text="Search by", bg=b_color, fg=fc, font=(fonts, fs,"bold"))
        searchby_label.grid(row=0, column=0, padx=5)

        searchby = ttk.Combobox(detail_button_frame, textvariable = self.search_by, value=["Roll_no", "CNIC_no", "First_Name"], font=(fonts, fs))
        searchby['state'] = 'readonly'
        searchby.grid(row=0, column=1,sticky="news",pady=7)
        # lable end

        # creating search entery widgit
        searchby_entery = Entry(detail_button_frame, textvariable = self.search_txt, width=20, font=(fonts, fs), bg=b2_color, fg=fc)
        searchby_entery.grid(row=0, column=2, padx=10)
        # entery widgit ends

        # creating search button
        search_butoon = Button(detail_button_frame, text="SEARCH", bg=button_color, fg=button_font_color, font=(fonts, button_size-2,"bold"), width=9,
                               cursor="hand2", activebackgroun=button_color, activeforeground=button_font_color,command = self.search_data)
        search_butoon.grid(row=0, column=3, padx=10, pady=5)
        # button end

        # creating show button
        show_butoon = Button(detail_button_frame, text="SHOW ALL", bg=button_color, fg=button_font_color, font=(fonts, button_size-2,"bold"),
                             cursor="hand2", activebackgroun=button_color, activeforeground=button_font_color,command = self.fetch_data)
        show_butoon.grid(row=0, column=4,padx=5)
        # button end

        #====================detail button frame ends===========================================

        # =============creating data_viewer_frame==================================================

        data_viewer_frame = Frame(detail_frame, bd=2, relief="ridge", bg=b_color)
        data_viewer_frame.pack(fill=BOTH,expand=True,after=detail_button_frame)
        # frame end

        # =============ceating scroll bars==================
        scroll_x = Scrollbar(data_viewer_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_viewer_frame, orient=VERTICAL)
        # ==================scroll bar ends=================

        # ================creating student table===============================================
        self.student_table = ttk.Treeview(data_viewer_frame,
                                     columns=("roll", "first_name","last_name","father_name", "cnic","contact","email", "dob","clas","sec" , "gender","ad"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        # sscroll bar ends

        # defining hedings to be shown
        self.student_table.heading("roll", text="ROll NO")
        self.student_table.heading("first_name", text="FIRTS NAME")
        self.student_table.heading("last_name", text="LAST NAME")
        self.student_table.heading("father_name", text="FATHER NAME")
        self.student_table.heading("cnic", text="CNIC")
        self.student_table.heading("contact", text="CONTACT")
        self.student_table.heading("email", text="EMAIL")
        self.student_table.heading("dob", text="D.O.B")
        self.student_table.heading("clas", text="ClASS")
        self.student_table.heading("sec", text="SECTION")
        self.student_table.heading("gender", text="GENDER")
        self.student_table.heading("ad", text="ADDRESS")

        # only giving heading will be shown
        self.student_table["show"] = "headings"

        # changing width of columnns
        self.student_table.column("roll", width=50,anchor="center")
        self.student_table.column("first_name", width=100,anchor="center")
        self.student_table.column("last_name", width=100,anchor="center")
        self.student_table.column("father_name", width=100,anchor="center")
        self.student_table.column("clas", width=50,anchor="center")
        self.student_table.column("sec", width=50,anchor="center")
        self.student_table.column("gender", width=50,anchor="center")
        self.student_table.column("contact", width=100,anchor="center")
        self.student_table.column("email", width=100,anchor="center")
        self.student_table.column("cnic", width=100,anchor="center")
        self.student_table.column("dob", width=100,anchor="center")
        self.student_table.column("ad", width=100,anchor="center")

        self.fetch_data()
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)

        self.student_table.pack(fill=BOTH, expand=1)
        # =====================date_viewer_frame end==========================================

        # =======================creating form_frame=================================================
        main_forme_farme=Frame(main_frame, bg=b_color)
        main_forme_farme.pack(side=BOTTOM,fill=X)

        #========================creating inner responsive to outer frame=============================
        form_frame = Frame(main_forme_farme, bg=b_color)
        form_frame.pack(fill=X)
        # frame end

        #First Name Lable
        f_name_label=Label(form_frame,text="FIRST NAME",fg=fc,bg=b_color,font=(fonts ,fs))
        f_name_label.grid(row=0,column=0,pady=10,ipadx=5)

        f_name_entery=Entry(form_frame,textvariable = self.first_name,font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        f_name_entery.grid(row=0,column=1,sticky="ew",padx=10)
        #lable end

        #setting cursor to focus on FIRST NAME
        f_name_entery.focus()

        # Last Name Lable
        l_name_label = Label(form_frame, text="LAST NAME", fg=fc, bg=b_color, font=(fonts ,fs))
        l_name_label.grid(row=0, column=2)

        l_name_entery = Entry(form_frame, textvariable = self.last_name, font=( fonts,fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        l_name_entery.grid(row=0, column=3,sticky="ew",padx=10)
        # lable end

        # Father Name Lable
        father_name_label = Label(form_frame, text="FATHER NAME", fg=fc, bg=b_color, font=(fonts,fs))
        father_name_label.grid(row=0, column=4)

        father_name_entery = Entry(form_frame, textvariable = self.father_name,font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        father_name_entery.grid(row=0, column=5,sticky="ew",padx=10)
        # lable end

        #  roll no Lable
        roll_no_label = Label(form_frame, text="ROLL NO", fg=fc, bg=b_color, font=(fonts,fs))
        roll_no_label.grid(row=0, column=6, pady=4)

        roll_no_entery = Entry(form_frame, textvariable = self.roll_no, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        roll_no_entery.grid(row=0, column=7,sticky="ew",padx=10)
        # lable end

        #  citizen no Lable
        cnic_label = Label(form_frame, text="CNIC NO", fg=fc, bg=b_color, font=(fonts, fs))
        cnic_label.grid(row=1, column=0)

        cnic_entery = Entry(form_frame, textvariable = self.cnic_no, font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        cnic_entery.grid(row=1, column=1,sticky="ew",padx=10)
        # lable end

        #  contact Lable
        contact_label = Label(form_frame, text="CONTACT", fg=fc, bg=b_color, font=(fonts,fs))
        contact_label.grid(row=1, column=2)

        contact_entery = Entry(form_frame, textvariable = self.contact_no, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        contact_entery.grid(row=1, column=3,sticky="ew",padx=10)
        # lable end

        #  D.O.B Lable
        dob_label = Label(form_frame, text="DATE OF BIRTH", fg=fc, bg=b_color, font=(fonts,fs))
        dob_label.grid(row=1, column=4)

        dob_entery = Entry(form_frame, textvariable = self.dob, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        dob_entery.grid(row=1, column=5,sticky="ew",padx=10)
        # lable end

        #  email Lable
        email_label = Label(form_frame, text="EMAIL", fg=fc, bg=b_color, font=(fonts, fs))
        email_label.grid(row=1, column=6)

        email_entery = Entry(form_frame, textvariable = self.email,font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        email_entery.grid(row=1, column=7,sticky="ew",padx=10)
        # lable end

        # gender Lable
        gender_label = Label(form_frame, text="GENDER", fg=fc, bg=b_color, font=(fonts,fs))
        gender_label.grid(row=2, column=0,pady=10)


        gender = ttk.Combobox(form_frame, textvariable = self.gender_var, value=["MALE", "FEMALE", "OTHER"], font=(fonts, fs))
        gender['state'] = 'readonly'
        gender.grid(row=2, column=1, sticky="ew",padx=10)
        # lable end

        # class Lable
        clas_label = Label(form_frame, text="CLASS", fg=fc, bg=b_color, font=(fonts, fs))
        clas_label.grid(row=2, column=2)

        clas = ttk.Combobox(form_frame, textvariable = self.clas_var, value=["4" ,"5", "6","7"], font=(fonts, fs))
        clas['state'] = 'readonly'
        clas.grid(row=2, column=3,  sticky="ew",padx=10)
        # lable end

        # SEC Lable
        sec_label = Label(form_frame, text="SECTION", fg=fc, bg=b_color, font=(fonts, fs))
        sec_label.grid(row=2, column=4, pady=5)

        sec = ttk.Combobox(form_frame, textvariable = self.sec_var, value=["A", "B", "C"], font=(fonts, fs))
        sec['state'] = 'readonly'
        sec.grid(row=2, column=5,  sticky="ew",padx=10)
        # lable end


        #  address Lable
        ad_label = Label(form_frame, text="ADDRESS", fg=fc, bg=b_color, font=(fonts, fs))
        ad_label.grid(row=2, column=6)

        ad_entery = Entry(form_frame, textvariable = self.address, font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        ad_entery.grid(row=2, column=7,sticky="ew",padx=10)
        # lable end

        #===============================form frame end==========================================

        # =========================creating button_frame=========================================
        button_frame = Frame(main_forme_farme, bg=b_color)
        button_frame.pack(after=form_frame)
        # frame end


        #creating back button
        backbtn = Button(button_frame, text="BACK", font=(fonts, button_size - 1, "bold"), width=10,
                        bg=button_color, fg=b_color
                        , cursor="hand2", activebackgroun=button_color, activeforeground=b_color)
        backbtn.grid(row=0, column=0, padx=25,ipadx=10, pady=10)
        # button end

        #creating add button
        addbtn=Button(button_frame,text="ADD",font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=b_color
                      ,cursor="hand2",activebackgroun=button_color,activeforeground=b_color,command=self.add_student)
        addbtn.grid(row=0,column=1,padx=25,ipadx=10,)
        #button enda

        # creating update button
        updatebtn = Button(button_frame, text="UPDATE", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                           ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color,command = self.update_student)
        updatebtn.grid(row=0, column=2,padx=25,ipadx=10,)
        # button end

        # creating delete button
        deletebtn = Button(button_frame, text="DELETE", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                           ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color,command = self.delete_data)
        deletebtn.grid(row=0, column=3, padx=25,ipadx=10,)
        # button end

        # creating clear button
        clearbtn = Button(button_frame, text="CLEAR", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                          ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color,command = self.clear)
        clearbtn.grid(row=0, column=4, padx=25,ipadx=10)
        # button end
        # ================================button frame end============================

        # ================================making form frame risponsive===========
        form_frame.grid_columnconfigure(0, weight=0)
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(2, weight=0)
        form_frame.grid_columnconfigure(3, weight=1)
        form_frame.grid_columnconfigure(4, weight=0)
        form_frame.grid_columnconfigure(5, weight=1)
        form_frame.grid_columnconfigure(6, weight=0)
        form_frame.grid_columnconfigure(7, weight=1)

    # ============defining all buttons funvtions=================
    def clear(self):
        self.first_name.set("")
        self.last_name.set("")
        self.father_name.set("")
        self.cnic_no.set("")
        self.contact_no.set("")
        self.roll_no.set("")
        self.address.set("")
        self.clas_var.set("")
        self.sec_var.set("")
        self.dob.set("")
        self.email.set("")
        self.gender_var.set("")

    def add_student(self):
        if (self.roll_no.get() == "" or self.first_name.get() =="" or self.last_name.get() == "" or self.father_name.get() == "" or
                self.cnic_no.get() == "" or self.dob.get() == "" or self.email.get() == "" or
                self.address.get() == "" or self.clas_var.get() == '' or self.sec_var.get() == "" or
                self.gender_var.get() == "" or self.contact_no.get() == ''):
            messagebox.showerror("Error","All fields are required")
        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="stm")
            cur = con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.roll_no.get(),
                self.first_name.get(),
                self.last_name.get(),
                self.father_name.get(),
                self.cnic_no.get(),
                self.contact_no.get(),
                self.email.get(),
                self.dob.get(),
                self.clas_var.get(),
                self.sec_var.get(),
                self.gender_var.get(),
                self.address.get()
            ))
            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("Congratulation", "Record has been insterted")

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row=contents["values"]
        self.roll_no.set(row[0])
        self.first_name.set(row[1])
        self.last_name.set(row[2])
        self.father_name.set(row[3])
        self.cnic_no.set(row[4])
        self.contact_no.set(row[5])
        self.email.set(row[6])
        self.dob.set(row[7])
        self.clas_var.set(row[8])
        self.sec_var.set(row[9])
        self.gender_var.set(row[10])
        self.address.set(row[11])


    def update_student(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("update students set first_name = %s,"
                    " last_name = %s,"
                    " father_name = %s,"
                    " cnic_no = %s,"
                    " contact_no =  %s,"
                    " email = %s,"
                    " dob = %s,"
                    " class = %s,"
                    " sec = %s, "
                    "gender = %s,"
                    " address = %s where roll_no = %s   ",
                    (
            self.first_name.get(),
            self.last_name.get(),
            self.father_name.get(),
            self.cnic_no.get(),
            self.contact_no.get(),
            self.email.get(),
            self.dob.get(),
            self.clas_var.get(),
            self.sec_var.get(),
            self.gender_var.get(),
            self.address.get(),
            self.roll_no.get()
        ))
        con.commit()
        self.fetch_data()
        con.close()

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("delete from students where roll_no = %s",self.roll_no.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="stm")
        cur = con.cursor()
        cur.execute("select * from students where" + str(self.search_by.get()) + "LIKE'%" + str(self.search_txt.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            con.commit()
        con.close()
    #===================functions ends=========================
class Teacher_page(Frame):
    def __init__(self, *args):
        Dashboard_Page.__init__(self, *args)
        #============================styling================================================

        #defining fonts
        fonts = "helvetica"
        #font size
        fs=10
        #font color
        fc="#FFCE00"

        # window background color
        b_color = "#1A1A1D"
        #inside frame color
        b2_color="#343439"

        #defining button color
        button_color = "#FFCE00"
        button_font_color=b_color
        button_size=10


        # ====================creating main_frame===========================================
        main_frame = Frame(self, bg=b_color)
        main_frame.pack(fill=BOTH,expand=True)
        # =======================frame end==================================================

        # =============creating detail_frame================================================
        detail_frame = Frame(main_frame, bg=b_color)
        detail_frame.pack(side=TOP,fill=BOTH,expand=True)
        # frame end

        #==========================creating button frame=========================
        detail_button_frame= Frame(detail_frame, bg=b_color)
        detail_button_frame.pack(side=TOP,fill=X)

        # creating search by lable
        searchby_label = Label(detail_button_frame, text="Search by", bg=b_color, fg=fc, font=(fonts, fs,"bold"))
        searchby_label.grid(row=0, column=0, padx=5)

        searchby = ttk.Combobox(detail_button_frame, value=["Roll no", "Contact no", "CNIC", "Name"], font=(fonts, fs))
        searchby['state'] = 'readonly'
        searchby.grid(row=0, column=1,sticky="news",pady=7)
        # lable end

        # creating search entery widgit
        searchby_entery = Entry(detail_button_frame, width=20, font=(fonts, fs), bg=b2_color, fg=fc)
        searchby_entery.grid(row=0, column=2, padx=10)
        # entery widgit ends

        # creating search button
        search_butoon = Button(detail_button_frame, text="SEARCH", bg=button_color, fg=button_font_color, font=(fonts, button_size-2,"bold"), width=9,
                               cursor="hand2", activebackgroun=button_color, activeforeground=button_font_color)
        search_butoon.grid(row=0, column=3, padx=10, pady=5)
        # button end

        # creating show button
        show_butoon = Button(detail_button_frame, text="SHOW ALL", bg=button_color, fg=button_font_color, font=(fonts, button_size-2,"bold"),
                             cursor="hand2", activebackgroun=button_color, activeforeground=button_font_color)
        show_butoon.grid(row=0, column=4,padx=5)
        # button end

        #====================detail button frame ends===========================================

        # =============creating data_viewer_frame==================================================

        data_viewer_frame = Frame(detail_frame, bd=2, relief="ridge", bg=b_color)
        data_viewer_frame.pack(fill=BOTH,expand=True,after=detail_button_frame)
        # frame end

        # =============ceating scroll bars==================
        scroll_x = Scrollbar(data_viewer_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(data_viewer_frame, orient=VERTICAL)
        # ==================scroll bar ends=================

        # ================creating student table===============================================
        teacher_table = ttk.Treeview(data_viewer_frame,
                                     columns=("s.no", "name","f_name","col","clas" , "gender","contact","email", "cnic", "dob","ad"),
                                     xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=teacher_table.xview)
        scroll_y.config(command=teacher_table.yview)
        # sscroll bar ends

        # defining hedings to be shown
        teacher_table.heading("s.no", text="S.NO")
        teacher_table.heading("name", text="NAME")
        teacher_table.heading("f_name", text="FATHER NAME")
        teacher_table.heading("col", text="COLIFICATION")
        teacher_table.heading("clas", text="ClASS")
        teacher_table.heading("gender", text="GENDER")
        teacher_table.heading("contact", text="CONTACT")
        teacher_table.heading("email", text="EMAIL")
        teacher_table.heading("cnic", text="CNIC")
        teacher_table.heading("dob", text="D.O.B")
        teacher_table.heading("ad", text="ADDRESS")

        # only giving heading will be shown
        teacher_table["show"] = "headings"

        # changing width of columnns
        teacher_table.column("s.no", width=20)
        teacher_table.column("name", width=100)
        # father name column
        teacher_table.column("f_name", width=100)
        #colification column
        teacher_table.column("col", width=50)
        teacher_table.column("clas", width=20)
        teacher_table.column("gender", width=20)
        teacher_table.column("contact", width=50)
        teacher_table.column("email", width=70)
        teacher_table.column("cnic", width=70)
        teacher_table.column("dob", width=50)
        teacher_table.column("ad", width=100)

        teacher_table.pack(fill=BOTH, expand=1)
        # =====================date_viewer_frame end==========================================

        # =======================creating form_frame=================================================
        main_forme_farme=Frame(main_frame, bg=b_color)
        main_forme_farme.pack(side=BOTTOM,fill=X)

        #========================creating inner responsive to oyter frame=============================
        form_frame = Frame(main_forme_farme, bg=b_color)
        form_frame.pack(fill=X)
        # frame end

        #First Name Lable
        f_name_label=Label(form_frame,text="FIRST NAME",fg=fc,bg=b_color,font=(fonts ,fs))
        f_name_label.grid(row=0,column=0,pady=10,ipadx=5)

        f_name_entery=Entry(form_frame,font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        f_name_entery.grid(row=0,column=1,sticky="ew",padx=10)
        #lable end

        #setting cursor to focus on FIRST NAME
        f_name_entery.focus()

        # Last Name Lable
        l_name_label = Label(form_frame, text="LAST NAME", fg=fc, bg=b_color, font=(fonts ,fs))
        l_name_label.grid(row=0, column=2)

        l_name_entery = Entry(form_frame, font=( fonts,fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        l_name_entery.grid(row=0, column=3,sticky="ew",padx=10)
        # lable end

        # Father Name Lable
        father_name_label = Label(form_frame, text="FATHER NAME", fg=fc, bg=b_color, font=(fonts,fs))
        father_name_label.grid(row=0, column=4)

        father_name_entery = Entry(form_frame,font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        father_name_entery.grid(row=0, column=5,sticky="ew",padx=10)
        # lable end

        #  serial no Lable
        s_no_label = Label(form_frame, text="SERIAL NO", fg=fc, bg=b_color, font=(fonts,fs))
        s_no_label.grid(row=0, column=6, pady=4)

        s_no_entery = Entry(form_frame, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        s_no_entery.grid(row=0, column=7,sticky="ew",padx=10)
        # lable end

        #  citizen no Lable
        cnic_label = Label(form_frame, text="CNIC NO", fg=fc, bg=b_color, font=(fonts, fs))
        cnic_label.grid(row=1, column=0)

        cnic_entery = Entry(form_frame, font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        cnic_entery.grid(row=1, column=1,sticky="ew",padx=10)
        # lable end

        #  contact Lable
        contact_label = Label(form_frame, text="CONTACT", fg=fc, bg=b_color, font=(fonts,fs))
        contact_label.grid(row=1, column=2)

        contact_entery = Entry(form_frame, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        contact_entery.grid(row=1, column=3,sticky="ew",padx=10)
        # lable end

        #  D.O.B Lable
        dob_label = Label(form_frame, text="DATE OF BIRTH", fg=fc, bg=b_color, font=(fonts,fs))
        dob_label.grid(row=1, column=4)

        dob_entery = Entry(form_frame, font=(fonts, fs),bd=2,relief=RIDGE,bg=b2_color,fg=fc)
        dob_entery.grid(row=1, column=5,sticky="ew",padx=10)
        # lable end

        #  email Lable
        email_label = Label(form_frame, text="EMAIL", fg=fc, bg=b_color, font=(fonts, fs))
        email_label.grid(row=1, column=6)

        email_entery = Entry(form_frame,font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        email_entery.grid(row=1, column=7,sticky="ew",padx=10)
        # lable end

        # gender Lable
        gender_label = Label(form_frame, text="GENDER", fg=fc, bg=b_color, font=(fonts,fs))
        gender_label.grid(row=2, column=0,pady=10)


        gender = ttk.Combobox(form_frame, value=["MALE", "FEMALE", "OTHER"], font=(fonts, fs))
        gender['state'] = 'readonly'
        gender.grid(row=2, column=1, sticky="ew",padx=10)
        # lable end

        # class Lable
        clas_label = Label(form_frame, text="CLASS", fg=fc, bg=b_color, font=(fonts, fs))
        clas_label.grid(row=2, column=2)

        clas = ttk.Combobox(form_frame, value=["4" ,"5", "6","7"], font=(fonts, fs))
        clas['state'] = 'readonly'
        clas.grid(row=2, column=3,  sticky="ew",padx=10)
        # lable end

        # colificationn Lable
        col_label = Label(form_frame, text="COLIFICATION", fg=fc, bg=b_color, font=(fonts, fs))
        col_label.grid(row=2, column=4, pady=5)

        col = ttk.Combobox(form_frame, value=["Matric", "Intermediate", "Bacholars","Masters"], font=(fonts, fs))
        col['state'] = 'readonly'
        col.grid(row=2, column=5,  sticky="ew",padx=10)
        # lable end


        #  address Lable
        ad_label = Label(form_frame, text="ADDRESS", fg=fc, bg=b_color, font=(fonts, fs))
        ad_label.grid(row=2, column=6)

        ad_entery = Entry(form_frame, font=(fonts, fs), bd=2, relief=RIDGE, bg=b2_color, fg=fc)
        ad_entery.grid(row=2, column=7,sticky="ew",padx=10)
        # lable end

        #===============================form frame end==========================================

        # =========================creating button_frame=========================================
        button_frame = Frame(main_forme_farme, bg=b_color)
        button_frame.pack(after=form_frame)
        # frame end

        #creating back button
        backbtn = Button(button_frame, text="BACK", font=(fonts, button_size - 1, "bold"), width=10,
                        bg=button_color, fg=b_color
                        , cursor="hand2", activebackgroun=button_color, activeforeground=b_color)
        backbtn.grid(row=0, column=0, padx=25,ipadx=10, pady=10)
        # button end

        #creating add button
        addbtn=Button(button_frame,text="ADD",font=(fonts, button_size-1,"bold","bold"),width=10,bg=button_color,fg=b_color
                      ,cursor="hand2",activebackgroun=button_color,activeforeground=b_color)
        addbtn.grid(row=0,column=1,padx=25,ipadx=10,)
        #button end

        # creating update button
        updatebtn = Button(button_frame, text="UPDATE", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                           ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color)
        updatebtn.grid(row=0, column=2,padx=25,ipadx=10,)
        # button end

        # creating delete button
        deletebtn = Button(button_frame, text="DELETE", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                           ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color)
        deletebtn.grid(row=0, column=3, padx=25,ipadx=10,)
        # button end

        # creating clear button
        clearbtn = Button(button_frame, text="CLEAR", font=(fonts, button_size-1,"bold"),width=10,bg=button_color,fg=button_font_color
                          ,cursor="hand2",activebackgroun=button_color,activeforeground=button_font_color)
        clearbtn.grid(row=0, column=4, padx=25,ipadx=10)
        # button end
        # ================================button frame end============================

        # ================================making form frame risponsive===========
        form_frame.grid_columnconfigure(0, weight=0)
        form_frame.grid_columnconfigure(1, weight=1)
        form_frame.grid_columnconfigure(2, weight=0)
        form_frame.grid_columnconfigure(3, weight=1)
        form_frame.grid_columnconfigure(4, weight=0)
        form_frame.grid_columnconfigure(5, weight=1)
        form_frame.grid_columnconfigure(6, weight=0)
        form_frame.grid_columnconfigure(7, weight=1)




class MainView(Frame):
    def __init__(self, *args):
        Frame.__init__(self, *args)
        # Pages Links

        Page_1 = Teacher_page(self)
        Page_2 = Student_Page(self)

        # Dashboard Frame Start
        Dashboard_Frame = Frame(self,bg="#FFCE00")
        Dashboard_Label = Label(Dashboard_Frame, text="DASHBOARD",
                                bg="#FFCE00", fg="#1A1A1D",font=("helvetica",15,"bold"), width=10)
        Dashboard_Label.grid(row=0, column=0, pady=20,sticky=EW)
        Dashboard_Frame.pack(side="left",fill="y")

        # Click Button and Show data
        Right_Data_Insert_Screen_Frame = Frame(self,bg="#343439")
        Right_Data_Insert_Screen_Frame.pack(side="right",fill="both",expand=True)


        Page_2.place(in_=Right_Data_Insert_Screen_Frame,
                     x=0, y=0 ,relwidth=1, relheight=1)
        Page_1.place(in_=Right_Data_Insert_Screen_Frame,
                     x=0, y=0, relwidth=1, relheight=1)

        # Teacher Button and Show Data
        Student_Area_Button = Button(
            Dashboard_Frame, text="STUDENT AREA",width="16",bg = "#FFCE00",activeforeground = "#1A1A1D",activebackground = "#FFCE00",
            font = ("helvetica",10,"bold"),cursor = "hand2",command=Page_2.lift)
        Student_Area_Button.grid(
            row=1, column=0, padx=5, pady=10)

        # Teacher Button and Show Data
        Teacher_Area_Button = Button(
            Dashboard_Frame, text="TEACHER AREA",width=16,bg = "#FFCE00",activeforeground = "#1A1A1D",activebackground = "#FFCE00",
            font = ("helvetica",10,"bold"),cursor = "hand2",command=Page_1.lift)
        Teacher_Area_Button.grid(
            row=2, column=0, padx=5)
        # Dashboard Frame End



window=Tk()

# title of main windw
window.title("School Managment System")

window.configure(bg="#3D3D3D")

window.state('zoomed')
# main windws finished

# creating boject for class
Object = MainView(window)
Object.pack(fill="both", expand=True)

window.mainloop()
