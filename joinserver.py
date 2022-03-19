import requests
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v9/invites/{}".format(server_invite), headers=header)
