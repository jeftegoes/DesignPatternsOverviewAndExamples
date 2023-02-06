class ElectricKettle:
    def __init__(self, adapter) -> None:
        self.adapter = adapter

    def boil(self):
        if (self.adapter.voltage() > 110):
            print("Kettle on fire!")
        else:
            if (self.adapter.live() == 1 and self.adapter.neutral() == -1):
                print("Coffe time!")
            else:
                print("No adapter.")