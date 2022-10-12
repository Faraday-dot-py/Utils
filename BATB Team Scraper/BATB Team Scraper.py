import requests
import json

with open("./url.txt", "r") as f:
    url = f.read()

raw = requests.get(url)

matches = json.loads(raw.text)

teams = []

for match in matches:
    temp = [match['alliances']['blue']['team_keys'], match['alliances']['red']['team_keys']]
    teams.append(temp)

teamsStr = str(teams)

teamsStr = teamsStr.replace("]], [[", "\n")
teamsStr = teamsStr.replace("], [", ", ")
teamsStr = teamsStr.replace("frc", "")
teamsStr = teamsStr.replace("'", "")
teamsStr = teamsStr.replace("B", "")
teamsStr = teamsStr[3:-3]

print(teamsStr)

with open("./teams.csv", "w") as f:
    f.write(teamsStr)

exit()