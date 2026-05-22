function twoSum(nums: number[], target: number): number[] {    
    let check: Record<number, number> = {}
    for(let i=0; i<nums.length; i++){
        let needed_value = target - nums[i]
        if (needed_value in check){
            return [check[needed_value], i]
        }
        check[nums[i]] = i
    }
    return[]
}