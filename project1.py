import pickle
import json
def line():
    print('-'*50)
def write():
    d = {}
    fw = open('bakerytestnew101.dat','ab') #main file 
    while True:
        pr = input('enter product = ')
        ct = input('enter category = ')
        rs = int(input('enter price = '))
        d['product = '] = pr
        d['category = '] = ct
        d['price = '] = rs
        pickle.dump(d,fw)
        a = input('enter to exit  y')
        if  a == 'y':
            break
        line()
    fw.close()
    fr = open('bakerytestnew101.dat','rb') 
    fnvw = open('nonvegtestnew101.dat','wb') #write non veg data
    fvw = open('vegtestnew101.dat','wb')#write veg data
    c = {}
    try:
        while True:
            c = pickle.load(fr)
            if c['category = '] == 'veg':
                pickle.dump(c,fvw)
            elif c['category = '] == 'non veg':
                pickle.dump(c,fnvw)          
    except EOFError:
        fr.close()
        fvw.close()
        fnvw.close()
        print('DATA TRANSFER SUCCESSFULLY!!!')
def readveg():     #read veg product details
    fvr = open('vegtestnew101.dat','rb')
    a = {}
    global listvg
    global lvgprice
    listvg = []
    lvgprice = []
    try:
        while True:
            a = pickle.load(fvr)
            for i in a:                
                if i == 'product = ':
                    listvg.append(a[i])
                if i == 'price = ':
                    lvgprice.append(a[i])
            print(json.dumps(a,indent=5))
    except EOFError:
        fvr.close()
def readnonveg():  #read nonveg product details
    fnvr = open('nonvegtestnew101.dat','rb')
    b = {}
    global listnvg
    global lnvgprice
    listnvg = []
    lnvgprice = []
    try:
        while True:
            b = pickle.load(fnvr)
            for j in b:
                if j == 'product = ':
                    listnvg.append(b[j])
                if j == 'price = ':
                    lnvgprice.append(b[j])
            print(json.dumps(b,indent=5))
    except EOFError:
        fnvr.close()
def append(x,name): #add to cart 
    n = int(input('enter how many producs u want to add = '))
    line()
    totalvg = 0
    totalnvg = 0
    if x == 'veg':
        for i in range(1,n+1):
            crt = input('enter product = ')
            quantvg = int(input('enter how much quantity u want for this product = '))
            line()
            print()
            for i in listvg:
                if i == crt:
                    indexpr = listvg.index(crt)
                    pricevg = lvgprice[indexpr]
                    totalvg+=pricevg*quantvg
        print('THANK YOU',name.upper(),'FOR YOUR ORDER your total bill--->',totalvg,'/-')
    if x == 'non veg':
        for j in range(1,n+1):
            crt = input('enter product = ')
            quantnvg = int(input('enter how much quantity u want for this product = '))
            line()
            print()
            for j in listnvg:
                  if j == crt:
                    indexpr = listnvg.index(crt)
                    pricenvg = lnvgprice[indexpr]
                    totalnvg+=pricenvg*quantnvg
        print('THANK YOU',name.upper(),'your total bill--->',totalnvg,'/-') 
#-------------------------------------------main root------------------------------------------------------------------
print('<-----------------------------------WELCOME TO THE WORLD OF BAKERY ----------------------------------------->')
print()
owner = input('ARE U THE OWNER yes/no = ')
if owner.lower() == 'yes':
    p = int(input('if u want to write enter password = ')) #password is 1212
    if p == 1212: #password
        a = int(input('do u want to add products press 1 for yes = '))
        if a == 1:
            write() #write open
else:
    name = input('Enter your name = ')
    print('CHOOSE YOUR PRODUCT CATEGORY:')
    line() #------------------------------------------------------------------------------------
    x = input('what u prefer veg or non veg products = ') #to ask for read
    print()
    if x.lower() in ['nonveg','non veg']: 
        readnonveg()
    if x.lower() == 'veg':
        readveg()
    line() #-----------------------------------------------------------------------------------
    n = input('do u want to add to cart anything yes/no = ')
    if n.lower() == 'yes':
        append(x,name)
    if n.lower() == 'no': 
        print('have a nice day')
print('<--------------------------------THANK YOU FOR YOUR VISIT---------------------------------------------------->')