from fastapi import FastAPI
from pydantic import BaseModel
from flows.accepting_animal_to_zoo import accepting_animal_request, accepting_animal_to_zoo, accepting_animal_response
from flows.config_registry_create import config_registry_create, RegistryCreateRequest, RegistryCreateResponse
from flows.config_cluster_create import config_cluster_create, ClusterCreateRequest, ClusterCreateResponse
app = FastAPI()


@app.post("/config/registry/create")
def create_registry_endpoint(request: RegistryCreateRequest):
    return config_registry_create(request)

@app.post("/config/cluster/create")
def create_cluster_endpoint(request: ClusterCreateRequest):
    return config_cluster_create(request)



# Accepting animal to zoo
request_accepting_animal = accepting_animal_request()
request_accepting_animal.name = "avi"
request_accepting_animal.age = 4
request_accepting_animal.legs = 4
request_accepting_animal.is_predador = True

response_accepting_animal = accepting_animal_to_zoo(request_accepting_animal)

print(response_accepting_animal)
print("animal added to zoo successfully!")

# Ejecting animal from zoo



# uvicorn main:app --reload