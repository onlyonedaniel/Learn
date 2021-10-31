<template>
  <div>

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
      <el-form-item label='确认密码'
                    prop='password2'>
        <el-input v-model="registerForm.password2"
                  show-password></el-input>
      </el-form-item>
      <el-form-item label='验证码'
                    prop='code'>
        <el-row>
          <el-col :span='12'>
            <el-input v-model="registerForm.varify_code"></el-input>
          </el-col>
          <el-col :span='12'>
            <img @click="get_code"
                 :src="image_url"
                 alt="">
          </el-col>
        </el-row>

      </el-form-item>
      <el-form-item label='手机号'
                    prop='mobile'>
        <el-input v-model="registerForm.mobile"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button @click="registe">
          注册
        </el-button>
      </el-form-item>
    </el-form>
  </div>

</template>

<script>
import { postRegisterApi, getCodeApi } from '../../http/api'
import { guid2 } from '../../common/utils'
export default {
  name: 'register',
  data () {
    return {
      registerForm: {
        username: "",
        password: "",
        password2: '',
        mobile: "",
        varify_code: '',
        uuid: ""
      }, rules: {
        name: [
          { required: true, message: '请输入用户名', trigger: 'blur' },
          { min: 3, max: 150, message: '长度在 3 到 150 个字符', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' },
        ],
        password2: [
          { required: true, message: '请确认密码', trigger: 'blur' },
        ],
        mobile: [
          { required: true, message: '请输入手机号', trigger: 'blur' },
          { min: 11, max: 11, message: '11个字符', trigger: 'blur' }
        ]
      },
      image_url: ""

    }
  },
  mounted () {
    console.log('123')
    this.init_page()
  },
  methods: {
    init_page () {
      this.get_code()
    },
    registe () {
      let form_data = new FormData();
      form_data.append('uuid', this.registerForm.uuid)
      form_data.append('username', this.registerForm.username)
      form_data.append('password', this.registerForm.password)
      form_data.append('mobile', this.registerForm.mobile)
      form_data.append('varify_code', this.registerForm.varify_code)
      postRegisterApi(form_data).then(
        res => {
          this.$message(res.data)
          if (res.data.errorcode == 0) {
            this.$router.push({ path: '/chart/' })
          }
        }
      )
    },
    get_code () {
      let uuid = guid2()
      this.registerForm.uuid = uuid
      getCodeApi(uuid).then(
        res => {
          console.log(res.data)
          this.image_url = 'data:image/jpg;base64,' + res.data
        }
      )
    }

  }
}
</script>

<style>
</style>