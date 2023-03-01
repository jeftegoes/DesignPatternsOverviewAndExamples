from person import Person


class ChatRoom:
    def __init__(self) -> None:
        self.peoples: list[Person] = []

    def join(self, person: Person):
        join_msg: str = f"{person.name} joins the chat"
        self.broadcast("room", join_msg)
        person.chat_room = self
        self.peoples.append(person)

    def broadcast(self, source: str, message: str) -> None:
        for people in self.peoples:
            if people.name != source:
                people.receive(source, message)

    def message(self, source, destination, message: str) -> None:
        for people in self.peoples:
            if people.name == destination:
                people.receive(source, message)