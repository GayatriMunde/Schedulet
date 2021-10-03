import os 

def convertPdf(filename):
    command = 'pdftotree -o ./data/output.html '+ filename
    os.system(command)

if __name__ == "__main__":
   convertPdf("./data/outline.pdf")