function countSheeps(arrayOfSheep){
  return arrayOfSheep.filter(sheep => sheep == true).length;
  ;
}

var array1 = [true,  true,  true,  false,
  true,  true,  true,  true ,
  true,  false, true,  false,
  true,  false, false, true ,
  true,  true,  true,  true ,
  false, false, true,  true ];
countSheeps(array1);
