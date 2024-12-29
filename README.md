#### KLS-monitoring ( Kafka, Logstash and Splunk).

###### Monitoring stack for Kafka, Logstash and Splunk.

###### Using logstash, collecting messages from kafka and sending them over to splunk.

###### This is just a sample project for self-learning.

##### Steps to run this service -

###### 1. Clone this repository using suitable method ( http or ssh ).

###### 2. Build images for respective services using docker-compose.yml file (docker compose up -d ). (Zookeeper, Kafka, Logstash and Splunk services)
###### Note- If any docker container, like Kafka, goes does at this step, please start / restart it.

###### 3. Please check all docker containers to see if they are running properly.

##### If using VSCode + Docker plugin, go to docker extension at left hand side on VSCode, select the container that you need to check, right-click on it and select logs. a terminal will open showing logs for this container. Note that, this terminal will show logs of this container as it executes.

##### Alternatively you can check docker container status by showing logs from terminal. Perform following actions for same -
##### 1. docker ps -> Lists all running docker container.
##### 2. docker logs <container-id> -> Lists current logs of the docker container that you need.

###### 4. Once splunk container is up and running, please go to "https://localhost:8000" to connect to Splunk web UI and create a HTTP event collector token, since it is used by logstash to send logs to splunk. Please save this token somewhere for future reference.

##### Note- Once splunk container is restarted, the logs and tokens get destroyed, so you have to create new token everytime splunk container is started.

###### 5. Use this token in logstash.yml, kafka_conn.py and kafka_cons.py.

##### Logstash.yml creates a successful connection from Kafka to Splunk using this token.
kafka_conn.py builds a successful producer connection and kafka_cons.py builds a successful consumer connection.

###### 6. You can use the same or edit kafka_conn.py script to send messages to splunk. Message or log should be in a proper json format to be sent. Also the key should be defined as "number", if you want to use the same script.

##### If you would like to use some other pattern for sending messages or logs, please define the same in logstash.yml in the filter for get.event field.