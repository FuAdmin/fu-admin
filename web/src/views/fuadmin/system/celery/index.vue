<template>
  <div style="margin: 16px">
    <Row :gutter="12">
      <Col :span="12">
        <Interval />
      </Col>
      <Col :span="12">
        <Crontab />
      </Col>
    </Row>

    <Row style="margin-top: 12px">
      <Col :span="24">
        <Task />
      </Col>
    </Row>
  </div>
</template>

<script lang="ts">
  import { Row, Col } from 'ant-design-vue';
  import { defineComponent } from 'vue';
  import Interval from '/@/views/fuadmin/system/celery/interval/index.vue';
  import Crontab from '/@/views/fuadmin/system/celery/crontab/index.vue';
  import Task from '/@/views/fuadmin/system/celery/task/index.vue';
  export default defineComponent({
    name: 'Celery',
    components: { Task, Crontab, Interval, Col, Row },
  });
</script>

<style scoped></style>
