from nimbella import redis
import sys

def main(args):
    try:
        # check auth
        r = redis()
        if not "token" in args or args["token"] != r.get("tag_token").decode('utf-8') :
            raise Exception("unauthorized")
        # tag
        tag = args['tag']
        key = "tag:%s" % tag
        count = r.llen(key)
        list =  [i.decode('utf-8') for i in r.lrange(key, 0, count)]
        res = {tag: list}
    except KeyError:
        res = { "error": "missing argument"}
    except Exception as e:
        res = { "error": str(e) }
    except:
        res = { "error": "unknown"}
    return {"body": res}
 