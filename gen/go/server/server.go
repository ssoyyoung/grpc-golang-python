package main

import (
	"context"
	"fmt"
	"log"
	"net"

	GRPCServer "github.com/ssoyyoung.p/grpc-ex2/gen/go/GRPCServer"
	"google.golang.org/grpc"
)

// server struct
type server struct {
	GRPCServer.UnimplementedGPRCServerServer
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

func main() {
	lis, err := net.Listen("tcp", ":50051")
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}

	s := grpc.NewServer()
	fmt.Println("Starting go server...")
	GRPCServer.RegisterGPRCServerServer(s, &server{})
	if err := s.Serve(lis); err != nil {
		log.Fatalf("failed to serve: %v", err)
	}
}
