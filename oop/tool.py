class Tool:
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1

    @classmethod
    def show_tool_count(cls):
        print('工具种类：%d' % cls.count)


if __name__ == '__main__':
    tool1 = Tool('futou')
    tool2 = Tool('langgtou')
    tool3 = Tool('tieqiu')
    print(Tool.count)
    Tool.show_tool_count()
