from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Configuração de CORS para permitir que o Front-end (HTML/JS) converse com o Back-end
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Em produção, substitua pelo domínio do seu site
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados simulado
mock_db = {
    "cliente@email.com": {
        "senha": "123", 
        "fotos": [
            "https://images.unsplash.com/photo-1576085898274-0616194a2840?auto=format&fit=crop&w=400&q=80", # Foto no parque 1
            "https://images.unsplash.com/photo-1541846430366-281ce13d7170?auto=format&fit=crop&w=400&q=80"  # Foto no parque 2
        ]
    }
}

class LoginData(BaseModel):
    email: str
    senha: str

@app.post("/api/login")
def login(data: LoginData):
    usuario = mock_db.get(data.email)
    
    if usuario and usuario["senha"] == data.senha:
        return {"sucesso": True, "fotos": usuario["fotos"]}
    
    raise HTTPException(status_code=401, detail="E-mail ou senha incorretos.")