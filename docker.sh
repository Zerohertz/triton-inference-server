docker build -t ${SERVER_IMAGE_NAME}:latest src/server

docker run -itd -e NVIDIA_VISIBLE_DEVICES=2 \
    -p 8000:8000 -p 8001:8001 -p 8002:8002 \
    --name triton-inference-server \
    ${SERVER_IMAGE_NAME}:latest \
    tritonserver --model-repository=/models --log-verbose=2

docker logs -f triton-inference-server