<template>
  <el-form ref='form'
           :model="registerForm"
           :rules="rules">
    <el-form-item label='用户名'
                  prop="username">
      <el-input v-model="registerForm.username"></el-input>
    </el-form-item>
    <el-form-item label='密码'
                  prop="password">
      <el-input v-model="registerForm.password"
                show-password></el-input>
    </el-form-item>
    <el-form-item>
      <el-button @click="login">登陆</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { postLoginApi } from '../../http/api'
export default {
  name: 'login',
  data () {
    return {
      registerForm: {
        username: "",
        password: "",
      }, rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 150, message: '长度在 3 到 150 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
        ],
      },
    }  },
  methods: {
    login () {
      let loginFrom = new FormData();
      loginFrom.append('username', this.registerForm.username)
      loginFrom.append('password', this.registerForm.password)
      postLoginApi(loginFrom).then(
        res => {
          this.$message(res.data);
          console.log('a')
          console.log(res.data.errorcode)
          console.log('b')
          if (res.data.errorcode != 0) {
            this.$router.push({ path: '/user/register' })
            return
          }
          this.$router.push({ path: '/chart' })
        }
      )
    }
  },
}
</script>

<style>
</style>