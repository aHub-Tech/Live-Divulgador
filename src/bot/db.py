import os
from urllib.parse import quote_plus

from psycopg2 import OperationalError as PostgreSqlError
from sqlalchemy import MetaData, create_engine
from sqlalchemy.exc import OperationalError as SqlAlchemyError

# Credenciais da Base de Dados
user_db = os.getenv('user_db')
passwd_db = os.getenv('passwd_db')

# Variaveis opcionais
host_db = "db"
port_db = "5432"

try:
    # Caso a password tenha caracteres especiais
    # escapamos com o quote_plus
    engine = create_engine(
        "postgresql://{}:{}@{}:{}/streamers".format(
            user_db, quote_plus(passwd_db), host_db, port_db
        )
    )

    # Guardar objeto da table livecoders
    metadata = MetaData(bind=engine)

    # Por algum motivo o reflect=True no MetaData deixou de funcionar
    # tendo então de chamar o método reflect
    metadata.reflect()

    livecoders = metadata.tables["livecoders"]
except PostgreSqlError as e:
    print(e)
    exit()
except SqlAlchemyError as e:
    print(e)
    exit()

def return_streamer_info():
    """
    Retonar as os valores das colunas de todos os streamers
    """

    result = engine.execute("SELECT * FROM livecoders")

    return result


def return_streamer_names():
    """
    Retorna o nome dos streamers
    """

    result = engine.execute("SELECT Nome FROM livecoders")

    return result


def insert_streamers(streamers):
    """
    NOTA: Para eliminar no futuro

    Insere novos streamers na DB
    """

    for _index, row in streamers.iterrows():

        ins = livecoders.insert().values(
            nome=row["Nome"],
            id=int(row["Id"]),
            twitch=row["Twitch"],
            twitter=row["Twitter"],
            onstream=row["OnStream"],
            print=row["Print"],
            tipo=row["Tipo"],
            hashtags=row["Hashtags"],
        )

        engine.execute(ins)

    return


def insert_on_stream(idt, value):
    """
    Atribui true ou false à coluna OnStream
    """

    upd = (
        livecoders.update()
        .values(onstream=value)
        .where(livecoders.c.id == int(idt))
    )
    engine.execute(upd)

    return

def update_name(idt, name, twitch):
    """
    Função que atualizar o nome e o link com base no id
    """

    upd = (
        livecoders.update()
        .values(nome=name, twitch=twitch)
        .where(livecoders.c.id == int(idt))
    )
    engine.execute(upd)

    return

def delete_streamer(idt):
    """
    Função que elimina streamer da DB com base no id
    """

    delete = livecoders.delete().where(livecoders.c.id == int(idt))
    engine.execute(delete)

    return

def set_timedout(idt, bool):
    """
    Atualizar booleano Timeadout
    """

    upd = (
        livecoders.update()
        .values(timedout=bool)
        .where(livecoders.c.id == int(idt))
    )
    engine.execute(upd)

    return
