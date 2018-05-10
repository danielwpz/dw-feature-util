from feature_util.indices import DowJIndexFeatureProducer
from test.util import (generate_ohlc_df, assert_ohlc_df)


def test_dowj_producer():
    df = generate_ohlc_df()
    producer = DowJIndexFeatureProducer()
    result = producer.produce(df)

    assert_ohlc_df(result)
    assert 'dowj' in result
