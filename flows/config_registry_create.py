from pydantic import BaseModel
import json
import os

class RegistryCreateRequest(BaseModel):
    registry: str
    username: str
    password: str
    name: str


class RegistryCreateResponse(BaseModel):
    success: bool
    message: str    


def config_registry_create(request: RegistryCreateRequest):
    # check if the registry is already exists
    # if exists, return error
    print("check if the registry is already exists")
    print(f"saving the registry name: {request.name}")

    path = f"config/registries/{request.name}.json"
    if os.path.exists(path):
        return RegistryCreateResponse(
            success = False,
            message = f"registry named: {request.name}, already exists"
        )

    # if not exists, create the registry
    with open(path, "w") as f: 
        json.dump(request.dict(), f)

    # return the registry
    return RegistryCreateResponse(
        success = True,
        message = f"registry named: {request.name}, created successfully"
    )


    
