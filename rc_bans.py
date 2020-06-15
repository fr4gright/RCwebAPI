import json
import rc_strings as rs

banned_names = r'/home/fr4gright/rc/banned-players.json'
banned_ips = r'/home/fr4gright/rc/banned-ips.json'

def read_banned_names():
    with open(banned_names) as bn:
        data = json.load(bn)
        data = rs.clear_ban_source(data)
        return data

def read_banned_ips():
    with open(banned_ips) as bip:
        data = json.load(bip)
        data = rs.clear_ban_source(data)
        return data

def read_bans():
    data = {
        'users': read_banned_names(),
        'ips': read_banned_ips()
        }
    
    return data
