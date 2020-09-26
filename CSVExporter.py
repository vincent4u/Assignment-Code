

class CSVExporter:

    def __int__(self, filename, headings):
        self.rows = []
        self.headings = headings
        self.filename = filename

    def saveRow(self, row):
        # pass a complete string of a row with elements broken up by commas
        self.rows.append(row)

    def export(self):
        name = self.filename + ".csv"
        f = open(name, "w")
        for r in self.rows:
            r = r + "\n"
            f.write(r)
