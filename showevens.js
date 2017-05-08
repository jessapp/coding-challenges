var showEvens = function(nums) {

    var even_indexes = [];

    for (i=0; i <= nums.length; i++) {
        if (nums[i] % 2 == 0) {
            even_indexes.push(i);
        }
    }

    return even_indexes
};