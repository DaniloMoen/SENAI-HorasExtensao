from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

SECRET_KEY = "SENAI_SECRET_KEY" # Chave para o Token
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verificar_senha(senha_plana, senha_hash):
    # Compara a senha digitada com o hash salvo no banco
    return pwd_context.verify(senha_plana, senha_hash)

def criar_token_acesso(dados: dict):
    # Gera o Token JWT para as telas do Figma
    para_codificar = dados.copy()
    expira = datetime.utcnow() + timedelta(minutes=480)
    para_codificar.update({"exp": expira})
    return jwt.encode(para_codificar, SECRET_KEY, algorithm=ALGORITHM)