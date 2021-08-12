<template>
  <el-row style="height:100%">
    <el-col :span='12'
            class="right-border">
      <chart-one @reflashChartTwo="reflashChartTwo">

      </chart-one>
    </el-col>
    <el-col :span='12'>
      <chart-two ref="chartTwo">

      </chart-two>
    </el-col>

  </el-row>

</template>

<script>
import chartOne from './chartOne'
import chartTwo from './chartTwo'
export default {
  name: 'chart',
  data () {
    return {

    }
  },
  methods: {
    reflashChartTwo () {
      this.$refs.chartTwo.init_page()
    }
  },
  components: {
    chartOne,
    chartTwo
  }
}
</script>

<style>
.right-border {
  border-right: 1px solid gray;
}
</style>