(k + 60)*1500
3000


if n <= k+60
	n*1500
	else {
		(k+60)*1500 + (n-(k+60))*3000
	}


package main

import (
	"fmt"
	"sort"
)

func twoPointer(nums []int, target int) (int, int) {
	n := len(nums)
	i := 0
	j := n - 1
	for k := 0; k < n; k++ {
		if nums[i]+nums[j] > target {
			j--
		} else if nums[i]+nums[j] < target {
			i++
		} else {
			return nums[i], nums[j]
		}
	}
	return 0, 0
}

func twoSum(nums []int, target int) []int {

	sortedNums := make([]int, len(nums))

	copy(sortedNums, nums)
	sort.Ints(sortedNums)                  // O(n*log(n))
	a, b := twoPointer(sortedNums, target) // O(n)
	fmt.Println(a, b)

	var ans []int
	for i, n := range nums {
		if n == a || n == b {
			ans = append(ans, i)
		}
	}
	return ans
}

func main() {
	a := []int{2, 5, 5, 5, 11}
	fmt.Println(twoSum(a, 10))

}
