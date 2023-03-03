package main

import (
	"fmt"
	"time"
	"reflect"
)

func main() {
	ch := make(chan int, 2)
	exit := make(chan struct{})

	go func() {
		for i := 0; i < 5; i++ {
			fmt.Println(time.Now(), i, "sending")
			ch <- i
			fmt.Println(time.Now(), i, "sent")

			// time.Sleep(1 * time.Second)
		}

		fmt.Println(time.Now(), "all completed, leaving")

		close(ch)
	}()

	go func() {
		// XXX: This is overcomplicated because is only channel only, "select"
		// shines when using multiple channels.
		// for {
		// 	select {
		// 	case v, open := <-ch:
		// 		if !open {
		// 			close(exit)
		// 			return
		// 		}

		// 		fmt.Println(time.Now(), "received", v)
		// 	}
		// }

		// XXX: In cases where only one channel is used
		for v := range ch {
			fmt.Println(time.Now(), "received", v)
		}

		close(exit)
	}()

	fmt.Println(time.Now(), "waiting for everything to complete")
	// close(exit)p(2*time.Second)

	var i struct {}
	i = <- exit
	fmt.Println(i, reflect.TypeOf(i))
	i = <- exit
	fmt.Println(i, reflect.TypeOf(i))

	fmt.Println(time.Now(), "exiting")
}
