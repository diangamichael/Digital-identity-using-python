from tkinter import *
from tkinter import filedialog
import ipfshttpclient


client = ipfshttpclient.Client('/dns/localhost/tcp/5001/http')


root = Tk()
root.title('selected file')

def dialogBox():
    root.filename = filedialog.askopenfilename(initialdir="/home/zero/Desktop", title="Select A File", filetypes=(("all files", "*.*"), ("jpg files", "*.jpg")))
    my_label = Label(root, text=root.filename).pack()
    print(root.filename)

def myClick():
    try:
        res = client.add(root.filename)
        print(res['Hash'])
        hashVal = res['Hash']
        myLabel = Label(root, text=f"{root.filename} for hash value :--> {hashVal}")
        myLabel.pack()
    except:
        print('Please turn on the IPFS Daemon Process if you are using linux run startDeamon.sh')




if __name__ == '__main__':
    while True:
        dialogBox()
        Button(root, text="Submit", command=myClick).pack()
        Button(root, text="Quit", command=quit).pack()
        root.mainloop()















