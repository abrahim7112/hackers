
# Import Module
import tkinter
from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from time import strftime
from tkinter import ttk

from tkinter import *
from tkinter import messagebox
import requests
import json
from tkinter import filedialog

import webbrowser
from tkinter import END, Text
import tkinter.simpledialog as sd
from tkterminal import Terminal


class home: 
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry('1350x700+0+0')
        self.frame1 = tkinter.Label(self.root,width = 400,height = 400,bg = 'black')
        self.frame1.pack()
        self.root.title("hackers")
        menu = Menu(self.root)
        self.root.config(menu=menu)
        file = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='File', menu = file)
        file.add_command(label ='New File', command = home)
        def browseFiles():
            filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files",".txt"),("all files","*.*")))
            label_file_explorer.configure(text="File Opened: "+filename)
        file.add_command(label ='Open...', command = browseFiles)
        file.add_command(label ='Save', command = None)
        file.add_separator()
        file.add_command(label ='Exit', command = self.root.destroy)
        # Adding Edit Menu and commands
        edit = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Edit', menu = edit)
        edit.add_command(label ='Cut', command = None)
        edit.add_command(label ='Copy', command = None)
        edit.add_command(label ='Paste', command = None)
        edit.add_command(label ='Select All', command = None)
        edit.add_separator()
        edit.add_command(label ='Find...', command = None)
        edit.add_command(label ='Find again', command = None)
        # Adding tooles Menu
        tooles = Menu(menu, tearoff = 0)
        menu.add_cascade(label ='Tooles', menu = tooles)
        def firefox(): 
            link = 'https://www.google.com'
            firefox = webbrowser.Mozilla("firefox")
            firefox.open(link)
        tooles.add_command(label ='open firefox', command = firefox)
        '''
        def sqlmap():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#d89239"  )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="work apron sqlmap", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="#ba6a04", fg="black").pack(fill=X)
            Hacher_des = Label(F2, text="sqlmap is an open source penetration testing tool that automates the process of detecting and exploiting SQL injection flaws and taking \nover of database servers. It comes with a powerful detection engine, many niche features for the ultimate penetration tester, and a broad range of \nswitches including database fingerprinting, over data fetching from the database, accessing the underlying file system,\n and executing commands on the operating system via out-of-band connections.", font=("arial", 10, "bold"), bd=7, relief=GROOVE, bg="white", fg="#404040").pack(fill=X)
            Hacher_part = LabelFrame(F2, text="commands sqlmap", font=("arial", 10, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_part.place(x=2, y=130, relwidth=0.26, relheight=0.77)
            p_part = Label(F2, text="Here is the workspace where commands are entered", font=("arial", 15, "bold"), bd=5, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            p_part.place(relx = 0.63, rely = 0.30, relwidth=0.73,anchor = 's')
            terminal = Terminal(pady=2, padx=2, relief=GROOVE, bg="#404040",fg = "white")
            terminal.shell = True
            terminal.place(x=580, y=256, relwidth=0.54, relheight=0.55)
            p = Label(F2, text="Download sqlmap by clicking", font=("arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.27,anchor = NE)
            b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",command=lambda: terminal.run_command(f'sqlmap -hh', 'y')).place(relx = 0.23, rely = 0.32,anchor = 's')

            p = Label(F2, text="To get a list of all options and\nswitches clicking:", font=("arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.20, rely = 0.31,anchor = NE)

            b1 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",command=lambda: terminal.run_command(f'sqlmap -hh', 'y')).place(relx = 0.23, rely = 0.38,anchor = 's')

            pat = Label(F2, text="Target URL. Option: -u or --url\nRun sqlmap against a single target URL.\n This option requires a target\nURL in following form:\nhttp(s)://targeturl[:port]/[...]\nFor example:", font=( "arial", 9, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.54,anchor = 's')

            pat1 = Label(F2, text="$sqlmap -u 'http://www.target.com/vuln.php?id=1'", font=("arial", 7, "bold"), fg="white", bg="#404040").place(relx = 0.13, rely = 0.56,anchor = 's')

            p2 = Label(F2, text="to run simple sqlmap", font=( "arial", 10, "bold"), fg="white", bg="#404040").place(relx = 0.16, rely = 0.59,anchor = NE)
            p3 = Button(F2, text="here", fg ="#ccc4c4",relief=GROOVE, bg="#404040",command=lambda: terminal.run_command(f'sqlmap --wizard', 'y')).place(relx = 0.23, rely = 0.63,anchor = 's')

            def callback(url):
                webbrowser.open_new(url)
            link1 = Label(F2, text="for further use.", fg="blue", cursor="hand2")
            link1.place(relx = 0.13, rely = 0.67,anchor = 's')
            link1.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/wiki/Usage"))
            link2 = Label(F2, text="to visit the home page", fg="blue", cursor="hand2")
            link2.place(relx = 0.13, rely = 0.73,anchor = 's')
            link2.bind("<Button-1>", lambda e: callback("https://github.com/sqlmapproject/sqlmap/"))

        '''
        tooles.add_command(label ='run sqlmap', command = None)
        tooles.add_command(label ='run commix', command = None)
        tooles.add_command(label ='run nmap', command = None)
        tooles.add_command(label ='run amass', command = None)
        tooles.add_command(label ='run nikto', command = None)
######################################################################################################
        terminal = Menu(menu, tearoff = 0)
        def terminall():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black"  )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="work apron terminal", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
            terminal = Terminal(pady=2, padx=2, relief=GROOVE, bg="black",fg = "white")
            terminal.shell = True
            terminal.place(x=324, y=138, relwidth=0.73, relheight=0.72)
        menu.add_cascade(label ='terminal', menu = terminal)
        terminal.add_command(label ='open terminal',command = terminall)
#########################################################################################################
        # Adding Help Menu
        help_ = Menu(menu, tearoff = 0)
        def Help(): 
            link = 'https://github.com/abrahim7112/hackers'
            firefox = webbrowser.Mozilla("firefox")
            firefox.open(link)
        def Use(): 
            link = 'https://github.com/abrahim7112/hackers/wiki'
            firefox = webbrowser.Mozilla("firefox")
            firefox.open(link)
        menu.add_cascade(label ='Help', menu = help_)
        help_.add_command(label ='Hackers Help', command = Help)
        help_.add_command(label ='Use Help', command = Use)
        help_.add_separator()
        help_.add_command(label ='About hackers', command = None)
        
        
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def sql():
            F2 = Frame(self.root, bd=8, relief=GROOVE,bg="#048920")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="sql injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#048920", fg="white").pack(fill=X) 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="SQL Injection : In this section, we'll explain what SQL injection is, describe some common examples, explain how to find \nand exploit various kinds of SQL injection vulnerabilities, and summarize how to prevent SQL injection.\nWhat is SQL injection (SQLi)?\nSQL injection is a web security vulnerability that allows an attacker to \ninterfere with the queries that an application makes to its database. It generally allows an attacker to view data that they are not normally able to \nretrieve. This might include data belonging to other users, or any other data that the application itself is able to\n access. In many cases, an attacker can modify or delete this data, causing persistent changes to the application's\n content or behavior.In some situations, an attacker can escalate an SQL injection \nattack to compromise the underlying server or other back-end infrastructure, or perform a denial-of-service attack.", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)

            def BlindSQL1():
                from sql import BlindSQL1
            b2_button = Button(F2, text ="BlindSQL1",command = BlindSQL1, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            def p():
                from sql.Remotephp1 import jeyiuwai
                return jeyiuwai()
            b4_button = Button(F2, text ="CVE-2023-0669",command = p, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            def CVE_2022_31101sql():
                from sql.CVE_2022_31101sql import CVE_2022_31101
                return CVE_2022_31101()
            b5_button = Button(F2, text ="CVE-2022-31101sql",command = CVE_2022_31101sql,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            def BlindSQLi0day():
                from sql import BlindSQLi0day
            b6_button = Button(F2, text ="BlindSQLi0day",command =BlindSQLi0day , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)

            def CVE_2012_5967():
                from sql import CVE_2012_5967
            b6_button = Button(F2, text ="CVE_2012_5967",command =CVE_2012_5967 , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)

            def CVE_2016_2386SQL():
                from sql.CVE_2016_2386SQL import APISIX
                return APISIX()
            b2_button = Button(F2, text ="CVE-2022-24112",command = CVE_2016_2386SQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            def CVE_2022_24707sql():
                from sql import CVE_2022_24707sql
            b2_button = Button(F2, text ="CVE_2022_24707sql",command = CVE_2022_24707sql, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            def databases():
                from sql import databases
            b4_button = Button(F2, text ="databases",command = databases, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            def first_available_hash():
                from sql import first_available_hash
            b5_button = Button(F2, text ="first_available",command = first_available_hash, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            def loginaspSQL():
                from sql.loginaspSQL import login_asp
                return login_asp()
            b6_button = Button(F2, text ="loginaspSQL",command = loginaspSQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)

            def MicrosoftSQLServer():
                from sql import MicrosoftSQLServer
            b6_button = Button(F2, text ="MicrosoftSQLServer",command = MicrosoftSQLServer, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            def MultipleSQL():
                from sql import MultipleSQL
            b2_button = Button(F2, text ="MultipleSQL",command = MultipleSQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold",relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)
            def NoSQL():
                from sql import NoSQL
            b2_button = Button(F2, text ="NoSQL",command = NoSQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            def PHP_MySQL():
                from sql import PHP_MySQL
            b4_button = Button(F2, text ="PHP_MySQL",command = PHP_MySQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            def PrivilegeEscalation():
                from sql import PrivilegeEscalation
            b5_button = Button(F2, text ="PrivilegeEscalation",command = PrivilegeEscalation, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            def SQL1InjectionRemote():
                from sql import SQL1InjectionRemote
            b6_button = Button(F2, text ="1InjectionRemote", command =SQL1InjectionRemote ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)

            def wordpressx_sql():
                from sql import wordpressx_sql
            b6_button = Button(F2, text ="wordpressx_sql",command = wordpressx_sql, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            def Webspell_wCMS_Clanscript():
                from sql import Webspell_wCMS_Clanscript
            b2_button = Button(F2, text ="Webspell_wCMS",command = Webspell_wCMS_Clanscript, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            def UnauthenticatedSQL():
                from sql import UnauthenticatedSQL
            b2_button = Button(F2, text ="Unauthenticated",command = UnauthenticatedSQL, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            def Symantec_Web_Gateway():
                from sql.Symantec_Web_Gateway import Gateway
                return Gateway()
            b4_button = Button(F2, text ="Web_Gateway",command = Symantec_Web_Gateway, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            def SQLSA_CORE_2014():
                from sql import SQLSA_CORE_2014
            b5_button = Button(F2, text ="SQLSA_CORE_2014",command = SQLSA_CORE_2014, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            def SQLPoC():
                from sql import SQLPoC
            b6_button = Button(F2, text ="SQLPoC", command = SQLPoC,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)

            def SQLPathDisclosure():
                from sql import SQLPathDisclosure
            b6_button = Button(F2, text ="SQLPathDisclosure", command =SQLPathDisclosure,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            def SQLInjectionRemote():
                from sql import SQLInjectionRemote
            b2_button = Button(F2, text ="SQLInjectionRemote",command = SQLInjectionRemote, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)
  
          
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def xss():
            F2 = Frame(self.root, bd=8, relief=GROOVE ,bg="#918713")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xss injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="#918713", fg="white").pack(fill=X)

            Hacher_tooles = LabelFrame(F2, text="The Description", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=240, y=49, relwidth=0.76, relheight=0.92)

            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)

            Hacher_title = Label(F2, text="A Cross-Site Scripting (XSS)\n attack is characterized by an attacker's ability\n to inject to a web application, scripts of any kind,\n such as Flash, HTML, or JavaScript, \nthat are intended to run and render on \nthe application serving the page. The web application unintentionally serves the\n script code which is executed by the browser and hence makes\n the user vulnerable to data theft and any privileges level\n which the script is allowed.The source of an \nXSS vulnerability lies in a web application that allows malicious\n code to be injected and evaluated as part of the web page\n being served to the user, and then the same malicious\n code is executed by the browser due to the web application\n inability to filter and sanitize the output.", font=("arial", 13, "bold"), bd=7, relief=GROOVE, bg="#b6ad48", fg="black").place(x=250, y=72, relwidth=0.74,relheight=0.88)
            
            def xssmap():
                from xss import xssmap
            b2_button = Button(F2, text ="xssmap",command = xssmap, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)

            def CVE_2022_26809():
                from xss.CVE_2022_26809 import Remote
                return Remote()
            b4_button = Button(F2, text ="CVE_2022_26809",command =CVE_2022_26809, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.23,anchor = NE)
            
            def CVE_2022_29455():
                from xss.CVE_2022_29455 import Cross_Site
                return Cross_Site()
            b5_button = Button(F2, text ="CVE_2022_29455",command =CVE_2022_29455,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.33,anchor = NE)
            
            def cve_2022_39197_poc():
                from xss.cve_2022_39197_poc import  Beichendream
                return Beichendream()
            b6_button = Button(F2, text ="cve_2022_39197_poc",command =cve_2022_39197_poc, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.41,anchor = NE)
            
            def CVE_2021_31762():
                from xss.CVE_2021_31762 import Webmin
                return Webmin()
            b2_button = Button(F2, text ="CVE_2021_31762",command =CVE_2021_31762, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.49,anchor = NE)

            def CVE_2021_31761():
                from xss.CVE_2021_31761 import  Apachemain
                return Apachemain()
            b4_button = Button(F2, text ="CVE_2021_31761",command =CVE_2021_31761, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.57,anchor = NE)
            
  
            def scancss():
                from xss import scancss
            b5_button = Button(F2, text ="xss_scancss",command =scancss,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.65,anchor = NE)
            
            def xssearch():
                from xss.xssearch import all_required
                return all_required()
            b6_button = Button(F2, text ="xssearch",command =xssearch, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.73,anchor = NE)

            def main():
                return xss()
            
            b2_button = Button(F2, text ="back",command =main, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
        def comment():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#9c6105")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="Command injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#9c6105", fg="white").pack(fill=X)   
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Command injection is an attack in which the goal is execution of arbitrary commands on the host operating system \nvia a vulnerable application. Command injection attacks are possible when an application \npasses unsafe user supplied data (forms, cookies, HTTP headers etc.) to a system shell. In this attack,\n the attacker-supplied operating system commands are usually executed with the privileges of the vulnerable application. \nCommand injection attacks are possible largely due to insufficient input validation.\nThis attack differs from Code Injection, in that code injection allows the attacker to add their own code that is\n then executed by the application. In Command Injection, the attacker extends the default functionality of\n the application, which execute system commands, without the necessity of injecting code.", font=(
            "arial", 10, "bold"), bd=7, relief=GROOVE, bg="#be8f47", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)
            
            def Apache_2017_5638():
                from comment import Apache_2017_5638
            b2_button = Button(F2, text ="Apache_2017_5638",command = Apache_2017_5638, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
          
            def AuthenticationBypass():
                from comment import AuthenticationBypass
            b4_button = Button(F2, text ="AuthenticationBypass",command =AuthenticationBypass, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
  
            def Belkin_Router_AC1200():
                from comment import Belkin_Router_AC1200
            b5_button = Button(F2, text ="Belkin_Router",command =Belkin_Router_AC1200,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
            def COM_JOOMANAGER():
                from comment import COM_JOOMANAGER
            b6_button = Button(F2, text ="COM_JOOMANAGER",command =COM_JOOMANAGER, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)

            def CommandInjection():
                from comment import  CommandInjection 
            b6_button = Button(F2, text ="CommandInjection",command =CommandInjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            
            def Cve_2012_1823():
                from comment import Cve_2012_1823
            b2_button = Button(F2, text ="Cve_2012_1823",command =Cve_2012_1823, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles Scan", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

            def CVE_2017_14143():
                from comment import CVE_2017_14143
            b2_button = Button(F2, text ="CVE_2017_14143",command =CVE_2017_14143, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          
            def CVE_2017_14738():
                from comment import CVE_2017_14738
            b4_button = Button(F2, text ="CVE_2017_14738",command =CVE_2017_14738, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
            def CVE_2021_24347():
                from comment import CVE_2021_24347
            b5_button = Button(F2, text ="CVE_2021_24347",command =CVE_2021_24347, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  
            def CVE_2021_35464():
                from comment import CVE_2021_35464
            b6_button = Button(F2, text ="CVE_2021_35464",command =CVE_2021_35464, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)

            def CVE_2022_36446():
                from comment import CVE_2022_36446
            b6_button = Button(F2, text ="CVE_2022_36446",command =CVE_2022_36446, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
            def Imperva_SecureSphere():
                from comment import Imperva_SecureSphere
            b2_button = Button(F2, text ="Imperva_SecureSphere",command =Imperva_SecureSphere, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

            def loneferret_of_Offensive():
                from comment import loneferret_of_Offensive
            b2_button = Button(F2, text ="loneferret_Offensive",command =loneferret_of_Offensive, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
          
            def ManageEngine_opManager():
                from comment import ManageEngine_opManager
            b4_button = Button(F2, text ="ManageEngine_Manager",command =ManageEngine_opManager, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
  
            def MicrosoftRemote():
                from comment import MicrosoftRemote
            b5_button = Button(F2, text ="MicrosoftRemote",command =MicrosoftRemote, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
  
            def Object_Injection_header():
                from comment import Object_Injection_header
            b6_button = Button(F2, text ="Object_Injection",command =Object_Injection_header, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
            def OctoBot_WebInterface():
                from comment import OctoBot_WebInterface
            b6_button = Button(F2, text ="OctoBot_WebInterface",command =OctoBot_WebInterface, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
            def PHPObjectInjection():
                from comment import PHPObjectInjection
            b2_button = Button(F2, text ="PHPObjectInjection",command =PHPObjectInjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="Tooles ", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

            def RCE_Authenticated():
                from comment import RCE_Authenticated
            b2_button = Button(F2, text ="RCE_Authenticated",command =RCE_Authenticated, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
            def RCEforUnitrends():
                from comment import RCEforUnitrends
            b4_button = Button(F2, text ="RCEforUnitrends",command =RCEforUnitrends, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
            def RCE_for_Unitrends_UEB():
                from comment import RCE_for_Unitrends_UEB
            b5_button = Button(F2, text ="RCE_Unitrends_UEB",command =RCE_for_Unitrends_UEB, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
            def Unauthenticated_root():
                from comment import Unauthenticated_root
            b6_button = Button(F2, text ="Unauthenticated_root",command =Unauthenticated_root, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)

            def UnauthenticatedEmail():
                from comment import UnauthenticatedEmail
            b6_button = Button(F2, text ="UnauthenticatedEmail",command =UnauthenticatedEmail, fg ="#ccc4c4",width=18, bd=6, font="arial 13 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
            
            def zerologon_tester():
                from comment import zerologon_tester
            b2_button = Button(F2, text ="zerologon_tester",command =zerologon_tester, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        def ssf():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#0c8c6d"  )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="ssf injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="#0c8c6d", fg="white").pack(fill=X)
            
            Hacher_tooles = LabelFrame(F2, text="The Description", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=240, y=49, relwidth=0.76, relheight=0.92)

            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)

            Hacher_title = Label(F2, text="SSIs are directives present on Web applications \nused to feed an HTML page with dynamic contents. \nThey are similar to CGIs, except that SSIs are used to\n execute some actions before the current page is\n loaded or while the page is being visualized.\n In order to do so, the web server analyzes SSI before supplying the\n page to the user. The Server-Side Includes attack \nallows the exploitation of a web application by injecting scripts in HTML \npages or executing arbitrary codes remotely.\n It can be exploited through manipulation of SSI \nin use in the application or force its use through \nuser input fields. It is possible to check if the application is properly\n validating input fields data by inserting characters \nthat are used in SSI directives, like:", font=("arial", 13, "bold"), bd=7, relief=GROOVE, bg="#7ea982", fg="black").place(x=250, y=72, relwidth=0.74,relheight=0.88)
            
            def ssrf():
                from ssf import ssrf
            b2_button = Button(F2, text ="scan_ssrf",command = ssrf, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)

            def CVE_2022_3590():
                from ssf import CVE_2022_3590
            b4_button = Button(F2, text ="CVE_2022_3590",command =CVE_2022_3590, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.23,anchor = NE)
            
  
            def CVE_2023_27163():
                from ssf import CVE_2023_27163
            b5_button = Button(F2, text ="CVE_2023_27163",command =CVE_2023_27163,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.33,anchor = NE)
            
  
            def CVE_2022_41082():
                from ssf import CVE_2022_41082
            b6_button = Button(F2, text ="CVE_2022_41082",command =CVE_2022_41082, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.41,anchor = NE)
            
            def CVE_2022_36663():
                from ssf import CVE_2022_36663
            b2_button = Button(F2, text ="CVE_2022_36663",command =CVE_2022_36663, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.49,anchor = NE)

            def CVE_2022_26135():
                from ssf import CVE_2022_26135
            b4_button = Button(F2, text ="CVE_2022_26135",command =CVE_2022_26135, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.57,anchor = NE)
            
  
            def CVE_2022_28117():
                from ssf import CVE_2022_28117
            b5_button = Button(F2, text ="CVE_2022_28117",command =CVE_2022_28117,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.65,anchor = NE)
            
  
            def CVE_2022_25260():
                from ssf import CVE_2022_25260
            b6_button = Button(F2, text ="CVE_2022_25260",command =CVE_2022_25260, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.73,anchor = NE)

            def main():
                return ssf()
            b2_button = Button(F2, text ="back",command =main, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def xml():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="#8322a4")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="xml injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="#8322a4", fg="white").pack(fill=X)
            
            Hacher_tooles = LabelFrame(F2, text="The Description", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=240, y=49, relwidth=0.76, relheight=0.92)

            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)

            Hacher_title = Label(F2, text="In this section, we'll explain what XML external \n entity injection is, describe some common examples, \n explain how to find and \nexploit various kinds of XXE injection,\n and summarize how to prevent XXE injection attacks.\nWhat is XML external entity injection?\nXML external entity injection (also known as XXE)\n is a web security vulnerability\n that allows an attacker to interfere with an application's \nprocessing of XML data. It often allows an attacker to view files on\n the application server filesystem, and to interact \nwith any backend or external systems that the application \nitself can access.In some situations,\n an attacker can escalate an XXE attack to compromise\n the underlying server or other\n backend infrastructure, by leveraging the XXE vulnerability to\n perform server-side request forgery (SSRF) attacks.", font=("arial", 13, "bold"), bd=7, relief=GROOVE, bg="#8322a4", fg="white").place(x=250, y=72, relwidth=0.74,relheight=0.88)
            
            def CVE_2022_40684():
                from xmlin.CVE_2022_40684 import  unauthenticated
                return unauthenticated()
            b2_button = Button(F2, text ="CVE_2022_40684",command = CVE_2022_40684, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)

            def CVE_2022_41040():
                from xmlin import CVE_2022_41040
            b4_button = Button(F2, text ="CVE_2022_41040",command = CVE_2022_41040, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.23,anchor = NE)
            
            def CVE_2022_41049_POC():
                from xmlin import CVE_2022_41049_POC
            b5_button = Button(F2, text ="CVE_2022_41049",command= CVE_2022_41049_POC,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.33,anchor = NE)
            
            def cve_2022_41876():
                from xmlin import cve_2022_41876
            b6_button = Button(F2, text ="cve_2022_41876",command = cve_2022_41876, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.41,anchor = NE)
            
            def CVE_2022_31854():
                from xmlin.CVE_2022_31854 import  phpIPAM
                return phpIPAM()
            b2_button = Button(F2, text ="CVE_2022_31854",command = CVE_2022_31854, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.49,anchor = NE)

            def cve_2022_2414_poc():
                from xmlin.cve_2022_2414_poc import cve_2022_2414_poc
                return cve_2022_2414_poc()
            b4_button = Button(F2, text ="cve_2022_2414",command = cve_2022_2414_poc, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.57,anchor = NE)
            
  
            def ScanAndroidXml():
                from xmlin import ScanAndroidXml
            b5_button = Button(F2, text ="ScanAndroidXml",command = ScanAndroidXml,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.65,anchor = NE)
            

            def main():
                return xml()         
            b2_button = Button(F2, text ="back",command = main, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
            
        def service():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#92147b" )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="denial of service", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="#92147b", fg="white").pack(fill=X)
                 
            Hacher_tooles = LabelFrame(F2, text="The Description", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=240, y=49, relwidth=0.76, relheight=0.92)

            Hacher_s = LabelFrame(F2, text="Tooles Exploits", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)

            Hacher_title = Label(F2, text="In computing, a denial-of-service attack \n(DoS attack) is a cyber-attack in which \nthe perpetrator seeks to make a machine or network\n resource unavailable to its intended users by\n temporarily or indefinitely disrupting services of a host \nconnected to a network. Denial of service is typically \naccomplished by flooding the targeted machine or\n resource with superfluous requests in an attempt to\n overload systems and prevent some or \nall legitimate requests from being fulfilled. ", font=("arial", 13, "bold"), bd=7, relief=GROOVE, bg="#af559f", fg="black").place(x=250, y=72, relwidth=0.74,relheight=0.88)
            
            def Overload_DoS():
                from service import Overload_DoS
            b2_button = Button(F2, text ="Overload_DoS",command = Overload_DoS, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)

            def CVE_2020_11579():
                from service import CVE_2020_11579
            b4_button = Button(F2, text ="CVE_2020_11579",command = CVE_2020_11579, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.23,anchor = NE)
            
            def ddos():
                from service import ddos
            b5_button = Button(F2, text ="attack_ddos",command = ddos,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.33,anchor = NE)
            
            def doss():
                from service import doss
            b6_button = Button(F2, text ="attack_dos",command = doss, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.41,anchor = NE)
            
            def exploit():
                from service import exploit
            b2_button = Button(F2, text ="exploit_dos",command = exploit, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.49,anchor = NE)

            def posddos():
                from service import posddos
            b4_button = Button(F2, text ="pos_ddos",command = posddos, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.57,anchor = NE)
            
  
            def apache_range_dos():
                from service.apache_range_dos import Apache
                return Apache()
                    
            b5_button = Button(F2, text ="apache_range_dos",command = apache_range_dos,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.65,anchor = NE)
            
            def attack():
                from service import dos
            b6_button = Button(F2, text ="attack",command = attack, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.73,anchor = NE)

            
            def main():
                return service()
            b2_button = Button(F2, text ="back",command = main, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################
###########################################################################################################
####################################################################################

###########################################################################################################

######################################################################################################################################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def injection():
            F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="shaw all injection", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                 
            Hacher_tooles = LabelFrame(F2, text="All Payloads", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
            Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)

            def xssinjection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"xss-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1)
                self.txtarea.configure(state ='disabled')
            
            def sqlinjection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"sql-injection-payload-list.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
                self.txtarea.configure(state ='disabled')
            
            def commamd_injection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"Command-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
                self.txtarea.configure(state ='disabled')
            
            def xml_injection():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"xxe-injection-payload-list.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1)
                self.txtarea.configure(state ='disabled')
            
            def ddos():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"dos-doss.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1) 
                self.txtarea.configure(state ='disabled')

            def server_side():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"server-side-injection.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1)
                self.txtarea.configure(state ='disabled')
                

            def Server_side_template():
                F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                self.txtarea = open(r"Server-side-template.txt", "r") 
                data = self.txtarea.read()
                scroll_y = Scrollbar(F3, orient=VERTICAL)
                self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                scroll_y.pack(side=RIGHT, fill=Y)
                scroll_y.config(command=self.txtarea.yview)
                self.txtarea.insert(END, data)
                self.txtarea.pack(fill=BOTH,expand=1)
                self.txtarea.configure(state ='disabled')

            def back():
                F3 = injection()
             
            Hacher_s = LabelFrame(F2, text="prat injection", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
            Hacher_s.place(x=2, y=49, relwidth=0.24, relheight=0.92)
            p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
            p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
            b2_button = Button(F2, text ="xss injection",command = xssinjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
            b4_button = Button(F2, text ="sql injection",command = sqlinjection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

            b5_button = Button(F2, text ="commamd injection",command = commamd_injection,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
  
            b6_button = Button(F2, text ="xml injection",command = xml_injection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.42,anchor = NE)

            b6_button = Button(F2, text ="dos ddos",command = ddos, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.51,anchor = NE)
            
            b2_button = Button(F2, text ="server-side-injection",command = server_side, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.60,anchor = NE)
            
            b2_button = Button(F2, text ="Server-side-template",command = Server_side_template, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.69,anchor = NE)
            
  
            b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
            

####################################################################################

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################


        def CVEPoC():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#105392" )
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="All hacks for a year CVE-2023", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#105392", fg="white").pack(fill=X)
            
            Hacher_s = LabelFrame(F2, text="CVE-2023 Exploits", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=45, relwidth=0.24, relheight=0.92)

            def CVE_2023_0861():
                from CVE_2023_poc.CVE_2023_0861 import Apache
                return Apache()
            b2_button = Button(F2, text ="CVE-2023-0861",command = CVE_2023_0861,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.15,anchor = NE)  
          
            def CVE_2023_1671():
                from CVE_2023_poc.CVE_2023_1671 import Main
                return Main()
            b5_button = Button(F2, text ="CVE-2023-1671",command = CVE_2023_1671,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.23,anchor = NE)
            
  
            def CVE_2023_1671_POC():
                from CVE_2023_poc import CVE_2023_1671_POC
            b6_button = Button(F2, text ="CVE-2023-1671poc",command =  CVE_2023_1671_POC,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.31,anchor = NE)

            def CVE_2023_2825_POC():
                from CVE_2023_poc.CVE_2023_2825_POC import GitLab
                return GitLab()
            b6_button = Button(F2, text ="CVE_2023_2825_POC",command = CVE_2023_2825_POC, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.39,anchor = NE)
            
            def CVE_2023_2825():
                from CVE_2023_poc.CVE_2023_2825 import GitLab1 
                return GitLab1()
            b2_button = Button(F2, text ="CVE-2023-2825",command = CVE_2023_2825, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.47,anchor = NE)
          
            def CVE_2023_2868():
                from CVE_2023_poc import poc_cve_2023_2868
            b4_button = Button(F2, text ="CVE-2023-2868",command = CVE_2023_2868 , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.55,anchor = NE)
            
  
            def CVE_2023_2877():
                from CVE_2023_poc.CVE_2023_2877 import  Subscriber
                return Subscriber()
            b5_button = Button(F2, text ="CVE-2023-2877",command =CVE_2023_2877 ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.63,anchor = NE)
            
            def CVE_2023_2982():
                from CVE_2023_poc.CVE_2023_2982 import Apachey
                return Apachey()
            b6_button = Button(F2, text ="CVE-2023-2982",command = CVE_2023_2982, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.71,anchor = NE)

            def CVE_2023_2986():
                from CVE_2023_poc import poc
            b6_button = Button(F2, text ="CVE-2023-2986",command = CVE_2023_2986, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.79,anchor = NE)
            
            def CVE_2023_3460():
                from CVE_2023_poc.CVE_2023_3460 import  Unauthorized
                return Unauthorized()
            b2_button = Button(F2, text ="CVE-2023-3460",command = CVE_2023_3460, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.87,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023 poc", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=45, relwidth=0.24, relheight=0.92)
 
            def CVE_2023_3519():
                from CVE_2023_poc import CVE_2023_3519_checker
            b2_button = Button(F2, text ="cve-2023-3519",command = CVE_2023_3519, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.15,anchor = NE)
          
            def CVE_2023_10608():
                from CVE_2023_poc import CVE_2023_10608
            b5_button = Button(F2, text ="cve-2023-10608",command =CVE_2023_10608 ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.23,anchor = NE)
            
            def CVE_2023_20110():
                from CVE_2023_poc.CVE_2023_20110 import SQL_Injection
                SQL_Injection()
                
            b6_button = Button(F2, text ="CVE-2023-20110",command = CVE_2023_20110, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.31,anchor = NE)

            def CVE_2023_20887():
                from CVE_2023_poc.CVE_2023_20887 import Networks
                return Networks()
            b6_button = Button(F2, text ="CVE-2023-20887", command = CVE_2023_20887,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.39,anchor = NE)
            
            def CVE_2023_21554():
                from CVE_2023_poc.CVE_2023_21554 import ip_address
                return ip_address()
            b2_button = Button(F2, text ="CVE-2023-21554",command = CVE_2023_21554, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.47,anchor = NE)
          
            def CVE_2023_21707():
                from CVE_2023_poc import CVE_2023_21707
            b4_button = Button(F2, text ="CVE-2023-21707",command = CVE_2023_21707, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.55,anchor = NE)
            
  
            def CVE_2023_21716poc():
                from CVE_2023_poc import CVE_2023_21716poc
            b5_button = Button(F2, text ="CVE-2023-21716",command =CVE_2023_21716poc ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.63,anchor = NE)
            
  
            def CVE_2023_21716():
                from CVE_2023_poc import CVE_2023_21716
            b6_button = Button(F2, text ="CVE-2023-21716",command = CVE_2023_21716, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.71,anchor = NE)

            def CVE_2023_21837():
                from CVE_2023_poc.CVE_2023_21837 import domin
                return domin()
            b6_button = Button(F2, text ="CVE-2023-21837",command = CVE_2023_21837, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.79,anchor = NE)
            
            def CVE_2023_21839():
                from CVE_2023_poc import CVE_2023_21839
            b2_button = Button(F2, text ="CVE-2023-21839",command = CVE_2023_21839, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.87,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=45, relwidth=0.24, relheight=0.92)

            def CVE_2023_22621():
                from CVE_2023_poc import CVE_2023_22621
            b2_button = Button(F2, text ="CVE-2023-22621",command =CVE_2023_22621 , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.15,anchor = NE)
          
            def CVE_2023_22809():
                from CVE_2023_poc import CVE_2023_22809
            b5_button = Button(F2, text ="CVE-2023-22809",command = CVE_2023_22809,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.23,anchor = NE)
            
  
            def CVE_2023_22884():
                from CVE_2023_poc import CVE_2023_22884_Airflow_SQLi
            b6_button = Button(F2, text ="CVE-2023-22884",command = CVE_2023_22884, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.31,anchor = NE)

            def CVE_2023_22906():
                from CVE_2023_poc import CVE_2023_22906
            b6_button = Button(F2, text ="CVE-2023-22906", command = CVE_2023_22906,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.39,anchor = NE)
            
            def CVE_2023_22960():
                from CVE_2023_poc import CVE_2023_22960
            b2_button = Button(F2, text ="CVE-2023-22960",command = CVE_2023_22960, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.47,anchor = NE)
          
            def CVE_2023_23333():
                from CVE_2023_poc.CVE_2023_23333 import Apacheld
                return Apacheld()
            b4_button = Button(F2, text ="CVE-2023-23333", command = CVE_2023_23333,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.55,anchor = NE)
            
  
            def CVE_2023_23397():
                from CVE_2023_poc import CVE_2023_23397
            b5_button = Button(F2, text ="CVE-2023-23397",command = CVE_2023_23397,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.63,anchor = NE)
            
  
            def CVE_2023_23488():
                from CVE_2023_poc.CVE_2023_23488 import r3nt0n
                return r3nt0n()
            b6_button = Button(F2, text ="CVE-2023-23488",command = CVE_2023_23488, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.71,anchor = NE)

            def CVE_2023_23752():
                from CVE_2023_poc import cve_2023_23752_PoC
            b6_button = Button(F2, text ="CVE-2023-23752", command = CVE_2023_23752,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.79,anchor = NE)
            
            def CVE_2023_24078():
                from CVE_2023_poc import CVE_2023_24078
            b2_button = Button(F2, text ="CVE-2023-24078", command = CVE_2023_24078,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.87,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="CVE-2023", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=45, relwidth=0.24, relheight=0.92)

            def CVE_2023_24488():
                from CVE_2023_poc.CVE_2023_24488 import Apachedom
                return Apachedom()
            b2_button = Button(F2, text ="CVE-2023-24488", command = CVE_2023_24488,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.15,anchor = NE)
          
            def CVE_2023_24489():
                from CVE_2023_poc import CVE_2023_24489_RCE
            b5_button = Button(F2, text ="CVE-2023-24489",command =CVE_2023_24489 ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.23,anchor = NE)
            
  
            def CVE_2023_24775():
                from CVE_2023_poc import CVE_2023_24775
            b6_button = Button(F2, text ="CVE-2023-24775",command = CVE_2023_24775, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.31,anchor = NE)

            def CVE_2023_25136():
                from CVE_2023_poc import CVE_2023_25136_POC
            b6_button = Button(F2, text ="CVE-2023-25136",command = CVE_2023_25136, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.39,anchor = NE)
            
            def CVE_2023_27163():
                from CVE_2023_poc.CVE_2023_27163 import attack
                return attack()
            b2_button = Button(F2, text ="CVE-2023-27163",command = CVE_2023_27163, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.47,anchor = NE)
          
            def CVE_2023_27350():
                from CVE_2023_poc.CVE_2023_27350 import vuln_version
                return vuln_version()
            b4_button = Button(F2, text ="CVE-2023-27350",command = CVE_2023_27350, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.55,anchor = NE)
            
  
            def CVE_2023_27372():
                from CVE_2023_poc import CVE_2023_27372
            b5_button = Button(F2, text ="CVE-2023-27372",command =CVE_2023_27372 ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.63,anchor = NE)
            
  
            def CVE_2023_27524():
                from CVE_2023_poc import CVE_2023_27524
            b6_button = Button(F2, text ="CVE-2023-27524",command = CVE_2023_27524, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.71,anchor = NE)
            def cve_2022_42475():
                from CVE_2023_poc.CVE_2022_42475_RCE_POC import exploit
                return exploit()
                     
            b6_button = Button(F2, text ="cve-2022-42475",command = cve_2022_42475, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.79,anchor = NE)

            def CVE_2023_28771_poc():
                from CVE_2023_poc.CVE_2023_28771_poc import exploitprint
                return exploitprint()
            b2_button = Button(F2, text ="CVE-2023-28771",command = CVE_2023_28771_poc, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.87,anchor = NE)
            

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

######################################################################################################################################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################

        F1 = LabelFrame(self.root, text="Tooles", font=("times new roman", 15, "bold"),  bd=12, relief=GROOVE, bg="#404040",fg = "white")
        F1.place(x=7, y=70, width=300, relheight=0.84)
        
        def main():
            F2 = Frame(self.root, bd=8, relief=GROOVE , bg="#679a80")
            F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
            Hacher_title = Label(F2, text="working", font=(
                "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4").pack(fill=X)
            Hacher_tooles = LabelFrame(F2, text="The Description", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_tooles.place(x=2, y=49, relwidth=0.99, relheight=0.36)
            Hacher_s = LabelFrame(F2, text="show Payloads", font=(
                "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=2, y=248, relwidth=0.24, relheight=0.56)
            Hacher_title = Label(F2, text="Welcome to the new hacking tools \n,There are new hacking tools here in the following sections.\n Choose the tool to test any website on the Internet \n and get new security vulnerabilities!!!! ", font=(
            "arial", 20, "bold"), bd=7, relief=GROOVE, bg="#679a80", fg="white")
            Hacher_title.place(x=15, y=72, relwidth=0.97,relheight=0.30)


       
############################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################   
            def redirect():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/alt-extensions-php.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/file-ul-filter-bypass-microsoft-asp-filetype-bf.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/file-ul-filter-bypass-ms-php.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def javascript_events():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/file-ul-filter-bypass-x-platform-generic.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def js_inject():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/file-ul-filter-bypass-x-platform-php.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def quotationmarks():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/invalid-filenames-linux.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def urls_template():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/redirect-urls-template.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def redirect_injection():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/redirect/redirect-injection-template.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="alt-extensions-php",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="file-ul-filter-bypass",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="file-ul-filter-bypass",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="bypass-x-platform-generic",command = javascript_events,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="bypass-x-platform-php",command = js_inject,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="invalid-filenames-linux",command = quotationmarks,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.58,anchor = NE)
                b5_button = Button(F2, text ="urls_template",command = urls_template,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.66,anchor = NE)
                b5_button = Button(F2, text ="injection-template",command = redirect_injection,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.74,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="redirect",command = redirect, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.50,anchor = NE)
#######################
######################
          
            def sql_injection():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/exploit/db2-enumeration.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-ORDER_BY.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/detect/MSSQL_blind.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def javascript_events():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-WHERE.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def js_inject():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/exploit/postgres-enumeration.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def quotationmarks():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/payloads-sql-blind/payloads-sql-blind-MSSQL-INSERT.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def urls_template():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/payloads-sql-blind/payloads-sql-blind-MSSQL-WHERE.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def redirect_injection():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/sql-injection/payloads-sql-blind/payloads-sql-blind-MySQL-INSERT.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="db2-enumeration",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
   
                b4_button = Button(F2, text ="MySQL-ORDER_BY",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
          
                b5_button = Button(F2, text ="MSSQL_blind",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="MySQL-WHERE",command = javascript_events,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="postgres-enumeration",command = js_inject,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="payloads-sql-blind",command = quotationmarks,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.58,anchor = NE)
                b5_button = Button(F2, text ="sql-blind-MSSQL",command = urls_template,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.66,anchor = NE)
                b5_button = Button(F2, text ="sql-blind-MySQL",command = redirect_injection,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.74,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################
            b4_button = Button(F2, text ="sql-injection",command =sql_injection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.23, rely = 0.58,anchor = NE)
            
#############################
#############################

            def all_attacks():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def all_attacks_unix():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/all-attacks/all-attacks-unix.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def all_attacks_win():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/all-attacks/all-attacks-win.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def all_attacks_xplatform():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/all-attacks/all-attacks-xplatform.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="all_attacks_unix",command = all_attacks_unix, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="all_attacks_win",command = all_attacks_win, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="all_attacks_xplatform",command = all_attacks_xplatform,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b5_button = Button(F2, text ="all-attacks",command = all_attacks,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.66,anchor = NE)
            
  
#############################
#############################

            def authentication():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def php_magic_hashes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/authentication/php_magic_hashes.fuzz.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def alt_extensions_asp():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/authentication/alt-extensions-asp.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def alt_extensions_coldfusion():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/authentication/alt-extensions-coldfusion.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def alt_extensions_perl():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/authentication/alt-extensions-perl.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="php_magic_hashes",command = php_magic_hashes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="alt_extensions_asp",command = alt_extensions_asp, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="alt_extensions_coldfusion",command = alt_extensions_coldfusion,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)

                b5_button = Button(F2, text ="alt_extensions_perl",command = alt_extensions_perl,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="authentication", command = authentication,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.74,anchor = NE)


#############################
#############################

            def business_logic():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def CommonDebugParamNames():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/business-logic/CommonDebugParamNames.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def CommonMethodNames():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/business-logic/CommonMethodNames.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def DebugParams_Json():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/business-logic/DebugParams.Json.fuzz.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="CommonDebugParamNames",command = CommonDebugParamNames, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="CommonMethodNames",command = CommonMethodNames, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="DebugParams_Json",command = DebugParams_Json,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="business-logic",command = business_logic,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.82,anchor = NE)
            

#############################
#############################

            def control_chars():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/control-chars/HexValsAllBytes.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/control-chars/imessage.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/control-chars/NullByteRepresentations.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="HexValsAllBytes",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="imessage",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="NullByteRepresentations",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="control-chars",command = control_chars, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.23, rely = 0.90,anchor = NE)

####################################################################################

            Hacher_s = LabelFrame(F2, text="show Payloads", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=252, y=248, relwidth=0.24, relheight=0.56)

#############################
#############################

            def disclosure_directory():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def directory_indexing():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-directory/directory-indexing-generic.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def filenames_microsoft():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-directory/invalid-filenames-microsoft.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def chars_microsoft():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-directory/invalid-filesystem-chars-microsoft.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="directory_indexing",command = directory_indexing, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="filenames_microsoft",command = filenames_microsoft, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="chars_microsoft",command = chars_microsoft,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################


            b2_button = Button(F2, text ="disclosure-directory",command = disclosure_directory, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.50,anchor = NE)
          

#############################
#############################

            def disclosure_localpaths():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def httpd_log_locations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"/home/ibrahim/hackers/attack/disclosure-localpaths/common-unix-httpd-log-locations.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def filesystem_chars():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-localpaths/invalid-filesystem-chars-osx.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="httpd_log_locations",command = httpd_log_locations, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="filesystem_chars",command = filesystem_chars, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b4_button = Button(F2, text ="disclosure-localpaths",command =disclosure_localpaths, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.48, rely = 0.58,anchor = NE)
            
  
#############################
#############################

            def disclosure_source():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-source/source-disc-cmd-exec-traversal.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-source/source-disclosure-generic.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/disclosure-source/source-disclosure-microsoft.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="cmd-exec-traversal",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="disclosure-generic",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="source-disclosure",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b5_button = Button(F2, text ="disclosure-source", command =disclosure_source ,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.66,anchor = NE)
            
  #############################
#############################

            def email():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/email/invalid-email-addresses.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/email/valid-email-addresses.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="email-addresses",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="email-addresses",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
          
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="email", command =email, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.74,anchor = NE)

#############################
#############################

            def format_strings():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/format-strings/format-strings.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/format-strings/file-ul-filter-bypass-commonly-writable-directories.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"/home/ibrahim/hackers/attack/format-strings/file-ul-filter-bypass-microsoft-asp.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="format-strings",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="writable-directories",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="bypass-microsoft",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="format-strings",command = format_strings,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.82,anchor = NE)
            
#############################
#############################

            def html_js_fuzz():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/HTML5sec_Injections.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/html_attributes.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/html_tags.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def javascript_events():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/javascript_events.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def js_inject():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/js_inject.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def quotationmarks():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/html_js_fuzz/quotationmarks.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="HTML5sec_Injections",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="html_attributes",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="html_tags",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="javascript_events",command = javascript_events,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="js_inject",command = js_inject,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="quotationmarks",command = quotationmarks,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.58,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="html_js_fuzz",command =html_js_fuzz, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.48, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="show Payloads", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=501, y=248, relwidth=0.24, relheight=0.56)

#############################
#############################

            def http_protocol():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/crlf-injection.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/hpp.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/http-header-cache-poison.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def protocol_methods():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/http-protocol-methods.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def header_field_names():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/http-request-header-field-names.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def header_field_names1():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/http-response-header-field-names.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def known_uri_types():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/known-uri-types.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def user_agents():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/http-protocol/user-agents.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="crlf-injection",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="hpp",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="http-header-cache",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="protocol_methods",command = protocol_methods,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="header_field_names",command = header_field_names,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="header_field_names1",command = header_field_names1,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.57,anchor = NE)
                b5_button = Button(F2, text ="known_uri_types",command = known_uri_types,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.65,anchor = NE)
                b5_button = Button(F2, text ="user_agents",command = user_agents,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.73,anchor = NE)

                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="http-protocol",command =http_protocol, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.50,anchor = NE)
#############################
#############################

            def integer_overflow():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/integer-overflow/integer-overflows.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/integer-overflow/two-byte-chars.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/integer-overflow/upsidedown.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="integer-overflows",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="two-byte-chars",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="upsidedown",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################
          
            b4_button = Button(F2, text ="integer-overflow",command = integer_overflow, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.73, rely = 0.58,anchor = NE)
            
#############################
#############################

            def ip():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ip/localhost.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ip/rfi.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ip/shell-expansion.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="localhost",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="rfi",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="shell-expansion",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

  
            b5_button = Button(F2, text ="ip",command = ip, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.66,anchor = NE)
            
#############################
#############################

            def json():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/html-event-attributes.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/JHADDIX_XSS_WITH_CONTEXT.doc.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/JSON_Fuzzing.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_other():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/xss-other.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def XSSPolyglot():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/XSSPolyglot.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_rsnake():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/xss-rsnake.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_uri():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/json/xss-uri.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="html-event-attributes",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="JHADDIX_XSS",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="JSON_Fuzzing",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="xss_other",command = xss_other,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="XSSPolyglot",command = XSSPolyglot,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="xss_rsnake",command = xss_rsnake,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.57,anchor = NE)
                b5_button = Button(F2, text ="xss_uri",command = xss_uri,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.65,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################
  
            b6_button = Button(F2, text ="xss-json",command =json, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.74,anchor = NE)
#############################
#############################

            def ldap():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ldap/ldap-injection.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ldap/default-javascript-event-attributes.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/ldap/all-encodings-of-lt.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="ldap-injection",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="javascript-event",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="all-encodings-of-lt",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="ldap",command =ldap, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.82,anchor = NE)
            
#############################
#############################

            def unicode1():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/corrupted.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/emoji.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/japanese-emoticon.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def naughty_unicode():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/naughty-unicode.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def regionalindicators():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/regionalindicators.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def right_to_left():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/right-to-left.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def specialchars():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/unicode/specialchars.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="corrupted",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="emoji",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="japanese-emoticon",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="naughty_unicode",command = naughty_unicode,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="regionalindicators",command = regionalindicators,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="right_to_left",command = right_to_left,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.57,anchor = NE)
                b5_button = Button(F2, text ="specialchars",command = specialchars,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.65,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="unicode",command = unicode1, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.73, rely = 0.90,anchor = NE)

###########################################################################################################
####################################################################################

            Hacher_s = LabelFrame(F2, text="show Payloads", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
            Hacher_s.place(x=751, y=248, relwidth=0.24, relheight=0.56)

#############################
#############################

            def mimetypes():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/mimetypes/xpath-injection.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/mimetypes/MimeTypes.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/mimetypes/JHADDIX_LFI.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def common_unix_httpd():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/mimetypes/common-unix-httpd-log-locations.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def httpd_log_locations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/mimetypes/common-ms-httpd-log-locations.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="xpath-injection",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="MimeTypes",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="JHADDIX_LFI",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="common_unix_httpd",command = common_unix_httpd,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="httpd_log_locations",command = httpd_log_locations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b2_button = Button(F2, text ="mimetypes",command =mimetypes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.50,anchor = NE)
          
#############################
#############################

            def no_sql_injection():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/no-sql-injection/mongodb.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/no-sql-injection/MySQL_MSSQL.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/no-sql-injection/oracle.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="mongodb",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="MySQL_MSSQL",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="oracle",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b4_button = Button(F2, text ="no-sql-injection",command =no_sql_injection, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx =0.98, rely = 0.58,anchor = NE)
            
  
#############################
#############################

            def os_cmd_execution():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/command-execution-unix.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/command-injection-template.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/Commands-Linux.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_other():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/OSCommandInject.Windows.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def XSSPolyglot():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/shell-delimiters.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_rsnake():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/source-disc-cmd-exec-traversal.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def xss_uri():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/useful-commands-unix.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def useful_commands():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-cmd-execution/useful-commands-windows.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="command-execution",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="command-injection",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="Commands-Linux",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
                b5_button = Button(F2, text ="OSCommandInject",command = xss_other,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.41,anchor = NE)
                b5_button = Button(F2, text ="shell-delimiters",command = XSSPolyglot,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.49,anchor = NE)
                b5_button = Button(F2, text ="source-disc-cmd",command = xss_rsnake,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.57,anchor = NE)
                b5_button = Button(F2, text ="commands-unix",command = xss_uri,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.65,anchor = NE)
                b5_button = Button(F2, text ="commands-windows",command = useful_commands,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.65,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b5_button = Button(F2, text ="os-cmd-execution",command =os_cmd_execution, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.66,anchor = NE)
            
  
#############################
#############################

            def os_dir_indexing():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-dir-indexing/Commands-OSX.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-dir-indexing/Commands-Windows.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/os-dir-indexing/directory-indexing.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="Commands-OSX",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="Commands-Windows",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="directory-indexing",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="os-dir-indexing",command =os_dir_indexing , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.74,anchor = NE)
#############################
#############################

            def path_traversal():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/path-traversal/path-traversal-windows.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/path-traversal/traversals-8-deep-exotic-encoding.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/path-traversal/Commands-WindowsPowershell.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="path-traversal-windows",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="traversals-8-deep",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="WindowsPowershell",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################

            b6_button = Button(F2, text ="path-traversal",command =path_traversal, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.82,anchor = NE)
#############################
#############################

            def server_side_include():
                F2 = Frame(self.root, bd=8, relief=GROOVE, bg="black")
                F2.place(x=310, y=80, relwidth=0.75, relheight=0.82)
                Hacher_title = Label(F2, text="shaw all injection", font=("arial", 20, "bold"), bd=7, relief=GROOVE, bg="black", fg="white").pack(fill=X)
                Hacher_tooles = LabelFrame(F2, text="All Payloads", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4")
                Hacher_tooles.place(x=245, y=49, relwidth=0.75, relheight=0.92)
                def HexValsAllBytes():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/server-side-include/server-side-includes-generic.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def imessage():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/server-side-include/xml-attacks.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')

                def NullByteRepresentations():
                    F3 = Frame(F2, bd=8, relief=GROOVE, bg="black")
                    F3.place(x=252, y=71, relwidth=0.74, relheight=0.87)
                    self.txtarea = open(r"attack/server-side-include/shell-operators.txt", "r") 
                    data = self.txtarea.read()
                    scroll_y = Scrollbar(F3, orient=VERTICAL)
                    self.txtarea = Text(F3, yscrollcommand=scroll_y.set, font=("times new roman", 15, "bold"), fg="#ccc4c4", bg="#404040")
                    scroll_y.pack(side=RIGHT, fill=Y)
                    scroll_y.config(command=self.txtarea.yview)
                    self.txtarea.insert(END, data)
                    self.txtarea.pack(fill=BOTH,expand=1)
                    self.txtarea.configure(state ='disabled')
                def back():
                    F3 = main()
             
                Hacher_s = LabelFrame(F2, text="prat injection", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="black", fg="#ccc4c4").place(x=2, y=49, relwidth=0.24, relheight=0.92)
                p = Label(F2, text="Here are the full payloads.\nTo view payloads all you need to do is click on the payload button", font=("times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=72, relwidth=0.72, relheight=0.20)
                p = Label(F2, text="Injection flaws occur when untrusted user data are sent to the web application \nas part of a command or query. The attacker’s hostile data can trick the \nweb application into executing unintended commands or accessing\n unauthorized data. Injection occurs when a hacker feeds malicious, \n input into the web application\n that is then acted on (processed) in an unsafe manner.\n This is one of the oldest attacks\n against web applications, but it’s still the king of the vulnerabilities\n because it is still widespread and very \ndamaging.Injection vulnerabilities can pop up in all \nsorts of places within the web application\n that allow the user to provide malicious input.\n Some of the most common injection attacks target\n the following functionality:", font=(
            "times new roman", 15, "bold"), bd=7, relief=GROOVE, bg="#404040", fg="#ccc4c4")
                p.place(x=260, y=190, relwidth=0.72, relheight=0.65)
                b2_button = Button(F2, text ="includes-generic",command = HexValsAllBytes, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.15,anchor = NE)
          
                b4_button = Button(F2, text ="xml-attacks",command = imessage, fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx =0.23, rely = 0.24,anchor = NE)
            

                b5_button = Button(F2, text ="shell-operators",command = NullByteRepresentations,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.33,anchor = NE)
            
                b5_button = Button(F2, text ="back",command = back,fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="black").place(relx = 0.23, rely = 0.90,anchor = NE)
###############################
###############################
            
            b2_button = Button(F2, text ="server-side-include",command =server_side_include , fg ="#ccc4c4",width=16, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040").place(relx = 0.98, rely = 0.90,anchor = NE)

###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
###########################################################################################################

###########################################################################################################
        F2 = main()

        self.btn = Button(self.root, text = "sql injection",command=sql, width=20, bd=7, font=("arial 15 bold", 15, "bold"), relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid
        self.btn.place(relx = 0.21, rely = 0.14,anchor = NE)
# inside
        self.btn = Button(self.root, text = "xss injection",command=xss, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid
        self.btn.place(relx = 0.21, rely = 0.22,anchor = NE)
# inside
        self.btn = Button(self.root, text = "Command injection",command=comment, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid

        self.btn.place(relx = 0.21, rely = 0.30,anchor = NE)
# inside
        self.btn = Button(self.root, text = "ssf injection",command=ssf, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
# set Button grid

        self.btn.place(relx = 0.21, rely = 0.38,anchor = NE)
        self.btn1 = Button(self.root, text = 'xml injection',command = xml, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.46,anchor = NE)
        self.btn1 = Button(self.root, text = 'denial of service',command = service, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.54,anchor = NE)
        self.btn1 = Button(self.root, text = 'show injection',command = injection, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.62,anchor = NE)
        self.btn1 = Button(self.root, text = 'CVE-2023-PoC',command = CVEPoC, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")

        self.btn1.place(relx = 0.21, rely = 0.70,anchor = NE)
        self.btn1 = Button(self.root, text = 'Back to Payloads',command = main, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="#ccc4c4")
        self.btn1.place(relx = 0.21, rely = 0.78,anchor = NE)
        self.btn1 = Button(self.root, text = 'Quit !',command = self.root.destroy, width=20, bd=7, font="arial 15 bold", relief=GROOVE, bg="#404040", fg="red")
        self.btn1.place(relx = 0.21, rely = 0.85,anchor = NE)

        
        title = Label(self.root, text="Hackers A Tooles", font=("times new roman", 20, "bold"),
                      pady=2, bd=12, width=100, relief=GROOVE, bg="#404040", fg="#ccc4c4")
        title.place(relx = 0.5, rely = 0.1,anchor = 's')
        title = Label(self.root, text="Hackers A Tooles", font=("times new roman", 12, "bold"),
                      pady=2, bd=4, width=165, relief=GROOVE, bg="#404040", fg="#ccc4c4")
        title.place(relx = 0.5, rely = 0.98,anchor = 's')
        self.root.resizable(True, True)


###########################################################################################################

###########################################################################################################
    
    def popup(self):
        self.popup_menu = tkinter.Menu(self.root,
                                       tearoff = 0)
          
        self.popup_menu.add_command(label = "Copy",
                                    command = lambda:self.hey("Ctrl-C"))
          
        self.popup_menu.add_command(label = "Paste",
                                    command = lambda:self.hey("Paste"))
        self.popup_menu.add_separator()
        self.popup_menu.add_command(label = "Select All",
                                    command = lambda:self.hey("Select All"))

   
    #display menu on right click
    def do_popup(self,event):
        try:
            self.popup_menu.tk_popup(event.x_root,
                                     event.y_root)
        finally:
            self.popup_menu.grab_release()
   
    def hey(self,s):
        self.frame1.configure(text = s)
          
    def run(self):
        self.popup()
        self.root.bind("<Button-3>",self.do_popup)
        tkinter.mainloop()
    
  
a = home()
a.run()
