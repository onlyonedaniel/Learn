<template>
  <div>
    <div id="container"></div>
    <el-tooltip class="item"
                effect="dark"
                content="保存数据"
                placement="top-start">
      <el-button type="primary"
                 icon="el-icon-circle-check"
                 @click="saveData"></el-button>
    </el-tooltip>
  </div>
</template>

<script>
import Highcharts from "highcharts/highstock";
import HighchartsMore from "highcharts/highcharts-more";
import HighchartsDrilldown from "highcharts/modules/drilldown";
import Highcharts3D from "highcharts/highcharts-3d";
HighchartsMore(Highcharts);
HighchartsDrilldown(Highcharts);
Highcharts3D(Highcharts);
import { getChartOneApi, postChartTwoApi } from '../../http/api'

export default {
  name: "charOne",
  data () {
    return {      chartData: [],
    }
  },
  mounted () {
    this.getData()
    this.timer()
  },
  beforeRouteLeave (to, from, next) {
    clearInterval(this.timer)
  },
  methods: {
    moreChart () {
      if (this.chart) {
        this.chart.destroy();
      }
      // 初始化 Highcharts 图表
      this.chart = new Highcharts.Chart("container", {
        title: {
          text: "动态数据"
        },
        yAxis: {
          title: {
            text: "值"
          }
        },
        legend: {
          layout: "vertical",
          align: "right",
          verticalAlign: "middle"
        },
        plotOptions: {
          series: {
            label: {
              connectorAllowed: false
            },
            pointStart: 0
          }
        },
        series: [
          {
            name: "",
            data: this.chartData
          }
        ],
        responsive: {
          rules: [
            {
              condition: {
                maxWidth: 500
              },
              chartOptions: {
                legend: {
                  layout: "horizontal",
                  align: "center",
                  verticalAlign: "bottom"
                }
              }
            }
          ]
        }
      });
    },
    async getData () {
      let that = this;
      await getChartOneApi().then(
        res => {
          console.log(res.data)
          if (res.data.errorcode == 0) {
            that.chartData = res.data.data
            that.moreChart(that.chartData)
          }
        }
      ).catch(err => {
        console.log(err)
        this.$message({
          type: 'error',
          message: 'get data fail'
        })
      }
      )
    },
    saveData () {
      let formData = new FormData()
      formData.append('data', JSON.stringify(this.chartData));
      postChartTwoApi(formData).then(
        res => {
          if (res.data.errorcode == 0) {
            this.$message(
              {
                type: 'success',
                message: 'save data success'
              }
            )
            this.$emit('reflashChartTwo')
          }
        }

      ).catch(err => {
        console.log(err)
        this.$message({
          type: 'error',
          message: 'save data fail'
        })
      }

      )

    },
    timer () {
      return setInterval(() => {
        this.getData()
      }, 10000)
    },
    destroyed () {
      clearInterval(this.timer)
    }


  }
};
</script>

<!-- Add "scoped" attribute to limit css to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
