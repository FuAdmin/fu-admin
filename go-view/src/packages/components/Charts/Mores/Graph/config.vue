<template>
  <div>
    <CollapseItem name="关系图" :expanded="true">
      <SettingItemBox name="样式">
        <setting-item name="布局">
          <n-select v-model:value="graphConfig.layout" :options="GraphLayout" size="small" />
        </setting-item>
      </SettingItemBox>
      <SettingItemBox name="标签">
        <setting-item name="展示">
          <n-select v-model:value="graphConfig.label.show" :options="LabelSwitch" size="small" />
        </setting-item>
        <setting-item name="位置">
          <n-select v-model:value="graphConfig.label.position" :options="LabelPosition" size="small" />
        </setting-item>
      </SettingItemBox>
      <SettingItemBox name="线条">
        <SettingItem name="弧线">
        <!-- 需要输入两位的小数才会变化 -->
          <n-input-number
          v-model:value="optionData.series[0].lineStyle.curveness"
          :min="0"
          :step="0.01"
          placeholder="弯曲程度"
          size="small"
        ></n-input-number>
        </SettingItem>
      </SettingItemBox>
      <SettingItemBox name="图例">
        <SettingItem name="颜色">
          <n-color-picker
            size="small"
            :modes="['hex']"
            v-model:value="optionData.legend.textStyle.color"
        ></n-color-picker>
        </SettingItem>
        <SettingItem name="文本">
          <n-input-number v-model:value="optionData.legend.textStyle.fontSize" :min="0" :step="1" size="small" placeholder="文字大小">
          </n-input-number>
        </SettingItem>
      </SettingItemBox>
    </CollapseItem>
  </div>
</template>

<script setup lang="ts">
import { PropType, computed } from 'vue'
import { CollapseItem, SettingItemBox, SettingItem } from '@/components/Pages/ChartItemSetting'
import { option, GraphLayout, LabelSwitch, LabelPosition } from './config'
import { GlobalThemeJsonType } from '@/settings/chartThemes/index'

const props = defineProps({
  optionData: {
    type: Object as PropType<typeof option & GlobalThemeJsonType>,
    required: true
  }
})

const graphConfig = computed<typeof option.series[0]>(() => {
  return props.optionData.series[0]
})
</script>
