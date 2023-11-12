from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDRaisedButton 
from kivymd.uix.selectioncontrol import MDCheckbox


from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.pagelayout import PageLayout
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager , Screen
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.properties import NumericProperty
from kivy.properties import BooleanProperty
# from kivy.properties import ObjectProperty
from kivy.properties import BoundedNumericProperty

from kivy.config import Config
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.uix.image import Image

import random
from main_db import *
from translateApi import *
from kivy.utils import platform


# from reg import *



# Config.set('graphics', 'resizable', '0')  
# Config.set('graphics', 'width', '360')
# Config.set('graphics', 'height', '800')



# class TableObj:
#     pass
 
    
# class ListScreen(Screen):
#     one  = ObjectProperty()
#     two  = ObjectProperty()
#     three  = ObjectProperty()
#     four = ObjectProperty()
#     five  = ObjectProperty()
    
#     def __init__(self, **kwargs):
#         super(Screen, self).__init__(**kwargs)
        
#         # self.layout = BoxLayout(orientation="vertical")
#         # self.layout1 = BoxLayout(orientation="horizontal",size_hint_y = 0.2)
#         # # self.layout2 = BoxLayout(orientation="vertical") 
#         # self.relativeLayout = PageLayout(size_hint_y = 0.8)     
#         # self.layout = BoxLayout(orientation="vertical")
        
#         self.layoutBox1 = BoxLayout(orientation="vertical")
#         self.layoutBox2 = BoxLayout(orientation="vertical")
#         self.layoutBox3 = BoxLayout(orientation="vertical")
#         self.layoutBox4 = BoxLayout(orientation="vertical")
#         self.layoutBox5 = BoxLayout(orientation="vertical")
         
#         self.Page = PageLayout()             
         


         
         
#         self.one = self.add_md_table(1)
#         self.two = self.add_md_table(2)
#         self.three = self.add_md_table(3)
#         self.four = self.add_md_table(4)
#         self.five = self.add_md_table(5)
        
#         buttonTest1= MDRaisedButton(text='Level 1')
#         buttonTest2= MDRaisedButton(text='Level 2')
#         buttonTest3= MDRaisedButton(text='Level 3')
#         buttonTest4= MDRaisedButton(text='Level 4')
#         buttonTest5= MDRaisedButton(text='Level 5')
        

        

#         self.layoutBox1.add_widget(buttonTest1)
#         self.layoutBox1.add_widget(self.one)
        
#         self.layoutBox2.add_widget(buttonTest2)
#         self.layoutBox2.add_widget(self.two)
        
#         self.layoutBox3.add_widget(buttonTest3)
#         self.layoutBox3.add_widget(self.three)
        
#         self.layoutBox4.add_widget(buttonTest4)
#         self.layoutBox4.add_widget(self.four)
        
#         self.layoutBox5.add_widget(buttonTest5)
#         self.layoutBox5.add_widget(self.five)
        

        
        
        
#         self.Page.add_widget(self.layoutBox1)
#         self.Page.add_widget(self.layoutBox2)
#         self.Page.add_widget(self.layoutBox3)
#         self.Page.add_widget(self.layoutBox4)
#         self.Page.add_widget(self.layoutBox5)



#         # self.layout.add_widget(self.layoutBox)
        
#         # self.layout0.add_widget(self.layoutButton)
#         # button1 = MDRaisedButton(text='Click Me')
#         # button1.bind(on_press=lambda instance, level=1: self.on_button_click(instance, level))
#         # button2 = MDRaisedButton(text='Click Me')
#         # button2.bind(on_press=lambda instance, level=2: self.on_button_click(instance, level))
#         # button3 = MDRaisedButton(text='Click Me')
#         # button3.bind(on_press=lambda instance, level=3: self.on_button_click(instance, level))
#         # button4 = MDRaisedButton(text='Click Me')
#         # button4.bind(on_press=lambda instance, level=4: self.on_button_click(instance, level))
#         # button5 = MDRaisedButton(text='Click Me')
#         # button5.bind(on_press=lambda instance, level=5: self.on_button_click(instance, level))



#         # # self.layout1.add_widget(button)
#         # # self.layout.add_widget(self.one)
#         # self.one.size_hint = (None,None)
#         # self.two.size_hint = (None,None)
#         # self.three.size_hint = (None,None)
#         # self.four.size_hint = (None,None)
#         # self.five.size_hint = (None,None)
        
#         # self.one.pos= (0, 0)#_hint = {'center_x': 0.5, 'center_y': 0.5}
#         # self.two.pos= (0, 0)#_hint = {'center_x': 0.5, 'center_y': 0.5}
#         # self.three.pos= (0, 0)#_hint = {'center_x': 0.5, 'center_y': 0.5}
#         # self.four.pos= (0, 0)#_hint = {'center_x': 0.5, 'center_y': 0.5}
#         # self.five.pos = (0, 0) #_hint = {'center_x': 0.5, 'center_y': 0.5}
        
#         # self.one.opacity = 0
#         # self.two.opacity = 0
#         # self.three.opacity = 1
#         # self.four.opacity = 1
#         # self.five.opacity = 1 
        
#         # self.layout1.add_widget(button1)
#         # self.layout1.add_widget(button2)
#         # self.layout1.add_widget(button3)
#         # self.layout1.add_widget(button4)
#         # self.layout1.add_widget(button5)
#         # self.layout.add_widget(self.layout1)
        
#         # self.relativeLayout.add_widget(self.one)
#         # self.relativeLayout.add_widget(self.two)
#         # self.relativeLayout.add_widget(self.three)
#         # self.relativeLayout.add_widget(self.four)
#         # self.relativeLayout.add_widget(self.five)
#         # self.layout2.add_widget(self.relativeLayout)
#         # self.layout.add_widget(self.relativeLayout)
        
        
#         self.add_widget(self.Page)
         
#     def add_md_table(self,level):
       
#         ls = takeFromDbList(level)
#         countLs = len(ls)
#         self.table = MDDataTable(
#             column_data= [
#             ("№", dp(40)),
#             ("word", dp(40)),
#             ("translation", dp(40)),
#             ("last practice (days)", dp(40))
#             ],
#             row_data = [],
#             rows_num = countLs
#                 # ('number','word','translation', 'last practice')
            
#                                  )
#         # self.layout.add_widget(self.table)
        
#         # for i in range(len(ls)):
#         # print(i+1,' ', ls[i])
#         # Remove vertical scrollbar

        
#         for i in range(countLs):
#             row = [i+1]
#             for j in range(3):
#                 row.append(ls[i][j])
#             self.table.row_data.append(row)
#         return self.table
    
#     def getTable(self):
#         self.layout.add_widget(self.one)        

CONST_BackroundColor = (151/255, 197/255, 196/255, 1)
CONST_ElipseLite = (141/255, 186/255, 185/255, 1)
CONST_ElipseDark = (136/255, 178/255, 178/255, 1)
CONST_SecondColor = (146/255, 146/255, 227/255, 1)
CONST_ShadowColor = (126/255, 165/255, 164/255, 1)
CONST_ActiveColor = (146/255, 227/255, 169/255, 1)
CONST_BorderMainStaticColor = (162/255, 212/255, 211/255, 1)
CONST_borderButtonColor  = (162/255,212/255,211/255,1)
# CONST_BorderSecondaryStaticColor = (146/255, 146/255, 227/255, 1)



class Main(Widget):
    pass

class Other(Screen):
    backroundColor = BoundedNumericProperty(CONST_BackroundColor)

        

 



        


class Manager(ScreenManager):
    pass

# class entity():
#     def __init__(self) -> None:



class MainScreen(Screen):
    one  = NumericProperty()
    two  = NumericProperty()
    three  = NumericProperty()
    four = NumericProperty()
    five  = NumericProperty()
    
    oneR  = NumericProperty()
    twoR  = NumericProperty()
    threeR  = NumericProperty()
    fourR = NumericProperty()
    fiveR  = NumericProperty()
    
    isDisable1 = BooleanProperty(False)
    isDisable2 = BooleanProperty(False)
    isDisable3 = BooleanProperty(False)
    isDisable4 = BooleanProperty(False)
    isDisable5 = BooleanProperty(False)
    
    backroundColor = BoundedNumericProperty(CONST_BackroundColor)
    borderStatic = BoundedNumericProperty(CONST_BorderMainStaticColor)
    secondColor = BoundedNumericProperty(CONST_SecondColor)
    elipseLite = BoundedNumericProperty(CONST_ElipseLite)
    elipseDark = BoundedNumericProperty(CONST_ElipseDark)
    borderButtonColor = BoundedNumericProperty(CONST_borderButtonColor)

    def on_pre_enter(self, *args):
        self.emptyCheck()
    def emptyCheck(self):
        self.countDict = selectCount()
        self.countDictReady = selectCountReady()
        #self.examp  = 200
        for i in range(1,6):
            self.countDict.setdefault(i,0)
            self.countDictReady.setdefault(i,0)            
            if i == 1:
                self.one = self.countDict[1]
                self.oneR = self.countDictReady[1]
                if self.countDictReady[1]>0:self.isDisable1 = False
                else: self.isDisable1 = True
            elif i== 2 :
                self.two = self.countDict[2]
                self.twoR = self.countDictReady[2]
                if self.countDictReady[2]>0:self.isDisable2 = False
                else: self.isDisable2 = True
            elif i== 3 : 
                self.three = self.countDict[3]
                self.threeR = self.countDictReady[3]
                if self.countDictReady[3]>0:self.isDisable3 = False
                else: self.isDisable3 = True
            elif i== 4 : 
                self.four = self.countDict[4]
                self.fourR = self.countDictReady[4]
                if self.countDictReady[4]>0:self.isDisable4 = False
                else: self.isDisable4 = True
            elif i== 5 : 
                self.five = self.countDict[5]
                self.fiveR = self.countDictReady[5]
                if self.countDictReady[5]>0:self.isDisable5 = False
                else: self.isDisable5 = True
                # if(self.countDict[i]<=0): 

       


# Practise screen widget
class WorkScreen(Screen):
    activeWord = StringProperty('eror')
    list = ListProperty()
    count = NumericProperty(10)
    level = NumericProperty(0)    
    fontSizeCalk = NumericProperty(0)
    SondVisible = NumericProperty(0)

    backroundColor = BoundedNumericProperty(CONST_BackroundColor)
    borderStatic = BoundedNumericProperty(CONST_BorderMainStaticColor)
    secondColor = BoundedNumericProperty(CONST_SecondColor)
    elipseLite = BoundedNumericProperty(CONST_ElipseLite)
    elipseDark = BoundedNumericProperty(CONST_ElipseDark)
    borderButtonColor = BoundedNumericProperty(CONST_borderButtonColor)

    def __init__(self, **kw):
        super().__init__(**kw)
        
    def callSound(self,text):
        giveSound(text)

    def calculateFontSize(self,width,height,text):
        font_size = min(width / len(text), height) * 0.65
        return font_size    

    def len_with_default(self,seq):
        length = len(seq)
        if length == 0:
            return 1
        else:
            return length
    # label_width = self.root.width - 10
    # get selected by user amount of word to practise/ return numeric variable
    def getNumberOfWords(self,value=10):
        self.count = int(value)
        # print('worked')
        return self.count

    def textFit(self,width,height,txt):
        words = txt.split()
        countWords = len(words)
        if countWords > 1:
            largestWord = max(words, key=len, default="")
            countHeight = height/countWords
            result = min(countHeight * 1.4, (width/ self.len_with_default(largestWord))*1.6 )
        else:
            result = min(height * 0.5, (width/ self.len_with_default(txt))*1.6 ) 
        return result
    #get tuple with selected by user amount of word to practice from databese 
    def getList(self,level):
        if self.count != 0:
            self.list = takeFromDbLim(level,self.count)#list(range(self.count))
            self.randOrder = list(range(len(self.list)))
            random.shuffle(self.randOrder)
        else:
            self.list = takeFromDb(level)
            self.randOrder = list(range(len(self.list)))
            random.shuffle(self.randOrder)
        # print(self.list)
        return self.list
    
    
    # funktion called when user select level 
    def changeLevel(self,level):
        self.level = level
        self.param = 1
        self.i = 0
        self.SondVisible = 0
        self.list = self.getList(self.level)
        self.manager.get_screen('second').ids.showWord.text = f'level {level}'

        if len(self.list) > 0:
            self.activeWord =  str(self.list[self.randOrder[self.i]][self.param])
        else:
            print('There not words')
        # self.fontSizeCalk = self.calculateFontSize(self.width*10-10,self.height*7,str(self.activeWord))
        
        return str(self.activeWord)
    
    
    # function that change word with translation and vise verse
    def showTranslation(self):
        if self.param == 1:
            self.param = 0
            self.SondVisible = 1
        elif self.param ==0:
            self.param =1
            self.SondVisible = 0
        self.activeWord = str(self.list[self.randOrder[self.i]][self.param])
        # self.fontSizeCalk = self.calculateFontSize(self.width-10,self.height*0.5,self.activeWord)

        
    # function that show next word    
    def nextWord(self):
        self.param = random.randint(0,1)
        if self.param == 1:
            self.SondVisible = 0
        elif self.param ==0:
            self.SondVisible = 1
        self.i = self.i+1
        if len(self.randOrder)>self.i:
            self.activeWord =  str(self.list[self.randOrder[self.i]][self.param])
            # self.fontSizeCalk = self.calculateFontSize(self.width-10,self.height*0.5,self.activeWord)
        else: 
            # print('finished')
            self.manager.current = 'first'
            
            
    # function that change level +1 of word and show next word when button 'remember pressed'
    def remember(self):
        self.check = self.level
        self.level = self.level + 1
        updateLevel(self.level,self.list[self.randOrder[self.i]][2])
        self.level = self.check
        self.nextWord()    
    
        
    # function that change level =1 of word and show next word when button 'Not remember pressed'         
    def notRemember(self):
        self.check = self.level
        self.level = 1
        updateLevel(self.level,self.list[self.randOrder[self.i]][2])
        self.level = self.check
        self.nextWord()       
        
    # select from db count of words in every level return dict


    # def show(self,level):
    #     print(self.countDict)
    #     print(self.examp)
    #     return self.countDict[level]
    #     # if level !=0:
    #     #     pass
    #     # else:
    #     #     self.contDict = {level:0,level:0,level:0,level:0,level:0}
    
        

class MenuScreen(Screen):
    backroundColor = BoundedNumericProperty(CONST_BackroundColor)
    borderStatic = BoundedNumericProperty(CONST_BorderMainStaticColor)
    borderButtonColor = BoundedNumericProperty(CONST_borderButtonColor)
    


# screen for adding words to DB
class AddWord(Screen):
    # add word and translation from input to DB
    backroundColor = BoundedNumericProperty(CONST_BackroundColor)
    borderStatic = BoundedNumericProperty(CONST_BorderMainStaticColor)
    secondColor = BoundedNumericProperty(CONST_SecondColor)
    elipseLite = BoundedNumericProperty(CONST_ElipseLite)
    elipseDark = BoundedNumericProperty(CONST_ElipseDark)

    wordError = StringProperty('')
    translationError = StringProperty('')
    
    
    def submit(self):
        word = self.ids.word.text
        #search(word)
        translation = self.ids.translation.text
        if len(translation )<1 and len(word)<1:
            self.wordError = 'Please enter word to study'
            self.translationError = 'Please enter translation to study'
        elif len(translation)<1: 
            self.wordError = ''
            self.translationError = 'Please enter translation to study'
        elif len(word)<1:
            self.wordError = 'Please enter word to study'
            self.translationError = '' 
        else:
            if len(word.split())>1:
                word.replace(' ','\n')
            if len(translation.split())>1:
                translation.replace(' ','\n')
            addInDb(word,translation)
            self.ids.word.text = ""
            self.ids.translation.text= ""
            self.wordError = ''
            self.translationError = ''
            print(word)
            
        
        # try: 
        #     int(word)
        #     int(translation)            
        #     print("EROOR")
        #     self.ids.word.text = ""
        #     self.ids.translation.text= ""
        #     self.ids.alert.text = "Numbers are not exepted"

        # except:
        # search(translation)        


class Experiment(Screen):
    pass

# class CustomCheckBox(MDCheckbox):
#     col = BoundedNumericProperty(CONST_SecondColor)
#     def __init__(self, **kwargs):
#         super(CustomCheckBox, self).__init__(**kwargs)
#         self.theme_text_color = 'Error'
#         self.text_color = self.col
#         self.unselected_color = [0, 0, 0, 0]  # Color when unchecked (green)
#         self.selected_color = [1, 0, 1, 1] 
#         self.thumb_color = [1,1,1,1]

class MyApp(MDApp):
    def getDB():
        if platform == 'android':
            db_path = App.get_running_app().user_data_dir+'\list.db'
            print('Platform information:', platform) 

        elif platform == 'win':
            Window.size = (360  ,760)
            db_path = App.get_running_app().user_data_dir +'\list.db'
            print('windows')
            print('Platform information:', platform) 
        else:
        # Use a different path for non-Android platforms
            db_path = 'list000.db'
            print('Platform information:', platform) 
        return db_path
    def build(self):
        print('here')
        getConect(MyApp.getDB())
        self.theme_cls.theme_style = "Dark"
        # self.theme_cls.primary_palette = "DeepPurple"
        self.root = Builder.load_file('My.kv')
    # def on_stop(self):
    #     closePyttsx3()
    # pass








    
if __name__ == "__main__":
    MyApp().run()   