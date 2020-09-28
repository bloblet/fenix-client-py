#!/usr/bin/env bash
cd fenix

pipenv run python -m grpc.tools.protoc -I ./fenix_protobufs --python_out=fenix_protobufs --grpc_python_out=fenix_protobufs \
	fenix_protobufs/user.proto \
	fenix_protobufs/auth.proto \
	fenix_protobufs/message.proto