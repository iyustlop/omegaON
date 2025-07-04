# omegaON
Project for OmegaON, resources and more

# Persistance layer.

The command 'docker compose up' start a kafka 

## Kafka Queue Initialization (for local, non-Docker deployments)
``` bash
docker compose up -d
```

### Topic creation 
``` bash
docker exec -it omegaon-kafka-1 \
  /bin/kafka-topics --create \
                    --topic omegaon.test.topic \
                    --bootstrap-server kafka:9092 \
                    --partitions 1 \
                    --replication-factor 1
```

### Topic list 
``` bash
docker exec -it omegaon-kafka-1 \
  /bin/kafka-topics --list \
                    --bootstrap-server kafka:9092 
```

### Broker Producer
``` bash
docker exec -it omegaon-kafka-1 \
  /bin/kafka-console-producer --broker-list kafka:9092 \
                    --topic omegaon.test.topic
```

### Broker Consumer
``` bash
docker exec -it omegaon-kafka-1 \
  /bin/kafka-console-consumer --bootstrap-server kafka:9092 \
                              --whitelist 'omegaon.test.topic' \
                              --from-beginning
```