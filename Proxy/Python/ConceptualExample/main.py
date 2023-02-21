from proxy import Proxy
from real_subject import RealSubject
from subject import Subject


def client_code(subject: Subject) -> None:
    subject.request()


print("Client: Executing the client code with a real subject:")
real_subject = RealSubject()
client_code(real_subject)

print("")

print("Client: Executing the same client code with a proxy:")
proxy = Proxy(real_subject)
client_code(proxy)
