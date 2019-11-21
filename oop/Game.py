class Game:
    top_score = 0

    def __init__(self, name):
        self.player_name = name

    @staticmethod
    def show_help():
        print('游戏帮助：让僵尸走进房间')

    @classmethod
    def show_top_score(cls):
        print('游戏最高分：%d' % cls.top_score)

    def start_game(self):
        print('[%s] 游戏开始' % self.player_name)
        Game.top_score = 999


if __name__ == '__main__':
    Game.show_help()
    Game.show_top_score()
    game = Game('小明')
    game.start_game()
    Game.show_top_score()
