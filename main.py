from kivy.properties import StringProperty, NumericProperty
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.list import OneLineListItem
from kivymd.uix.card import MDCard
from kivy.lang import Builder
from kivymd.uix.list import TwoLineListItem
from kivymd.uix.label import MDLabel
from kivy.core.window import Window
from kivymd.uix.menu import MDDropdownMenu
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import json
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
import requests
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
helpstr='''
<Command>
    size_hint_y: None
    pos_hint: {"right": .98}
    height: self.texture_size[1]
    padding: 1, 10
    theme_text_color: "Custom"
    text_color: 1, 1, 1, 1
    canvas.before:
        Color:
            rgb: (255/255,153/255,51/255,1)
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 23, 23]
<Respo>
    size_hint_y: None
    pos_hint: {"right": .98}
    height: self.texture_size[1]
    padding: 1, 10
    theme_text_color: "Custom"
    text_color: 0,0,0, 1
    canvas.before:
        Color:
            rgb:app.theme_cls.primary_color
        RoundedRectangle:
            size: self.width, self.height
            pos: self.pos
            radius: [23, 23, 23, 23]            
ScreenManager:
	FirstScreen:
<FirstScreen>:
	name:'firstscreen'
	MDBoxLayout:
		orientation:'vertical'
		padding:0
		md_bg_color:.1,.1,0.4,1
		MDBoxLayout:
			pos_hint:{'top':1}
			md_bg_color:1,1,1,1
			size_hint_x:1
			size_hint_y:0.1
			MDLabel:
				text:'Table Finder !!! '
				font_style:'H6'
				halign:'center'
		MDBoxLayout:
			pos_hint:{'top':0.9}
			md_bg_color:1,1,.1,1
			size_hint_x:1
			size_hint_y:0.1
			MDTextField:
				font_style:'H1'
				id:inputt
				hint_text:'Enter a No. to find its Table ...'
				mode:'fill'
				size_hint_x:0.05
				size_hint_y:1
			MDFlatButton:
				text:'Find'
				size_hint_y:1
				md_bg_color:app.theme_cls.primary_color
				on_release:
					app.func()
		MDBoxLayout:
			orientation:'vertical'
			pos_hint:{'bottom':1}
			md_bg_color:0.8,0.8,.8,1
			id:field
			padding:50
			MDScrollView:
				MDList:
					spacing:'10dp'
					id:lsst
					Respo:
						id:com
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com1
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40				
					Command:
						id:com2
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com3
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com4
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com5
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40		
					Command:
						id:com6
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40				
					Command:
						id:com7
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40							
					Command:
						id:com8
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com9
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40
					Command:
						id:com10
						text:''
						size_hint_x:.77
						halign:'center'
						font_size:40		
'''
class Command(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    #font_name = "Poppins"
    font_size = 40
class Respo(MDLabel):
    text = StringProperty()
    size_hint_x = NumericProperty()
    halign = StringProperty()
    #font_name = "Poppins"
    font_size = 40
class FirstScreen(Screen):
	pass
sm = ScreenManager()
sm.add_widget(FirstScreen(name='firstscreen'))
class TableApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(helpstr)
        return self.strng
    def func(self):
    	try:
    		i=self.strng.get_screen('firstscreen').ids.inputt.text
    	#i=int(i)
    		if self.strng.get_screen('firstscreen').ids.inputt.text !='':
    			i=int(i)
    			self.strng.get_screen('firstscreen').ids.com.text=f'Table of {i}'
    			self.strng.get_screen('firstscreen').ids.com1.text=f'{i} X {1} = {1*i}'
    			self.strng.get_screen('firstscreen').ids.com2.text=f'{i} X {2} = {2*i}'
    			self.strng.get_screen('firstscreen').ids.com3.text=f'{i} X {3} = {3*i}'
    			self.strng.get_screen('firstscreen').ids.com4.text=f'{i} X {4} = {4*i}'
    			self.strng.get_screen('firstscreen').ids.com5.text=f'{i} X {5} = {6*i}'
    			self.strng.get_screen('firstscreen').ids.com6.text=f'{i} X {6} = {6*i}'
    			self.strng.get_screen('firstscreen').ids.com7.text=f'{i} X {7} = {7*i}'
    			self.strng.get_screen('firstscreen').ids.com8.text=f'{i} X {8} = {8*i}'
    			self.strng.get_screen('firstscreen').ids.com9.text=f'{i} X {9} = {9*i}'
    			self.strng.get_screen('firstscreen').ids.com10.text=f'{i} X {10} = {10*i}'
    			self.strng.get_screen('firstscreen').ids.inputt.text =''
    	except:
    			Snackbar(text="An Error Occur").open()
    			self.strng.get_screen('firstscreen').ids.inputt.text =''
TableApp().run()
