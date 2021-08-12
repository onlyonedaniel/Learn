<template>
  <div>
    <el-table :data="tableData"
              height="500"
              border
              style="width: 100%">
      <el-table-column prop="id"
                       label="编号"
                       width="50">
      </el-table-column>
      <el-table-column label="数据"
                       width="">
        <template slot-scope="scope">

          <el-tag :type="'success'"
                  v-for='(item,index) in scope.row.array'
                  :key='index'
                  disable-transitions>{{item}}</el-tag>
        </template>
      </el-table-column>

    </el-table>
  </div>
</template>

<script>
import { getChartTwoApi } from '../../http/api'
export default {
  name: 'chartTwo',
  data () {
    return {
      tableData: []
    }
  },
  mounted () {
    this.init_page()
  },
  methods: {
    init_page () {
      getChartTwoApi().then(
        res => {
          if (res.data.errorcode == 0) {
            console.log(res.data.data)
            this.tableData = res.data.data
          }
        }
      )
    }
  }
}
</script>

<style>
</style>