docker build -t ${SERVER_IMAGE_NAME}:latest src/server
docker build -t ${CLIENT_IMAGE_NAME}:latest src/client

kubectl create namespace ${NAMESPACE}
kubectl apply -f triton-inference-server.yaml -n ${NAMESPACE}
kubectl apply -f fastapi.yaml -n ${NAMESPACE}
kubectl apply -f ingress.yaml -n ${NAMESPACE}