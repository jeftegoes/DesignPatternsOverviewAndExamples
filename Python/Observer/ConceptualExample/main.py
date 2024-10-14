from concrete_observer_a import ConcreteObserverA
from concrete_observer_b import ConcreteObserverB
from concrete_subject import ConcreteSubject

subject = ConcreteSubject()

observer_a = ConcreteObserverA()
subject.attach(observer_a)

observer_b = ConcreteObserverB()
subject.attach(observer_b)

subject.some_business_logic()
subject.some_business_logic()

subject.detach(observer_a)

subject.some_business_logic()