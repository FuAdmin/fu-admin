import { useI18n } from '/@/hooks/web/useI18n';
const { t } = useI18n();
export function getCrontabData(val) {
  if (!val || Object.keys(val).length === 0) return '';
  const week = { 1: '周一', 2: '周二', 3: '周三', 4: '周四', 5: '周五', 6: '周六', 7: '周日' };
  let res = '';
  if (val.month_of_year !== '*') {
    res = `${val.month_of_year} 月 ${val.day_of_month} 日 ${val.hour}点${val.minute}分`;
  } else if (val.day_of_month !== '*') {
    res = `每月 ${val.day_of_month} 日 ${val.hour}点${val.minute}分`;
  } else if (val.day_of_week !== '*') {
    res = `每${week[val.day_of_week] || val.day_of_week} ${val.hour}点${val.minute}分 `;
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
  const lists = {
    days: t('common.task.dayText'),
    hours: t('common.task.hourText'),
    seconds: t('common.task.secondText'),
    minutes: t('common.task.minuteText'),
  };
  return `${t('common.task.everyText')} ${val.every !== 1 ? val.every : ''} ${lists[val.period]}`;
}
