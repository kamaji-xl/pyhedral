import zmq
import random
from stat_class import Stat

COUNT = "count"
HUNDRED = 100
SIDES = "sides"


def dice_roller(req, stat_list):
    results = []
    start = 1
    dice_count = req["count"]
    sides = req["sides"]
    char_name = req["name"]
    roll_type = req["type"]
    roll_mod = req["mod"]

    if char_name not in stat_list:
        new_char = Stat(char_name)
        stat_list[char_name] = new_char

    if sides == HUNDRED:
        start = 0
        sides = sides - 1

    for i in range(dice_count):
        roll = random.randint(start, sides)
        results.append(roll)
        stat_list[char_name].rolls[roll_type].append([roll, roll_mod])

    print(f"\n{results}")
    for stat in stat_list:
        print(stat_list[stat])

    return {
        "results": results
    }


def get_stats(req, stat_list):
    char_name = req["name"]
    roll_type = req["type"]
    res_stats = []

    if stat_list.get(char_name, None):
        if roll_type == "all":
            for stat in stat_list[char_name].rolls:
                if stat_list[char_name].rolls[stat]:
                    for roll in stat_list[char_name].rolls[stat]:
                        res_stats.append(roll)
        else:
            character = stat_list.get(char_name, None)
            if character is not None:
                res_stats = stat_list[char_name].rolls[roll_type]

    print(f"\n{res_stats}")

    res = {
        "character": char_name,
        "stats": res_stats
    }

    return res


def request_handler(req, stat_list):
    if req["command"] == "roll":
        res = dice_roller(req, stat_list)

    elif req["command"] == "get_stats":
        res = get_stats(req, stat_list)

    else:
        res = {"status": "error"}

    return res


if __name__ == "__main__":
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind(f"tcp://*:5555")

    print(f"Listening on port tcp://localhost:5555")

    stats = {}

    while True:
        try:
            request_json = socket.recv_json()
            print(request_json)
            response = request_handler(request_json, stats)
            print(f"\nsending response:")
            for key in response.keys():
                print(f"\t{key}: {response[key]}")
            socket.send_json(response)
        except zmq.error.ZMQError as e:
            print("ZMQ Error:", e)
