# P25_cluster_cassandra_restaurants

Aude, Ludivine

## Création du Docker-Compose

Voir le contenu du docker compose dans [docker-compose.yml](docker-compose.yml)

pour démarrer la stack docker-compose :<br>
`docker-compose up -d`

vérifier le statut de la stack :<br>
`docker-compose ps`

pour monitorer l'état des clusters :<br>
`docker exec cass1  nodetool status`

et vérifier que CQL fonctionne sur le cluster :<br>
`docker exec -it cass1 cqlsh  -e "describe keyspaces"`

## Création de la base de données

démarrer le shell cqlsh : <br>
```cql
docker exec -it cass1 cqlsh
```

Création de la base de données:<br>
```cql
CREATE KEYSPACE IF NOT EXISTS resto_NY WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor': 1};
```

Sélectionner cette base :<br>
```cql
USE resto;
```

Création des tables :<br>
```cql
 CREATE TABLE Restaurant (
   id INT, Name VARCHAR, borough VARCHAR, BuildingNum VARCHAR, Street VARCHAR,
   ZipCode INT, Phone text, CuisineType VARCHAR,
   PRIMARY KEY ( id )
 ) ;
 
  CREATE TABLE Inspection (
   idRestaurant INT, InspectionDate date, ViolationCode VARCHAR,
   ViolationDescription VARCHAR, CriticalFlag VARCHAR, Score INT, GRADE VARCHAR,
   PRIMARY KEY ( idRestaurant, InspectionDate )
 ) ;
 ```
 
Création des index :
```cql
CREATE INDEX TypeResto ON Restaurant ( CuisineType ) ;
CREATE INDEX GradeInspec ON Inspection ( Grade ) ;
```

Copier les fichiers dans le conteneur à partir de docker :<br>
`docker cp :/<PATH-TO-CSV> <CONTAINER-ID>:/`
_dans notre cas_<br>
`docker cp :/mnt/c/ubu/cassandra/restaurants.csv a3a6aee998df:/`<br>
`docker cp :/mnt/c/ubu/cassandra/restaurants_inspections.csv a3a6aee998df:/`<br>

```cql
use resto ;
COPY Restaurant (id, name, borough, buildingnum, street, zipcode, phone, cuisinetype) FROM '/restaurants.csv' WITH DELIMITER=',';
COPY Inspection (idrestaurant, inspectiondate, violationcode, violationdescription, criticalflag, score, grade) FROM '/restaurants_inspections.csv' WITH DELIMITER=',';
```

