package main

import (
	"time"
	"log"
)

func main() {
	ch := make(chan int, 2)
	exit := make(chan struct{})

	producer := func() {
		for i := 0; i < 5; i++ {
			log.Println("Sending", i)
			ch <- i
			log.Println("Sent", i)

			time.Sleep(1 * time.Second)
		}

		log.Println("Finished producing")

		close(ch)
	}

	consumer := func() {
		for v := range ch {
			log.Println("Received", v)
		}
		log.Println("Finished consuming")
		close(exit)
	}

	go producer()
	go consumer()

	log.Println("Waiting for everything to complete")
	<-exit
	log.Println("All done, exiting!")
}
