import os
import random
import shutil
import time

#populateFolder

def createFile(fname,size):
    with open(f"temp/{fname}", "wb") as out:
        out.truncate(1024 * size)

def GenerateAttachments(fileExtension,size,numberOfAttachments):
    for i in range(numberOfAttachments):
        if fileExtension == 'mixed':
            createFile(f"sampleAttachment{i}{mixedAttachments()}",size)
        else:
            createFile(f"sampleAttachment{i}{fileExtension}",size)

def mixedAttachments():
    extensions = ['.pdf','.txt','.doc','.csv','.xls','.jpg','.mp3']
    return random.choice(extensions)

def Generate(fExt,fSize,noOfAttachments):
    os.mkdir('temp')
    GenerateAttachments(fExt,fSize,noOfAttachments)
    shutil.rmtree('temp')