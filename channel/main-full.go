package main

import (
	_ "fmt"
	"time"
	"log"
	_ "reflect"
)

func main() {
	ch := make(chan int, 2)
	exit := make(chan struct{})

	go func() {
		for i := 0; i < 5; i++ {
			log.Println("Sending", i)
			ch <- i
			log.Println("Sent", i)

			time.Sleep(1 * time.Second)
		}

		log.Println("Finished producing")

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
			log.Println("Received", v)
		}
		log.Println("Finished consuming")
		close(exit)
	}()

	log.Println("Waiting for everything to complete")
	<-exit
	// var i struct {}
	// i = <- exit
	// fmt.Println(i, reflect.TypeOf(i))
	// i = <- exit
	// fmt.Println(i, reflect.TypeOf(i))

	log.Println("All done, exiting!")
}
