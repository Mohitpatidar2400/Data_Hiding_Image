import tkinter as tk
from PIL import Image, ImageTk

def run(path):
    # This creates the main window for application
    window = tk.Tk()
    # Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    img0 = ImageTk.PhotoImage(Image.open(path))
    # This creates the main window of an application
    window.title("Wavelet compression")
    window.geometry(str(2*img0.width())+"x"+str(2*img0.height()))
    window.configure(background='grey')

    outputDir = 'output'

    img1 = ImageTk.PhotoImage(Image.open(outputDir + '/2.jpg'))
    img2 = ImageTk.PhotoImage(Image.open(outputDir + '/3.jpg'))
    img3 = ImageTk.PhotoImage(Image.open(outputDir + '/4.jpg'))
    img4 = ImageTk.PhotoImage(Image.open(outputDir + '/hidden.jpg'))

    

    panel1 = tk.Label(window, image = img1, borderwidth=0).grid(row=0,column=0) #Original
    panel2 = tk.Label(window, image = img2, borderwidth=0).grid(row=0,column=1) #YCbCr
    panel3 = tk.Label(window, image = img3, borderwidth=0).grid(row=1,column=0) #DWT
    panel4 = tk.Label(window, image = img4, borderwidth=0).grid(row=1,column=1) #iDWT RGB

    

   
    window.mainloop()

if __name__ == '__main__':
    run()
