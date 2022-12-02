package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"strings"
)

type O int
type P int

const (
	WIN  = 6
	LOSE = 0
	DRAW = 3

	A O = iota
	B
	C

	X P = iota
	Y
	Z
)

var (
	p1 = 0
	p2 = 0
        L = 0
        R = 0
)
func RemoveIndex(s []string, index int) []string {
	return append(s[:index], s[index+1:]...)
}

func main() {
        var p P

	file, err := ioutil.ReadFile("./in.txt")
	if err != nil {
		log.Fatal(err)
	}
	data := string(file)

	v := strings.Split(data, "\n")
	for _, val := range v {
                if val != " " {
		lr := strings.Split(val, " ")

                l := lr[0]
                r := lr[1]
                if l == "A" { L = 1}
                if l == "B" { L = 2}
                if l == "C" { L = 3}
                if r == "C" { R = 1}
                if r == "C" { R = 2}
                if r == "C" { R = 3}
		if L > R {
			p2 = p2 + LOSE + int(p)
		}
		if l < r {
			p2 = p2 + WIN + int(p)
		}
		if l > r {
			p2 = p2 + DRAW + int(p)
		}
	}
}
        fmt.Printf("Score: %v", p2)
}
