import type { RouteLocationNormalized, RouteRecordNormalized } from 'vue-router';
import type { App, Plugin } from 'vue';

import { unref } from 'vue';
import { isObject } from '/@/utils/is';

export const noop = () => {};

/**
 * @description:  Set ui mount node
 */
export function getPopupContainer(node?: HTMLElement): HTMLElement {
  return (node?.parentNode as HTMLElement) ?? document.body;
}

/**
 * Add the object as a parameter to the URL
 * @param baseUrl url
 * @param obj
 * @returns {string}
 * eg:
 *  let obj = {a: '3', b: '4'}
 *  setObjToUrlParams('www.baidu.com', obj)
 *  ==>www.baidu.com?a=3&b=4
 */
export function setObjToUrlParams(baseUrl: string, obj: any): string {
  let parameters = '';
  for (const key in obj) {
    parameters += key + '=' + encodeURIComponent(obj[key]) + '&';
  }
  parameters = parameters.replace(/&$/, '');
  return /\?$/.test(baseUrl) ? baseUrl + parameters : baseUrl.replace(/\/?$/, '?') + parameters;
}

export function deepMerge<T = any>(src: any = {}, target: any = {}): T {
  let key: string;
  for (key in target) {
    src[key] = isObject(src[key]) ? deepMerge(src[key], target[key]) : (src[key] = target[key]);
  }
  return src;
}

export function openWindow(
  url: string,
  opt?: { target?: TargetContext | string; noopener?: boolean; noreferrer?: boolean },
) {
  const { target = '__blank', noopener = true, noreferrer = true } = opt || {};
  const feature: string[] = [];

  noopener && feature.push('noopener=yes');
  noreferrer && feature.push('noreferrer=yes');

  window.open(url, target, feature.join(','));
}

// dynamic use hook props
export function getDynamicProps<T, U>(props: T): Partial<U> {
  const ret: Recordable = {};

  Object.keys(props).map((key) => {
    ret[key] = unref((props as Recordable)[key]);
  });

  return ret as Partial<U>;
}

export function getRawRoute(route: RouteLocationNormalized): RouteLocationNormalized {
  if (!route) return route;
  const { matched, ...opt } = route;
  return {
    ...opt,
    matched: (matched
      ? matched.map((item) => ({
          meta: item.meta,
          name: item.name,
          path: item.path,
        }))
      : undefined) as RouteRecordNormalized[],
  };
}

export const withInstall = <T>(component: T, alias?: string) => {
  const comp = component as any;
  comp.install = (app: App) => {
    app.component(comp.name || comp.displayName, component);
    if (alias) {
      app.config.globalProperties[alias] = component;
    }
  };
  return component as T & Plugin;
};

//字节转换，到指定单位结束 is_unit：是否显示单位  fixed：小数点位置 end_unit：结束单位
export function formatUnitSize(bytes, is_unit, fixed, end_unit) {
  let val;
  if (bytes == undefined) return 0;

  if (is_unit == undefined) is_unit = true;
  if (fixed == undefined) fixed = 2;
  if (end_unit == undefined) end_unit = '';

  if (typeof bytes == 'string') bytes = parseInt(bytes);
  const unit = [' B', ' KB', ' MB', ' GB', 'TB'];
  const c = 1024;
  for (let i = 0; i < unit.length; i++) {
    const cUnit = unit[i];
    if (end_unit) {
      if (cUnit.trim() == end_unit.trim()) {
        val = i == 0 ? bytes : fixed == 0 ? bytes : bytes.toFixed(fixed);
        if (is_unit) {
          return val + cUnit;
        } else {
          val = parseFloat(val);
          return val;
        }
      }
    } else {
      if (bytes < c) {
        val = i == 0 ? bytes : fixed == 0 ? bytes : bytes.toFixed(fixed);
        if (is_unit) {
          return val + cUnit;
        } else {
          val = parseFloat(val);
          return val;
        }
      }
    }

    bytes /= c;
  }
}
