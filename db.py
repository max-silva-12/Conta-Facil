from sqlalchemy import create_engine, text
from config import DATABASE_URL

engine = create_engine(DATABASE_URL)

def verificar_usuario(telegram_chat_id: int) -> bool:
    with engine.connect() as conn:
        resultado = conn.execute(
            text("SELECT 1 FROM negocios WHERE telegram_chat_id = :chat_id"),
            {"chat_id": telegram_chat_id}
        )
        return resultado.fetchone() is not None