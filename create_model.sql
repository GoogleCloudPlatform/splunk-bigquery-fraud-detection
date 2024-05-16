/* Copyright 2024 Google LLC

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. */

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
          
