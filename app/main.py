from typing import List
import crud
import models
import schema
from dependency import SessionDependency

from fastapi import Depends, FastAPI
from lifespan import lifespan

app = FastAPI(title="Advertisement", version="0.1", description="Список объявлений*", lifespan=lifespan)

@app.post("/v1/advertisement/", response_model=schema.CreateAdvertisementResponse)
async def create_advertisement(
    session: SessionDependency,
    create_advertise_request: schema.CreateAdvertisementRequest
    ):
    
    create_advertisement_dict = create_advertise_request.model_dump()
    advertisement = models.Advertisement(**create_advertisement_dict)
    await crud.add_item(session, advertisement)
    return advertisement.id_dict

@app.get("/v1/advertisement/{advertisement_id}", response_model=schema.GetAdvertisementResponse)
async def get_advertisement_by_id(
    session: SessionDependency,
    advertisement_id: int
    ):
    
    advertisement = await crud.get_item(session, models.Advertisement, advertisement_id)
    return advertisement.dict

@app.get("/v1/advertisement", response_model=List[schema.GetAdvertisementResponse])
async def get_advertisement_by_query(
    session: SessionDependency,
    get_advertisement_request: schema.GetAdvertisementsRequest = Depends()
    ):
    params_dict = get_advertisement_request.model_dump(exclude_none=True)
    advertisements = await crud.get_items(session, models.Advertisement, params_dict)
    return [advertise.dict for advertise in advertisements]

@app.patch("/v1/advertisement/{advertisement_id}", response_model=schema.UpdateAdvertisementResponse)
async def update_advertisement(
    session: SessionDependency,
    update_advertisement_request: schema.UpdateAdvertisementRequest,
    advertisement_id: int
    ):
    
    advertisement = await crud.get_item(session, models.Advertisement, advertisement_id)
    advertisement_dict = update_advertisement_request.model_dump(exclude_none=True)
    for key, value in advertisement_dict.items():
        setattr(advertisement, key, value)
    await crud.add_item(session, advertisement)
    return advertisement.id_dict

@app.delete("/v1/advertisement/{advertisement_id}", response_model=schema.DeleteAdvertisementResponse)
async def delete_advertisement(
    session: SessionDependency,
    advertisement_id: int
    ):
    
    await crud.delete_item(session, models.Advertisement, advertisement_id)
    return {"status" : "success"}

