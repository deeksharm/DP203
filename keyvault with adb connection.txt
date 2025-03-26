getting scope from databricks
dbutils.secrets.listScopes()
adlskey = dbutils.secrets.get(scope='adb-kv-connectivity', key='adls-connect-key')
spark.conf.set('fs.azure.account.key.adlsdemo2025training.dfs.core.windows.net', adlskey)
