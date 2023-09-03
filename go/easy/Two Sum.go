package easy

func twoSum(nums []int, target int) []int {
	hashNums := make(map[int]int)

	for i, e := range nums {
		s := target - e
		if index, found := hashNums[s]; found {
			return []int{i, index}
		}
		hashNums[e] = i
	}
	return []int{}
}
