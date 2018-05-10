from feature_util.indices import NasdaqIndexFeatureProducer
from test.util import (generate_ohlc_df, assert_ohlc_df)


def test_nasdaq_feature():
    df = generate_ohlc_df()
    producer = NasdaqIndexFeatureProducer()
    result = producer.produce(df)

    assert_ohlc_df(result)
    assert 'nasdaq' in result
