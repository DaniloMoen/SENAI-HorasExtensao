from app.core.security import gerar_hash_senha

def preparar_novo_usuario(senha_plana):
    # Função para ser usada caso precise criar um usuário com senha protegida
    return gerar_hash_senha(senha_plana)