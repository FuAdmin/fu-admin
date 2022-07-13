<template>
  <CollapseContainer title="密码设置" :canExpan="false">
    <a-row :gutter="24">
      <a-col :span="14">
        <BasicForm @register="register" />
      </a-col>
    </a-row>
    <Button type="primary" @click="handleSubmit"> 更新密码 </Button>
  </CollapseContainer>
</template>
<script lang="ts">
  import { Button, Row, Col } from 'ant-design-vue';
  import { computed, defineComponent, onMounted, ref } from 'vue';
  import { BasicForm, useForm } from '/@/components/Form/index';
  import { CollapseContainer } from '/@/components/Container';

  import { useMessage } from '/@/hooks/web/useMessage';

  import headerImg from '/@/assets/images/header.jpg';
  import { secureSetschemas } from './data';
  import { useUserStore } from '/@/store/modules/user';
  import { repassword } from '/@/views/fuadmin/system/account/account.api';
  import { useRoute } from 'vue-router';

  export default defineComponent({
    components: {
      BasicForm,
      CollapseContainer,
      Button,
      ARow: Row,
      ACol: Col,
    },
    setup() {
      const { createMessage } = useMessage();
      const userStore = useUserStore();
      const route = useRoute();
      const userId = ref(route.params?.id);

      const [register, { validate }] = useForm({
        labelWidth: 120,
        schemas: secureSetschemas,
        showActionButtonGroup: false,
      });

      onMounted(async () => {
        // const data = await accountInfoApi();
        // setFieldsValue(data);
      });

      const avatar = computed(() => {
        const { avatar } = userStore.getUserInfo;
        return avatar || headerImg;
      });
      async function handleSubmit() {
        const values = await validate();
        values.id = userId.value;
        console.log(values);
        await repassword(values);
        createMessage.success('更新成功！');
      }
      return {
        avatar,
        register,
        handleSubmit,
      };
    },
  });
</script>

<style lang="less" scoped>
  .change-avatar {
    img {
      display: block;
      margin-bottom: 15px;
      border-radius: 50%;
    }
  }
</style>
