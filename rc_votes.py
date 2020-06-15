import json, time, os
import _thread as t
import rc_sqlite as rsql
import rc_stats as rs
import rc_strings as rstr

votes_file = r"/home/fr4gright/rc/plugins/VotingPlugin/Users.db"
task = "SELECT PlayerName, DailyTotal, WeeklyTotal, MonthTotal, AllTimeTotal FROM Users WHERE AllTimeTotal > '{0}'"
file_mode = ["", "daily", "weekly", "monthly", "total"]
folder = "votedata"

cache_time = 5

def get_vote_data():
    if time.time() - os.path.getmtime("{0}/{1}.json".format(folder, file_mode[1])) > cache_time*60:
        data = rsql.get_sqlite_data(votes_file, task.format(0))
        
        for i in range(1, 5):
            t.start_new_thread(cache_vote_data, (data, i))

def cache_vote_data(data, mode):
    proccessed = sorted(data, key = lambda x: x[mode], reverse=True)
    selected = []
    
    for i in range (0,10):
        selected.append(proccessed[i])

    f = open("{0}/{1}.json".format(folder, file_mode[mode]), 'w')
    f.write(json.dumps(selected))
    f.close()

def read_vote_data():
    result = []
        
    for i in range(1, 5):
        f = open("{0}/{1}.json".format(folder, file_mode[i]), 'r')
        result.append(json.loads(f.readlines()[0]))
        f.close()

    t.start_new_thread(get_vote_data, ())

    return result

get_vote_data()
