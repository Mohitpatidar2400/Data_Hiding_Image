

import text_main as tm
import Stego as st
from PIL import Image
import numpy as np

 

def Encoder(image_path):
   
    Tree, message=tm.Encoder_text()

    new_image=st.Encode_text(image_path,message)
    new_image=Image.fromarray(new_image)
    new_image.save("hidden.png")
    return Tree


def Decoder(Tree):
    im=Image.open("hidden.png")
    image=np.array(im)
    message=st.Decode_text(image)
    msg=""
    msg=tm.Decoder_text(Tree,message)
    
    with open("Process_text.txt",'w') as f:
        f.write(msg)

if __name__=="__main__":
    Tree=Encoder('hide image.jpg')
    Decoder(Tree)
    print("Execution Successful")
