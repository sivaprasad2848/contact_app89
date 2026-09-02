from fastapi import FastAPI
from pydantic import BaseModel
from fileop import contact_write , contact_read

app = FastAPI()


class Contact(BaseModel):
    name: str
    email: str
    mobile: str


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/items/")
def create_item(item: Contact):
    c = [(item.name, item.email, item.mobile)]

    contact_write(c)

    return {
        "message": "Contact created successfully",
        "contact": item.model_dump()
    }
@app.get("/items/")
def get_contacts():
    contacts = contact_read()

    return {
        "contacts": contacts
    }
