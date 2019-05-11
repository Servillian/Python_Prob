class car:
    brand = "Honda"
    model = "CRV-H7"
    kms = 50000
    def sound(self):
        if self.brand == "Honda":
            print("Vroom")
        elif self.brand == "Tesla":
            print("Zwooo")



a = car()
b = car()
b.brand = "Tesla"
print(a.brand, b.brand)
a.sound()
b.sound()