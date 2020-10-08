# grpc-golang-python
grpc-golang-python tutorial

### Installation
```
$ go get google.golang.org/grpc
$ go get github.com/golang/protobuf/proto
$ go get github.com/golang/protobuf/protoc-gen-go
$ go get google.golang.org/grpc/cmd/protoc-gen-go-grpc

# only for gRPC-gateway
$ go get github.com/grpc-ecosystem/grpc-gateway/protoc-gen-grpc-gateway
$ go get github.com/grpc-ecosystem/grpc-gateway/runtime
$ go get github.com/envoyproxy/protoc-gen-validate
```  
    
    
### gRPC - gen folder (with protox/GRPCServer.proto)
generate code from the protofiles

* go_out
```
protoc --go_out=plugins=grpc:./gen/go/ protos/GRPCServer.proto
```


### gRPC-gateway - gen2 folder (with protox/GRPCServer2.proto)
generate code from the protofiles

* go_out
```
protoc -I/usr/local/include -I. \
                -I${GOPATH}/src \
                -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
                -I${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
                --go-grpc_out=./gen2/go \     
                protos/GRPCServer2.proto
```               

* go-grpc_out
```
protoc -I/usr/local/include -I. \
                -I${GOPATH}/src \
                -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
                -I${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
                --go-grpc_out=./gen2/go \     
                protos/GRPCServer2.proto
```                

* Gateway
```
protoc -I/usr/local/include -I. \
                -I${GOPATH}/src \
                -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
                -I${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
                --go-grpc_out=./gen2/go \     
                protos/GRPCServer2.proto
```

* Swagger
```
protoc -I/usr/local/include -I. \
                -I${GOPATH}/src \
                -I${GOPATH}/src/github.com/grpc-ecosystem/grpc-gateway/third_party/googleapis \
                -I${GOPATH}/src/github.com/envoyproxy/protoc-gen-validate \
                --swagger_out=./gen2/go \
                    protos/GRPCServer2.proto
```                    

