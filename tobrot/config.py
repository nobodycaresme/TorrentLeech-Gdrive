from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
    TG_BOT_TOKEN= "a9998b2484a340f4b42b0875eff039db"
    APP_ID = 1921102
    API_HASH = "fill--your--data"
    OWNER_ID = 1125210189
    AUTH_CHANNEL = [-1001201511342]
    DESTINATION_FOLDER = "Leech Bot" #Name of your folder read readme(not id of the folder)
    #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
    RCLONE_CONFIG = """
[DRIVE]
type = drive
client_id = 28dslkgjsdl-fill-your-details-apps.googleusercontent.com
client_secret = 6Tib48-fill-your-details-KuXXDX-eWgnRBYc
scope = drive
root_folder_id = 
token = {"access_token":"ya29.a0AfH6SMC5qXURw8VtpdLv02aXTJilZTLwtbDxPDiRGt89driFeMHcmIyqpHjDtpOD4W7ccjJOKhOyPqgF4AVG7lcn5nmipcxkNxynsyzQuqloId_A3jstbDnr05r1vuj81lKqw4ZFgcZQ6ticW0aTVGd6mSOPMQajXUHe7pkJJjU","token_type":"Bearer","refresh_token":"1//0gKcciOVxqNz_CgYIARAAGBASNwF-L9Ir-oBOjzk0BNm7qUWFAZh6xFUkFRK2Fd0FgsMoIDt7G0y4MT1kDBGnmcJEplpWxw_uV9c","expiry":"2021-01-25T23:22:40.6046154+05:30"}
team_drive = 0AJ2wFSkoxz_AUk9PVA
"""