from simpletransformers.language_generation import LanguageGenerationModel

import os.path

def download_model():
    import dropbox
    dbx = dropbox.Dropbox("gzhGYnEbdx0AAAAAAAAAAW5Ab2pW_0ShlpGFbDOnBkzRTlSLJCBn889-RDubhfLt")

    with open("from_scratch/best_model/pytorch_model.bin", "wb") as f:
        print("getting file")
        metadata, res = dbx.files_download(path="/mcnlp/pytorch_model.bin")
        print("writing file")
        f.write(res.content)
class McNLP:
    def __init__(self,):
        if not os.path.isfile('from_scratch/best_model/pytorch_model.bin'):
            download_model()    
        
        self.model = LanguageGenerationModel("gpt2", "from_scratch/best_model", args={"max_length": 200, "temperature":1},use_cuda=False)


    def generate(self,string_to_start,temperature=1, max_length=200):
        generated = self.model.generate(string_to_start,args={'temperature':temperature,'max_length':max_length}, verbose=False)
        return generated[0].replace(',','\n')



# mc = McNLP()
# f = open("demofile2.txt", "a", encoding='utf8')
# f.write(mc.generate("שורף את הביט", temperature=1.8,max_length=300))
# f.close()
# print()