# P25_cluster_cassandra_restaurants



### Création du Docker-Compose

Voir le contenu du docker compose dans [docker-compose.yml](docker-compose.yml)

pour démarrer la stack docker-compose :<br>
`docker-compose up -d`

vérifier le statut de la stack :<br>
`docker-compose ps`

### Démarrage du CQL sur cass1

`docker exec -it cass1 cqlsh  -e "describe keyspaces"`
