from abc import ABC, abstractmethod
from dataclasses import dataclass


# Example 1
class Observer(ABC):
    @abstractmethod
    def update(self, observable):
        pass


class Observable(ABC):
    @abstractmethod
    def register_observer(self, *observer):
        pass

    @abstractmethod
    def notify(self):
        pass


@dataclass
class Person(Observer):
    name: str

    def reply(self, chat):
        cmd = input('Vrei sa raspunzi? (Y/N) ')
        if cmd == 'Y':
            self.send_message(chat)

    def update(self, observable):
        last_message = observable._messages[-1]
        if last_message.content.startswith(self.name) and last_message.author != self:
            print(f'{self.name}: am primit un mesaj!')
            self.reply(observable)

    def send_message(self, chat):
        the_input = input(f'{self.name} please enter the message: ')
        chat.add_message(Message(self, the_input))


class Chat(Observable):
    _observers = []

    def __init__(self):
        self._messages = []

    def add_message(self, msg):
        self._messages.append(msg)
        self.notify()

    def register_observer(self, *observer):
        self._observers.extend(observer)

    def notify(self):
        for obs in self._observers:
            obs.update(self)


@dataclass
class Message:
    author: Person
    content: str


chat = Chat()
# print(chat._messages)
a = Person('Alex')
b = Person('Bianca')
c = Person('Cristina')
chat.register_observer(a, b, c)
print(chat._observers)
a.send_message(chat)


# Example 2
class ObservableAddUser:
    name = "ObservableAddUser"

    def __init__(self):
        self._observers = []

    def __str__(self):
        return f'I am {self.name}'

    def registre_observer(self, observer):
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs):
        for obs in self._observers:
            obs.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, observable):
        observable.registre_observer(self)

    def notify(self, observable, *args, **kwargs):
        print('Got:', args, kwargs, 'From:', observable)


subject = ObservableAddUser()
observer_obj = Observer(subject)

subject.notify_observers('test', kw='python')
