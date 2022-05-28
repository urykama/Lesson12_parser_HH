class Statistics:

    def __init__(self):
        self.stat = {
            'образование': 0,
            'ооп': 0,
            'парсинг': 0,
            'c++': 0,
            'c#': 0,
            'html': 0,
            'java': 0,
            'javascript': 0,
            'js': 0,
            'ph': 0,
            'python': 0,
            'нейронные сети': 0,
            'big data': 0,
            'django': 0,
            'resr': 0,
            'linux': 0,
            'api': 0,
            'http': 0,
            'flask': 0,
            'git': 0,
            'pytest': 0,
            'oracle': 0,
            'postgresql': 0,
            'sql': 0,
            'mysql': 0,
            'mssql': 0
        }

    def find(self, requirement):
        n = 0
        try:
            for key in self.stat.keys():
                if requirement.find(key) > 0:
                    self.stat[key] += 1
                    n += 1
        except AttributeError:
            pass
        return n

    def get_stat(self):
        sorted_tuple = sorted(self.stat.items(), key=lambda x: x[1], reverse=True)
        return sorted_tuple
