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
        url = args['url']
        key = "tag:%s" % tag
        r.lpush(key, url)
        res = { "add": r.hincrby("tag_index", tag, 1) }
    except KeyError:
        res = { "error": "missing argument"}
    except Exception as e:
        res = { "error": str(e) }
    except:
        res = { "error": "unknown"}

    return {"body": res}
