import time, os

not_found = 'USER_NOT_FOUND'
login_failed = 'LOGIN_FAILED'
no_custom_skin = 'NO_CUSTOM_SKIN'

staff_translate = [
    'fr4gright',
    'Fearless',
    'Dennis',
    'Retlix',
    'BjornNL',
    'Console'
]


def server_start():
    os.system('clear')
    print("#     Developed by    #\n" +
          "#         RvT         #\n" +
          "# RebrovoCraft @ 2020 #\n" +
          "\n>> Phyton Server started at {0}\n".format(get_time()))


def get_time():
    timestamp = time.localtime()
    formated = time.strftime("%x %X", timestamp)
    return '{0}'.format(formated)


def login_attempt(user):
    return '[{0}] Login request from user: {1}'.format(get_time(), user)


def stats_request(user):
    return '[{0}] Stats request for: {1}'.format(get_time(), user)


def votes_request(size):
    return '[{0}] Vote data request ({1}B)'.format(get_time(), size)


def bans_request(size):
    return '[{0}] Ban list request ({1}B)'.format(get_time(), size)


def unknown_request(source):
    return '[{0}] Unknown request by {1}'.format(get_time(), source)


def decode_error(source):
    return '[{0}] Error decoding request from {1}'.format(get_time(), source)


def clear_ban_source(data):
    for d in data:
        if "uuid" in d.keys():
            del (d["uuid"])

        if 'The Ban Hammer has spoken!' in d["reason"]:
            del (d["reason"])

        if 'forever' in d["expires"]:
            del (d["expires"])

        for st in staff_translate:
            if st in d["source"]:
                d["source"] = st

    return data
