from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()
class User(BaseModel):
    name:str = Field(min_length=2)
    age:int = Field(gt=0, lt=120)
    email:str =Field(min_length=5)

users_db = []
next_id = 1

@app.post("/users")
def create_user(user: User):
    global next_id
    new_user = {"id": next_id, "name": user.name, "age": user.age, "email":user.email}
    users_db.append(new_user)
    next_id += 1
    return{"message": f"User {user.name} created", "user":new_user}

@app.get("/users")
def get_all_users():
    return users_db

@app.get("/users/{user_id}")
def get_user_by_id(user_id:int):
    for user in users_db:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    for user in users_db:
        if user["id"] == user_id:
            users_db.remove(user)
            return {"message": f"User {user_id} deleted"}
    raise HTTPException(status_code=404 , detail="User not found")

@app.put("/users/{user_id}")
def update_user(user_id:int, update_user: User):
    for user in users_db:
        if user["id"] == user_id:
            user["name"] = update_user.name
            user["age"] = update_user.age
            user["email"] = update_user.email
            return {"message": f"User {user_id} updated", "user":user}
    raise HTTPException(status_code=404, detail="User not found")
