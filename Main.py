import requests
import time
import pandas as pd
from PIL import Image, ImageDraw
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor, as_completed

key = "RGAPI-1ddda9c4-1609-4f2f-9556-9c9c3e7bcb88"


def player_puuid(summoner_name, tag, Regoins_m, api_key):
    Full_api = f"https://{Regoins_m}.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/{tag}?api_key={api_key}"
    while True:
        resp = requests.get(Full_api)
        if resp.status_code == 429:
            print("loading, please wait...")
            time.sleep(10)
            continue
        resp.raise_for_status()
        return resp.json()["puuid"]


def get_matches(Regoins_m, player_puuid, count, api_key, type_of_game):
    api_url = (f"https://{Regoins_m}.api.riotgames.com/lol/match/v5/matches/by-puuid/{player_puuid}/ids?"
               f"type={type_of_game}&start=0&count={count}&api_key={api_key}")
    while True:
        resp = requests.get(api_url)
        if resp.status_code == 429:
            print("loading, please wait...")
            time.sleep(10)
            continue
        resp.raise_for_status()
        return resp.json()


def match_data_per_game(Regoins_m, api_key, match_ID):
    api_url = f"https://{Regoins_m}.api.riotgames.com/lol/match/v5/matches/{match_ID}?api_key={api_key}"
    while True:
        resp = requests.get(api_url)
        if resp.status_code == 429:
            print("loading, please wait...")
            time.sleep(10)
            continue
        resp.raise_for_status()
        return resp.json()


def time_line_data(Regions, matchid, api_key):
    api_url = f"https://{Regions}.api.riotgames.com/lol/match/v5/matches/{matchid}/timeline?api_key={api_key}"
    while True:
        resp = requests.get(api_url)
        if resp.status_code == 429:
            print("loading, please wait...")
            time.sleep(10)
            continue
        resp.raise_for_status()
        return resp.json()


def finding_opponent_puuid(player_puuid, match_data):
    participants = match_data["metadata"]["participants"]
    player_index = participants.index(player_puuid)
    position = match_data["info"]["participants"][player_index]["individualPosition"]
    for player in participants:
        opp_index1 = match_data["metadata"]["participants"].index(player)
        position_opp = match_data["info"]["participants"][opp_index1]["individualPosition"]
        if position_opp == position and player != player_puuid:
            break
    return player


def type_of_killing(Time_line_data_per_game, player_index):
    My_main_kill, ks, Regular_kill, Solo_kill = 0, 0, 0, 0
    for frame in Time_line_data_per_game["info"]["frames"]:
        for event in frame["events"]:
            if event.get("killerId") == player_index + 1 and event.get("type") == "CHAMPION_KILL":
                my_DMG = sum(damage["magicDamage"] + damage["physicalDamage"] + damage["trueDamage"]
                             for damage in event.get("victimDamageReceived", [])
                             if damage.get("participantId") == player_index + 1)
                Total_DMG_to_enemy = sum(damage["magicDamage"] + damage["physicalDamage"] + damage["trueDamage"]
                                         for damage in event.get("victimDamageReceived", []))
                Kill_rate = my_DMG / (Total_DMG_to_enemy or 1)
                if 0.65 <= Kill_rate < 1:
                    My_main_kill += 1
                elif Kill_rate <= 0.1:
                    ks += 1
                elif Kill_rate == 1:
                    Solo_kill += 1
                else:
                    Regular_kill += 1
    return My_main_kill, ks, Regular_kill, Solo_kill


def level_5(player_index, opponent_index, Time_line_data_per_game):
    time_lvl5_player, time_lvl5_opponent = None, None
    for frame in Time_line_data_per_game["info"]["frames"]:
        for event in frame["events"]:
            if event.get("type") == "LEVEL_UP" and event.get("level") == 5:
                if event.get("participantId") == player_index + 1:
                    time_lvl5_player = event["timestamp"]
                elif event.get("participantId") == opponent_index + 1:
                    time_lvl5_opponent = event["timestamp"]
    # Ensure we handle None values by setting default high values if None
    if time_lvl5_player is None:
        time_lvl5_player = float('inf')
    if time_lvl5_opponent is None:
        time_lvl5_opponent = float('inf')
    return time_lvl5_player, time_lvl5_opponent


def K_D_A_10mini_jump(player_index, Time_line_data_per_game):
    Dic_of_all = {}
    Time_intervals = [601000, 1201000, 1801000, 2401000, 3001000, 3601000]
    Flag = False
    for time in Time_intervals:
        if Flag:
            Flag = False
        Count_kills, Count_assists, Count_deaths = 0, 0, 0
        for frame in Time_line_data_per_game["info"]["frames"]:
            if Flag:
                break
            for event in frame["events"]:
                if Flag:
                    break
                if event.get("timestamp") <= time:
                    if event.get("type") == "GAME_END":
                        Flag = True
                        break
                    if event.get("type") == "CHAMPION_KILL":
                        if event.get("killerId") == player_index + 1:
                            Count_kills += 1
                        if event.get("victimId") == player_index + 1:
                            Count_deaths += 1
                        if player_index + 1 in event.get("assistingParticipantIds", []):
                            Count_assists += 1
                    Dic_of_all[f'Kills_{time}'] = Count_kills
                    Dic_of_all[f'Deaths_{time}'] = Count_deaths
                    Dic_of_all[f'Assists_{time}'] = Count_assists
                else:
                    Flag = True
                    break
    return Dic_of_all


def death_x_y(Time_line_data_per_game, player_index):
    death_positions = {}
    death_counter = 1
    for frame in Time_line_data_per_game["info"]["frames"]:
        for event in frame["events"]:
            if event.get("victimId") == player_index + 1 and "position" in event:
                death_positions[death_counter] = event["position"]
                death_counter += 1
    return death_positions


def kill_x_y(Time_line_data_per_game, player_index):
    kill_positions = {}
    kill_counter = 1
    for frame in Time_line_data_per_game["info"]["frames"]:
        for event in frame["events"]:
            if event.get("killerId") == player_index + 1 and "position" in event:
                kill_positions[kill_counter] = event["position"]
                kill_counter += 1
    return kill_positions


def ponit_on_map(x, y, color, map):
    image_width, image_height = map.size
    scaled_x = int(x * image_width / 16000)
    scaled_y = int(image_height - (y * image_height / 16000))
    draw = ImageDraw.Draw(map)
    dot_color = (255, 0, 0) if color == "Red" else (0, 0, 255)
    dot_radius = 4
    dot_position = (scaled_x - dot_radius, scaled_y - dot_radius, scaled_x + dot_radius, scaled_y + dot_radius)
    draw.ellipse(dot_position, fill=dot_color)


def draw_point_by_kda(kda, death_x_y, map):
    color = "Blue" if kda > 2 else "Red"
    for position in death_x_y.values():
        ponit_on_map(position['x'], position['y'], color, map)


def wards(respone_match_data, player_puuid):
    player_stats = {"wardsPlaced": 0, "wardsKilled": 0, "visionWardsBoughtInGame": 0}
    team_stats = {100: {"wardsPlaced": 0, "wardsKilled": 0, "visionWardsBoughtInGame": 0},
                  200: {"wardsPlaced": 0, "wardsKilled": 0, "visionWardsBoughtInGame": 0}}
    my_team_ID = None

    for participant in respone_match_data["info"]["participants"]:
        team_id = participant["teamId"]
        if participant["puuid"] == player_puuid:
            player_stats["wardsPlaced"] = participant["wardsPlaced"]
            player_stats["wardsKilled"] = participant["wardsKilled"]
            player_stats["visionWardsBoughtInGame"] = participant["visionWardsBoughtInGame"]
            my_team_ID = team_id
        team_stats[team_id]["wardsPlaced"] += participant["wardsPlaced"]
        team_stats[team_id]["wardsKilled"] += participant["wardsKilled"]
        team_stats[team_id]["visionWardsBoughtInGame"] += participant["visionWardsBoughtInGame"]

    return (
    player_stats["wardsPlaced"], player_stats["wardsKilled"], player_stats["visionWardsBoughtInGame"], my_team_ID,
    team_stats[100]["wardsPlaced"], team_stats[100]["wardsKilled"], team_stats[100]["visionWardsBoughtInGame"],
    team_stats[200]["wardsPlaced"], team_stats[200]["wardsKilled"], team_stats[200]["visionWardsBoughtInGame"])


def process_match(Regoins_m, key, match, player_puuid):
    match_data = match_data_per_game(Regoins_m, key, match)
    player_index = match_data["metadata"]["participants"].index(player_puuid)
    opponent_puuid = finding_opponent_puuid(player_puuid, match_data)
    opponent_index = match_data["metadata"]["participants"].index(opponent_puuid)
    player_position = match_data["info"]["participants"][player_index]["individualPosition"]
    player_position = {
        "BOTTOM": "adc",
        "UTILITY": "supp",
        "MIDDLE": "mid",
        "JUNGLE": "jungler"
    }.get(player_position, "top")
    time_line_data_per_game = time_line_data(Regoins_m, match, key)
    champion_name = match_data["info"]["participants"][player_index]["championName"]
    kills = match_data["info"]["participants"][player_index]["kills"]
    deaths = match_data["info"]["participants"][player_index]["deaths"]
    assists = match_data["info"]["participants"][player_index]["assists"]
    kda = (kills + assists) / (deaths or 1)
    data_for_type_of_killing = type_of_killing(time_line_data_per_game, player_index)
    lvl5 = level_5(player_index, opponent_index, time_line_data_per_game)
    counter_player_lvl5 = lvl5[0] < lvl5[1]
    deaths_corr = death_x_y(time_line_data_per_game, player_index)
    kills_corr = kill_x_y(time_line_data_per_game, player_index)
    k_d_a_time_intervals = K_D_A_10mini_jump(player_index, time_line_data_per_game)
    wards_info = wards(match_data, opponent_puuid)

    game_duration = match_data["info"]["gameDuration"]
    kda_per_min = kda / (game_duration / 60)
    dmg_per_min = match_data["info"]["participants"][player_index]["totalDamageDealtToChampions"] / (game_duration / 60)
    gold_per_min = match_data["info"]["participants"][player_index]["goldEarned"] / (game_duration / 60)
    cs_per_min = match_data["info"]["participants"][player_index]["neutralMinionsKilled"]


    for frame in time_line_data_per_game["info"]["frames"]:
        if frame["timestamp"] > 600000:
            break
        for participant in frame["participantFrames"].values():
            if participant["participantId"] == player_index + 1:
                player_cs = participant["minionsKilled"] + participant["jungleMinionsKilled"]
                player_xp = participant["xp"]
                player_gold = participant["totalGold"]
            if participant["participantId"] == opponent_index + 1:
                opponent_cs = participant["minionsKilled"] + participant["jungleMinionsKilled"]
                opponent_xp = participant["xp"]
                opponent_gold = participant["totalGold"]
    cs_diff_at_10 = player_cs - opponent_cs
    xp_diff_at_10 = player_xp - opponent_xp
    gold_diff_at_10 = player_gold - opponent_gold

    return {
        "Match_ID": match,
        "Player_index": player_index,
        "Opponent_puuid": opponent_puuid,
        "Opponent_index": opponent_index,
        "Champion_name": champion_name,
        "Player_position": player_position,
        "Kills": kills,
        "Deaths": deaths,
        "Assists": assists,
        "KDA": kda,
        "Wards_placed": match_data["info"]["participants"][player_index]["wardsPlaced"],
        "Wards_killed": match_data["info"]["participants"][player_index]["wardsKilled"],
        "My_main_kill": data_for_type_of_killing[0],
        "Kill_Steal": data_for_type_of_killing[1],
        "Regular_kill": data_for_type_of_killing[2],
        "Solo_kill": data_for_type_of_killing[3],
        "Time_level_5_player": lvl5[0],
        "Time_level_5_Opponent": lvl5[1],
        "level_5_player": counter_player_lvl5,
        "KDA_per_min": kda_per_min,
        "Dmg_per_min": dmg_per_min,
        "Gold_per_min": gold_per_min,
        "CS_diff_at_10": cs_diff_at_10,
        "XP_diff_at_10": xp_diff_at_10,
        "Gold_diff_at_10": gold_diff_at_10,
        **k_d_a_time_intervals,
        "CS_per_min": cs_per_min,
    }


def Main(matches_list, Regoins_m, player_puuid, key):
    image = Image.open("Summoner_rift_map.png")
    all_position_KD = {}
    Main_frame = pd.DataFrame(columns=[
        "Match_ID", "Player_index", "Opponent_puuid", "Opponent_index", "Champion_name", "Player_position",
        "Kills", "Deaths", "Assists", "KDA", "Wards_placed", "Wards_killed", "My_main_kill", "Kill_Steal",
        "Regular_kill", "Solo_kill", "Time_level_5_player", "Time_level_5_Opponent", "level_5_player",
        "KDA_per_min", "Dmg_per_min", "Gold_per_min", "CS_diff_at_10", "XP_diff_at_10", "Gold_diff_at_10"
    ])

    match_data_list = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_match = {executor.submit(process_match, Regoins_m, key, match, player_puuid): match for match in
                           matches_list}

        for future in as_completed(future_to_match):
            match_data = future.result()
            match_data_list.append(match_data)
            # Draw points on map by KDA
            deaths_corr = death_x_y(time_line_data(Regoins_m, match_data["Match_ID"], key), match_data["Player_index"])
            draw_point_by_kda(match_data["KDA"], deaths_corr, image)
            print(f"Processed match: {match_data['Match_ID']}")

    Main_frame = pd.concat([Main_frame, pd.DataFrame(match_data_list)], ignore_index=True)
    Main_frame.index = range(1, len(Main_frame) + 1)
    return Main_frame, image, all_position_KD


def start_main(summoner_name, tagline_name, summoner_region, number_of_games, type_of_game):
    summoner_region_match = {
        "EUNE": "europe",
        "EUW": "europe",
        "NA": "AMERICAS"
    }[summoner_region]
    player_puuid11 = player_puuid(summoner_name, tagline_name, summoner_region_match, key)
    matches_list = get_matches(summoner_region_match, player_puuid11, number_of_games, key, type_of_game)
    return Main(matches_list, summoner_region_match, player_puuid11, key)