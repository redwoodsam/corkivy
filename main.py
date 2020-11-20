"""Calculadora de cores Kivy"""
from kivy.config import Config

Config.set('graphics', 'multisamples', '0')
Config.set('graphics', 'resizable', '0')
Config.set('input', 'mouse', 'mouse, disable_multitouch')

import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'

from kivy.core.window import Window
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

Window.size = 400, 400

VALOR_MAXIMO = 255
PORCENTAGEM_MAXIMA = 100

    
class Tela(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def tratar_entrada(self):
        texto = self.ids.digitado.text
        
        try:
            texto = texto.split(',')
            r = texto[0]
            g = texto[1]
            b = texto[2]

            r = (int(r)*PORCENTAGEM_MAXIMA/VALOR_MAXIMO)
            g = (int(g)*PORCENTAGEM_MAXIMA/VALOR_MAXIMO)
            b = (int(b)*PORCENTAGEM_MAXIMA/VALOR_MAXIMO)

            r = r/100
            g = g/100
            b = b/100

            if r>1 or g>1 or b>1:
                raise ValueError


            self.ids.output.text = "Cor kivy RGB: {:.2f}, {:.2f}, {:.2f} \n \nCor kivy RGBA: {:.2f}, {:.2f}, {:.2f}, 1.00".format(r, g, b,r,g,b)
            self.ids.digitado.text = ""
    
        except:
            self.ids.output.text = "Digite um valor RGB válido."    
            self.ids.digitado.text = ""


class CorApp(App):
    def build(self):
        return Tela()


if __name__ == "__main__":

    CorApp().run()