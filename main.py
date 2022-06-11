import requests # -- библиотека, необходимая для реализации api-запросов


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
        ''' Открывающий общение с пользователем метод '''

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
        ''' Метод производит поиск по фильтрам '''

        what = int(input("Что ты хочешь посмотреть?\n"
                         "Введи цифру:\n 1.Фильм\n 2.Телевизионное шоу\n "
                         "3.Сериал\n 4.Мини-сериал\n"))
        if what == 1:
            my_type = "FILM"
        if what == 2:
            my_type = "TV_SHOW"
        if what == 3:
            my_type = "TV_SERIES"
        if what == 4:
            my_type = "MINI_SERIES"
        else:
            my_type = None
        while int(what) >= 5:
            print("Нет такого значения.")
            what = int(input("Введи цифру заново:\n"))
        genre = input("Какой жанр ты хочешь посмотреть?\n"
                      "Введи цифру из списка:\n 1.Триллер\n 2.Драма\n "
                      "3.Криминал\n 4.Мелодрама\n 5.Детектив\n")
        while int(genre) >= 6:
            print("Нет такого значения.")
            genre = (input("Введи цифру заново:\n"))
        ratingFrom = input("Рейтинг может быть от 0 до 10.\n"
                           "Я буду искать проивзведения с рейтингом не ниже:\n")
        while int(ratingFrom) >= 11:
            print("Нет такого значения.")
            ratingFrom = (input("Введи цифру заново:\n"))
        print("Выбери временной промежуток.")
        yearFrom = input("От какого года мне искать?\n")
        yearTo = input("На каком годе остановиться?\n")
        return RequestData(my_type, genre, ratingFrom, yearFrom, yearTo, "")

    # Метод, вызываемый в случае выбора пользователем поиска по ключевым словам
    def dataRequestFromUserByKeywords(self) -> RequestData:
        ''' Метод производит поиск по ключевым словам '''
        keywords = input("Введи ключевые слова:\n")
        return RequestData("", 0, 0, 0, 2022, keywords)


# Класс, в котором реализованы методы взаимодействия с api
class ApiRequester:
    def callApi(self,url_film_info,params):
        API_KEY = 'bda95582-a1ca-4627-ae54-fa46a777f350'
        response = requests.get(url_film_info,
                                params=params,
                                headers={
                                    'X-API-KEY': API_KEY,
                                    'Content-Type': 'application/json',
                                })
        json_response = response.json()
        return json_response

# -- Переменная, отвечающая за хранение url-ссылки запроса --
url_film_info = ""
# -- Переменная, отвечающая за хранение данных, полученных от пользователя --
dataFromUser: RequestData

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
elif choice == 2:
    url_film_info = 'https://kinopoiskapiunofficial.tech/api/v2.1/films/' \
                    'search-by-keyword'
    print(url_film_info)
    dataFromUser: RequestData = userCommunicator.dataRequestFromUserByKeywords()
    params = {
        'keyword': dataFromUser.keywords
    }

apiRequester: ApiRequester = ApiRequester()
json_response = apiRequester.callApi(url_film_info, params)


print("Вот, что ты можешь посмотреть:")
if choice == 1:
    for slovar in json_response["items"]:
        print(slovar["kinopoiskId"], slovar["nameRu"])
elif choice == 2:
    for slovar in json_response["films"]:
        print(slovar["filmId"], slovar["nameRu"])

print("\n")
id = input("О какой из этих работ ты хотел бы узнать больше?\n"
           "Введи id фильма (цифры перед названием):\n")
url_film_awards = 'https://kinopoiskapiunofficial.tech/api/v2.2/films/'\
                  + id + '/awards'


params = {
    "id": id
}

json_awards_response = apiRequester.callApi(url_film_awards, params)

print("Это произведение получило следующие награды:")
for slovar in json_awards_response["items"]:
    print(f'{slovar["name"]}. {slovar["nominationName"]}.')



