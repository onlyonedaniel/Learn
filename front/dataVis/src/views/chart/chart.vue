<template>
  <div>
    <el-row>
      <el-col :span='2'
              :offset='20'>
        {{username}}
      </el-col>
    </el-row>
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
  </div>

</template>

<script>
import chartOne from './chartOne'
import chartTwo from './chartTwo'
export default {
  name: 'chart',
  mounted () {
    this.get_usernname()
  },
  data () {
    return {
      username: ''
    }
  },
  methods: {
    reflashChartTwo () {
      this.$refs.chartTwo.init_page()
    },
    get_usernname () {
      if (this.$cookies.isKey('username')) {
        this.username = this.$cookies.get('username')
      } else {
        this.$router.push('/user/login')
      }
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