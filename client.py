import zmq


def get_char_stats(name, roll_type):
    request_json = {
        "command": "get_stats",
        "name": name,
        "type": roll_type
    }

    send_and_recv(request_json)


def make_roll(count, sides, name, roll_type, mod=0):
    request_json = {
        "command": "roll",
        "count": count,
        "sides": sides,
        "name": name,
        "type": roll_type,
        "mod": mod
    }

    send_and_recv(request_json)


def send_and_recv(req):
    socket.send_json(req)
    response = socket.recv_json()
    print("\nReceived response: ")
    print(f"\t{response}")


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    make_roll(5, 100, "test", "int", 0)
    make_roll(5, 100, "test", "spd", 0)
    make_roll(5, 100, "test", "str", 0)
    make_roll(5, 100, "test", "cbt", 0)
    get_char_stats("test", "all")
