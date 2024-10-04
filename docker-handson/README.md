# Docker Training HandsOn
### The repo covers a mock security events UI with functionalities to update event status, delete them as well as a service to ingest logs.

### Training Notes:
#### Running the Application without `docker compose`:
0. Prepare Dockerfile
1. Build Images in 3 different directories.
2. Create Network for container to container communication with bridge driver.
3. Create Volume for database.
4. Run the Images in dedicated containers with volumes and networks

#### Running the Application with `docker compose`:
0. Prepare `docker-compose.yaml` file
1. Run the application in single command with necessary entworking isolation.
