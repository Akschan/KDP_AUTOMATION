from Functions import KdpAuto
from Data import *


driver = KdpAuto.getdriver()
wait = KdpAuto.wait(driver)
long_wait = KdpAuto.longwait(driver)
super_long_wait = KdpAuto.superlongwait(driver)

automate = KdpAuto(personalinfos=Personalinfo,bookinfos=Bookinfos,paperback=Paperback,cover=Cover)
automate.Automation(driver,wait,long_wait,super_long_wait)