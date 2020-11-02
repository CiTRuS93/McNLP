from simpletransformers.language_generation import LanguageGenerationModel

class McNLP:
    def __init__(self,):
        self.model = LanguageGenerationModel("gpt2", "from_scratch/best_model", args={"max_length": 200, "temperature":1},use_cuda=False)
    
    def generate(self,string_to_start,temperature=1, max_length=200):
        generated = self.model.generate(string_to_start,args={'temperature':temperature,'max_length':max_length}, verbose=False)
        return generated[0].replace(',','\n')



# mc = McNLP()
# f = open("demofile2.txt", "a", encoding='utf8')
# f.write(mc.generate("שורף את הביט", temperature=1.8,max_length=300))
# f.close()
# print()