import asyncio
import asyncpg

async def migrate_database():
    conn = await asyncpg.connect(user='user', password='password', database='database', host='host', port='port')

    try:
        await conn.execute('''
            CREATE TABLE IF NOT EXISTS characters (
                id SERIAL PRIMARY KEY,
                birth_year TEXT,
                eye_color TEXT,
                films TEXT,
                gender TEXT,
                hair_color TEXT,
                height TEXT,
                homeworld TEXT,
                mass TEXT,
                name TEXT,
                skin_color TEXT,
                species TEXT,
                starships TEXT,
                vehicles TEXT
            );
        ''')

        await conn.execute('CREATE INDEX IF NOT EXISTS characters_id_index ON characters (id);')

    finally:
        await conn.close()

asyncio.get_event_loop().run_until_complete(migrate_database())