class Cat:
    def __init__(self, name):
        """
        __init__ 方法类似于java中得构造函数
        同时该方法也是用来定义类的属性的
        :param name: 名字
        """
        self.name = name
        print('%s 来了' % name)

    def __del__(self):
        print('%s 走了' % self.name)

    def __str__(self):
        """
        __str__ 方法类似于java中得 toString 方法
        :return:
        """
        return '我是小猫：%s' % self.name

    def eat(self):
        print('%s爱吃鱼' % self.name)

    def drink(self):
        print('%s在喝水' % self.name)


if __name__ == '__main__':
    tom = Cat('Tom')
    tom.drink()
    tom.eat()

    lazy_cat = Cat('大懒猫')
    lazy_cat.eat()
    lazy_cat.drink()

    print(tom)
    print(lazy_cat)
    print('tom is lazy_cat: %s' % str(tom is lazy_cat))