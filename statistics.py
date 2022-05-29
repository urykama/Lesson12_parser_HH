class Statistics:

    def __init__(self):
        self.stat = {}

    def find(self, requirement):
        for item in requirement:
            # print(item['name'].lower())
            if item['name'] in self.stat:
                self.stat[item['name']] += 1
            else:
                self.stat[item['name']] = 1
        return 0

    def get_stat(self):
        sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        return sorted_tuple
