<template>
  <Row>
    <Col :span="12" :offset="6">
      <div style="padding-top: 20px">
        <Form
          :model="formData"
          name="basic"
          :label-col="{ span: 4 }"
          :wrapper-col="{ span: 20 }"
          autocomplete="off"
        >
          <FormItem
            label="模板名称"
            name="template_name"
            :rules="[{ required: true, message: 'Please input your username!' }]"
          >
            <Input v-model:value="formData.template_name" />
          </FormItem>

          <FormItem
            label="模板编码"
            name="template_code"
            :rules="[{ required: true, message: 'Please input your template_code!' }]"
          >
            <Input v-model:value="formData.template_code" />
          </FormItem>

          <FormItem label="模板说明" name="template_name">
            <a-textarea v-model:value="formData.template_des" />
          </FormItem>
        </Form>
      </div>
    </Col>
  </Row>
</template>
<script lang="ts">
  import { defineComponent, reactive, ref, watch } from 'vue';
  import { useMessage } from '/@/hooks/web/useMessage';
  import { Row, Col, Input, Form, FormItem } from 'ant-design-vue';

  export default defineComponent({
    name: 'BasicSetting',
    components: { Input, Row, Col, Form, FormItem },
    props: {
      basicInfo: Object,
    },
    emits: ['basicInfo'],
    setup(props, { emit }) {
      const { createMessage } = useMessage();

      const formData = reactive({
        template_name: '',
        template_code: '',
        template_des: '',
      });

      watch(props.basicInfo, (value) => {
        console.log(value);
        formData.template_code = value.template_code;
        formData.template_name = value.template_name;
        formData.template_des = value.template_des;
      });

      let a = ref(0);

      watch(formData, (value) => {
        emit('basicInfo', value);
      });

      return {
        formData,
        handleSubmit: (values: any) => {
          createMessage.success('click search,values:' + JSON.stringify(values));
        },
        a,
      };
    },
  });
</script>
