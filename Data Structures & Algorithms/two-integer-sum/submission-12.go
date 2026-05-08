func twoSum(nums []int, target int) []int {
    hashmap:=make(map[int]int)
    for i,value:=range nums{
        key:=target-value
        if comp,ok:=hashmap[key];ok{
            return[]int{comp,i}
        }else{
            hashmap[value]=i
        }
    }
    return nil
}
