var printDigits = function(num) {
    var s = num.toString()

    var len = s.length

    for (var i = len; i >= 0; i--) {
        console.log(s[i]);
    }

};