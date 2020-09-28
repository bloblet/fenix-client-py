import asyncio

import grpc

from fenix.fenix_protobufs import auth_pb2, auth_pb2_grpc

class Client:
	__channel: grpc.Channel
	__sessionTokenUpdates: asyncio.Queue

	def __init__(self, fenixAddress: str) -> None:
		self.__channel = grpc.insecure_channel(fenixAddress)
	
	async def startSession(self, username: str) -> None:
		sessionStub = auth_pb2_grpc.AuthStub(self.__channel)
		res = await sessionStub.Login(auth_pb2.ClientAuth(username=username), 10)
		print(type(res))
