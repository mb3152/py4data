import os
import sys
import time
import urllib2
import urllib
import cStringIO
import json
import Image
import ImageDraw
from Tkinter import * 
from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance

class ImageManipGUI(Tk):
    def __init__(self):

        Tk.__init__(self)

        #create user interface
        f = Frame(self, height=2, bd=1, relief=SUNKEN,background='grey')
        f.pack(fill='x')
        
        #get input
        self.Label = Label(f, background = 'grey', text="Type Image Search Below:").pack()
        self.entrytext = StringVar()
        self.Entry = Entry(f, textvariable=self.entrytext).pack()
        self.Search  = Button(f,text='Search or Reset Image!', command = self.get_image).pack()

        #make frame 
        self.frameButton = Button(f, text='Frame', command=self.draw_rectangle).pack(side='left')

        #brighten
        self.brightenButton = Button(f, text='Brighten',command=self.on_brighten).pack(side='left')

        #mirror
        self.mirrorButton = Button(f, text='Mirror',command=self.on_mirror).pack(side='left')

        #sharpen
        self.sharpenButton = Button(f, text='Sharpen', command=self.sharpen).pack(side='left')

        #contrast
        self.contrastButton = Button(f, text='Contrast',command=self.contrast).pack(side='left')

        # set the angle of the rotation
        self.angle = StringVar(self)
        self.angleMenu = OptionMenu(f, self.angle,*('1','5','10','20','30','45','90'))
        self.angleMenu.config(width=5)
        self.angle.set('90')
        self.angleMenu.pack(side='left')

        #rotate, pack it next to the option menu
        self.rotateButton = Button(f, text='Rotate', command=self.rotate).pack(side='left')
        #save image
        self.saveButton = Button(f, text = 'Save Image', command = self.save_image).pack(side='left')
        #make canvas
        self.canvas = Canvas(self, bd=0, highlightthickness=0, width=150, height=150,background='black')
        self.canvas.pack(fill='both', expand=1)
        #show url box
        self.text = Text(self,height=2, font=8)

    def get_image(self): #passes input to a google image search.
        try: 
            x = self.entrytext.get()
            search = x.split()
            search = '%20'.join(map(str, search))
            url = 'http://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=%s&safe=off' % search
            search = urllib2.Request(url)
            result = urllib2.urlopen(search)
            outs = result.read()
            js = json.loads(outs)
            results = js['responseData']['results']
            for i in results: 
                rest = i['unescapedUrl']
            x = rest.encode('ascii','ignore')
            img = cStringIO.StringIO(urllib.urlopen(x).read())
        except:
            img = 'try-again.jpg'  #load try again image if there is an error getting image data
        im = Image.open(img)
        im.thumbnail((512,512))
        self.tkphoto = ImageTk.PhotoImage(im)
        self.canvasItem = self.canvas.create_image(0,0,anchor='nw',image=self.tkphoto)
        self.canvas.config(width=im.size[0], height=im.size[1])
        self.img = im
        self.temp = im.copy()
        self.display_url(url) #call url show function.
    
    def display_url (self,url):
        self.text.delete(1.0,END) #delete old URL
        self.text.insert(INSERT, 'IMAGE URL:' + url)
        self.text.pack()
    def display_image(self, aImage):
        self.tkphoto = pic = ImageTk.PhotoImage(aImage)
        self.canvas.itemconfigure(self.canvasItem, image=pic)

    def on_mirror(self):
        im = ImageOps.mirror(self.temp)
        self.display_image(im)
        self.temp = im

    def on_brighten(self):
        brightener = ImageEnhance.Brightness(self.temp)
        self.temp = brightener.enhance(1.05) # +5%
        self.display_image(self.temp)

    def sharpen(self):
        sharper = ImageEnhance.Sharpness(self.temp)
        self.temp = sharper.enhance(1.15) # +15%
        self.display_image(self.temp)
    def contrast(self):
        contrast = ImageEnhance.Contrast(self.temp)
        self.temp = contrast.enhance(1.2) # +20%
        self.display_image(self.temp)
    def draw_rectangle(self):
        bbox = 5, 5, self.temp.size[0] - 15, self.temp.size[1] - 15        
        draw = ImageDraw.Draw(self.temp)
        draw.rectangle(bbox, outline='grey')
        self.display_image(self.temp)
    def rotate(self):
        im = self.temp.rotate(float(self.angle.get()))
        self.display_image(im)
        self.temp = im
    def save_image(self):
    	image = self.temp
    	image.save('manipulatedimage.jpg')

GUI = ImageManipGUI()
GUI.mainloop()