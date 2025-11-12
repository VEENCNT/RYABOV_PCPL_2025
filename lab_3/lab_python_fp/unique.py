class Unique:
    def __init__(self, data, **kwargs):
        self.used_elements = set()
        self.data = data
        self.index = 0
        
        if len(kwargs) == 1 and "ignore_case" in kwargs.keys():
            self.ignore_case = kwargs["ignore_case"]
        else:
            self.ignore_case = False

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]      
                self.index = self.index + 1

                if self.ignore_case and str(current).lower() in [str(i).lower() for i in self.used_elements]:
                    continue

                if not self.ignore_case and current in self.used_elements:
                    continue

                self.used_elements.add(current)
                return current
            
if __name__ == "__main__":
    data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']

    print(list(Unique(data)))
    print(list(Unique(data, ignore_case=True)))