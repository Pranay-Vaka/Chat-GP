import json
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    categories = models.Manager()
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    description = models.CharField(max_length=1000, default="")


class Forum(models.Model):
    forums = models.Manager()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.CharField(max_length=500)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)


class Message(models.Model):
    messages = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    content = models.CharField(max_length=4096)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    posts = models.Manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default="No title")
    content = models.CharField(max_length=4096)
    time_stamp = models.DateTimeField(auto_now_add=True)


class Person:
    def __init__(
        self, name, condition, age, languages, nationality, phoneNumber, ispatient, city
    ):
        self.ispatient: bool = ispatient
        self.name: str = name
        self.condition: str = condition
        self.age: int = age
        self.languages: list[str] = languages
        self.nationality: str = nationality
        self.phoneNumber: str = phoneNumber
        self.city: str = city
        self.requestUsers = []

    def sendMessage(self, message, chat):
        msg = message(message, self)
        chat.addMessage(msg)

    def leaveChat(self, chat):
        chat = None

    def sendRequest(self, desiredUser):
        desiredUser.requestUsers.append(self)

    def removeRequest(self, requestedUser):
        self.requestUsers.remove(requestedUser)

    def retractRequest(self, requestedUser):
        requestedUser.requestUsers.remove(self)

    def acceptRequest(self, request):
        self.requestUsers.remove(request)
        chat = Chat(self, request)
        return chat

    def rankUsers(self, users):
        # sort the users by the compare function
        users.sort(key=compare(self, users), reverse=True)
        return users


class Chat:
    def __init__(self, patient, advisor):
        self.patient = patient
        self.advisor = advisor
        self.messages = []

    def addMessage(self, message):
        self.messages.append(message)


def compare(patient, advisor):
    score = 0
    if patient.condition == advisor.condition:
        score += 550

    for i in patient.languages:
        for a in advisor.languages:
            if a == i:
                score += 150

    if patient.age - advisor.age < 5:
        score += 150
    elif patient.age - advisor.age < 10:
        score += 75
    elif patient.age - advisor.age < 20:
        score += 50
    else:
        score += 25

    if patient.city == advisor.city:
        score += 150

    return score


users = []
chats = []


# Users is a list of objects of class Person, which need to be added to the file backup.json. Write a function SaveData that saves the users list to a file called backup.json. The function should take no arguments and return nothing.


def SaveData():
    with open("users.json", "w") as file:
        # upload the chats list to the file
        json.dump(users, file, default=lambda o: o.__dict__, indent=4)
    with open("chats.json", "w") as file:
        json.dump(chats, file, default=lambda o: o.__dict__, indent=4)


def LoadData():
    with open("users.json", "r") as file:
        users = json.load(file)
    with open("chats.json", "r") as file:
        chats = json.load(file)
    return chats, users


set = [-2, -4, 1, 3]
set.sort(key=lambda x: abs(x))
print(set)


def main():
    chats, users = LoadData()
    print(chats)
    print(users)
    request = ""

    """
    if request == "send" and user == x and chat == y:
        if users[x].isPatient and chat.patient == users[x] or not users[x].isPatient and chat.advisor == users[x]:
            users[x].sendMessage("Hello", chats[y])
    elif request == "leave":
        if chats[0].patient == users[0] or chats[0].advisor == users[0]:
            users[0].leaveChat(chats[0])
    elif request == "join":
        if users[0].ispatient != users[1].ispatient:
            users[x].sendRequest(users[y])
    elif request == "remove":
        if users[0].ispatient != users[1].ispatient and users[0].requestUsers[0] == users[1]:
            users[x].removeRequest(users[y])
    elif request == "retract":
        if users[0].ispatient != users[1].ispatient and users[0].requestUsers[0] == users[1]:
            users[x].retractRequest(users[y])
    elif request == "accept":
        if users[0].ispatient != users[1].ispatient and users[0].requestUsers[0] == users[1]:
            users[0].acceptRequest(users[1])
    """
    SaveData()


# Create your models here.
