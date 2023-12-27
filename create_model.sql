CREATE OR REPLACE MODEL
  `<porjectname>.<datasetname>.<model name>`
OPTIONS(
  model_type='ARIMA_PLUS',
  time_series_timestamp_col='ts',
  time_series_data_col='amount',
  time_series_id_col=['user_id'],
  auto_arima=TRUE,
  data_frequency='AUTO_FREQUENCY')
AS SELECT
user_id  , timestamp as ts,amount
FROM
  `<porjectname>.<datasetname>.<your table name>`;

-- 
SELECT
user_id, ts,amount,lower_bound,upper_bound,anomaly_probability, is_anomaly 
FROM
  ML.DETECT_ANOMALIES(MODEL`<porjectname>.<datasetname>.<model name>`,STRUCT(0.9 AS anomaly_prob_threshold),
  (
      SELECT
       user_id, timestamp as ts,amount
      FROM
        `<porjectname>.<datasetname>.<your table name>`))   order by ts ;
          