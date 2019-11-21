class MusicPlayer(object):
    instance = None
    init_flag = False

    # 分配空间
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            print('实例化')
            cls.instance = super().__new__(cls)

        return cls.instance

    # 初始化对象，赋值
    def __init__(self):
        if not MusicPlayer.init_flag:
            MusicPlayer.init_flag = True
            print('初始化播放器')


if __name__ == '__main__':
    m1 = MusicPlayer()
    m2 = MusicPlayer()
    print(m1)
    print(m2)
