from nimbella import redis
import sys

def main(args):

    res = { "error": "nothing to do"}
    try:
        # check auth
        r = redis()
        if not "token" in args or args["token"] != r.get("tag_token").decode('utf-8') :
            raise Exception("unauthorized")

        # tags
        tags = []
        if "yes_really_remove_all" in args:
            tags = [i.decode('utf-8')[4:] for i in r.keys("tag:?*")]
        elif "tag" in args:
            if "url" in args:
                url = args['url']
                tag = args['tag']
                n = r.lrem("tag:%s" % tag, 1, url)
                r.hincrby("tag_index", tag, -int(n))
                res = { "del": n, "url": url, "tag": tag} 
            else:
                tags = [ args['tag'] ]
        if len(tags) > 0:
            for tag in tags:
                r.hdel("tag_index", tag)
                res = { "del": r.delete("tag:%s" % tag), "tags": tags  }
    except KeyError:
        res = { "error": "missing argument"}
    except Exception as e:
        res = { "error": str(e) }
    except:
        res = { "error": "unknown"}
    return {"body": res}
