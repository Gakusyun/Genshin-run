package main

import (
	"fmt"
	"os"
	"os/exec"
)

func main() {
	word := make([]byte, 100)
	if len(os.Args) < 2 {
		fmt.Println("请输入密码:")
		fmt.Fscanln(os.Stdin, &word)
		cmd := exec.Command("python", "start.py", string(word))
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	} else {
		cmd := exec.Command("python", "start.py", os.Args[1])
		cmd.Stdout = os.Stdout
		cmd.Stderr = os.Stderr
		cmd.Run()
	}
}
