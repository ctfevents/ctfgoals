This repo is of the final repo

  
CLIENT_ID: [0-9a-z\-]{36}
CLIENT_SECRET: [0-9A-Za-z\+\=]{40,50}
TENANT_ID: [0-9a-z\-]{36}
    
[default]
aws_access_key_id = BKIAXXXREA7OYXXGNX
aws_secret_access_key = v3EfO4+UC8cNssjTTZ219mS7xqccapo3E/WOOXXLF
  
#!/bin/bash
function mytest {
    "$@"
    local status=$?
    if [ $status -ne 0 ]; then
        echo "error with $1" >&2
    fi
    return $status
}
command1=$( ls & )
command2=pwd  
mytest $command1
mytest $command2

