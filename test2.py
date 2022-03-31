class Software:
    pass


class LightSoftware(Software):
    pass


class Hardware:
    def __init__(self):
        self.soft = []

    def install(self, software: Software):
        if isinstance(software, Software):
            self.soft.append(software)

    def uninstall(self, software: Software):
        for el in self.s
h = Hardware()
ls = LightSoftware()
h.install(ls)

