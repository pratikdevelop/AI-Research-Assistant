from mongodb import MongoDBManager

db = MongoDBManager()

db.save_message(
    "demo_session",
    "user",
    "Hello Atlas!"
)

messages = db.load_messages("demo_session")

print(messages)