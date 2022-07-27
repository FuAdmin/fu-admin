<template>
  <div class="md:flex">
    <Card
      size="small"
      title="负载状态"
      :loading="loading"
      class="md:w-1/4 w-full !md:mt-0"
      :class="{ '!md:mr-4': 1 < 4, '!mt-4': 0 > 0 }"
    >
      <div class="py-2 px-2 flex items-center">
        <Progress
          type="circle"
          :percent="dataList.load_average.percent"
          :width="120"
          :strokeColor="getProgressColor(dataList.load_average.percent)"
        />
        <div class="space-main-up-cpu">
          <span>最近1分钟平均负载：{{ dataList.load_average.one }}</span>
          <span>最近5分钟平均负载：{{ dataList.load_average.five }}</span>
          <span>最近15分钟平均负载：{{ dataList.load_average.fifteen }}</span>
        </div>
      </div>
    </Card>

    <Card
      size="small"
      title="CPU使用率"
      :loading="loading"
      class="md:w-1/4 w-full !md:mt-0"
      :class="{ '!md:mr-4': 2 < 4, '!mt-4': 1 > 0 }"
    >
      <div class="py-2 px-2 flex items-center">
        <Progress
          type="circle"
          :percent="dataList.cpu[0]"
          :width="120"
          :strokeColor="getProgressColor(dataList.cpu[0])"
        />
        <div class="space-main-up-cpu">
          <span>CPU型号：{{ dataList.cpu[3] }}</span>
          <span>物理CPU：{{ dataList.cpu[5] }}颗</span>
          <span>物理核心：{{ dataList.cpu[5] * dataList.cpu[4] }}个</span>
          <span>逻辑核心：{{ dataList.cpu[1] }}个</span>
        </div>
      </div>
    </Card>

    <Card
      size="small"
      title="内存使用率"
      :loading="loading"
      class="md:w-1/4 w-full !md:mt-0"
      :class="{ '!md:mr-4': 3 < 4, '!mt-4': 2 > 0 }"
    >
      <div class="py-2 px-2 flex items-center">
        <Progress
          type="circle"
          :percent="dataList.mem.percent"
          :width="120"
          :strokeColor="getProgressColor(dataList.mem.percent)"
        />
        <div class="space-main-up-cpu">
          <span>总共内存：{{ dataList.mem.total }}GB</span>
          <span>已用内存：{{ dataList.mem.used }}GB</span>
          <span>剩余内存：{{ dataList.mem.free }}GB</span>
        </div>
      </div>
    </Card>

    <Card
      size="small"
      title="硬盘使用率"
      :loading="loading"
      class="md:w-1/4 w-full !md:mt-0"
      :class="{ '!md:mr-4': 4 < 4, '!mt-4': 3 > 0 }"
    >
      <div class="py-2 px-2 flex items-center" v-for="(item, index) in dataList.disk" :key="index">
        <Progress
          type="circle"
          :percent="item.size[3]"
          :width="120"
          :strokeColor="getProgressColor(item.size[3])"
        />
        <div class="space-main-up-cpu">
          <span>总共大小：{{ item.size[0] }}</span>
          <span>已用大小：{{ item.size[1] }}</span>
          <span>剩余大小：{{ item.size[2] }}</span>
        </div>
      </div>
    </Card>
  </div>
</template>

<script>
  import { Progress, Card } from 'ant-design-vue';

  export default {
    name: 'LyStatuscard',
    components: { Progress, Card },

    props: {
      loading: {
        type: Boolean,
        default: false,
      },
      count: {
        type: Number,
        default: 1,
      },
      rows: {
        type: Number,
        default: 4,
      },
      animated: {
        type: Boolean,
        default: true,
      },
      modelValue: {
        type: Object,
        // eslint-disable-next-line vue/require-valid-default-prop
        default: {
          cpu: [0, 0, [0, 0, 0, 0], 'Intel(R) Core(TM) i5-71200 CPU @ 3.40GHz * 1', 0, 1],
          disk: [{ path: '', size: ['0GB', '0GB', '0GB', 0], inodes: false }],
          is_windows: true,
          load_average: { one: 0, five: 0, fifteen: 0, max: 0, limit: 0, safe: 0, percent: 0 },
          mem: { percent: 0, total: 0, free: 0, used: 0 },
          system: 'Windows 10 Pro (build 16299) x64 (Py3.9.8)',
          time: '0天',
        },
      },
      height: {
        type: Number,
        default: 200,
      },
    },
    data() {
      return {
        dataList: {
          cpu: [0, 0, [0, 0, 0, 0], 'Intel(R) Core(TM) i5-71200 CPU @ 3.40GHz * 1', 0, 1],
          disk: [{ path: '', size: ['0GB', '0GB', '0GB', 0], inodes: false }],
          is_windows: true,
          load_average: { one: 0, five: 0, fifteen: 0, max: 0, limit: 0, safe: 0, percent: 0 },
          mem: { percent: 0, total: 0, free: 0, used: 0 },
          system: 'Windows 10 Pro (build 16299) x64 (Py3.9.8)',
          time: '0天',
        },
        load_config: [
          {
            title: '运行堵塞',
            percentage: 90,
            color: '#dd2f00',
          },
          {
            title: '运行缓慢',
            percentage: 80,
            color: '#ff9900',
          },
          {
            title: '运行正常',
            percentage: 70,
            color: '#20a53a',
          },
          {
            title: '运行流畅',
            percentage: 30,
            color: '#20a53a',
          },
        ],
      };
    },
    watch: {
      modelValue: function (nval) {
        this.dataList = nval;
      },
      dataList: function (nval) {
        this.$emit('update:modelValue', nval);
      },
    },
    mounted() {
      this.dataList = this.modelValue;
    },

    methods: {
      // 进度条根据完成度自定义分段的颜色 -- 参数successPercent表示已完成的分段百分比
      getProgressColor(successPercent) {
        let color = '';
        if (successPercent < 40) {
          color = '#20a53a';
        } else if (successPercent >= 40 && successPercent < 70) {
          color = '#20a53a';
        } else if (successPercent >= 70 && successPercent < 80) {
          color = '#ff9900';
        } else {
          color = '#dd2f00';
        }
        console.log(color);

        return color;
      },
    },
  };
</script>

<style scoped>
  .space-main-up-cpu {
    padding-left: 15px;
    font-size: 12px;
    display: flex;
    flex-direction: column;
    line-height: 20px;
    /*width: 200px;*/
    color: #666666;
  }
  ::v-deep(.Col) {
    margin-bottom: 11px;
  }
</style>
