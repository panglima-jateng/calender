#!/usr/bin/python

# module
import os,sys,time,calendar
from os import system
from time import sleep

# tampilan
banner = """
===============================================
 {•} Author : Panglima Jateng
 {•} Team   : Codingers indonesia Hunter
 {•} Pesan  : Gak Ngoding Gak Makan
=============================================="""
system("clear")
system("figlet Calender")
print(banner)
#input
tahun = int(input("Tahun > "))
bulan = int(input("Bulan > "))
# out put
print(calendar.month(tahun, bulan))
