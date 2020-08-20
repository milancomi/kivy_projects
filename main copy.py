import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button



class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid,self).__init__(**kwargs) # GRIDLAYOUT CONSTRUCTOR CALL
        self.cols=1

        self.inside = GridLayout()
        self.inside.cols=2


        #First Name input
        self.inside.add_widget(Label(text="First name: "))
        self.firstName= TextInput(multiline=False)
        self.inside.add_widget(self.firstName)

        #Last name input
        self.inside.add_widget(Label(text="Last name: "))
        self.lastName= TextInput(multiline=False)
        self.inside.add_widget(self.lastName)
 
         #mail input
        self.inside.add_widget(Label(text="Email: "))
        self.email= TextInput(multiline=False)
        self.inside.add_widget(self.email)
 
        self.add_widget(self.inside)


        # submit button
        self.submit = Button(text="Submit",font_size=40)
        self.submit.bind(on_press=self.pressed)
        self.add_widget(self.submit)

    def pressed(self,instance):
        fName = self.firstName.text
        lName = self.lastName.text
        email = self.email.text

        print("Name: ",fName,"last Name: ",lName,"Email: ",email)
        self.firstName.text = ""
        self.lastName.text = ""
        self.email.text = ""

class MyApp(App):
    def build(self):
        return MyGrid()
        #Label(text="Malo nesto ozbiljnije")




if __name__=="__main__":
    MyApp().run()



 