var twoSum = function(nums, target) {
    
    var index_and_nums = {};
    var final = []

    for (i=0; i <= nums.length; i++){

        console.log(nums[i])

        index_and_nums[nums[i]] = i;

        console.log(index_and_nums)

        var complement = target - nums[i];
        console.log(complement)

        if (complement in index_and_nums == true) {
            final.push(index_and_nums[nums[i]])
            final.push(index_and_nums[complement])
            return final
        }
    }
}