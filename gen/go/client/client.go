package main

import (
	"context"
	"fmt"
	"log"
	"time"

	GRPCServer "github.com/ssoyyoung.p/grpc-golang-python/gen/go/GRPCServer"
	"google.golang.org/grpc"
)

func main() {
	// Set up a connection to the server
	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		log.Fatalf("did not connect: %v", err)
	}
	defer conn.Close()

	c := GRPCServer.NewGPRCServerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	res, _ := c.ConnectGRPC(ctx, &GRPCServer.FirstRequest{Name: "soyoung"})
	fmt.Println(res.GetMsg())

	res2, _ := c.DisconnectGRPC(ctx, &GRPCServer.LastRequest{Name: "soyoung"})
	fmt.Println(res2.GetMsg())

}
