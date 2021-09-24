#import httpx

POLYGONDATA = {}


def _load_polygondata(data: str):
    polygon_data = data
    print(polygon_data)


async def get_polygon_data(path: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(path)
        _load_polygondata(response.json())

        #print(response.text)
        #_load_polygondata("works")

