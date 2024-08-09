# longchain
## Usage
There is an example project in the examples folder.
## Development
### to build:
```
.\venv\Scripts\activate
py -m build
python -m twine upload --repository testpypi dist/*
```
### to regenerate the bag api:
1. download the update bag.proto
2. `pip install grpcio grpcio_tools`
3. run `cd .\src\longchain\plugins\bag\api\`
4. run `python -m grpc_tools.protoc -I . --grpc_python_out . --python_out . --pyi_out . bag.proto`
5. Go to the generated bag_pb2_grpc.py and change the `bag_pb2` import to `import longchain.plugins.bag.api.bag_pb2 as bag__pb2`
