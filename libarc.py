import requests
import json
import base64
import uuid

headers = {
    'Accept-Language': 'en-us',
    'Accept': '*/*',
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept-Encoding': 'br, gzip, deflate',
    'AppVersion': '2.0.1',
    'Cookie': '',
    'User-Agent': 'Arc-mobile/2.0.1.0 CFNetwork/976 Darwin/18.2.0'
}

# generate uuid: str(uuid.uuid4()).upper()
# generate auth: user_login() or user_register()
static_uuid = '41EA0069-AED7-4902-BF82-1E03793146A7'
auth_str = ''
headers['Authorization'] = auth_str

print ('static_uuid: ' + static_uuid)
print ('auth_str: ' + auth_str)


def friend_add(friend_code):
    '''
    usage:
        friend_code: the 9-digit code of the user that you want to add as a friend
        by adding a friend you may check his/her best30 data via rank_friend
    example:
        friend_add(114514810)
    return:
        {
            "success": true,
            "value": {
                "user_id": 1506141,
                "updatedAt": "2019-03-28T18:46:48.021Z",
                "createdAt": "2019-03-28T17:03:51.959Z",
                "friends": [
                    {
                        "user_id": *,
                        "name": "*",
                        "recent_score": [
                            {
                                "song_id": "paradise",
                                "difficulty": 2,
                                "score": 10000727,
                                "shiny_perfect_count": 727,
                                "perfect_count": 729,
                                "near_count": 0,
                                "miss_count": 0,
                                "clear_type": 3,
                                "best_clear_type": 3,
                                "health": 100,
                                "time_played": 1553611941291,
                                "modifier": 2,
                                "rating": 9.8
                            }
                        ],
                        "character": 7,
                        "join_date": 1493860119612,
                        "rating": 1210,
                        "is_skill_sealed": false,
                        "is_char_uncapped": false,
                        "is_mutual": false
                    }
                ]
            }
        }
    '''
    friend_add_data = {'friend_code': friend_code}
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    friend_add_url = 'https://arcapi.lowiro.com/5/friend/me/add'
    #
    friend_add_response = requests.post(friend_add_url, headers=headers, data=friend_add_data)
    friend_add_json = json.loads(friend_add_response.content)
    print (json.dumps(friend_add_json, indent=4))


    return (friend_add_json)


def friend_del(friend_id):
    '''
    usage:
        friend_id: the (private) id of the user that you want to delete
    example:
        friend_del(1919810)
    return:
        {
            "success": true,
            "value": {
                "friends": []
            }
        }
    '''
    friend_del_data = {'friend_id': friend_id}
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    friend_del_url = 'https://arcapi.lowiro.com/5/friend/me/delete'

    friend_del_response = requests.post(friend_del_url, headers=headers, data=friend_del_data)
    friend_del_json = json.loads(friend_del_response.content)
    print (json.dumps(friend_del_json, indent=4))

    return (friend_del_json)


def frag_friend_slot():
    '''
    attention:
        be aware of getting banned for frequent/excessive use of this api
    usage:
        run directly to get you a friend slot (if possible) without costing your fragments
    '''
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    friend_slot_url = 'https://arcapi.lowiro.com/5/purchase/me/friend/fragment'
    friend_slot_response = requests.post(friend_slot_url, headers=headers)
    friend_slot_json = json.loads(friend_slot_response.content)
    print (json.dumps(friend_slot_json, indent=4))

    return (friend_slot_json)


# def frag_song():


def frag_stamina():
    '''
    attention:
        be aware of getting banned for frequent/excessive use of this api
    usage:
        run directly to get you 6 stamina (if possible) without costing your fragments
    return:
        {
            "success": true,
            "value": {
                "user_id": *,
                "stamina": *,
                "max_stamina_ts": *,
                "next_fragstam_ts": *
            }
        }
    '''
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    stamina_url = 'https://arcapi.lowiro.com/5/purchase/me/stamina/fragment'
    stamina_response = requests.post(stamina_url, headers=headers)
    stamina_json = json.loads(stamina_response.content)
    print (json.dumps(stamina_json, indent=4))

    return (stamina_json)


def get_character_info():
    '''
    usage:
        to get information about all your characters
    return:
        {
            "success": true,
            "value": {
                "user_id": 1506141,
                "characters": [
                    {
                        "character_id": 0,
                        "name": "hikari",
                        "level": 1,
                        "exp": 0,
                        "level_exp": 0,
                        "frag": 55,
                        "prog": 35,
                        "overdrive": 35,
                        "skill_id": "gauge_easy",
                        "skill_unlock_level": 0,
                        "char_type": 1,
                        "uncap_cores": [
                            {
                                "core_type": "core_hollow",
                                "amount": 25
                            },
                            {
                                "core_type": "core_desolate",
                                "amount": 5
                            }
                        ],
                        "is_uncapped": false
                    },
                    {
                        "character_id": 1,
                        "name": "tairitsu",
                        "level": 1,
                        "exp": 0,
                        "level_exp": 0,
                        "frag": 55,
                        "prog": 55,
                        "overdrive": 55,
                        "skill_id": "",
                        "skill_unlock_level": 0,
                        "char_type": 0,
                        "uncap_cores": [
                            {
                                "core_type": "core_desolate",
                                "amount": 25
                            },
                            {
                                "core_type": "core_hollow",
                                "amount": 5
                            }
                        ],
                        "is_uncapped": false
                    }
                ]
            }
        }
    '''

    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    get_character_info_url = 'https://arcapi.lowiro.com/5/user/me/character'

    get_character_info_response = requests.get(get_character_info_url, headers=headers)
    get_character_info_json = json.loads(get_character_info_response.content)
    print(json.dumps(get_character_info_json, indent=4))

    return (get_character_info_json)


def get_score_token():
    '''
    usage:
        to get token for submitting score online
        don't know how to use it yet
    return:
        {
            "success": true,
            "value": {
                "token": "sqpxWXzF9ohxec8I7+5RyXVfNtf6TFv7VuhGM0Paf40="
            }
        }
    '''

    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    get_score_token_url = 'https://arcapi.lowiro.com/5/score/token'

    get_score_token_response = requests.get(get_score_token_url, headers=headers)
    get_score_token_json = json.loads(get_score_token_response.content)
    print(json.dumps(get_score_token_json, indent=4))

    return (get_score_token_json)


def get_world_map():
    '''
    usage:
        get the world map data and your progress
    return:
        please view map.json
    '''

    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    get_world_map_url = 'https://arcapi.lowiro.com/5/world/map/me'

    get_world_map_response = requests.get(get_world_map_url, headers=headers)
    get_world_map_json = json.loads(get_world_map_response.content)
    print(json.dumps(get_world_map_json, indent=4))

    return (get_world_map_json)


def get_map_token(song_id, difficulty, select_session_uuid):
    '''
    attention:
        you must be in a map before getting token from map
        this function will cost you (at least 1/2 by default) stamina
    usage:
        song_id: please check song_id.json
        difficulty: 0=pst, 1=prs, 2=ftr
        select_session_uuid: a uuid
    example:
        get_map_token('fairytale', 0, str(uuid.uuid4()).upper())
    return:
        {
            "success": true,
            "value": {
                "stamina": 5,
                "max_stamina_ts": 1553877288261,
                "token": "rn2hBgdKJL20UO8ZYBuixi2kZva7FmS4mcSlTz3Eks8="
            }
        }
    '''

    map_token_params = {
        'song_id': song_id,
        'difficulty': difficulty,
        'select_session': select_session_uuid,
    }
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    map_token_url = 'https://arcapi.lowiro.com/5/score/token/world'

    map_token_response = requests.get(map_token_url, headers=headers, params=map_token_params)
    map_token_json = json.loads(map_token_response.content)
    print (json.dumps(map_token_json, indent=4))

    return (map_token_json)


def rank_friend(song_id, difficulty, start, limit):
    '''
    usage:
        song_id: please check song_id.json
        dificcuty: 0=pst, 1=prs, 2=ftr
        start: larger start, higher rank (start from you: start=0)
        limit: returns at most 21 records due to the number limit of friends
    example:
        rank_friend('themessage', 2, 0, 10)
    '''

    rank_friend_params = {
        'song_id': song_id,
        'difficulty': difficulty,
        'start': start,
        'limit': limit
    }
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    rank_friend_url = 'https://arcapi.lowiro.com/5/score/song/friend'

    rank_friend_response = requests.get(rank_friend_url, headers=headers, params=rank_friend_params)
    rank_friend_json = json.loads(rank_friend_response.content)
    print (json.dumps(rank_friend_json, indent=4))

    return (rank_friend_json)


def rank_me(song_id, difficulty, start, limit):
    '''
    usage:
        song_id: please check song_id.json
        dificcuty: 0=pst, 1=prs, 2=ftr
        start: larger start, higher rank (start from you: start=0)
        limit: returns at most 101 records when limit>=100
        in theory, you can get the whole rank list via rank_me
    example:
        rank_me('themessage', 2, 0, 10)
    '''

    rank_me_params = {
        'song_id': song_id,
        'difficulty': difficulty,
        'start': start,
        'limit': limit
    }
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    rank_me_url = 'https://arcapi.lowiro.com/5/score/song/me'

    rank_me_response = requests.get(rank_me_url, headers=headers, params=rank_me_params)
    rank_me_json = json.loads(rank_me_response.content)
    print (json.dumps(rank_me_json, indent=4))

    return (rank_me_json)


def rank_world(song_id, difficulty, start, limit):
    '''
    usage:
        song_id: please check song_id.json
        dificcuty: 0=pst, 1=prs, 2=ftr
        start: must be 0
        limit: returns at most 100 records when limit>=100
    example:
        rank_world('themessage', 2, 0, 10)
    return:
        {
            "success": true,
            "value": [
                {
                    "user_id": 358014,
                    "song_id": "themessage",
                    "difficulty": 2,
                    "score": 10000992,
                    "shiny_perfect_count": 992,
                    "perfect_count": 992,
                    "near_count": 0,
                    "miss_count": 0,
                    "health": 100,
                    "modifier": 0,
                    "time_played": 1548328059753,
                    "best_clear_type": 3,
                    "clear_type": 3,
                    "name": "tiram1su",
                    "character": 0,
                    "is_skill_sealed": false,
                    "is_char_uncapped": true
                }
            ]
        }
    '''

    rank_world_params = {
        'song_id': song_id,
        'difficulty': difficulty,
        'start': start,
        'limit': limit
    }
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    rank_world_url = 'https://arcapi.lowiro.com/5/score/song'

    rank_world_response = requests.get(rank_world_url, headers=headers, params=rank_world_params)
    rank_world_json = json.loads(rank_world_response.content)
    print (json.dumps(rank_world_json, indent=4))

    return (rank_world_json)


def set_character(character, skill_sealed=False):
    '''
    usage:
        character: character id, from 1 to ?
        skill_sealed: whether to seal the character's skill
    example:
        set_character(1)
    return:
        {
            "success": true,
            "value": {
                "user_id": 1506141,
                "character": 1
            }
        }
    '''

    set_character_data = {
        'character': character,
        'skill_sealed': skill_sealed
    }
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    set_character_url = 'https://arcapi.lowiro.com/5/user/me/character'

    set_character_response = requests.post(set_character_url, headers=headers, data=set_character_data)
    set_character_json = json.loads(set_character_response.content)
    print(json.dumps(set_character_json, indent=4))

    return (set_character_json)


def set_map(map_id):
    '''
    usage:
        map_id: please refer to map.json to find your map_id
    example:
        set_map('hikari_art')
    return:
        {
            "success": true,
            "value": {
                "user_id": 1506141,
                "curr_position": 0,
                "curr_capture": 0,
                "is_locked": false,
                "map_id": "hikari_art"
            }
        }
    '''
    set_map_data = {'map_id': map_id}
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    set_map_url = 'https://arcapi.lowiro.com/5/world/map/me/'
    #
    set_map_response = requests.post(set_map_url, headers=headers, data=set_map_data)
    set_map_json = json.loads(set_map_response.content)
    print (json.dumps(set_map_json, indent=4))

    return (set_map_json)


def user_info():
    '''
    usage:
        run directly to get your user info
    return:
        please view user.json
    '''
    if (auth_str and ('Authorization' not in headers)):
        headers['Authorization'] = auth_str
    user_info_params = {}
    call_list = [
                    {
                        "endpoint": "user/me",
                        "id": 0
                    },
                    {
                        "endpoint": "purchase/bundle/pack",
                        "id": 1
                    },
                    {
                        "endpoint": "serve/download/me/song?url=false",
                        "id": 2
                    }
                ]
    user_info_params['calls'] = json.dumps(call_list)
    user_info_url = 'https://arcapi.lowiro.com/5/compose/aggregate'
    user_info_response = requests.get(user_info_url, headers=headers, params=user_info_params)
    user_info_json = json.loads(user_info_response.content)
    print (json.dumps(user_info_json, indent=4))

    return (user_info_json)


def user_login(name, password, add_auth=True, change_device_id=False):
    '''
    attention:
        your account will be banned for a while if it is logged into more than 2 devices of different uuid
    usage:
        name: username
        password: password
        add_auth: whether to use the (new) authorization code for following functions
        change_device_id: whether to change (and use) a new device id instead of using default device id
    example:
        user_login('tester2234', 'tester223344')
    '''

    login_cred = {'name': name, 'password': password}
    login_data = {'grant_type': 'client_credentials'}
    if (change_device_id):
        headers['DeviceId'] = str(uuid.uuid4()).upper()
        static_uuid = headers['DeviceId']
        print ('new_uuid: ' + static_uuid)
    headers['Authorization'] = 'Basic ' + str(base64.b64encode((login_cred['name'] + ':' + login_cred['password']).encode('utf-8')), 'utf-8')
    login_url = 'https://arcapi.lowiro.com/5/auth/login'

    login_response = requests.post(login_url, headers=headers, data=login_data)
    login_json = json.loads(login_response.content)
    print (json.dumps(login_json, indent=4))


    if (login_json['success']):
        if (add_auth):
            headers['Authorization'] = login_json['token_type'] + ' ' + login_json['access_token']
            auth_str = headers['Authorization']
            print('new_auth: ' + auth_str)
        else:
            headers['Authorization'] = auth_str
        headers.pop('DeviceId')

    return (login_json)


def user_register(name, password, email, add_auth=True, platform='ios', change_device_id=True):
    '''
    usage:
        name: username
        password: password
        email: email address
        add_auth: whether to use the (new) authorization code for following functions
        platform: 'ios' or 'android' (or 'web'?)
        change_device_id: whether to change (and use) a new device id instead of using default device id
    example:
        user_register('holy616', '616isgod', 'love616forever@gmail.com')
    '''

    register_data = {
        'name': name,
        'password': password,
        'email': email,
        'device_id': '',
        'platform': platform
    }
    if (change_device_id):
        register_data['device_id'] = str(uuid.uuid4()).upper()
        static_uuid = register_data['device_id']
        print ('new_uuid: ' + static_uuid)
    if ('Authorization' in headers):
        headers.pop('Authorization')
    register_url = 'https://arcapi.lowiro.com/5/user/'

    register_response = requests.post(register_url, headers=headers, data=register_data)
    register_json = json.loads(register_response.content)
    print (json.dumps(register_json, indent=4))


    if (register_json['success']):
        if (add_auth):
            headers['Authorization'] = 'Bearer ' + register_json['value']['access_token']
            auth_str = headers['Authorization']
            print ('new_auth: ' + auth_str)
        else:
            headers['Authorization'] = auth_str

    return (register_json)






