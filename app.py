import random
import requests
import time
import urllib.parse
import json
import base64
import socket
import os
from datetime import datetime
import secrets
from urllib.parse import parse_qs, unquote
from colorama import Fore, Style

def _banner():
    print(r"""


▓██   ██▓▓█████   ██████  ▄████▄   ▒█████   ██▓ ███▄    █     ▄▄▄▄    ▒█████  ▄▄▄█████▓
 ▒██  ██▒▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒██▒  ██▒▓██▒ ██ ▀█   █    ▓█████▄ ▒██▒  ██▒▓  ██▒ ▓▒
  ▒██ ██░▒███   ░ ▓██▄   ▒▓█    ▄ ▒██░  ██▒▒██▒▓██  ▀█ ██▒   ▒██▒ ▄██▒██░  ██▒▒ ▓██░ ▒░
  ░ ▐██▓░▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒▒██   ██░░██░▓██▒  ▐▌██▒   ▒██░█▀  ▒██   ██░░ ▓██▓ ░ 
  ░ ██▒▓░░▒████▒▒██████▒▒▒ ▓███▀ ░░ ████▓▒░░██░▒██░   ▓██░   ░▓█  ▀█▓░ ████▓▒░  ▒██▒ ░ 
   ██▒▒▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░░ ▒░▒░▒░ ░▓  ░ ▒░   ▒ ▒    ░▒▓███▀▒░ ▒░▒░▒░   ▒ ░░   
 ▓██ ░▒░  ░ ░  ░░ ░▒  ░ ░  ░  ▒     ░ ▒ ▒░  ▒ ░░ ░░   ░ ▒░   ▒░▒   ░   ░ ▒ ▒░     ░    
 ▒ ▒ ░░     ░   ░  ░  ░  ░        ░ ░ ░ ▒   ▒ ░   ░   ░ ░     ░    ░ ░ ░ ▒    ░      
 ░ ░        ░  ░      ░  ░ ░          ░ ░   ░           ░     ░          ░ ░           
 ░ ░                     ░                                         ░                   


            """)
    print(Fore.GREEN + Style.BRIGHT + "YESCOIN BOT")
    print(Fore.RED + Style.BRIGHT + "Contact: https://t.me/thog099")
    print(Fore.BLUE + Style.BRIGHT + "Replit: Thog")
    print("")

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def load_credentials():
    try:
        with open('query_id.txt', 'r') as f:
            queries = [line.strip() for line in f.readlines()]
        return queries
    except FileNotFoundError:
        print("File query_id.txt not found.")
        return []
    except Exception as e:
        print(f"An error occurred while loading tokens: {e}")
        return []

def print_(word):
    now = datetime.now().isoformat(" ").split(".")[0]
    print(f"[{now}] {word}")

headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-ID,en-US;q=0.9,en;q=0.8,id;q=0.7',
    'content-length': '0',
    'priority': 'u=1, i',
    'Origin': 'https://www.yescoin.gold',
    'Referer': 'https://www.yescoin.gold/',
    'sec-ch-ua': '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
}

def getuseragent(index):
    try:
        with open('useragent.txt', 'r') as f:
            useragents = [line.strip() for line in f.readlines()]
        if 0 <= index < len(useragents):
            return useragents[index]
        else:
            return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except FileNotFoundError:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'
    except Exception as e:
        return 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36'

def parse_and_reconstruct(url_encoded_string):
    parsed_data = urllib.parse.parse_qs(url_encoded_string)
    user_data_encoded = parsed_data.get('user', [None])[0]

    if user_data_encoded:
        user_data_json = urllib.parse.unquote(user_data_encoded)
    else:
        user_data_json = None

    reconstructed_string = f"user={user_data_json}"
    for key, value in parsed_data.items():
        if key != 'user':
            reconstructed_string += f"&{key}={value[0]}"

    return reconstructed_string

def generate_random_hex(length=32):
    return secrets.token_hex(length // 2)

def login(query, useragent):
    url = 'https://api-backend.yescoin.gold/user/login'
    headers['User-Agent'] = useragent
    payload = {
        'code': f'{query}'
    }
    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getgameinfo(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/getGameInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getaccountinfo(token, useragent):
    url = 'https://api-backend.yescoin.gold/account/getAccountInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialboxreloadpage(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/specialBoxReloadPage'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialboxinfo(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/getSpecialBoxInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getacccountbuildinfo(token, useragent):
    url = 'https://api-backend.yescoin.gold/build/getAccountBuildInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def collectCoin(token, useragent, count):
    url = 'https://api-backend.yescoin.gold/game/collectCoin'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json={'count':count})
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getspecialbox(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/recoverSpecialBox'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getcoinpool(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/recoverCoinPool'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def collectspecialbox(token, useragent, payload):
    url = 'https://api-backend.yescoin.gold/game/collectSpecialBoxCoin'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getwallet(token, useragent):
    url = 'https://api-backend.yescoin.gold/wallet/getWallet'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def offline(token, useragent):
    url = 'https://api-backend.yescoin.gold/user/offline'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_daily(token, useragent):
    url = 'https://api-backend.yescoin.gold/mission/getDailyMission'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def finish_daily(token, useragent, missionId):
    url = 'https://api-backend.yescoin.gold/mission/finishDailyMission'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json=missionId)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_finish_status_task(token, useragent):
    url = 'https://api-backend.yescoin.gold/task/getFinishTaskBonusInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_account_build_info(token, useragent):
    url = 'https://api-backend.yescoin.gold/build/getAccountBuildInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def get_task_list(token, useragent):
    url = 'https://api-backend.yescoin.gold/task/getTaskList'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def check_task_status(token, useragent, taskId):
    url = 'https://api-backend.yescoin.gold/task/checkTask'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json=taskId)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claim_reward_task(token, useragent, taskId):
    url = 'https://api-backend.yescoin.gold/task/claimTaskReward'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json=taskId)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claim_bonus_task(token, useragent, id):
    url = 'https://api-backend.yescoin.gold/task/claimBonus'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json={'id':id})
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def level_up(token, useragent, id):
    url = 'https://api-backend.yescoin.gold/build/levelUp'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json={'id':id})
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def getofflineyespacbonusinfo(token, useragent):
    url = 'https://api-backend.yescoin.gold/game/getOfflineYesPacBonusInfo'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def claimofflinebonus(token, useragent, payload, time):
    url = 'https://api.yescoin.gold/game/claimOfflineYesPacBonus'
    headers['Token'] = token
    headers['User-Agent'] = useragent
    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print_(f'Error making request: {e}')
        return None

def printdelay(delay):
    now = datetime.now().isoformat(" ").split(".")[0]
    hours, remainder = divmod(delay, 3600)
    minutes, sec = divmod(remainder, 60)
    print(f"{now} | Waiting Time: {hours} hour(s), {minutes} minute(s), and {sec} second(s)")

def parse_query(query: str):
    parsed_query = parse_qs(query)
    parsed_query = {k: v[0] for k, v in parsed_query.items()}
    user_data = json.loads(unquote(parsed_query['user']))
    parsed_query['user'] = user_data
    return parsed_query

def main():

    _clear()
    _banner()

    queries = load_credentials()
    tokens = [None] * len(queries)
    giftboxs = [0] * len(queries)
    offlines = [0] * len(queries)

    interval_giftbox = 3600
    interval_offline = 7200

    selector_upgrade = input("Automatically upgrade level y/n  : ").strip().lower()
    while True:
        for index, query in enumerate(queries):
            parse = parse_query(query)
            user = parse.get('user')
            currentTime = int(time.time())
            useragent = getuseragent(index)
            user_data = parse_and_reconstruct(query)
            token = tokens[index]
            if token is None:
                datalogin = login(user_data, useragent)
                if datalogin is not None:
                    codelogin = datalogin.get('code')
                    if codelogin == 0:
                        data = datalogin.get('data')
                        tokendata = data.get('token')
                        tokens[index] = tokendata
                        print_("Refreshing Token")
                    else:
                        print_(f"{datalogin.get('message')}")
                        
            token = tokens[index]

            data_account_info = getaccountinfo(token, useragent)
            if data_account_info is not None:
                code = data_account_info.get('code')
                if code == 0:
                    username = user.get('username')
                    data = data_account_info.get('data')
                    currentAmount = data.get('currentAmount')
                    levelInfo = data.get('levelInfo')
                    rankName = levelInfo.get('rankName')
                    level = levelInfo.get('level')
                    print_(f"-- Username: {username} | Level: {rankName} - {level} | Balance: {currentAmount}")

            daily = get_daily(token, useragent)
            if daily is not None:
                print_('Daily Mission List')
                data = daily.get('data')
                for da in data:
                    missionStatus = da.get('missionStatus')
                    name = da.get('name')
                    missionId = da.get('missionId')
                    if missionStatus == 0:
                        time.sleep(2)
                        finish_ = finish_daily(token, useragent, {'missionId':missionId})
                        if finish_ is not None:
                            code = finish_.get('code')
                            if code == 0:
                                data = finish_.get('data')
                                reward = data.get('reward')
                                print_(f'Task: {name} | Reward: {reward}')
                    else:
                        print_(f"Task: {name} completed")

            time.sleep(2)
            data_list_task = get_task_list(token, useragent)
            if data_list_task is not None:
                print_('Retrieving the Task List')
                code = data_list_task.get('code')
                if code == 0:
                    data = data_list_task.get('data')
                    taskList = data.get('taskList', [])
                    specialTaskList = data.get('specialTaskList', [])
                    for task in taskList:
                        taskStatus = task.get('taskStatus')
                        checkStatus = task.get('checkStatus')
                        taskId = task.get('taskId')
                        taskDetail = task.get('taskDetail')
                        if checkStatus == 0:
                            time.sleep(2)
                            data_check_status_task = check_task_status(token, useragent, {'taskId':taskId})
                            if data_check_status_task is not None:
                                code = data_check_status_task.get('code')
                                if code == 0:
                                    data = data_check_status_task.get('data')
                                    if data:
                                        time.sleep(2)
                                        data_reward_task = claim_reward_task(token, useragent, {'taskId':taskId})
                                        if data_reward_task is not None:
                                            code = data_reward_task.get('code')
                                            if code == 0:
                                                print_(f"Task {taskDetail} completed, reward {data_reward_task.get('data').get('bonusAmount')}")

                        elif taskStatus == 0:
                            time.sleep(2)
                            data_reward_task = claim_reward_task(token, useragent, {'taskId':taskId})
                            if data_reward_task is not None:
                                code = data_reward_task.get('code')
                                if code == 0:
                                    print_(f"Task {taskDetail} completed, reward {data_reward_task.get('data').get('bonusAmount')}")
                        else:
                            print_(f"Task {taskDetail} has been completed")

                    for task in specialTaskList:
                        taskStatus = task.get('taskStatus')
                        checkStatus = task.get('checkStatus')
                        taskId = task.get('taskId')
                        taskDetail = task.get('taskDetail')
                        if checkStatus == 0:
                            time.sleep(2)
                            data_check_status_task = check_task_status(token, useragent, {'taskId':taskId})
                            if data_check_status_task is not None:
                                code = data_check_status_task.get('code')
                                if code == 0:
                                    data = data_check_status_task.get('data')
                                    if data:
                                        time.sleep(2)
                                        data_reward_task = claim_reward_task(token, useragent, {'taskId':taskId})
                                        if data_reward_task is not None:
                                            code = data_reward_task.get('code')
                                            if code == 0:
                                                print_(f"Special task {taskDetail} completed, reward {data_reward_task.get('data').get('bonusAmount')}")

                        elif taskStatus == 0:
                            time.sleep(2)
                            data_reward_task = claim_reward_task(token, useragent, {'taskId':taskId})
                            if data_reward_task is not None:
                                code = data_reward_task.get('code')
                                if code == 0:
                                    print_(f"Special task {taskDetail} completed, reward {data_reward_task.get('data').get('bonusAmount')}")
                        else:
                            print_(f"Special task {taskDetail} has been completed")

            time.sleep(2)
            data_check_task = get_finish_status_task(token, useragent)
            if data_check_task is not None:
                code = data_check_task.get('code')
                if code == 0:
                    data = data_check_task.get('data')
                    dailyTaskBonusStatus = data.get('dailyTaskBonusStatus')
                    if dailyTaskBonusStatus == 1:
                        time.sleep(2)
                        data_claim_task = claim_bonus_task(token, useragent, {'id':1})
                        if data_claim_task is not None:
                            code = data_claim_task.get('code')
                            if code == 0:
                                print_(f"Successfully claimed daily task reward, reward {data_claim_task.get('data').get('bonusAmount')}")

                    commonTaskBonusStatus = data.get('commonTaskBonusStatus')
                    if commonTaskBonusStatus == 1:
                        time.sleep(2)
                        data_claim_task = claim_bonus_task(token, useragent, {'id':2})
                        if data_claim_task is not None:
                            code = data_claim_task.get('code')
                            if code == 0:
                                print_(f"Successfully claimed regular task reward, reward {data_claim_task.get('data').get('bonusAmount')}")

            if currentTime - giftboxs[index] >= interval_giftbox:
                giftboxs[index] = currentTime
                datalogin = login(user_data, useragent)
                if datalogin is not None:
                    codelogin = datalogin.get('code')
                    if codelogin == 0:
                        data = datalogin.get('data')
                        tokendata = data.get('token')
                        token = tokendata
                        tokens[index] = tokendata
                    else:
                        print_(f"{datalogin.get('message')}")

                data_getaccountbuild = getacccountbuildinfo(token, useragent)
                if data_getaccountbuild is not None:
                    data = data_getaccountbuild.get('data')
                    specialbox = data.get('specialBoxLeftRecoveryCount')
                    coinpool = data.get('coinPoolLeftRecoveryCount')
                    time.sleep(2)
                    if specialbox > 0:
                        data_specialbox = getspecialbox(token, useragent)
                        if data_specialbox is not None:
                            code = data_specialbox.get('code')
                            if code == 0:
                                print_("Claim special boxes")
                                time.sleep(10)
                    if selector_upgrade == 'y':
                        singleCoinLevel = data.get('singleCoinLevel')
                        singleCoinUpgradeCost = data.get('singleCoinUpgradeCost')
                        if singleCoinUpgradeCost <= currentAmount:
                            time.sleep(2)
                            data_level_up = level_up(token, useragent, {'id':1})
                            if data_level_up is not None:
                                code = data_level_up.get('code')
                                if code == 0:
                                    currentAmount -= singleCoinUpgradeCost
                                    print_(f"Successfully upgraded Single Coin, current level {singleCoinLevel+1}")
                        coinPoolRecoveryLevel = data.get('coinPoolRecoveryLevel')
                        coinPoolRecoveryUpgradeCost = data.get('coinPoolRecoveryUpgradeCost')
                        if coinPoolRecoveryUpgradeCost <= currentAmount:
                            time.sleep(2)
                            data_level_up = level_up(token, useragent, {'id':2})
                            if data_level_up is not None:
                                code = data_level_up.get('code')
                                if code == 0:
                                    currentAmount -= coinPoolRecoveryUpgradeCost
                                    print_(f"Successfully upgraded Recovery Coin, current level {coinPoolRecoveryLevel+1}")
                        coinPoolTotalLevel = data.get('coinPoolTotalLevel')
                        coinPoolTotalUpgradeCost = data.get('coinPoolTotalUpgradeCost')
                        if coinPoolTotalUpgradeCost <= currentAmount:
                            time.sleep(2)
                            data_level_up = level_up(token, useragent, {'id':3})
                            if data_level_up is not None:
                                code = data_level_up.get('code')
                                if code == 0:
                                    currentAmount -= coinPoolTotalUpgradeCost
                                    print_(f"Successfully upgraded Pool Coin, current level {coinPoolTotalLevel+1}")

            data_getspecialboxreload = getspecialboxreloadpage(token, useragent)
            if data_getspecialboxreload is not None:
                code = data_getspecialboxreload.get('code')
                time.sleep(2)
                if code == 0:
                    data_giftbox = getspecialboxinfo(token, useragent)
                    if data_giftbox is not None:
                        data = data_giftbox.get('data')
                        autobox = data.get('autoBox')
                        recoverybox = data.get('recoveryBox')
                        if autobox is not None:
                            payload = {
                                'boxType': 1,
                                'coinCount': autobox.get('specialBoxTotalCount')
                            }
                            data_collectbox = collectspecialbox(token, useragent, payload)
                            data = data_collectbox.get('data')
                            print_(f"Claim the box : {data.get('collectAmount')}")
                            time.sleep(5)

                    if recoverybox is not None:
                        payload = {
                            'boxType': 2,
                            'coinCount': recoverybox.get('specialBoxTotalCount')
                        }
                        data_collectbox = collectspecialbox(token, useragent, payload)
                        data = data_collectbox.get('data')
                        print_(f"Claim the box : {data.get('collectAmount')}")
                        time.sleep(5)

                        time.sleep(2)

            if currentTime - offlines[index] >= interval_offline:
                offlines[index] = currentTime
                data_getofflineyespacbonusinfo = getofflineyespacbonusinfo(token, useragent)
                if data_getofflineyespacbonusinfo is not None:
                    code = data_getofflineyespacbonusinfo.get('code')
                    if code == 0:
                        data = data_getofflineyespacbonusinfo.get('data')
                        detail_data = data[1]
                        claimtype = detail_data.get('claimType')
                        transId = detail_data.get('transactionId')
                        claimtime = int(time.time())
                        payload = {
                            'claimType': claimtype,
                            'createAt': claimtime,
                            'destination': '',
                            'id': transId
                        }
                        data_claimoffline = claimofflinebonus(token, useragent, payload, claimtime)
                        if data_claimoffline is not None:
                            code = data_claimoffline.get('code')
                            if code == 0:
                                data = data_claimoffline.get('data')
                                print_(f"Collected offline rewards = {data.get('collectAmount')}")
                                offline(token, useragent)
                                time.sleep(1)
                    else:
                        print_(f"{data_getofflineyespacbonusinfo.get('message')}")

            defcount = 250
            while True:
                takecount = random.randint(5, 15)
                defcount = defcount - takecount
                data_collectcoin = collectCoin(token, useragent, {'count':defcount})
                if data_collectcoin is not None:
                    code = data_collectcoin.get('code')
                    message = data_collectcoin.get('message')
                    if code == 0:
                        data = data_collectcoin.get('data')
                        data_accountinfo = getaccountinfo(token, useragent)
                        if data_accountinfo is not None:
                            code = data_accountinfo.get('code')
                            if code == 0:
                                dataacc = data_accountinfo.get('data')
                                if dataacc is not None:
                                    print_(f"Collected : {data.get('collectAmount')} || Current coin balance: {dataacc.get('currentAmount')}")
                        else:
                            print_('Error collecting coins')
                    else:
                        if coinpool > 0:
                            datagetcoin = getcoinpool(token, useragent)
                            if datagetcoin is not None:
                                code = datagetcoin.get('code')
                                if code == 0:
                                    print_("Using coin pool rewards")
                                    coinpool -= 1
                                    defcount = 250
                            time.sleep(2)
                        else:
                            print_(f"Notification : {message}")
                            time.sleep(2)
                            print_("Switching to another account")
                            break
                time.sleep(5)
        delay = random.randint(600, 700)
        printdelay(delay)
        time.sleep(delay)

if __name__ == "__main__":
    main() 
