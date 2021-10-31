<template>
  <div>
    <el-row>
      <el-col :span="12"
              :offset='6'>
        <router-view></router-view>
      </el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'user'
}
</script>

<style>
</style>