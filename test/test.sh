#!/bin/bash
export PASSWORD=${1:?password}
export TOKEN=xxx

# development
function invoke { 
    nim action invoke "$@" | jq .body
}
# test function
function invoke {
    echo "# $@" | sed -e "s/$TOKEN/xxx/" >>test.out
    nim action invoke "$@" | jq .body | tee -a test.out
}
rm test.out
export TOKEN=$(nim action invoke bookmark/login -p password $PASSWORD | jq -r .body.token)

# login
invoke bookmark/login
invoke bookmark/login -p password badpass
invoke bookmark/login -p token badpass
invoke bookmark/login -p token $TOKEN

# unauthorized
invoke bookmark/del
invoke bookmark/del -p token xxx
invoke bookmark/add
invoke bookmark/add -p token xxx
invoke bookmark/tag
invoke bookmark/tag -p token xxx
invoke bookmark/tags
invoke bookmark/tags -p token xxx


invoke bookmark/del -p token $TOKEN -p yes_really_remove_all 1 

# test
invoke bookmark/tags -p token $TOKEN
invoke bookmark/tag -p token $TOKEN -p tag search
invoke bookmark/add -p token $TOKEN -p tag search -p url http://www.google.com
invoke bookmark/tag -p token $TOKEN -p tag search
invoke bookmark/add -p token $TOKEN -p tag search -p url http://www.duckduckgo.com
invoke bookmark/tags -p token $TOKEN 
invoke bookmark/tag -p token $TOKEN -p tag search
invoke bookmark/add -p token $TOKEN -p tag social -p url http://www.facebook.com
invoke bookmark/tags -p token $TOKEN
invoke bookmark/add -p token $TOKEN -p tag social -p url http://www.linkedin.com
invoke bookmark/tag -p token $TOKEN -p tag social
invoke bookmark/tag -p token $TOKEN -p tag search -p url http://www.google.com
invoke bookmark/tags -p token $TOKEN
invoke bookmark/tag -p token $TOKEN -p tag social
invoke bookmark/tag -p token $TOKEN -p tag search
invoke bookmark/del -p token $TOKEN -p tag search -p url http://www.google.com
invoke bookmark/tags -p token $TOKEN
invoke bookmark/del -p token $TOKEN -p tag social -p url http://www.linkedin.com
invoke bookmark/tags -p token $TOKEN
invoke bookmark/tag -p token $TOKEN -p tag social
invoke bookmark/del -p token $TOKEN -p tag social
invoke bookmark/tags -p token $TOKEN
invoke bookmark/del -p token $TOKEN -p tag search
invoke bookmark/tags -p token $TOKEN

# check
if diff test.out test.ok
then echo SUCCESS
else echo FAIL ; exit 1
fi