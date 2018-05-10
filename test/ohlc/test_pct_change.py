import pandas as pd
import numpy as np
from test.util import array_equal
from feature_util.ohlc import PercentChangeFeatureProducer


def test_pct_change_producer():
    ohlc_df = pd.DataFrame([
        {'open': 1, 'high': 9, 'low': 1, 'close': 1, 'volume': 100},
        {'open': 1, 'high': 8, 'low': 1, 'close': 2, 'volume': 100},
        {'open': 1, 'high': 7, 'low': 1, 'close': 4, 'volume': 100},
        {'open': 1, 'high': 6, 'low': 1, 'close': 8, 'volume': 100},
        {'open': 1, 'high': 5, 'low': 1, 'close': 16, 'volume': 100},
        {'open': 1, 'high': 4, 'low': 1, 'close': 32, 'volume': 100},
        {'open': 1, 'high': 3, 'low': 1, 'close': 64, 'volume': 100}
    ])

    close_pct_change_producer = PercentChangeFeatureProducer()
    result_close_pct_change = close_pct_change_producer.produce(ohlc_df)['close_pct_change'].values
    expected_close_pct_change = [1] * len(result_close_pct_change)
    expected_close_pct_change[0] = np.nan
    assert array_equal(result_close_pct_change, expected_close_pct_change)

    volume_pct_change_producer = PercentChangeFeatureProducer(feature='volume')
    result_vol_pct_change = volume_pct_change_producer.produce(ohlc_df)['volume_pct_change'].values
    expected_vol_pct_change = [0] * len(result_vol_pct_change)
    expected_vol_pct_change[0] = np.nan
    assert array_equal(result_vol_pct_change, expected_vol_pct_change)
