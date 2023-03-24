""" 專案在學習grid的編排 """
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        ttkStyle =ttk.Style()
        ttkStyle.theme_use('default')
        ttkStyle.configure('red.TFrame',background='red')
        ttkStyle.configure('white.TFrame',background='white')
        ttkStyle.configure('yellow.TFrame',background='yellow')
        ttkStyle.configure('gridLabel.TLabel',font=('Helvetica', '16'),foreground='#666666')
        ttkStyle.configure('gridEntry.TEntry',font=('Helvetica', '16'))

        mainFrame = ttk.Frame(self)
        #ttk.Label(mainFrame,text='BMI試算').pack()
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=20,pady=20)
    
        #上面的Frame
        topFrame = ttk.Frame(mainFrame,height=100)
        topFrame.pack(fill=tk.X)

        ttk.Label(topFrame,text="BMI試算",font=('Helvetica', '16')).pack(pady=20)

        bottomFrame = ttk.Frame(mainFrame)
        bottomFrame.pack(expand=True,fill=tk.BOTH)
        #下面的Frame的間格
        bottomFrame.columnconfigure(0,weight=3,pad=20)
        bottomFrame.columnconfigure(1,weight=5,pad=20)
        bottomFrame.rowconfigure(0,weight=1,pad=20)
        bottomFrame.rowconfigure(3, weight=1, pad=20)
        bottomFrame.rowconfigure(4, weight=1, pad=20)
        bottomFrame.rowconfigure(5, weight=1, pad=20)
        bottomFrame.rowconfigure(6, weight=1, pad=20)

        #姓名欄位
        ttk.Label(bottomFrame,text="姓名:",style='gridLabel.TLabel').grid(column=0,row=0,sticky=tk.E)
        nameEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        nameEntry.grid(column=1,row=0,sticky=tk.W,padx=10)

        #出生年月日欄位
        ttk.Label(bottomFrame,text="出生年月日:",style='gridLabel.TLabel').grid(column=0,row=1,sticky=tk.E)
        ttk.Label(bottomFrame,text="(2000/03/01)",style='gridLabel.TLabel').grid(column=0,row=2,sticky=tk.E)
        birthEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        birthEntry.grid(column=1, row=1, sticky=tk.W, rowspan=2, padx=10)

        #身高欄位
        ttk.Label(bottomFrame,text="身高(cm):",style='gridLabel.TLabel').grid(column=0,row=3,sticky=tk.E)
        heightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        heightEntry.grid(column=1, row=3, sticky=tk.W, padx=10)

        #體重欄位
        ttk.Label(bottomFrame,text="體重(kg):",style='gridLabel.TLabel').grid(column=0,row=4,sticky=tk.E)
        weightEntry = ttk.Entry(bottomFrame,style='gridEntry.TEntry')
        weightEntry.grid(column=1, row=4, sticky=tk.W, padx=10)

        #訊息顯示區域
        messageText = tk.Text(bottomFrame,height=5,width=35,state=tk.DISABLED)
        messageText.grid(column=0,row=5,sticky=tk.N+tk.S,columnspan=2)

        #計算鍵
        commitBtn = ttk.Button(bottomFrame,text="計算")
        commitBtn.grid(column=1,row=6,sticky=tk.W)





def main():
    
    """ 這是執行點 """
    window = Window()
    window.title("BMI計算")
    #window.geometry("400x500")
    window.mainloop()

if __name__ == "__main__":
    main()