class Baby:
    def __init__ (self , name , energy , happiness) :
        self.name = name
        self.energy = energy
        self.happiness = happiness

    def info(self):
        print (f"{self.name} is so {self.happiness} and {self.energy}")

if __name__ == "__main__" :
    b1 = Baby("Ali","he is full of energy", "Happy")
    b1.info()