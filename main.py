from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition

class First(Screen):
    pass


class Calculator(Screen):

    def __init__(self, **kwargs):
        super(Calculator, self).__init__(**kwargs)

    def calculate(self):
        try:
            weight = int(self.ids.weight.text)
            t = round(weight - 2006)
            Proj = round(18825957328633.58 * 4253641/ (4253641 + (18825957328633.58 - 4253641) * 2.71828**(-0.030 * (t))))

            self.ids.results.text = (
                f"Hello! The population growth projection of Benue State for the year {weight} is {Proj}. "
                f"The following parameters were used: Time (t)={t}, and Growth rate (r)=3%."
            )
        except ValueError:
            self.ids.results.text = "Please enter a valid number."

    def clear(self):
        self.ids.results.text = ""
        self.ids.weight.text = ""


class ScreenManagement(ScreenManager):
    pass


starter = Builder.load_file("simeonbmiapp.kv")


class SimeonBmiApp(App):
    def build(self):
        return starter


if __name__ == '__main__':
    SimeonBmiApp().run()
