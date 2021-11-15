from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
import random


Builder.load_file('frontend.kv')

class FirstScreen(Screen):
    def get_image_link(self):
        #get user query from text input

        query= self.manager.current_screen.ids.user_query.text

        #get wikipedia page and link of first image
        try:
            page= wikipedia.page(query,auto_suggest=False)
            image_link= page.images[0]
        except wikipedia.exceptions.DisambiguationError as e:
            page =wikipedia.page(random.choice(e.options))
            image_link = page.images[0]

        return image_link

        #download image
    def download_image(self):
        headers={'User-agent':'Safari'}
        req= requests.get(self.get_image_link(),headers=headers)
        imagepath='files/image.jpg'
        with open(imagepath,'wb') as file:
            file.write(req.content)
        return imagepath

        #set image in the image widget
    def set_image(self):
        self.manager.current_screen.ids.img.source=self.download_image()
        self.manager.current_screen.ids.img.reload()


class RootWidget(ScreenManager):
    pass

class Image_SearcherApp(App):
    def build(self):
        return RootWidget()
Image_SearcherApp().run()
