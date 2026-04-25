docker pull mongo:latest
docker pull mongo-express:latest

# 1. Stop and remove the existing MongoDB container
docker stop mongodb
docker rm mongodb

# 2. Create MongoDB with CORRECT environment variables
docker run -d \
  -p 27017:27017 \
  --name mongodb \
  -e MONGO_INITDB_ROOT_USERNAME=admin \
  -e MONGO_INITDB_ROOT_PASSWORD=password \
  --net mongo-network \
  mongo

# 3. Wait a few seconds for MongoDB to initialize
sleep 5

# 4. Remove the failed mongo-express container
docker rm -f mongo-express

# 5. Create mongo-express with correct configuration
docker run -d \
  -p 8081:8081 \
  --network mongo-network \
  -e ME_CONFIG_BASICAUTH_USERNAME=admin \
  -e ME_CONFIG_BASICAUTH_PASSWORD=password \
  -e ME_CONFIG_MONGODB_ADMINUSERNAME=admin \
  -e ME_CONFIG_MONGODB_ADMINPASSWORD=password \
  -e ME_CONFIG_MONGODB_SERVER=mongodb \
  --name mongo-express \
  mongo-express

# 6. Check the logs (should work now)
docker logs mongo-express
