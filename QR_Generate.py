###############imports###########
# pip install qrcode
# pip install pillow
# pip install python-resize-image


import qrcode
from tkinter import *
from PIL import Image, ImageTk
from resizeimage import resizeimage

class Or_Generator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("900x500+200+50")
        self.root.title("Qr-Code Generator | Create My Mehadi")
        self.root.resizable(False, False)

        title = Label(self.root, text="Qr Code Generator", font=("times new roman", 40), bg='#ff0000', fg='white',
                      anchor='w').place(x=0, y=0, relwidth=1)

        self.var_emp_code = StringVar()
        self.var_name = StringVar()
        self.var_department = StringVar()
        self.var_designation = StringVar()

        emp_Framr = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        emp_Framr.place(x=50, y=100, width=500, height=380)

        emp_title = Label(emp_Framr, text="Developers Details", font=("goudy old style", 30), bg='#ff0000',
                          fg='white').place(x=0, y=0, relwidth=1)

        lbl_emp_code = Label(emp_Framr, text="Developer ID", font=("times new roman", 19, 'bold'), bg='white').place(
            x=20, y=60)
        lbl_name = Label(emp_Framr, text="Name", font=("times new roman", 19, 'bold'), bg='white').place(x=20, y=100)
        lbl_department = Label(emp_Framr, text="Department", font=("times new roman", 19, 'bold'), bg='white').place(
            x=20, y=140)
        lbl_designation = Label(emp_Framr, text="Designation", font=("times new roman", 19, 'bold'), bg='white').place(
            x=20, y=180)

        txt_emp_code = Entry(emp_Framr, text="Developer ID", font=("times new roman", 15),
                             textvariable=self.var_emp_code, bg='lightyellow').place(x=200, y=60)
        txt_name = Entry(emp_Framr, font=("times new roman", 15), textvariable=self.var_name, bg='lightyellow').place(
            x=200, y=100)
        txt_department = Entry(emp_Framr, font=("times new roman", 15), textvariable=self.var_department,
                               bg='lightyellow').place(x=200, y=140)
        txt_designation = Entry(emp_Framr, font=("times new roman", 15), textvariable=self.var_designation,
                                bg='lightyellow').place(x=200, y=180)

        btn_generate = Button(emp_Framr, text="QR Generate", command=self.generate,
                              font=("times new roman", 18, 'bold'), bg="#56c2eb", fg='white').place(x=90, y=250,
                                                                                                    width=180,
                                                                                                    height=30)
        btn_clear = Button(emp_Framr, text="Clear", command=self.clear, font=("times new roman", 18, 'bold'),
                           bg="#56c2eb", fg='white').place(x=280, y=250, width=120, height=30)

        self.msg = ""
        self.lbl_msg = Label(emp_Framr, text=self.msg, font=("times new roman", 20), bg='white', fg='green')
        self.lbl_msg.place(x=0, y=310, relwidth=1)

        qr_Framr = Frame(self.root, bd=2, relief=RIDGE, bg='white')
        qr_Framr.place(x=600, y=100, width=250, height=380)
        emp_title = Label(qr_Framr, text="Developers QR Code", font=("goudy old style", 18), bg='#ff0000',
                          fg='white').place(x=0, y=0, relwidth=1)

        self.qr_code = Label(qr_Framr, text=" No QR \nAvailable", font=("times new roamn", 15), bg='#2009f7',
                             fg='white', bd=1, relief=RIDGE)
        self.qr_code.place(x=35, y=100, width=180, height=180)

    def clear(self):

        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_department.set('')
        self.var_designation.set('')
        self.msg = ''
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image="")

    def generate(self):
        if self.var_designation.get() == '' or self.var_emp_code.get() == '' or self.var_department.get() == '' or self.var_name.get() == '':
            self.msg = 'All Fields are Required!!!!'
            self.lbl_msg.config(text=self.msg, fg='red')


        else:
            qr_data=(f"Emoloyee ID: {self.var_emp_code.get()}\nEmployee Name: {self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation : {self.var_designation.get()} ")
            qr_code=qrcode.make(qr_data)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save(""+str(self.var_emp_code.get())+'.png')

            self.im=ImageTk.PhotoImage(file=""+str(self.var_emp_code.get())+'.png')
            self.qr_code.config(image=self.im)

            self.msg='QR Generate Successfully!!!!!!!'
            self.lbl_msg.config(text=self.msg,fg='green')




root = Tk()
obj = Or_Generator(root)
root.mainloop()
