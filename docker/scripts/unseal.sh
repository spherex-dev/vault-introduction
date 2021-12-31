#!/bin/sh

echo ">>>>  Right before vault initialization <<<<"
while true
do
    netstat -uplnt | grep :8200 | grep LISTEN > /dev/null
    verifier=$?
    if [ 0 = $verifier ]
        then
            echo "Unsealing Vault"
            vault operator unseal PCIw/QuAEdaULjNRe9r10tTtxwWeoURhvW/fczEMe/E=
            break
        else
            echo "vault is not running yet"
            sleep 2
    fi
done
