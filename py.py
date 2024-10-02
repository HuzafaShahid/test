from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Define the data model for input validation
class CalculatorInput(BaseModel):
    num1: float
    num2: float
    operation: str

# Initialize FastAPI app
app = FastAPI()

# GET route to check if the API is working
@app.get("/calculator")
def test_calculator():
    return {"message": "Calculator API is working. Use POST to perform operations."}

# POST route to perform calculator operations
@app.post("/calculator")
def calculator(input_data: CalculatorInput):
    num1 = input_data.num1
    num2 = input_data.num2
    operation = input_data.operation

    # Perform operations
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = num1 / num2
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Use add, subtract, multiply, or divide")

    return {"result": result}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
