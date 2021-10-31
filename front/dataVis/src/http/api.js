import axios from './http';
// 获取列表
export function getChartOneApi () {
    return axios.get('/chart/1/')
}

export function getChartTwoApi () {
    return axios.get('/chart/2/')
}

export function postChartTwoApi (data) {
    return axios.post('/chart/2/', data)
}

//user
export function postRegisterApi (data,) {
    return axios.post('/user/register/', data)
}
export function postLoginApi (data) {
    return axios.post('/user/login/', data)
}

export function getCodeApi (uuid) {
    return axios.get('/image/image_code/' + uuid + '/')
}
