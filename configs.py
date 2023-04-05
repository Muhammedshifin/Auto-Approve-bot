from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "18302370"))
    API_HASH = getenv("API_HASH", "03c2cced4dea9b1e96dce87558dd2381")
    BOT_TOKEN = getenv("BOT_TOKEN", "5924932917:AAFHC6sQkot3C1GHeurOuY_K3eG-75KJ7LY")
    FSUB = getenv("FSUB", "CinemavillaAutoAccept")
    CHID = int(getenv("CHID", "-1001234100577"))
    SUDO = list(map(int, getenv("SUDO").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Mst:Mst@cluster0.0sjrq6j.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
