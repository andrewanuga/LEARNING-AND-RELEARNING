const main = () => {
    let nums = [9,12,5,10,14,3,10] // [-3,4,3,2]
    let pivot = 10 // 2
    return pivotArray(nums, pivot)
}

const pivotArray = (nums: number[], pivot:number): number[] => {
    let left: number[] = []
    let right: number[] = []
    let equal: number[] = []

    for (const num of nums) {
        if (num < pivot) {
            left.push(num)
        } else if (num > pivot) {
            right.push(num)
        } else {
            equal.push(num)
        }
    }

    return [...left, ...equal, ...right]
}