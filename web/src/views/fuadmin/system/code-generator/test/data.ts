/**
 * -*- coding: utf-8 -*-
 * time: 7/3/2023 10:06 PM
 * file: data.ts
 * author: 臧成龙
 * QQ: 939589097
 */
import { IFormConfig } from "/@/views/sys/form-design/typings/v-form-component";

export const formConfigData: IFormConfig = {
  schemas: [
    {
      component: "InputCountDown",
      label: "倒计时输入",
      "icon": "line-md:iconify2",
      "colProps": {
        "span": 24
      },
      "field": "_input_count_down_1",
      "componentProps": {},
      "key": "_input_count_down_1",
      "itemProps": {
        "labelCol": {},
        "wrapperCol": {}
      }
    },
    {
      "component": "IconPicker",
      "label": "图标选择器",
      "icon": "line-md:iconify2",
      "colProps": {
        "span": 24
      },
      "field": "_icon_picker_2",
      "componentProps": {},
      "key": "_icon_picker_2",
      "itemProps": {
        "labelCol": {},
        "wrapperCol": {}
      }
    }
  ],
  "layout": "horizontal",
  "labelLayout": "flex",
  "labelWidth": 100,
  "labelCol": {},
  "wrapperCol": {},
  "currentItem": {
    "component": "IconPicker",
    "label": "图标选择器",
    "icon": "line-md:iconify2",
    "colProps": {
      "span": 24
    },
    "field": "_icon_picker_2",
    "componentProps": {},
    "key": "_icon_picker_2",
    "itemProps": {
      "labelCol": {},
      "wrapperCol": {}
    }
  },
  "activeKey": 2
}
