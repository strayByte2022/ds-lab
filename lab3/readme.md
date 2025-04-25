# Instructions to run the lab 1

1. Check if your Docker is running.
2. Navigate to this folder. Run

    `docker-compose up -d`
3. Check if the containers are running `docker ps`

4. Make sure the files `AIR2308.csv`, `WATER2308.csv`, `EARTH2308.csv` are in the same folders.

5. Create the topics

`docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Air --bootstrap-server localhost:9092`

`docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Earth --bootstrap-server localhost:9092`

`docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Water --bootstrap-server localhost:9092`

`docker exec -it lab3-kafka-fog-1 kafka-topics --create --topic Air --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092`

`docker exec -it lab3-kafka-fog-1 kafka-topics --create --topic Earth --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092`

`docker exec -it lab3-kafka-fog-1 kafka-topics --create --topic Water --partitions 2 --replication-factor 1 --bootstrap-server localhost:9092`

6. Run `python producer.py`
7. Run `python consumer.py`

# The results

After running both the producer and consumer scripts, you should see the following results:

1. **Data Processing**
   - The consumer will process messages from three topics: Air, Water, and Earth
   - Each message contains sensor data in CSV format

2. **Data Imputation**
   - Missing values in the sensor data will be handled using linear interpolation
   - Invalid data points will be filtered out

3. **Output Files**
   - Processed data will be saved in the following files:
     - `processed_Air.csv`
     - `processed_Water.csv`
     - `processed_Earth.csv`

4. **Verification**
   - Check the output files to verify the processed data
   - Compare the processed data with the original CSV files to ensure accuracy

5. **Cleanup**
   - To remove the Kafka topics, run:
     ```
     docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Air --bootstrap-server localhost:9092
     docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Water --bootstrap-server localhost:9092
     docker exec -it lab3-kafka-fog-1 kafka-topics --delete --topic Earth --bootstrap-server localhost:9092
     ```

