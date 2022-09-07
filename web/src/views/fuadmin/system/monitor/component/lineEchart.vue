<template>
  <div class="lymonitor-info">
    <div class="lymonitor-info-item"
      ><p><span class="ico-up"></span>{{ t('common.monitor.upText') }}</p
      ><a id="upSpeed">{{ modelValue.up + 'KB' }}</a></div
    >
    <div class="lymonitor-info-item"
      ><p><span class="ico-down"></span>{{ t('common.monitor.downText') }}</p
      ><a id="downSpeed">{{ modelValue.down + 'KB' }}</a></div
    >
    <div class="lymonitor-info-item"
      ><p>{{ t('common.monitor.sentText') }}</p
      ><a id="upAll">{{ formatUnitSize(modelValue.upTotal) }}</a></div
    >
    <div class="lymonitor-info-item"
      ><p>{{ t('common.monitor.receivedText') }}</p
      ><a id="downAll">{{ formatUnitSize(modelValue.downTotal) }}</a></div
    >
    <!--    <el-select v-model="networkValue"  placeholder="Select" size="large" @change="networkSelectChange">-->
    <!--      <el-option-->
    <!--        v-for="item in networkOptions"-->
    <!--        :key="item.value"-->
    <!--        :label="item.label"-->
    <!--        :value="item.value"-->
    <!--      />-->
    <!--    </el-select>-->
  </div>
  <div id="lyechartmain" style="width: 100%; height: 280px"></div>
</template>

<script>
  import { onBeforeUnmount, onMounted, reactive, watch } from 'vue';
  import echarts from '/@/utils/lib/echarts';
  import { formatUnitSize } from "/@/utils";
  import { useI18n } from '/@/hooks/web/useI18n';
  export default {
    name: 'LyMonitorLineEchart',
    props: {
      // 绑定文本值
      modelValue: {},
    },
    setup(props, { emit }) {
      const { t } = useI18n();
      const state = reactive({
        contentValue: props.modelValue, // 绑定文本
        timeout: null,
        echartData: {
          uData: [],
          dData: [],
          aData: [],
        },
      });

      let myChart = null;
      let option = {};
      onMounted(() => {
        //需要获取到element,所以是onMounted的Hook
        setTimeout(() => {
          myChart = echarts.init(document.getElementById('lyechartmain'));
          state.contentValue = props.modelValue;
          addData(state.contentValue.up, state.contentValue.down);
          initEcharts();
          // myChart = echarts.init(document.getElementById("lyechartmain"));
          // myChart.setOption(option);
        }, 200);
      });
      onBeforeUnmount(() => {
        window.onresize = null;
      });
      // 侦听文本变化并传给外界
      watch(
        () => state.contentValue,
        (n) => {
          debounce(() => {
            emit('update:modelValue', state.contentValue);
          });
        },
      );
      // 侦听默认值 外界第一次传进来一个 v-model 就赋值给 contentValue
      watch(
        () => props.modelValue,
        (n) => {
          if (n && n !== state.contentValue) {
            state.contentValue = n;
            addData(n.up, n.down);
            initEcharts();
          }
        },
      );
      function initEcharts() {
        var obj = {};
        obj.dataZoom = [];
        obj.unit = '单位:KB/s';
        obj.tData = state.echartData.aData;
        obj.formatter = function (config) {
          var _config = config,
            _tips = '';
          for (var i = 0; i < config.length; i++) {
            if (typeof config[i].data == 'undefined') return false;
            _tips +=
              '<span style="display: inline-block;width: 10px;height: 10px;margin-rigth:10px;border-radius: 50%;background: ' +
              config[i].color +
              ';"></span>  ' +
              config[i].seriesName +
              '：' +
              parseFloat(config[i].data).toFixed(2) +
              ' KB/s' +
              (config.length - 1 !== i ? '<br />' : '');
          }
          return '时间：' + _config[0].axisValue + '<br />' + _tips;
        };
        obj.list = [];
        obj.list.push({
          name: t('common.monitor.upText'),
          data: state.echartData.uData,
          circle: 'circle',
          itemStyle: { color: '#4c8ff1' },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                { offset: 0, color: 'rgba(76, 143, 241)' },
                { offset: 1, color: 'rgba(76, 143, 241)' },
              ],
              false,
            ),
          },
          lineStyle: { width: 1, color: '#aaa' },
        });
        obj.list.push({
          name: t('common.monitor.downText'),
          data: state.echartData.dData,
          circle: 'circle',
          itemStyle: { color: '#1cd798' },
          areaStyle: {
            color: new echarts.graphic.LinearGradient(
              0,
              0,
              0,
              1,
              [
                { offset: 0, color: 'rgba(28, 215, 152)' },
                { offset: 1, color: 'rgba(28, 215, 152)' },
              ],
              false,
            ),
          },
          lineStyle: { width: 1, color: '#aaa' },
        });
        option = format_option(obj);
        if (option !== null || option !== '' || option !== undefined) {
          myChart.setOption(option);
        }
        // myChart.setOption(option);
        window.onresize = function () {
          //自适应大小
          myChart.resize();
        };
      }
      function addData(up, down) {
        var limit = 16;
        var d = new Date();
        if (state.echartData.uData.length >= limit) state.echartData.uData.splice(0, 1);
        if (state.echartData.dData.length >= limit) state.echartData.dData.splice(0, 1);
        if (state.echartData.aData.length >= limit) state.echartData.aData.splice(0, 1);

        state.echartData.uData.push(up);
        state.echartData.dData.push(down);
        state.echartData.aData.push(d.getHours() + ':' + d.getMinutes() + ':' + d.getSeconds());
      }
      function format_option(obj, type) {
        var option = {
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'cross',
            },
            formatter: obj.formatter,
          },
          grid: {
            left: '3%',
            right: '3%',
            bottom: '3%',
            containLabel: true,
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: obj.tData,
            axisLine: {
              lineStyle: {
                color: '#666',
              },
            },
          },
          yAxis: {
            type: 'value',
            name: obj.unit,
            boundaryGap: [0, '100%'],
            min: 0,
            splitLine: {
              lineStyle: {
                color: '#ddd',
              },
            },
            axisLine: {
              lineStyle: {
                color: '#666',
              },
            },
          },
          dataZoom: [
            {
              type: 'inside',
              start: 0,
              zoomLock: true,
            },
            {
              start: 0,
              handleIcon:
                'M10.7,11.9v-1.3H9.3v1.3c-4.9,0.3-8.8,4.4-8.8,9.4c0,5,3.9,9.1,8.8,9.4v1.3h1.3v-1.3c4.9-0.3,8.8-4.4,8.8-9.4C19.5,16.3,15.6,12.2,10.7,11.9z M13.3,24.4H6.7V23h6.6V24.4z M13.3,19.6H6.7v-1.4h6.6V19.6z',
              handleSize: '80%',
              handleStyle: {
                color: '#fff',
                shadowBlur: 3,
                shadowColor: 'rgba(0, 0, 0, 0.6)',
                shadowOffsetX: 2,
                shadowOffsetY: 2,
              },
            },
          ],
          series: [],
        };
        if (obj.legend) option.legend = obj.legend;
        if (obj.dataZoom) option.dataZoom = obj.dataZoom;

        for (var i = 0; i < obj.list.length; i++) {
          var item = obj.list[i];
          var series = {
            name: item.name,
            type: item.type ? item.type : 'line',
            smooth: item.smooth ? item.smooth : true,
            symbol: item.symbol ? item.symbol : 'none',
            showSymbol: item.showSymbol ? item.showSymbol : false,
            sampling: item.sampling ? item.sampling : 'average',
            areaStyle: item.areaStyle ? item.areaStyle : {},
            lineStyle: item.lineStyle ? item.lineStyle : {},
            itemStyle: item.itemStyle ? item.itemStyle : { color: 'rgb(0, 153, 238)' },
            symbolSize: 6,
            symbol: 'circle',
            data: item.data,
          };
          option.series.push(series);
        }
        return option;
      }
      function debounce(fn, wait = 400) {
        // console.log('进到了防抖', wait)
        if (state.timeout !== null) {
          clearTimeout(state.timeout);
        }
        state.timeout = setTimeout(fn, wait);
      }
      function handleResize() {
        myChart.resize();
      }
      return {
        debounce,
        handleResize,
        addData,
        formatUnitSize,
        initEcharts,
        format_option,
        t,
      };
    },
  };
</script>

<style scoped>
  .lymonitor-info {
    display: flex;
    width: 100%;
    text-align: center;
    align-items: center;
    justify-content: center;
    column-gap: 5%;
    font-size: 13px;
    line-height: 20px;
  }
  .lymonitor-info .ico-up {
    width: 12px;
    height: 12px;
    border-radius: 100%;
    background-color: #4c8ff1;
    display: inline-block;
    margin-right: 3px;
  }
  .lymonitor-info .ico-down {
    width: 12px;
    height: 12px;
    border-radius: 100%;
    background-color: #1cd798;
    display: inline-block;
    margin-right: 3px;
  }
  /*.lymonitor-info-item{*/
  /*    flex: 1;*/
  /*}*/
</style>
