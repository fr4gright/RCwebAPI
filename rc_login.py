import rc_strings as rcs
import rc_sqlite as rsql

dbfile = r"/home/fr4gright/rc/plugins/LoginSecurity/LoginSecurity.db"
task = "SELECT password FROM ls_players WHERE last_name = '{0}'"

def user_login(user):
    password = rsql.get_sqlite_data(dbfile, task.format(user))
    if password:
        return password[0][0]
    else:
        return rcs.not_found
