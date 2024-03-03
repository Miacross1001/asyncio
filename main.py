import asyncio
import asyncpg
import httpx

async def load_data():
    conn = await asyncpg.connect(user='user', password='password', database='database', host='host', port='port')

    try:
        async with httpx.AsyncClient() as client:
            response = await client.get('https://swapi.dev/api/people/')

            data = response.json()
            characters = data['results']

            for character in characters:
                id = character['url'].split('/')[-2]
                birth_year = character.get('birth_year')
                eye_color = character.get('eye_color')
                films = ', '.join(character.get('films', []))
                gender = character.get('gender')
                hair_color = character.get('hair_color')
                height = character.get('height')
                homeworld = character.get('homeworld')
                mass = character.get('mass')
                name = character.get('name')
                skin_color = character.get('skin_color')
                species = ', '.join(character.get('species', []))
                starships = ', '.join(character.get('starships', []))
                vehicles = ', '.join(character.get('vehicles', []))

                await conn.execute('''
                    INSERT INTO characters (
                        id, birth_year, eye_color, films, gender,
                        hair_color, height, homeworld, mass, name,
                        skin_color, species, starships, vehicles
                    )
                    VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, $11, $12, $13, $14)
                ''', id, birth_year, eye_color, films, gender, hair_color, height, homeworld, mass, name, skin_color, species, starships, vehicles)

    finally:
        await conn.close()

asyncio.get_event_loop().run_until_complete(load_data())