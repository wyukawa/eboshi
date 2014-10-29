About eboshi
-----------

eboshi is Azkaban CLI tool

Installing
----------

``pip install eboshi``

Usage
----------

* upload azkaban job zip file

  ``eboshi upload --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --filename azkaban_job.zip``

* scheducle azkaban job

  ``eboshi schedule --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --flow azkaban_flow --date '08/07/2014' --time '10,30,AM,JST' --period 1d --option '{"failureAction":"finishPossible"}'``
