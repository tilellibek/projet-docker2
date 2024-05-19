kubectl create namespace production
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f db_deployment.yaml
kubectl apply -f api.yaml
kubectl apply -f infrastructure.yaml
kubectl apply -f microservices.yaml
