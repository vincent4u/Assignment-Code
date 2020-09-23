
class fileOutputer:

    def __int__(self,filename):
        self.lines = []
        self.filename = filename

    def addLine(self, line):
        self.lines.append(line)

    def output(self):
        f = open(self.filename, "w")
        for line in self.lines:
            f.write(line)
