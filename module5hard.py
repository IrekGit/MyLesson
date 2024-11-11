import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(str(password))
        self.age = age


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if self.current_user is not None:
            print(f'Такой пользователь уже авторизован как {self.current_user.nickname}')
            return

        for user in self.users:
            if user.nickname == nickname and user.password == hash(str(password)):
                self.current_user = user
                print(f'Добро пожаловать, {nickname}!')
                return
        print('Неверный логин или неверный пароль')

    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return

        new_user = User(nickname, password, age)
        self.users.append(new_user)
        self.current_user = new_user
        print(f'Регистрация прошла успешно, добро пожаловать {nickname}!')

    def log_out(self):
        if self.current_user is None:
            print('Вы не авторизованы')
        else:
            print(f'До свидания, {self.current_user.nickname}!')
            self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not any(v.title == video.title for v in self.videos):
                self.videos.append(video)
                print(f'Видео "{video.title}" добавлено')
            else:
                print(f'Видео "{video.title}" уже существует')

    def get_videos(self, search_word):
        search_word = search_word.lower()
        found_videos = [video.title for video in self.videos if search_word in video.title.lower()]
        return found_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Войдите в аккаунт для просмотра видео')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста, покиньте страницу!')
                    return

                print(title)
                while video.time_now < video.duration:
                    print(video.time_now)
                    time.sleep(1)  # Пауза 1 секунда
                    video.time_now += 1

                print('Конец видео')
                return

        print(f'Видео "{title}" не найдено')


if __name__ == "__main__":

    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user.nickname)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')