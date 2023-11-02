<template>
  <svg
      :class="[prefixCls, $attrs.class, spin && 'svg-icon-spin']"
      :style="getStyle"
      aria-hidden="true"
  >
    <use :xlink:href="symbolId" />
  </svg>
</template>
<script lang="ts">
import type { CSSProperties } from 'vue';
import { defineComponent, computed } from 'vue';
import { useDesign } from '/@/hooks/web/useDesign';

export default defineComponent({
  name: 'SvgIcon',
  props: {
    prefix: {
      type: String,
      default: 'icon',
    },
    name: {
      type: String,
      required: true,
    },
    height: {
      type: [Number, String],
      default: 16,
    },
    weight: {
      type: [Number, String],
      default: 16,
    },
    spin: {
      type: Boolean,
      default: false,
    },
  },
  setup(props) {
    const { prefixCls } = useDesign('svg-icon');
    const symbolId = computed(() => `#${props.prefix}-${props.name}`);

    const getStyle = computed((): CSSProperties => {
      const { height, weight } = props;
      let h = `${height}`;
      h = `${h.replace('px', '')}px`;
      let w = `${weight}`;
      w = `${w.replace('px', '')}px`;
      return {
        width: w,
        height: h,
      };
    });
    return { symbolId, prefixCls, getStyle };
  },
});
</script>
<style lang="less" scoped>
@prefix-cls: ~'@{namespace}-svg-icon';

.@{prefix-cls} {
  display: inline-block;
  overflow: hidden;
  vertical-align: -0.15em;
  fill: currentColor;
}

.svg-icon-spin {
  animation: loadingCircle 1s infinite linear;
}
</style>
