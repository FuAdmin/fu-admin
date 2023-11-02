<template>
<!--  <BasicTitle :helpMessage="helpMessage">-->
<!--    {{ title }}-->
<!--  </BasicTitle>-->

  <Row :gutter="12">
    <Col :span="8">
      <BasicTitle :helpMessage="helpMessage">
        {{ title }}
      </BasicTitle>
    </Col>
    <Col :span="8">
      <slot name="insertHeaderMiddle"></slot>
    </Col>
    <Col :span="8" style="display: flex; justify-content: flex-end">
      <div>
        <slot name="insertHeaderRight"></slot>
      </div>
    </Col>
  </Row>
</template>
<script lang="ts">
  import type { PropType } from 'vue';
  import { defineComponent } from 'vue';
  import { BasicTitle } from '/@/components/Basic';
  import {Row, Col} from 'ant-design-vue';
  export default defineComponent({
    name: 'BasicModalHeader',
    components: {BasicTitle,Col, Row},
    props: {
      helpMessage: {
        type: [String, Array] as PropType<string | string[]>,
      },
      title: { type: String },
    },
  });
</script>
