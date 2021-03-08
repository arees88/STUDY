$ python logs.py
WARNING - Warning: Falling back to use azure cli login credentials.
If you run your code in unattended mode, i.e., where you can't give a user input, then we recommend to use ServicncipalAuthentication or MsiAuthentication.
Please refer to aka.ms/aml-notebook-auth for different authentication mechanisms in azureml-sdk.
2021-03-08T12:58:38,283474300+00:00 - gunicorn/run
2021-03-08T12:58:38,290321500+00:00 - rsyslog/run
2021-03-08T12:58:38,303655500+00:00 - iot-server/run
2021-03-08T12:58:38,307228600+00:00 - nginx/run
/usr/sbin/nginx: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libcrypto.so.1.0.0: no version informn available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libcrypto.so.1.0.0: no version informn available (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libssl.so.1.0.0: no version informativailable (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libssl.so.1.0.0: no version informativailable (required by /usr/sbin/nginx)
/usr/sbin/nginx: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libssl.so.1.0.0: no version informativailable (required by /usr/sbin/nginx)
rsyslogd: /azureml-envs/azureml_b2d8eee6e84c19a49f59e0af54bdd679/lib/libuuid.so.1: no version information availabrequired by rsyslogd)
EdgeHubConnectionString and IOTEDGE_IOTHUBHOSTNAME are not set. Exiting...
2021-03-08T12:58:39,447597700+00:00 - iot-server/finish 1 0
2021-03-08T12:58:39,453216600+00:00 - Exit code 1 is normal. Not restarting iot-server.
Starting gunicorn 19.9.0
Listening at: http://127.0.0.1:31311 (63)
Using worker: sync
worker timeout is set to 300
Booting worker with pid: 95
SPARK_HOME not set. Skipping PySpark Initialization.
Initializing logger
2021-03-08 12:58:44,728 | root | INFO | Starting up app insights client
Starting up app insights client
2021-03-08 12:58:44,729 | root | INFO | Starting up request id generator
Starting up request id generator
2021-03-08 12:58:44,729 | root | INFO | Starting up app insight hooks
Starting up app insight hooks
2021-03-08 12:58:44,730 | root | INFO | Invoking user's init function
Invoking user's init function
2021-03-08 12:58:54,072 | root | INFO | Users's init has completed successfully
Users's init has completed successfully
2021-03-08 12:58:54,076 | root | INFO | Skipping middleware: dbg_model_info as it's not enabled.
Skipping middleware: dbg_model_info as it's not enabled.
2021-03-08 12:58:54,076 | root | INFO | Skipping middleware: dbg_resource_usage as it's not enabled.
Skipping middleware: dbg_resource_usage as it's not enabled.
2021-03-08 12:58:54,078 | root | INFO | Scoring timeout is found from os.environ: 60000 ms
Scoring timeout is found from os.environ: 60000 ms
2021-03-08 13:03:42,742 | root | INFO | 200
200
127.0.0.1 - - [08/Mar/2021:13:03:42 +0000] "GET /swagger.json HTTP/1.0" 200 2849 "-" "Go-http-client/1.1"
2021-03-08 13:29:02,915 | root | INFO | 200
200
127.0.0.1 - - [08/Mar/2021:13:29:02 +0000] "GET /swagger.json HTTP/1.0" 200 2849 "-" "Go-http-client/1.1"
2021-03-08 13:40:02,176 | root | INFO | 200
200
127.0.0.1 - - [08/Mar/2021:13:40:02 +0000] "GET /swagger.json HTTP/1.0" 200 2849 "-" "Go-http-client/1.1"
2021-03-08 13:40:03,543 | root | INFO | 200
200
127.0.0.1 - - [08/Mar/2021:13:40:03 +0000] "GET /swagger.json HTTP/1.0" 200 2849 "-" "Go-http-client/1.1"


demouser@labvm MINGW64 ~/Desktop/nd00333_AZMLND_C2-master/Exercise_starter_files
$

