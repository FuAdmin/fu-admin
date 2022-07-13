export function getCrontabData(val) {
  if (!val || Object.keys(val).length === 0) return '';
  const week = { 1: '一', 2: '二', 3: '三', 4: '四', 5: '五', 6: '六', 7: '日' };
  let res = '';
  if (val.month_of_year !== '*') {
    res = `${val.month_of_year} 月 ${val.day_of_month} 日 ${val.hour}点${val.minute}分`;
  } else if (val.day_of_month !== '*') {
    res = `每月 ${val.day_of_month} 日 ${val.hour}点${val.minute}分`;
  } else if (val.day_of_week !== '*') {
    res = `每周周${week[val.day_of_week] || val.day_of_week} ${val.hour}点${val.minute}分 `;
  } else if (val.hour !== '*') {
    res = `每天 ${val.hour}点${val.minute}分`;
  } else if (val.minute !== '*') {
    res = `每分钟 ${val.minute}秒`;
  } else {
    res = `${val.month_of_year} 月 ${val.day_of_month} 日 ${val.hour}点${val.minute}分`;
  }
  return res.replace(/\*/g, '00');
}

export function getIntervalData(val) {
  if (!val || Object.keys(val).length === 0) return '';
  const lists = { days: '天', hours: '小时', seconds: '秒', minutes: '分钟' };
  return `每${val.every !== 1 ? val.every : ''}${lists[val.period]}`;
}
