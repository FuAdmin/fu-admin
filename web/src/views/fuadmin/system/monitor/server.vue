<template>
  <div class="p-4">
    <Card size="small">
      <div class="lycard-left">
        <span :class="iconClass">{{ t('common.monitor.osText') }}：</span>
        <span>{{ monitorData.system }}</span>
        <span style="margin-left: 20px">
          {{ t('common.monitor.runTimeText') }}: {{ monitorData.time }}</span
        >
        <span style="margin-left: 20px">{{ t('common.monitor.autoRefreshText') }}：</span>
        <InputNumber
          v-model:value="refreshInterval"
          size="small"
          :min="3"
          @change="restartIntervalMonitor"
        />
        <a-button
          style="margin-left: 20px"
          type="link"
          v-if="timer"
          :text="true"
          link
          @click="getData"
          ><span style="font-size: 13px" @click="clearIntervalMonitor">{{
            t('common.monitor.stopText')
          }}</span></a-button
        >
        <a-button
          style="margin-left: 20px"
          type="link"
          v-if="timer == null"
          :text="true"
          link
          @click="getData"
        >
          <span style="font-size: 13px" @click="restartIntervalMonitor">{{
            t('common.monitor.startText')
          }}</span>
        </a-button>
        <a-button type="link" :text="true" link @click="getData"
          ><span style="font-size: 13px">
            {{ t('common.monitor.manualRefreshText') }}</span
          ></a-button
        >
      </div>
    </Card>
    <div>
      <ly-statuscard v-model="monitorData" class="!my-4 enter-y" />
    </div>
    <div>
      <EchartCard :network="monitorData.network" class="!my-4 enter-y" />
    </div>
  </div>
</template>

<script>
  import { InputNumber, Card } from 'ant-design-vue';
  import LyStatuscard from './component/statusCard.vue';
  import { getSystemInfo } from './api';
  import EchartCard from './component/echartCard.vue';
  import { useI18n } from '../../../../hooks/web/useI18n';
  export default {
    name: 'Server',
    components: { EchartCard, LyStatuscard, InputNumber, Card },
    data() {
      return {
        t: undefined,
        isFull: false,
        isRunning: false,
        showloading: true,
        tableHeight: '500px',
        monitorData: {
          cpu: [0, 0, [0, 0, 0, 0], '', 0, 1],
          disk: [{ path: '', size: ['0GB', '0GB', '0GB', 0], inodes: false }],
          is_windows: true,
          load_average: { one: 0, five: 0, fifteen: 0, max: 0, limit: 0, safe: 0, percent: 0 },
          mem: { percent: 0, total: 0, free: 0, used: 0 },
          system: '',
          time: '0day',
          network: {
            up: 0,
            down: 0,
            downTotal: 0,
            upTotal: 0,
            network: {},
          },
        },
        refreshInterval: 3,
        iconClass: '',
        timer: null, //定时器
      };
    },
    watch: {
      isFull: function () {
        this.listenResize();
      },
    },
    created() {
      this.getData();
      const { t } = useI18n();
      this.t = t;
    },
    mounted() {
      if (!this.isRunning) {
        this.intervalMonitor();
        this.isRunning = true;
        setTimeout(() => {
          this.showloading = false;
        }, 2000);
      }
      // 监听页面宽度变化搜索框的高度
      window.addEventListener('resize', this.listenResize);
      this.listenResize();
    },
    activated() {
      if (!this.isRunning) {
        this.intervalMonitor();
        this.isRunning = true;
      }
    },
    deactivated() {
      this.isRunning = false;
      this.clearIntervalMonitor();
    },
    unmounted() {
      this.clearIntervalMonitor();
      // 页面销毁，去掉监听事件
      window.removeEventListener('resize', this.listenResize);
    },
    methods: {
      setFull() {
        this.isFull = !this.isFull;
      },
      //获取列表
      getData() {
        getSystemInfo().then((res) => {
          this.monitorData = res;
          let tempsystem = res.system.split(' ')[0].toLowerCase();
          this.iconClass = 'ico-' + tempsystem;
        });
      },
      intervalMonitor() {
        let that = this;
        this.timer = setInterval(() => {
          that.getData();
        }, that.refreshInterval * 1000);
      },
      restartIntervalMonitor() {
        this.clearIntervalMonitor();
        this.intervalMonitor();
      },
      clearIntervalMonitor() {
        clearInterval(this.timer);
        this.timer = null;
      },
      handleResize() {},
      // 计算搜索栏的高度
      listenResize() {},
      getTheTableHeight() {},
    },
  };
</script>

<style lang="less" scoped>
  .lycontainer {
    width: 100%;
    /*height: calc(100vh - 130px); //动态计算长度值*/
    /*overflow-x: hidden;*/
    /*overflow-y:auto;*/
  }
  .echarts-inner {
    margin-top: 1px;
  }
  ::v-deep(.el-scrollbar__bar.is-horizontal) {
    display: none;
  }
  .lycard-left {
    display: flex;
    align-items: center;
  }
  .lycard-right {
    display: flex;
    align-items: center;
  }
  /*系统图标*/

  .ico-linux {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABEAAAATBAMAAACEi/vCAAAAA3NCSVQICAjb4U/gAAAAMFBMVEX///9mZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmambAcKAAAAEHRSTlMAESIzRFVmd4iZqrvM3e7/dpUBFQAAAAlwSFlzAAAOwwAADsMBx2+oZAAAABZ0RVh0Q3JlYXRpb24gVGltZQAwOC8xNi8xOCL5ZhgAAAAcdEVYdFNvZnR3YXJlAEFkb2JlIEZpcmV3b3JrcyBDUzbovLKMAAAAmUlEQVQImWNgYGCQ/GvAAAHz/1+CMBjPvvoOYTFVLXkNZZ2u+isAZjE/4vyvAGaxlgbnJ4BZHAoM3A/BLA8GBpafYNYiIL4PMpt1A5DYPwFIcDWArDkAJPgWAInzF4BE9jMGBvb/QM2SBfEGDFy7UhkY3Bk4CxisGdgCGMwYGI97vGKwSmAQC1G8e+aN2WagDuP0IEGbawIMAPDJKG706GgtAAAAAElFTkSuQmCC');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }

  .ico-windows {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQBAMAAADt3eJSAAAAA3NCSVQICAjb4U/gAAAALVBMVEX///+ZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZny8jBSAAAAD3RSTlMAESIzRFVmd4iZqrvM7v/Y8bBbAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAFnRFWHRDcmVhdGlvbiBUaW1lADA4LzE2LzE4IvlmGAAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAABGSURBVAiZY2AAAkbTqrMMDEJuHvfevXvHcPbdu+53IMY7Ihi7d+9O7QACBiB2BTOAol0wNbgY59696wQzGFQqw8GWwpwBAGURWs03JAEWAAAAAElFTkSuQmCC');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }

  .ico-centos {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAPCAMAAADjyg5GAAAAA3NCSVQICAjb4U/gAAAASFBMVEX///9mZmZmZmZiYmJaWlpYWFhmZmZiYmJgYGBmZmZgYGBmZmZiYmJmZmZiYmJmZmZiYmJmZmZmZmZmZmZmZmZmZmZmZmZmZmbwNFvuAAAAGHRSTlMAESIiIiIzMzNERFVVZmZ3d4iZqrvM3f93YyfbAAAACXBIWXMAAA7DAAAOwwHHb6hkAAAAFnRFWHRDcmVhdGlvbiBUaW1lADA4LzE3LzE4mkUBfQAAABx0RVh0U29mdHdhcmUAQWRvYmUgRmlyZXdvcmtzIENTNui8sowAAAB6SURBVAiZVY5ZEsIwDEMdUpYQghIv9f1vWpNCp/hH1oz1LKI5if5G5ezuzLff7ibO7KK+H2LaBp1WDMLcYDNf3A31CXMvRCy995rSK0SExhjAkh/XEK5E2YOCN5r75RNGUJgtZJLXoMQjw/ot2LR3baJHSbN8Ll3LrhtQxAfrvVHLpQAAAABJRU5ErkJggg==');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }

  .ico-ubuntu {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAA3NCSVQICAjb4U/gAAAAOVBMVEX///9mZmZhYWFmZmZiYmJmZmZiYmJmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZVQ1Z+AAAAE3RSTlMAEREiIjMzRFVmd4iZqrvM3e7/67N/KAAAAAlwSFlzAAAOwwAADsMBx2+oZAAAABZ0RVh0Q3JlYXRpb24gVGltZQAwOC8xNy8xOJpFAX0AAAAcdEVYdFNvZnR3YXJlAEFkb2JlIEZpcmV3b3JrcyBDUzbovLKMAAAAbElEQVQImU2OWQ6AMAhEcW3Z2jL3P6xWjHE+CMPwCESfDOXtFmutAp6OtwC0jUwZVlWHaaaBniyYVq6B/Rn3G3aEjDxRuPwtN6NFzkB97IAlE3ddHTimPUKkd3TlhLb5huvLzAWWE2j0k0elCynoBUe/zXGJAAAAAElFTkSuQmCC');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }

  .ico-debian {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAQCAMAAAARSr4IAAAAA3NCSVQICAjb4U/gAAAAPFBMVEX///9paWlmZmZgYGBdXV1mZmZgYGBmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmYdQ+x6AAAAFHRSTlMAERERESIiM0RVZneImaq7zN3u/ynguF0AAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDgvMTcvMTiaRQF9AAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAHJJREFUCJlVjlESwjAIRLFFIRhCaO5/VyHijN2vt+zCABBq87IhT/hK1+zdfOl2Y71r2rPp1UKfAOdFgaTtAWIRWgacMUUquSi7TR6U2LflFuW0nOVjYB7JQBqwHklOe49f9dOAf+HvjRIZ3L3ePTIWfQAgiAODqr7Z+QAAAABJRU5ErkJggg==');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }

  .ico-fedora {
    background-image: url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAMAAAAolt3jAAAAA3NCSVQICAjb4U/gAAAAPFBMVEX///9VVVVLS0tmZmZaWlpmZmZiYmJmZmZiYmJmZmZiYmJiYmJmZmZmZmZmZmZmZmZmZmZmZmZmZmZmZmYd2jWRAAAAFHRSTlMAEREiIjMzRERVVWaImaq7zN3u/2KENScAAAAJcEhZcwAADsMAAA7DAcdvqGQAAAAWdEVYdENyZWF0aW9uIFRpbWUAMDgvMTcvMTiaRQF9AAAAHHRFWHRTb2Z0d2FyZQBBZG9iZSBGaXJld29ya3MgQ1M26LyyjAAAAGJJREFUCJlFj1kSwCAIQ9N9Lxjuf9faUKf5IPNQiAJAZ4yg9ZCWkMj5pxWwGCqK5skLg8AphMv2dIJC0106nNmu5VLA1bBmfqclF7fZO9HTYqzO4tMuOt5XGLA1enMzQ194ADH/CrSqGfFbAAAAAElFTkSuQmCC');
    background-repeat: no-repeat;
    padding-left: 20px;
    background-size: contain;
  }
</style>
