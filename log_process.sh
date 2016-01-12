#! /bin/bash

Py_PATH="."

Py_Script="log_process.py"

Location="ps"

IP_Table="logs"

DL_Table="logs2"

Log_Path="/var/log/nginx"

My_Log="/var/log/test"

#Log_File=$(ls -t $Log_Path/*.log | head -2 | tail -1)
Log_File="2015-12-28-09-access.log"

### IP/uuid  -> DB

python3 $Py_PATH/$Py_Script --location=$Location --ip --table=$IP_Table  $Log_File | sed '$ s/,$/;/' | psql -d database -u testuser >> $My_Log 2>&1
#$Py_PATH/$Py_Script --location=$Location --ip --table=$IP_Table  $Log_File     | sed '$ s/,$/;/' | psql -d database -u testuser >> $My_Log 2>&1

if [ $? != 0 ]; then
      echo "NO OK IP"
fi

### Download Counts -> DB

python3 $Py_PATH/$Py_Script --location=$Location --counter --table=$DL_Table $Log_File | sed '$ s/,$/;/' | psql -d database2 -u testuser >> $My_Log 2>&1
#$Py_PATH/$Py_Script --location=$Location --counter --table=$DL_Table $Log_File | sed '$ s/,$/;/' | psql -d database2 -u testuser >> $My_Log 2>&1


if [ $? != 0 ]; then
      echo "NO OK Counter"
fi
