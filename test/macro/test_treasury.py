from feature_util.macro import USTreasuryYieldFeatureProducer
from test.util import generate_ohlc_df, assert_ohlc_df

def test_us_treasury_yield():
    df = generate_ohlc_df()
    producer = USTreasuryYieldFeatureProducer()
    result = producer.produce(df)

    assert_ohlc_df(result)
    assert 'us_treasury_10y' in result
