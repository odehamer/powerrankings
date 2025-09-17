import requests
import pandas as pd

id = input("Enter League ID: ") #League ID = 1254922727656001536
#id = 1254922727656001536

users = requests.get('https://api.sleeper.app/v1/league/' + id + '/users')
rosters = requests.get('https://api.sleeper.app/v1/league/1254922727656001536/rosters')
user_df = pd.DataFrame(users.json())

user_df.drop(columns=[ 'is_bot', 'is_owner', 'league_id', 'settings'], inplace=True)
user_df['name'] = user_df.apply(lambda row: row['metadata']['team_name'] if row['metadata'] and 'team_name' in row['metadata'] else row['display_name'], axis=1)
user_df.drop(columns=['metadata', 'display_name'], inplace=True)

roster_df = pd.DataFrame(rosters.json())

merged_df = pd.merge(user_df, roster_df, left_on='user_id', right_on='owner_id', how='left')
merged_df.drop(columns=['co_owners', 'keepers', 'league_id', 'metadata', 'owner_id', 'player_map', 'roster_id'], inplace=True)
merged_df['wins'] = merged_df['settings'].apply(lambda x: x['wins'] if x and 'wins' in x else 0)
merged_df['losses'] = merged_df['settings'].apply(lambda x: x['losses'] if x and 'losses' in x else 0)
merged_df['fpts'] = merged_df['settings'].apply(lambda x: x['fpts'] if x and 'fpts' in x else 0)
merged_df.drop(columns=['settings'], inplace=True)

# print(merged_df)
print(merged_df.columns)  

list = merged_df.to_dict(orient='records')
print(list[1].keys())

def compare_teams(team1, team2):
    valid_input = True
    while(valid_input):
        print("1 " + team1['name'] + " " + str(team1['wins']) + "-" + str(team1['losses']) + " (" + str(team1['fpts']) + " fpts)")
        print("2 " + team2['name'] + " " + str(team2['wins']) + "-" + str(team2['losses']) + " (" + str(team2['fpts']) + " fpts)")

        winner = input("Enter the winner's number: ")

        if winner == "1":
            return True
        elif winner == "2":
            return False
        else:
            print("Invalid input, please enter 1 or 2.")
            valid_input = False

def mergeSort(user_list):
    if len(user_list) > 1:
        mid = len(user_list) // 2
        L = user_list[:mid]
        R = user_list[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if compare_teams(L[i], R[j]):
                user_list[k] = L[i]
                i += 1
            else:
                user_list[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            user_list[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            user_list[k] = R[j]
            j += 1
            k += 1

    return user_list

user_list = [merged_df.iloc[i] for i in range(len(merged_df))]

mergeSort(user_list)

print("Final Rankings:")
for idx, row in enumerate(user_list):
    print(f"{idx + 1}. {row['name']}")
