import os, yaml
import rc_strings as rs

RCwebBridge = r'/home/fr4gright/rc/plugins/RCwebBridge/{0}.yml'
skins_path = r'/home/fr4gright/rc/plugins/SkinsRestorer/Players/{0}.player'

def get_user_stats(user):
    playerData = RCwebBridge.format(user)

    if os.path.exists(playerData):
     
        with open(playerData) as d:
            stats = yaml.load(d, Loader=yaml.FullLoader)
            
            dataDict = {
                'username': user,
                'uuid':stats['user']['uuid'],
                'rank': stats['user']['rank'],
                'pvp_kills': stats['user']['pvp_kills'],
                'deaths': stats['user']['deaths'],
                'damage_dealt': stats['user']['damage_dealt'],
                'money': stats['balance']['money'],
                'exp': stats['exp']['current'],
                'level': stats['exp']['level'],
                'play_time': stats['time']['playtime'],
                'joined': stats['time']['first_join'],
                'last_played': stats['time']['last_played'],
                'jobs': stats['jobs'],
                'res': stats['res'],
                'homes': stats['homes'],
                'vote_day': stats['vote']['day'],
                'vote_week': stats['vote']['week'],
                'vote_month': stats['vote']['month'],
                'vote_total': stats['vote']['total'],
                'vote_points': stats['vote']['points']
            }

            if 'email' in stats['user']:
                dataDict['email'] = stats['user']['email']
 
            if stats['user']['nick'] != user:
                dataDict['nick'] = stats['user']['nick']

            skin = get_skin(user)
            
            if skin != rs.no_custom_skin:
                dataDict['skin'] = skin
                
            return dataDict
    else:
        return rs.not_found

def get_skin(player):
    try:
        with open(skins_path.format(player.lower())) as skin:
            return skin.readlines()[0]
    except:
        return rs.no_custom_skin
