import  hashlib

def main(args):
    password = args["config_password"]
    if password == "":
        password = "nimbella"
    token = hashlib.sha256(password.encode("utf-8")).hexdigest()
    if "password" in args:
        if args["password"] == password:
            res = {"token": token}
        else:
            res = {"error": "bad password"}
    else:
         res = {"error": "no password specified"}
    return { "body": res }
