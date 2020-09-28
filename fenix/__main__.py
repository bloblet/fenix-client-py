import asyncio 
from fenix.client import Client

if __name__ == "__main__":
	asyncio.run(Client("bloblet.com:4000").startSession("bob"))