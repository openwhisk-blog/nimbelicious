import secrets
import nimbella

def main(args):
    password = args["nimbelicious_password"]
    r = nimbella.redis()
    if r.exists("tag_token"):
        token = r.get("tag_token").decode('utf-8')
    else:
        token = secrets.token_hex(16)
        r.set("tag_token", token)
    res = {"error": "no args"}
    if "password" in args:
        if args["password"] == password:
            res = {"token": token}
        else:
            res = {"error": "bad password"}
    if "token" in args:
        if args['token'] == token:
            res = { "ok": True}
        else: 
            res = {"error": "bad token"}
    return { "body": res }
