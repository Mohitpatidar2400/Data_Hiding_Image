import Rsa
import huffman

# Text Encryption and lossless Compression

def Encoder_text():
    inp=str(input("Enter a Plain text : "))
    with open("input.txt",'w') as f:
        f.write(inp)


    
    msg=Rsa.rsaEncryption('input.txt');
    encoding,tree=huffman.Huffman_Encoding(msg)
    buffer=bytearray(encoding,encoding="utf-8")
    return tree, buffer

# Text Decryption and Decompression

def Decoder_text(Tree,msg):
    
    decoding=huffman.Huffman_Decoding(str(msg),Tree)
    msg2=  Rsa.rsaDecryption(decoding)
    string=""
    for i in msg2:
        string+=i

    print(" Decrypted message: ",string)
    return string
