import json

class message:
    def __init__(self, message, owner):
        self.message = message
        self.owner = owner
    
class Person:
    def __init__(self, name, condition, age, languages, nationality, phoneNumber, ispatient, city):
        self.ispatient: bool = ispatient
        self.name: str = name 
        self.condition: str = condition
        self.age: int = age
        self.languages: list[str] = languages
        self.nationality: str = nationality
        self.phoneNumber: str = phoneNumber
        self.city: str = city
        self.requestUsers = []

    def sendMessageToChat(self, message, chat):
        msg = message(message, self)
        chat.addMessage(msg)

    def leaveChat(self, other):
        for i in chats:
            if (i.patient == self and i.advisor == other) or (i.advisor == self and i.patient == other):
                chats.remove(i)
        return chats

    def sendMessageToGroupChat(self, message, groupChat):
        msg = message(message, self)
        groupChat.addMessage(msg)

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

class GroupChat:
    def __init__(self, users):
        self.users = users
        self.messages = []
    
    def addMessage(self, message):
        self.messages.append(message)

    def addUser(self, user):
        self.users.append(user)

    def removeUser(self, user):
        self.users.remove(user)

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

users = [Chat("buss", "ing")]
chats = [Chat("buss", "ing"),  Chat("buss", "ing"), Chat("buss", "ing")]
GroupChats = [GroupChat([Person("hi", "hi", 1, ["hi"], "hi", "hi", True, "hi"), Person("hi", "hi", 1, ["hi"], "hi", "hi", True, "hi")])]


# Users is a list of objects of class Person, which need to be added to the file backup.json. Write a function SaveData that saves the users list to a file called backup.json. The function should take no arguments and return nothing.

def SaveData(): 
    with open('users.json', 'w') as file:     
        #upload the chats list to the file
        json.dump(users, file, default=lambda o: o.__dict__, indent=4)
    with open('chats.json', 'w') as file:
        json.dump(chats, file, default=lambda o: o.__dict__, indent=4)
    with open('groupchat.json', 'w') as file:
        json.dump(GroupChats, file, default=lambda o: o.__dict__, indent=4)

def LoadData():
    with open('users.json', 'r') as file:
        users = json.load(file)
    with open('chats.json', 'r') as file:
        chats = json.load(file)
    with open('groupchat.json', 'r') as file:
        GroupChats = json.load(file)
    return chats, users, GroupChats

def convertToChat(chat):
    patient = convertToPerson(chat.get("patient"))
    advisor = convertToPerson(chat.get("advisor"))
    messages = chat.get("messages")
    chat = Chat(patient, advisor)
    chat.messages = messages
    return chat    

def convertToPerson(user):
    name = user.get("name")
    condition = user.get("condition")
    age = user.get("age")

    languages = user.get("languages")
    nationality = user.get("nationality")
    phoneNumber = user.get("phoneNumber")
    ispatient = user.get("ispatient")
    city = user.get("city")

    person = Person(name, condition, age, languages, nationality, phoneNumber, ispatient, city)
    return person

def convertToGroupChat(gc):
    x = gc.get("users")
    users = []
    for i in x:
        users.append(convertToPerson(i))
    messages = gc.get("messages")
    groupChat = GroupChat(users)
    groupChat.messages = messages
    return groupChat

def convert(chats, users, GroupChats):
    newChats = []
    newUsers = []
    newGroupChats = []
    for chat in chats:
        newChats.append(convertToChat(chat))
    for user in users:
        newUsers.append(convertToPerson(user))
    for groupChat in GroupChats:
        newGroupChats.append(convertToGroupChat(groupChat))
    
    return newChats, newUsers, newGroupChats


# def main():
#     c, u, g = LoadData()
#     SaveData()
#     c1, u1, g1 = convert(c, u, g)
    
# main() 
