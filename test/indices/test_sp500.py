from feature_util.indices import SP500IndexFeatureProducer
from test.util import (generate_ohlc_df, assert_ohlc_df)


def test_sp500_feature():
    df = generate_ohlc_df()
    producer = SP500IndexFeatureProducer()
    result = producer.produce(df)

    assert_ohlc_df(result)
    assert 'sp500' in result
