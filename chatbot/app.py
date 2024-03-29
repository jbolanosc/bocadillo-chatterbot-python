"""Application definition."""
from bocadillo import App, discover_providers

from .bot import diego

app = App()
discover_providers("chatbot.providerconf")

# Create routes here.
@app.websocket_route("/conversation")
async def converse(ws, diego): 
    async for message in ws:
        response = diego.get_response(message)
        await ws.send(str(response))

