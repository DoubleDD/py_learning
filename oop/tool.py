

class Tool:
    count = 0

    def __init__(self, name):
        self.name = name

        Tool.count += 1


if __name__ == '__main__':
    tool1 = Tool('futou')
    tool2 = Tool('langgtou')
    tool3 = Tool('tieqiu')
    print(Tool.count)

