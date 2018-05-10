# OpenShift

## General

Sync local files with target pod:

```
POD=`oc get pods --selector name=mysql -o custom-columns=name:.metadata.name --no-headers`
echo $POD
oc rsync ./ $POD:/opt/app-root/src

# Enable port forwarding
oc port-forward $POD 13306:3306
```

From another terminal on your local machine you can run to connect to remote db container:
```
mysql -u <USER> -p --host=127.0.0.1 --port=13306
```

