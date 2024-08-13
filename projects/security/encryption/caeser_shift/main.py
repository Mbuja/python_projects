import string

class cipher():
    session_id=""
    #has default of 1
    cipher_rotation =1
    keys = string.printable

    def __init__(self,rotation):
        self.cipher_rotation =rotation
    
   
    def encrpyt(self,text):
        cipher_text= ""
        for i in text:
            index = self.keys.find(i)
            new_index = (index+self.cipher_rotation) % 100
            cipher_text += self.keys[new_index]
        return cipher_text
    
    
    def decrpyt(self,text):
        plain_text =""
        for i in text:
            index = self.keys.find(i)
            new_index =(index-self.cipher_rotation)%100
            plain_text+=self.keys[new_index]
        return plain_text


    def terminate(self):
        self.session_id=-1


if __name__=="__main__":
    myCipher = cipher(5)
    text = "K "
    print((myCipher.encrpyt(myCipher.encrpyt(text))))
    