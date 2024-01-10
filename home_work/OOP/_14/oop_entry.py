class Phone:
    __phone_number = None
    __incoming_calls = 0

    def set_number(self, number: str):
        self.__phone_number = number

    def accept_call(self):
        self.__incoming_calls += 1

    def get_incoming_calls(self) -> int:
        return self.__incoming_calls


tel1 = Phone()
tel2 = Phone()
tel3 = Phone()

tel1.set_number("+380503456789")
tel2.set_number("+380503000000")
tel3.set_number("+380667788990")

tel1.accept_call()
tel1.accept_call()

tel2.accept_call()
tel2.accept_call()
tel2.accept_call()

tel3.accept_call()
tel3.accept_call()
tel3.accept_call()
tel3.accept_call()


def get_all_accept_call(*args: object) -> int:
    all_accept_call = 0
    for obj in args:
        all_accept_call += obj.get_incoming_calls()

    return all_accept_call


def write_accept_calls(all_accept_call):
    with open("accept_calls.txt", "w") as file:
        file.write(f"The total number of received calls from all phones: {all_accept_call}")


write_accept_calls(get_all_accept_call(tel1, tel2, tel3))
