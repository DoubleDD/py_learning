class Women:
    def __init__(self, name):
        self.name = name
        self.__age = 18

    def __secret(self):
        print('我今年 %d 岁' % self.__age)

if __name__ == '__main__':
    xiaofang = Women('xiaofang')
    xiaofang._Women__secret()
    print(xiaofang._Women__age)
