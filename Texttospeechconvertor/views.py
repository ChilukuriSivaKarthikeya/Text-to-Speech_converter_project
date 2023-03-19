from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from googletrans import Translator
from gtts import gTTS
import os
os.environ['SDL_AUDIODRIVER'] = 'dsp'
import pygame
from io import BytesIO
import pytesseract
from PIL import Image

def home(request):
    return render(request,'tts.html')
def textreader(request):
    t=request.POST['text']
    l=request.POST['languages']
    translator = Translator()
    file1 = BytesIO()
    x=translator.translate(t,src='en',dest=l)
    s=x.text
    o=gTTS(text=s,lang=l,slow=False)
    o.write_to_fp(file1)
    pygame.mixer.init()
    pygame.mixer.music.load(file1,"mp3")
    pygame.mixer.music.play()
    clock = pygame.time.Clock()
    while pygame.mixer.music.get_busy():
        clock.tick(60)
    return redirect('/')
def filereader(request):
   if request.method=="POST":
      f=request.FILES['document']
      l=request.POST['languages']
      translator = Translator()
      fs = FileSystemStorage()
      fs.save(f.name,f) 
      file1 = BytesIO()
      filepath="media\\"+f.name 
      f=open(filepath,'r')
      result=f.read()
      x=translator.translate(result,src='en',dest=l)
      text1=x.text
      o=gTTS(text=text1,lang=l,slow=False)
      o.write_to_fp(file1)
      pygame.mixer.init()
      pygame.mixer.music.load(file1,"mp3")
      pygame.mixer.music.play()
      clock = pygame.time.Clock()
      while pygame.mixer.music.get_busy():
         clock.tick(60)
      f.close()  
      os.remove(filepath)
    
   return redirect('/')
def imagereader(request):
    if request.method=="POST":
      f=request.FILES['image']
      fs = FileSystemStorage()
      fs.save(f.name,f)
      imagepath='media\\'+f.name
      l=request.POST['languages']
      img = Image.open(imagepath)
      pytesseract.pytesseract.tesseract_cmd="C:\Program Files\Tesseract-OCR/tesseract.exe"
      result = pytesseract.image_to_string(img)
      translator = Translator()
      file1 = BytesIO()
      x=translator.translate(result,src='en',dest=l)
      s=x.text
      o=gTTS(text=s,lang=l,slow=False)
      o.write_to_fp(file1)
      pygame.mixer.init()
      pygame.mixer.music.load(file1,"mp3")
      pygame.mixer.music.play()
      '''while True:
        x=request.POST.get("action",False)
        if x=="pause":
            pygame.mixer.music.pause()
        elif x=="unpause":
            pygame.mixer.music.unpause()
        elif x=="stop":
            pygame.mixer.music.stop()
            break'''
      clock = pygame.time.Clock()
      while pygame.mixer.music.get_busy():
        clock.tick(60)
      
      os.remove(imagepath)
      
    return redirect('/')  


 