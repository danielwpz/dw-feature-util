import pandas as pd
import numpy as np
from test.util import array_equal
from feature_util.ohlc import TimeLagsFeatureProducer


def test_time_lags_producer():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 3, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 5, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 6, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 7, 'volume': 100}
    ])

    close_3_producer = TimeLagsFeatureProducer(lags=3, feature='close')
    close_3_result = close_3_producer.produce(ohlc_df)['close_tlag_3'].values
    expect_result_close_3 = np.asarray([np.nan, np.nan, np.nan, 1., 2., 3., 4.])
    assert array_equal(close_3_result, expect_result_close_3)
