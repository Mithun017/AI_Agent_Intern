docker build -t my-llm-app .

docker tag my-llm-app mithun1701/my-llm-app:latest

docker push mithun1701/my-llm-app:latest


docker pull mithun1701/my-llm-app:latest
docker run -it --rm mithun1701/my-llm-app:latest
