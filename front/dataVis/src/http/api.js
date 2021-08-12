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

