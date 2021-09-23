import httpx

POLYGONDATA = {}

async_def get_polygon_data(path: str):
    async with httpx.Client() as client:
        response = await client.get(path)
        print(response.json())


