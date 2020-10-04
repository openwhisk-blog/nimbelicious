from nimbella import redis
import sys

def main(args):
    try:
        # check auth
        r = redis()
        if not "token" in args or args["token"] != r.get("tag_token").decode('utf-8') :
            raise Exception("unauthorized")
        # tags
        hash = r.hgetall("tag_index")
        list = [ [k.decode('utf-8'), int(hash[k].decode('utf-8'))] 
                for k in hash.keys()]
        res = { "tags": list }
    except KeyError:
        res = { "error": "missing argument"}
    except Exception as e:
        res = { "error": str(e) }
    except:
        res = { "error": "unknown"}
    return {"body": res}


        


    