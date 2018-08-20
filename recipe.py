from abc import ABC,abstractmethod

class AbstractRecipe(ABC):

    def excute(self):
        self.prepare()
        self.recipe()
        self.cleanup()

    @abstractmethod
    def prepare(self):pass

    @abstractmethod
    def recipe(self):pass

    @abstractmethod
    def cleanup(self):pass


class Recipe1(AbstractRecipe):

    def prepare(self):
        print("do dishes")
        print("get raw materials")

    def recipe(self):
        print("follow the recipe")

    def cleanup(self):
        print("clean all bowls")


recipe1 = Recipe1()
recipe1.excute()