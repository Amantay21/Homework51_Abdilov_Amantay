from random import randint

CAT_PHOTO_PATH_1 = 'images/cat1.jpg'
CAT_PHOTO_PATH_2 = 'images/cat2.jpg'
CAT_PHOTO_PATH_3 = 'images/cat3.jpg'
CAT_PHOTO_PATH_4 = 'images/cat4.jpg'

class Cat:
    name = ""
    age = 1
    satiety = 40
    mood = 40
    is_sleep = False
    avatar = CAT_PHOTO_PATH_1

    @classmethod
    def play(cls):
        if cls.is_sleep == True:
            cls.is_sleep = False
            cls.mood -= 5
            if cls.satiety < 0:
                cls.satiety = 0
            elif cls.mood < 0:
                cls.mood = 0
        else:
            rand_mood = randint(1, 3)
            if rand_mood == 1:
                cls.mood = 0
                cls.satiety -= 10
                if cls.satiety < 0:
                    cls.satiety = 0
                elif cls.mood > 100:
                    cls.mood = 100

            else:
                cls.mood += 15
                cls.satiety -= 10
                if cls.satiety < 0:
                    cls.satiety = 0
                if cls.mood > 100:
                    cls.mood = 100
        cls.avatar_status()

    @classmethod
    def feed(cls):
        if cls.is_sleep == True:
            return False
        else:
            cls.mood += 5
            cls.satiety += 15
            if cls.satiety >= 100:
                cls.satiety = 100
                cls.mood -= 30
                if cls.mood < 0:
                    cls.mood = 0
            elif cls.satiety < 0:
                cls.satiety = 0
        cls.avatar_status()


    @classmethod
    def put_to_sleep(cls):
        cls.is_sleep = True

    @classmethod
    def avatar_status(cls):
        if 75 <= cls.mood <= 100:
            cls.avatar = CAT_PHOTO_PATH_2
        if 50 <= cls.mood < 75:
            cls.avatar = CAT_PHOTO_PATH_1
        if 25 <= cls.mood < 50:
            cls.avatar = CAT_PHOTO_PATH_3
        if 0 <= cls.mood < 25:
            cls.avatar = CAT_PHOTO_PATH_4
