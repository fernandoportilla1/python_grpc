# Fernando Portilla

## Python, gRPC, Docker, and Docker Compose

This project uses gRPC for inter-service communication, Python for server and client logic, and Docker for containerizing the services.

### Generating gRPC code

To generate the gRPC code from `.proto` files, you can use the following command:

````bash
python3 -m grpc_tools.protoc -I protobufs --python_out=. --grpc_python_out=. protobufs/sales_records.proto

### Generating pb2 files with Makefile

This project includes a `Makefile` that automates the process of generating the `pb2` files from the `.proto` files. To use it, simply run the following command:

```bash
make pb2

# Build the services
docker-compose build

# Build and Run services
docker-compose up --build

# Build and Run the services add 5 instances
docker-compose up --build --scale srv_reader=5

# Run the services
docker-compose up

# Initialize the swarm
docker swarm init

# Deploy the stack to the swarm
docker stack deploy -c docker-compose.yml mystack
````
