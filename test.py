from langserve import RemoteRunnable

chain = RemoteRunnable("http://localhost:8000/chain/c/N4XyA")
chain.invoke({"language": "French", "text": "Hello, how are you?"})
print(chain.invoke({"language": "Bangla", "text": "Hello, how are you?"}))