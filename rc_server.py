import socket, json, sys

import rc_login as rcl
import rc_strings as rcs
import rc_stats as rs
import rc_votes as rv
import rc_bans as rb


def open_socket():
    s = socket.socket()
    port = 18181

    s.bind(('', port))
    s.listen(5)

    while True:
        c, addr = s.accept()

        try:
            decoded = json.loads(c.recv(128).decode())
        except (UnicodeDecodeError, json.decoder.JSONDecodeError):
            print(rcs.decode_error(addr[0]))
            continue

        if decoded["task"] == "rc_login":
            rq = decoded["username"]
            print(rcs.login_attempt(rq))
            result = rcl.user_login(rq)
            c.send(result.encode())

        elif decoded["task"] == "rc_getstats":
            rq = decoded["username"]
            stats = rs.get_user_stats(rq)
            c.send(json.dumps(stats).encode())

        elif decoded["task"] == "rc_getvotes":
            votes = rv.read_vote_data()
            sendit = json.dumps(votes).encode()
            print(rcs.votes_request(sys.getsizeof(sendit)))
            c.send(sendit)

        elif decoded["task"] == "rc_getbans":
            bans = rb.read_bans()
            sendit = json.dumps(bans).encode()
            print(rcs.bans_request(sys.getsizeof(sendit)))
            c.send(sendit)

        else:
            print(rcs.unknown_request(addr[0]))

        c.close()


if __name__ == '__main__':
    rcs.server_start()
    open_socket()
