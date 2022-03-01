from Functions import KdpAuto
from Data import *
from Functions import Data
import concurrent.futures
import threading

data = Data(filepath=books_data_path)
books = data.two_books()


def thread(book):
    driver = KdpAuto.getdriver()
    KdpAuto(personalinfos=Personalinfo, bookinfos=book, paperback=Paperback, cover=Cover).Automate(driver)