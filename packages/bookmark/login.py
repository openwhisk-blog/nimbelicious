import secrets
import nimbella

def main(args):
    password = args["nimbelicious_password"]
    r = nimbella.redis()
    if "password" in args:
        if args["password"] == password:
            if r.exists("tag_token"):
                token = r.get("tag_token").decode('utf-8')
            else:
                token = secrets.token_hex(16)
                r.set("tag_token", token)
            res = {"token": token}
        else:
            res = {"error": "bad password"}
    else:
         res = {"error": "no password specified"}
    return { "body": res }
