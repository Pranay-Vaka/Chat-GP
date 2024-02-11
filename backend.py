class message:
    def __init__(self, message, owner):
        self.message = message
        self.owner = owner
    
class person:
    def __init__(self, name, condition, age, languages, nationality, phoneNumber, ispatient):
        self.ispatient: bool = ispatient
        self.name: str = name 
        self.condition: str = condition
        self.age: int = age
        self.languages: list[str] = languages
        self.nationality: str = nationality
        self.phoneNumber: str = phoneNumber

    def sendMessage(self, message, chat):
        msg = message(message, self)
        chat.addMessage(msg)

    def leaveChat(self, chat):
        chat = None

    def joinChat(self, userList):
        for i in userList:
            if i.ispatient != self.ispatient:
               if compare(self, i):
                    if self.ispatient:
                        chat = chat(self, i)
                        return chat
                    chat = chat(i, self)
                    return chat
        return None
    
class chat:
    def __init__(self, patient, advisor):
        self.patient = patient
        self.advisor = advisor
        self.messages = []
    
    def addMessage(self, message):
        self.messages.append(message)

def compare(patient, advisor):
    if patient.condition == advisor.condition:
        for i in patient.languages:
            for a in advisor.languages:
                if a == i:
                    return True
                
