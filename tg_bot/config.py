from tg_bot.sample_config import Config


class Development(Config):
    OWNER_ID = 5556908572  # my telegram ID
    OWNER_USERNAME = "Noob_xd"  # my telegram username
    API_KEY = "5340621721:AAGJH7oMhJMgNIfKnPjmQh5HCqWJ0y0A3_U"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgres://pgadmin:4455Hasan@181.214.240.87:5432/testdb'  # sample db credentials
    MESSAGE_DUMP = '-1001786848035' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [5136746907, 5762853941, 5556908572]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
