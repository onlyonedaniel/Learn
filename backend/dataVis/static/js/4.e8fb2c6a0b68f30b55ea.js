webpackJsonp([4],{"5Jgp":function(e,r){},NxzY:function(e,r,s){"use strict";Object.defineProperty(r,"__esModule",{value:!0});var t=s("m4jk"),o={name:"register",data:function(){return{registerForm:{username:"",password:"",password2:"",mobile:""},rules:{name:[{required:!0,message:"请输入用户名",trigger:"blur"},{min:3,max:150,message:"长度在 3 到 150 个字符",trigger:"blur"}],password:[{required:!0,message:"请输入密码",trigger:"blur"}],password2:[{required:!0,message:"请确认密码",trigger:"blur"}],mobile:[{required:!0,message:"请输入手机号",trigger:"blur"},{min:11,max:11,message:"11个字符",trigger:"blur"}]}}},mounted:function(){console.log("123")},methods:{init_page:function(){},registe:function(){var e=this,r=new FormData;r.append("username",this.registerForm.username),r.append("password",this.registerForm.password),r.append("mobile",this.registerForm.mobile),Object(t.e)(r).then(function(r){e.$message(r.data),0==r.data.errorcode&&e.$router.push({path:"/chart/"})})}}},a={render:function(){var e=this,r=e.$createElement,s=e._self._c||r;return s("div",[s("el-form",{ref:"form",attrs:{model:e.registerForm,rules:e.rules}},[s("el-form-item",{attrs:{label:"用户名",prop:"username"}},[s("el-input",{model:{value:e.registerForm.username,callback:function(r){e.$set(e.registerForm,"username",r)},expression:"registerForm.username"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"密码",prop:"password"}},[s("el-input",{attrs:{"show-password":""},model:{value:e.registerForm.password,callback:function(r){e.$set(e.registerForm,"password",r)},expression:"registerForm.password"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"确认密码",prop:"password2"}},[s("el-input",{attrs:{"show-password":""},model:{value:e.registerForm.password2,callback:function(r){e.$set(e.registerForm,"password2",r)},expression:"registerForm.password2"}})],1),e._v(" "),s("el-form-item",{attrs:{label:"手机号",prop:"mobile"}},[s("el-input",{model:{value:e.registerForm.mobile,callback:function(r){e.$set(e.registerForm,"mobile",r)},expression:"registerForm.mobile"}})],1),e._v(" "),s("el-form-item",[s("el-button",{on:{click:e.registe}},[e._v("\n        注册\n      ")])],1)],1)],1)},staticRenderFns:[]};var i=s("VU/8")(o,a,!1,function(e){s("5Jgp")},null,null);r.default=i.exports}});
//# sourceMappingURL=4.e8fb2c6a0b68f30b55ea.js.map