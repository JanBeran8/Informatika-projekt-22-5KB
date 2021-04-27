#Fast API testing program


from typing import Optional
from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel

DataBaseRead = FastAPI()


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    is_offer: Optional[bool] = None


@DataBaseRead.get("/") 								#dekorator urceni ze se to tyka FastApi
async def root():									#funkce (asynchroní, může být i normál def)
    return {"test": "message", "Hello": "World"}	#navratova hodnota po zavolani (muze vratit list, slovnik, int, atd...)


@DataBaseRead.get("/it/{item_id}")					
def read_item(item_id):									#definovani bez typu item_id
    return {"item_id": item_id}							#vrati "string" (neparsuje!)


@DataBaseRead.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):	#definovani s typem int (automaticke generovani chyby, neshodi server!)
    return {"item_id": item_id, "q": q}					#vrati int (sam to pasuje!)


@DataBaseRead.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_price": item.price, "item_id": item_id}

@DataBaseRead.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@DataBaseRead.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}



#FIXED values:

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

@DataBaseRead.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW! (Hloubkove uceni FTW)"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images (LeCNN všechny obrázky)"}

    return {"model_name": model_name, "message": "Have some residuals (Zbytek)"}


#Vlozeni specificke veci do "Path"

@DataBaseRead.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


#query parametry (zadavaji se do url po ? a rozdeluji se &)

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@DataBaseRead.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


#query parametry a bool typ
"""
Pokud ma parametr hodnotu None tak je optional, pokud ma defaultni hodnotu neni povinny, jinak je POVINNY! 
"""

@DataBaseRead.get("/veci/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


#Vice parametru najednou

@DataBaseRead.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Optional[str] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item

#Povinne parametry

@DataBaseRead.get("/pov/{item_id}")
async def read_user_item(item_id: str, needy: str):
    item = {"item_id": item_id, "needy": needy}
    return item

#MIX povine a optional parametry

@DataBaseRead.get("/mixik/{item_id}")
async def read_user_item(
    item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {"item_id": item_id, "needy": needy, "skip": skip, "limit": limit}
    return item
"""
needy, a required str.
skip, an int with a default value of 0.
limit, an optional int.
"""

#post (put)

""" Uz mame definovano nahore !

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None
    is_offer: Optional[bool] = None
"""

@DataBaseRead.post("/posttest/")
async def create_item(item: Item):
    return item

""" Prikalad jak muze vypadat
{
    "name": "Foo",
    "description": "An optional description",
    "price": 45.2,
    "tax": 3.5
}
"""

#pristup k atributum funkce

@DataBaseRead.post("/atributyFCE/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict

#Pozadavek na body + path + query parametry

@DataBaseRead.put("/pozad/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# KONZOLE : uvicorn zaklady:DataBaseRead --reload     # --reload = automaticky po zmene v kodu se server reloadne
# server jede na : http://127.0.0.1:8000/


"""
		 # POZNAMKA #

		POST: to create data.		DataBaseRead.post()
		GET: to read data.			DataBaseRead.get()
		PUT: to update data.		DataBaseRead.put()
		DELETE: to delete data.		DataBaseRead.delete()
"""
