import os
import random
import shutil
import time

#populateFolder

def createFile(fname,size):
    with open(f"temp/{fname}", "wb") as out:
        out.truncate(1024 * size)

def GenerateAttachments(fileExtension,minfSize,maxfSize,numberOfAttachments):
    for i in range(numberOfAttachments):
        if fileExtension == 'mixed':
            createFile(f"sampleAttachment{i}{mixedAttachments()}",random.randint(int(minfSize),int(maxfSize)))
        else:
            createFile(f"sampleAttachment{i}{fileExtension}",random.randint(int(minfSize),int(maxfSize)))

def mixedAttachments():
    extensions = ['.pdf','.txt','.doc','.csv','.xls','.jpg','.mp3']
    return random.choice(extensions)

def Generate(fExt,minfSize,maxfSize,noOfAttachments):
    os.mkdir('temp')
    GenerateAttachments(fExt,minfSize,maxfSize,noOfAttachments)

def Remove():
    shutil.rmtree('temp')