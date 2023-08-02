import src.dwt as dwt
import src.windows as win
import time

def run():
    pathImg = 'DATA/'
    filename = 'cover image.png'
    pathImg = pathImg+filename
    print(pathImg)
    dwt.run(pathImg)
    win.run(pathImg)

if __name__ == '__main__':

    start=time.time()
    run()
    end=time.time()
    total=end-start
    print("Time Taken To compress image",str(total))
