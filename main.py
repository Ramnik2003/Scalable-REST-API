from fastapi import FastAPI

app = FastAPI ()

@app.get("/")
async def health_check():
  """
  Check if API is running.
  """
  return {
    "status" : "online",
    "message" : "API is functional"
  }

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload = True)
  
  
