function calculateDaysBetweenDates(begin, end) {
  const beginDate = new Date(begin);
  const endDate = new Date(end);
  const timeDiff = endDate.getTime() - beginDate.getTime();
  return Math.ceil(timeDiff / (1000 * 3600 * 24));
}

function translateChineseToEnglish(chineseString) {
  const chineseToEnglish = {
    一: 'one',
    二: 'two',
    三: 'three',
    四: 'four',
    五: 'five',
    六: 'six',
    七: 'seven',
    八: 'eight',
    九: 'nine',
    十: 'ten',
  };

  return chineseToEnglish[chineseString];
}

function translateAllChineseToEnglish(chineseString) {
  const chineseToEnglish = {
    一: 'one',
    二: 'two',
    三: 'three',
    四: 'four',
    五: 'five',
    六: 'six',
    七: 'seven',
    八: 'eight',
    九: 'nine',
    十: 'ten',
  };
  let englishString = '';
  for (let i = 0; i < chineseString.length; i++) {
    englishString += chineseToEnglish[chineseString[i]];
  }
  return englishString;
}
