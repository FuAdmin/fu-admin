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
          :rules="rules"
          ref="formRef"
        >
          <FormItem label="模板名称" name="template_name">
            <Input v-model:value="formData.template_name" />
          </FormItem>

          <FormItem label="模板编码" name="template_code">
            <Input v-model:value="formData.template_code" />
          </FormItem>

          <FormItem label="模板说明" name="template_des">
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
  import { Row, Col, Input, Form, FormItem, FormInstance } from 'ant-design-vue';
  import { Rule } from 'ant-design-vue/lib/form';

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

      const validateLowercaseInput = (_, value) => {
        // 验证规则：只能输入小写字母和下划线，且不能以下划线开头
        const regex = /^(?!_)[a-z_]+$/;
        if (!regex.test(value)) {
          return Promise.reject(new Error('只能输入小写字母和下划线，且不能以下划线开头'));
        }
        return Promise.resolve();
      };

      watch(formData, (value) => {
        emit('basicInfo', value);
      });

      const rules: Record<string, Rule[]> = {
        template_name: [{ required: true, message: '请输入模板名称' }],
        template_code: [
          { required: true, message: '请输入模板代码' },
          { validator: validateLowercaseInput, trigger: 'change' },
        ],
      };

      const formRef = ref<FormInstance>();

      async function validateForm() {
        try {
          await formRef.value?.validate();
          return true;
        } catch (e) {
          return false;
        }
      }

      return {
        formData,
        formRef,
        rules,
        validateForm,
        handleSubmit: (values: any) => {
          createMessage.success('click search,values:' + JSON.stringify(values));
        },
        a,
      };
    },
  });
</script>
