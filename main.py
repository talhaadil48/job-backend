import uvicorn

if __name__ == "__main__":
    # Run the FastAPI app using Uvicorn.
    uvicorn.run("api.server:app", host="0.0.0.0", port=8000, reload=True)