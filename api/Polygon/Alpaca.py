import httpx

ALPACADATA = {}
ORDERDATA = {}

def _load_alpacadata(data: str):
    ALPACADATA[0] = data


async def get_alpaca_data():
    async with httpx.AsyncClient() as client:
        url = 'https://paper-api.alpaca.markets/v2/account'
        headers = {'APCA-API-KEY-ID': 'PKQO6B0V53BM8BRO3FHL', 'APCA-API-SECRET-KEY': '5Uwl32ELftgVw40RKnxpQvvu3dN6nprg4mI8nzkD'}
        response = await client.get(url, headers=headers)

        #response = "suckshere"
        _load_alpacadata(response.json())


def market_order_aapl():
    #async with httpx.AsyncClient() as client:
        # url = 'https://paper-api.alpaca.markets/v2/account'
        # headers = {'APCA-API-KEY-ID': 'PKQO6B0V53BM8BRO3FHL', 'APCA-API-SECRET-KEY': '5Uwl32ELftgVw40RKnxpQvvu3dN6nprg4mI8nzkD'}
        # response = await client.get(url, headers=headers)

        response = "applsuckshere"
        ORDERDATA[0] = response.json()


