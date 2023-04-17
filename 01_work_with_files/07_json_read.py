import json
from files import JSON_FILE_PATH

with open(JSON_FILE_PATH) as f:
    users = json.loads(f)

users_list = users['users']

for user in users_list:
    print(user)
