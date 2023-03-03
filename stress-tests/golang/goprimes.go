package main

import (
   "fmt"
)

func printPrimeNumbers(num1 int){

   	for j := 2; j <= num1; j++{

		isPrime := true
		for i := 2; i <= num1; i++ {
			if num1 % i == 0{
				isPrime = false
				break
			}
		}
		if isPrime {
			fmt.Printf("%d ", num1)
		}
		num1++

	}
   fmt.Println()
}

func main(){
   printPrimeNumbers(10_000)
}