from tkinter.messagebox import showerror
import re


def checkmail(email):

    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        showerror(title="Error", message="Please enter a valid email")


def checkphone(phone):


    if not re.match(r'[789]\d{9}$', phone):
        showerror(title="Error", message="Please enter a valid Phone number")


def checkname(name):
    if not re.match('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        showerror(title="Error", message="Please enter a valid Name")


def checkProduct(product):
    if product is None:
        showerror(title="Error", message="Please select the product for review")


def checkdob(dob):
    if not re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', dob):
        showerror(title="Error", message="Please enter Date Of Birth in [dd/mm/yyy] format ")

