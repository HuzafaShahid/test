# print("hello world")
# print (8)
# '''hello pakistan'''
# a=1
# print(a)
# from fastapi import FastAPI,Request

# app = FastAPI()
# @app.get("/")
# def read_root():
#     return{"hello": "World"}
# @app.post("/add-function")

# async def add_function(request : Request):
#     data = await request.json()
#     print(data)
#     return {"result":data["x"]+data["y"]}   
# from fastapi import FastAPI, Request, HTTPException
# from fastapi.responses import JSONResponse
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Dict, Any

# app = FastAPI()

# # Allow all origins
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class InputData(BaseModel):
#     text: str
#     numbers: List[int]

# @app.("/preprocess")
# async def preprocess_data(input_data: InputData):
#     try:
#         # Preprocess the text: convert to uppercase and remove spaces
#         processed_text = input_data.text.upper().replace(" ", "")
        
#         # Preprocess the numbers: calculate the sum and average
#         sum_numbers = sum(input_data.numbers)
#         avg_numbers = sum_numbers / len(input_data.numbers) if input_data.numbers else 0
        
#         # Prepare the result
#         result = {
#             "processed_text": processed_text,
#             "sum_numbers": sum_numbers,
#             "avg_numbers": avg_numbers,
#             "original_data": input_data.dict()
#         }
        
#         return JSONResponse(content=result, status_code=200)
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# # Your existing endpoints
# @app.get("/test")
# def read_root():
#     return JSONResponse(
#         content={
#             "message": "Hello World",
#             "status": "ok",
#             "method": "GET"
#         }
#     )

# @app.post("/add-function")
# async def add_function(request: Request):
#     data = await request.json()
#     print(data)
#     return {"result": data["x"] + data["y"]}
from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict, Any

app = FastAPI()

# Allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Model for Input Data
class InputData(BaseModel):
    text: str
    numbers: List[int]

# # Route for POST request with JSON body
# @app.post("/preprocess")
# async def preprocess_data(input_data: InputData):
#     try:
#         # Preprocess the text: convert to uppercase and remove spaces
#         processed_text = input_data.text.upper()
        
#         # Preprocess the numbers: calculate the sum and average
#         sum_numbers = sum(input_data.numbers)
#         avg_numbers = sum_numbers / len(input_data.numbers) if input_data.numbers else 0
        
#         # Prepare the result
#         result = {
#             "processed_text": processed_text,
#             "sum_numbers": sum_numbers,
#             "avg_numbers": avg_numbers,
#             "original_data": input_data.dict()
#         }
        
#         return JSONResponse(content=result, status_code=200)
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# Route for GET request with query parameters



# @app.get("/preprocess")
# async def preprocess_data_query(
#     text: str = Query(..., description="Text to preprocess"),
#     numbers: List[int] = Query(..., description="List of numbers")
# ):
#     try:
#         # Preprocess the text: convert to uppercase and remove spaces
#         processed_text = text.upper().replace(" ", "")
        
#         # Preprocess the numbers: calculate the sum and average
#         sum_numbers = sum(numbers)
#         avg_numbers = sum_numbers / len(numbers) if numbers else 0
        
#         # Prepare the result
#         result = {
#             "processed_text": processed_text,
#             "sum_numbers": sum_numbers,
#             "avg_numbers": avg_numbers,
#             "original_data": {"text": text, "numbers": numbers}
#         }
        
#         return JSONResponse(content=result, status_code=200)
    
#     except Exception as e:
#         raise HTTPException(status_code=400, detail=str(e))

# # Test endpoint
# @app.get("/test")
# def read_root():
#     return JSONResponse(
#         content={
#             "message": "Hello World",
#             "status": "ok",
#             "method": "GET"
#         }
#     )

# # POST example with body
# @app.post("/add-function")
# async def add_function(request: Request):
#     data = await request.json()
#     return {"result": data["x"] + data["y"]}




def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    # Check if the choice is valid
    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {num1 + num2}")
        elif choice == '2':
            print(f"{num1} - {num2} = {num1 - num2}")
        elif choice == '3':
            print(f"{num1} * {num2} = {num1 * num2}")
        elif choice == '4':
            if num2 != 0:
                print(f"{num1} / {num2} = {num1 / num2}")
            else:
                print("Error: Division by zero is not allowed")
    else:
        print("Invalid input, please select a valid operation.")

# Call the calculator function
calculator()

# a= "huzafa"
# b=10
# print (a+b)
# x=input("Enter your name = ")
# print("my name is  ",x)

# name = "huzafa ##"
# print(name[-4:-2])
# print(name.upper())
# print(name.upper())
# print(name.replace("a","b"))
# print(name.replace("b","a"))
# print(name.rstrip("##"))
# print(name.split(" "))
# print(name.capitalize())
