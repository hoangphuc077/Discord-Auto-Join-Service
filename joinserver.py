import requests
def join(token, server_invite):
    header = {"authorization": token}
    r = requests.post("https://discord.com/api/v8/invites/{}".format(server_invite), headers=header)
    
join("OTU0OTYwNjE5NDE5ODY5MjA1.Yjaubw.DIgkgTaVYT6-ZK0Wo5ZykBE0U8g", 'rzynTzBE')
