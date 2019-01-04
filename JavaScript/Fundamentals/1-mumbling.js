function accum(s) {
 var word = "";
 var j;
 for(var i = 1; i <= s.length; i++){
  j = i - 1;
  var a = s.substring(j,i).charAt(0).toUpperCase();
  var b = a.repeat(j).toLowerCase();
   i == s.length ? word+= (a + b) : word += (a + b + "-");
 }
 return word
}

accum("ZpglnRxqenU");

// accum("abcd") -> "A-Bb-Ccc-Dddd"
// accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
// accum("cwAt") -> "C-Ww-Aaa-Tttt"