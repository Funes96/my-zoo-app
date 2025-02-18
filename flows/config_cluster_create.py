from pydantic import BaseModel
import json
import os

class ClusterCreateRequest(BaseModel):
    registry: str
    username: str
    password: str
    name: str

class ClusterCreateResponse(BaseModel):
    success: bool
    message: str

def config_cluster_create(request: ClusterCreateRequest):
    print("creating the cluster")
    print(f"saving the cluster name: {request.name}")

    path = f"config/clusters/{request.name}.json"
    if os.path.exists(path):
        return ClusterCreateResponse(
            success = False,
            message = f"cluster named: {request.name}, already exists"
        )

    with open(path, "w") as f: 
        json.dump(request.dict(), f)

    return ClusterCreateResponse(
        success = True,
        message = f"cluster named: {request.name}, created successfully"
    )   