class User:
    def say_hello(some_user):
        print("Hi! I'm {}!".format(some_user.name))

user1 = User()
user2 = User()
user3 = User()

user1.name = "김우진"
user1.email = "woojin@codeit.kr"
user1.password = "12345"

user2.name = "강영훈"
user2.email = "younghoon@codeit.kr"
user2.password = "98765"

user3.name = "최지웅"
user3.email = "jiwoong@codeit.kr"
user3.password = "78945"

User.say_hello(user1)