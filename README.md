## The Problem
I am now working with python + protobuf. I come across a problem when I debug with rookout. The object variable is collected by rookout, but it not able to print the string version of a protobuf message, it print something like "<class 'all_pb2.User'>" instead. The protobuf message can be easily print by python, for example `str(user)` as protobuf have facilitated the toString function. Can rookout support auto toString in the message console for the object variable?

## How to Reproduce
1. pip install requirements.txt
2. `chmod 755 run.py` 
3. python run.py (python 3.6.1)

## Compile Protobuf (Optional)
1. install protoc
2. run `protoc all.proto --python_out=./`
3. all_pb2.py will be generated



#### Reference:
Protobuf: https://developers.google.com/protocol-buffers/

