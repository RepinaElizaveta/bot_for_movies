import requests  # -- библиотека, необходимая для реализации api-запросов


# Класс, в котором хранятся данные о фильме, полученные от пользователя
# в ходе взаимодействия
class RequestData:
    my_type = ""
    genre = 0
    ratingFrom = 0
    yearFrom = 0
    yearTo = 2022
    keywords = ""

    def __init__(self, my_type, genre, ratingFrom, yearFrom, yearTo, keywords):
        self.my_type = my_type
        self.genre = genre
        self.ratingFrom = ratingFrom
        self.yearFrom = yearFrom
        self.yearTo = yearTo
        self.keywords = keywords


# Класс, в котором реализованы методы взаимодействия с пользователем
class UserCommunication:
    def startCommunication(self) -> int:
        """ Открывающий общение с пользователем метод """

        print("Привет! Я - бот для поиска фильмов, телевизионных шоу, "
              "сериалов и мини-сериалов.\n"
              "Я помогу найти то, что тебе точно понравится! "
              "Для того, чтобы я смог помочь,пожалуйста, "
              "ответь на несколько вопросов.")
        try:
            trial = int(input("Пожалуйста, выбери цифру способа, "
                              "которым ты хочешь найти фильм:\n"
                              "1. По фильтрам\n"
                              "2. По ключевым словам\n"))
        except:
            trial = int(input("Введно некорректное значение.\n"
                              "Пожалуйста, выбери цифру способа, "
                              "которым ты хочешь найти фильм:\n"
                              "1. По фильтрам\n"
                              "2. По ключевым словам\n"))
        while trial not in range(0, 3):
            try:
                trial = int(input("Введно некорректное значение.\n"
                                  "Пожалуйста, выбери цифру способа, "
                                  "которым ты хочешь найти фильм:\n"
                                  "1. По фильтрам\n"
                                  "2. По ключевым словам\n"))
            except:
                trial = int(input("Введно некорректное значение.\n"
                                  "Пожалуйста, выбери цифру способа, "
                                  "которым ты хочешь найти фильм:\n"
                                  "1. По фильтрам\n"
                                  "2. По ключевым словам\n"))
        return trial

    # Метод, вызываемый в случае выбора пользователем поиска по фильтрам
    def dataRequestFromUserByFilter(self) -> RequestData:
        """ Метод производит поиск по фильтрам """

        while True:
            try:
                my_type = ()
                what = int(input("Что ты хочешь посмотреть?\n"
                                 "Введи цифру:\n 1.Фильм\n 2.Телевизионное шоу\n"
                                 " 3.Сериал\n 4.Мини-сериал\n"))
                if what > 4:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Введно некорректное значение.\n"
                      "Пожалуйста, выбери цифру снова. \n")
        if what == 1:
            my_type = "FILM"
        if what == 2:
            my_type = "TV_SHOW"
        if what == 3:
            my_type = "TV_SERIES"
        if what == 4:
            my_type = "MINI_SERIES"

        while True:
            try:
                genre = int(input("Какой жанр ты хочешь посмотреть?\n"
                                  "Введи цифру из списка:\n 1.Триллер\n 2.Драма\n "
                                  "3.Криминал\n 4.Мелодрама\n 5.Детектив\n"))
                if genre > 5:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Введно некорректное значение.\n"
                      "Пожалуйста, выбери цифру снова. \n")

        while True:
            try:
                ratingFrom = int(input("Рейтинг может быть от 0 до 10.\n"
                                       "Я буду искать проивзведения с рейтингом не ниже:\n"))
                if ratingFrom > 10:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Введно некорректное значение.\n"
                      "Пожалуйста, выбери цифру снова. \n")

        print("Выбери временной промежуток.")

        while True:
            try:
                yearFrom = int(input("От какого года мне искать?\n"))
                if yearFrom < 0:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Введно некорректное значение.\n"
                      "Пожалуйста, выбери цифру снова. \n")
        while True:
            try:
                yearTo = int(input("На каком годе остановиться?\n"))
                if yearTo > 2022:
                    raise ValueError
                else:
                    break
            except ValueError:
                print("Введно некорректное значение.\n"
                      "Пожалуйста, выбери цифру снова. \n")
        # Возвращаем информацию о введенных фильтрах
        return RequestData(my_type, genre, ratingFrom, yearFrom, yearTo, "")

    # Метод, вызываемый в случае выбора пользователем поиска по ключевым словам
    def dataRequestFromUserByKeywords(self) -> RequestData:
        """ Метод производит поиск по ключевым словам """
        keywords = input("Введи через запятую ключевые слова:\n")

        # Возвращаем информацию о введенных ключевых словах
        return RequestData("", 0, 0, 0, 2022, keywords)


# Класс, в котором реализованы методы взаимодействия с api
class ApiRequester:
    def callApi(self, url_film_info, params):
        API_KEY = 'bda95582-a1ca-4627-ae54-fa46a777f350'
        response = requests.get(url_film_info,
                                params=params,
                                headers={
                                    'X-API-KEY': API_KEY,
                                    'Content-Type': 'application/json',
                                })
        json_response = response.json()
        # Возвращаем JSON с полученными от api данными
        return json_response


# -- Переменная, отвечающая за хранение url-ссылки запроса --
url_film_info = ""
# -- Переменная, отвечающая за хранение данных, полученных от пользователя --
dataFromUser: RequestData

# -- Список, хранящий разные параметры для словарей
#    в зависимости от траектории --
keys_of_dict = []
# -- Словарь для хранения необходимых параметорв фильма id --
params = dict()

# -- Инициализация класса UserCommunication --
userCommunicator: UserCommunication = UserCommunication()

# !Начало общения с пользователем!
choice = userCommunicator.startCommunication()

# На основе выбранной траектории происходит зарос данных по определенной ссылке
if choice == 1:
    url_film_info = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'
    dataFromUser: RequestData = userCommunicator.dataRequestFromUserByFilter()
    params = {
        'genres': dataFromUser.genre,
        'type': dataFromUser.my_type,
        'ratingFrom': dataFromUser.ratingFrom,
        'yearFrom': dataFromUser.yearFrom,
        'yearTo': dataFromUser.yearTo,
    }
    keys_of_dict = ['items', 'kinopoiskId', 'ratingKinopoisk']
elif choice == 2:
    url_film_info = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/' \
                    'search-by-keyword'
    dataFromUser: RequestData = userCommunicator.dataRequestFromUserByKeywords()
    params = {
        'keyword': dataFromUser.keywords
    }
    keys_of_dict = ['films', 'filmId', 'rating']

apiRequester: ApiRequester = ApiRequester()
json_response = apiRequester.callApi(url_film_info, params)

print("Вот, что ты можешь посмотреть:")

for slovar in json_response[keys_of_dict[0]]:
    print(slovar[keys_of_dict[1]], slovar["nameRu"])

print("\n")

# Выбор пользователем фильма, о котором он хотел бы узнать подробнее
id = input("О какой из этих работ ты хотел бы узнать больше?\n"
           "Введи id фильма (цифры перед названием):\n")

# -- Словарь для хранения информации о выбранном фильме --
wanted_film = {}

# -- Переменная, хранящая информацию о существовании выбранного фильма
#    в предложенном списке --
found = False
for film in json_response[keys_of_dict[0]]:
    if film[keys_of_dict[1]] == int(id):
        wanted_film = film
        found = True

# Блок, который проверяет случай ненахождения выбранного фильма в списке
while not found:
    id = input("В найденом списке нет введенного id.\n"
               "Пожалуйста, введи id фильма (цифры перед названием) из списка:\n")
    for film in json_response[keys_of_dict[0]]:
        if film[keys_of_dict[1]] == int(id):
            wanted_film = film
            found = True

# -- Переменная, хранящая ссылку на api с данными о наградах фильма --
url_film_awards = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/' \
                  + id + '/awards'
params = {
    "id": id
}

# -- Переменная, хранящая полученные после запроса данные о наградах --
json_awards_response = apiRequester.callApi(url_film_awards, params)

# Блок с выводом основной информации о выбранном фильме
message = ""
if wanted_film.get('nameRu'):
    message += f"Название фильма: {wanted_film['nameRu']}\n"
if wanted_film.get(keys_of_dict[2]):
    message += f"Рейтинг фильма: {wanted_film[keys_of_dict[2]]}\n"
if wanted_film.get('year'):
    message += f"Год выхода: {wanted_film['year']}\n"
if wanted_film.get('countries'):
    message += f"Страна: {wanted_film['countries'][0]['country']}\n"
if wanted_film.get('genres'):
    message += f"Жанр: {wanted_film['genres'][0]['genre']}\n"
if wanted_film.get('description'):
    message += f"Описание:\n{wanted_film['description']}"

print(message)

# Вывод на экран информации о наградах фильма
print("Это произведение получило следующие награды:")
for slovar in json_awards_response["items"]:
    print(f'{slovar["name"]}. {slovar["nominationName"]}.')
if len(json_awards_response["items"]) == 0:
    print("Нет наград")

print("\n")
while True:
    try:
        mark = int(input("Пожалуйста, оцени работу бота!\n"
                         "Выбери цифру от 1 до 5, "
                         "где 1 - очень плохо, а 5 - очень хорошо.\n"))
        if mark > 5 or mark < 1:
            raise ValueError
        else:
            break
    except ValueError as ex:
        print("Введно некорректное значение.\n"
              "Пожалуйста, выбери цифру снова. \n")
if mark == 5:
    good = input("Что тебе особенно понравилось?\n")
    print("Спасибо за твой отзыв!")
if mark == 2 or mark == 3 or mark == 4:
    cool = input("Что тебе понравилось?\n")
    bad = input("Что тебе не понравилось?\n")
    advice = input("Как ты считаешь, что еще можно добавить в бот?\n")
    print("Спасибо за твой отзыв!")
if mark == 1:
    bad = input("Что тебе не понравилось?\n")
    advice = input("Как ты считаешь, что еще можно добавить в бот?\n")
    print("Спасибо за твой отзыв!")