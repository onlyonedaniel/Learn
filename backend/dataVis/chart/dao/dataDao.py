import logging
import json
from chart.models import LatestData, Data
logger = logging.getLogger("django")


def get_latest_data():
    records = LatestData.objects.all()
    if len(records) == 0:
        logging.info('there is no data in table {}, will create '.format(
            LatestData.__name__))


def save_chart_one(array_data: list):
    records = LatestData.objects.all()
    if len(records) == 0:
        logging.info('there is no data in table {}, will create '.format(
            LatestData.__name__))
        LatestData(array=json.dumps(array_data)).save()


def save_chart_two(array_data: str):
    Data(array=array_data).save()
    logging.info('save array to {} table'.format(
        Data.__name__))


def get_chart_two(start, limit):
    sql = """
      select * 
      from 
        chart_data
      limit {},{}
    """.format(start, limit)
    logging.info('{} {}'.format(
        get_chart_two, sql))
    records = Data.objects.raw(sql)
    ret = []
    if records:
        for it in records:
            record = it.__dict__
            if '_state' in record:
                del record['_state']
            record['array'] = json.loads(record['array'])
            ret.append(record)
    return ret
