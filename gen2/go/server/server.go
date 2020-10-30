package main

import (
	"context"
	"fmt"
	"log"
	"net"
	"net/http"
	"sync"

	"github.com/grpc-ecosystem/grpc-gateway/runtime"
	"google.golang.org/grpc"

	GRPCServer "github.com/ssoyyoung.p/grpc-golang-python/gen2/go/GRPCServer2"
)

type server struct {
	wg sync.WaitGroup
	GRPCServer.UnimplementedGPRCServerServer
}

// New func
func New() *server {
	return &server{}
}

// ConnectGRPC implements
func (s *server) ConnectGRPC(ctx context.Context, in *GRPCServer.FirstRequest) (*GRPCServer.FirstResponse, error) {
	log.Printf("Received: %v", in.GetName())
	return &GRPCServer.FirstResponse{Msg: "Hello " + in.GetName()}, nil
}

// DisconnectGRPC implements
func (s *server) DisconnectGRPC(ctx context.Context, in *GRPCServer.LastRequest) (*GRPCServer.LastResponse, error) {
	log.Printf("Received: %v", in.GetName())
	return &GRPCServer.LastResponse{Msg: "GoodBye " + in.GetName()}, nil
}

// Start starts server
func (s *server) Start() {
	s.wg.Add(1)
	go func() {
		log.Fatal(s.startGRPC())
		s.wg.Done()
	}()
	s.wg.Add(1)
	go func() {
		log.Fatal(s.startREST())
		s.wg.Done()
	}()
	s.wg.Wait()
}

func (s *server) startGRPC() error {
	lis, err := net.Listen("tcp", "localhost:8080")
	if err != nil {
		return err
	}
	grpcServer := grpc.NewServer()
	fmt.Println("starting grpc Server")
	GRPCServer.RegisterGPRCServerServer(grpcServer, s)
	grpcServer.Serve(lis)
	return nil
}
func (s *server) startREST() error {
	ctx := context.Background()
	ctx, cancel := context.WithCancel(ctx)
	defer cancel()

	mux := runtime.NewServeMux()
	fmt.Println("starting rest API")

	opts := []grpc.DialOption{grpc.WithInsecure()}
	err := GRPCServer.RegisterGPRCServerHandlerFromEndpoint(ctx, mux, ":8080", opts)
	if err != nil {
		return err
	}

	return http.ListenAndServe(":8090", mux)
}

func main() {
	ser := server{}
	ser.Start()
}
