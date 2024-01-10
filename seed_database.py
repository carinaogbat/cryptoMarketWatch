# [
#     {
#         "user_name": "Ogbot",
#         "email" : "ogbot@test.com"
#     },

#     {
#         "user_name" : "Testbot",
#         "email": "test@test.com"
#     }

# ]
import os, json, crud, model, server

os.system("drop db crytpo")
os.system("createdb crypto")

model.connect_to_db(server.app)
model.db.create_all()

with open("data/users.json") as f:
    data = json.loads(f.read())

users_db = []
for user in data:
    username, email, password = (
    user["username"], user["email"], user["password"]
    )
    db_user = crud.create_user(username, email, password)

    users_db.append(db_user)

model.db.session.add_all(users_db)
model.db.session.commit()