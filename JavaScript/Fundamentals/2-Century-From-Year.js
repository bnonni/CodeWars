function century(year) {
  var strYear = String(year);
  var strYearSlice = strYear.slice(0,2);
  var century = Number(strYearSlice) + 1;
  var strCentury = String(century) + "00";
  return strCentury;
}

century(1705);