#eboshi

eboshi is Azkaban CLI tool

Azkaban provides API. see http://azkaban.github.io/azkaban/docs/2.5/#ajax-api

ebosi requests Azkaban API.

##Prerequisites
Python 2.7

##Required Python Libraries
* requests
* cliff

##Install
```
pip install eboshi
```

Usage
----------

```
$ eboshi -h
usage: eboshi [--version] [-v] [--log-file LOG_FILE] [-q] [-h] [--debug]

Azkaban CLI

optional arguments:
  --version            show program's version number and exit
  -v, --verbose        Increase verbosity of output. Can be repeated.
  --log-file LOG_FILE  Specify a file to log output. Disabled by default.
  -q, --quiet          Suppress output except warnings and errors.
  -h, --help           Show this help message and exit.
  --debug              Show tracebacks on errors.

Commands:
  addCronSchedule  add cron schedule azkaban job
  addSchedule    add schedule azkaban job
  complete       print bash completion command
  createProject  create azkaban project
  deleteProject  delete azkaban project
  exec           exec azkaban job
  fetchFlow      fetch flow azkaban job
  getMostRecentNextExecTime  get most recent next exec time
  getSchedule    get schedule azkaban job
  help           print detailed help for another command
  listSchedules  list schedules azkaban job
  removeAllSchedules  remove all schedules azkaban job
  removeSchedule  remove schedule azkaban job
  upload         upload azkaban job zip file
```

* create azkaban project
```
$ eboshi createProject
usage: eboshi createProject [-h] --url URL --username USERNAME --password
PASSWORD --project PROJECT --description
DESCRIPTION
eboshi createProject: error: argument --url is required
```
```
eboshi createProject --url http://localhost:8081 --username azkaban --password azkaban --project test --description test
```

* delete azkaban project
```
$ eboshi deleteProject
usage: eboshi deleteProject [-h] --url URL --username USERNAME --password
                            PASSWORD --project PROJECT
eboshi deleteProject: error: argument --url is required
```
```
eboshi deleteProject --url http://localhost:8081 --username azkaban --password azkaban --project testt
```

* upload azkaban job zip file
```
$ eboshi upload
usage: eboshi upload [-h] --url URL --username USERNAME --password PASSWORD
                     --project PROJECT --filename FILENAME
eboshi upload: error: argument --url is required
```
```
eboshi upload --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --filename azkaban_job.zip
```

* add schedule azkaban job
```
$ eboshi addSchedule
usage: eboshi addSchedule [-h] --url URL --username USERNAME --password
                          PASSWORD --project PROJECT --flow FLOW --date DATE
                          --time TIME --period PERIOD [--option OPTION]
eboshi addSchedule: error: argument --url is required
```
```
eboshi addSchedule --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --flow azkaban_flow --date '08/07/2014' --time '10,30,AM,JST' --period 1d --option '{"failureAction":"finishPossible"}'
```

* add cron schedule azkaban job
```
$ eboshi addCronSchedule
usage: eboshi addCronSchedule [-h] --url URL --username USERNAME --password
                              PASSWORD --project PROJECT --flow FLOW --cron
                              CRON [--option OPTION]
eboshi addCronSchedule: error: argument --url is required
```
```
eboshi addCronSchedule --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --flow azkaban_flow --cron '0 10 * * *' --option '{"failureAction":"finishPossible"}'
```

* list schedules azkaban job
```
$ eboshi listSchedules
usage: eboshi listSchedules [-h] --url URL --username USERNAME --password
                            PASSWORD
eboshi listSchedules: error: argument --url is required
```
```
eboshi listSchedules --url http://localhost:8081 --username azkaban --password azkaban
```

* remove all schedules azkaban job
```
$ eboshi removeAllSchedules
usage: eboshi removeAllSchedules [-h] --url URL --username USERNAME --password
                                 PASSWORD
eboshi removeAllSchedules: error: argument --url is required
```
```
eboshi removeAllSchedules --url http://localhost:8081 --username azkaban --password azkaban
```

* remove schedule azkaban job
```
$ eboshi removeSchedule
usage: eboshi removeSchedule [-h] --url URL --username USERNAME --password
                             PASSWORD --scheduleId SCHEDULEID
eboshi removeSchedule: error: argument --url is required
```
```
eboshi removeSchedule --url http://localhost:8081 --username azkaban --password azkaban --scheduleId 1
```

* exec azkaban job flow
```
$ eboshi exec
usage: eboshi exec [-h] --url URL --username USERNAME --password PASSWORD
                   --project PROJECT --flow FLOW
                   [--flowOverride [FLOWOVERRIDE [FLOWOVERRIDE ...]]]
                   [--disabled DISABLED] [--successEmails SUCCESSEMAILS]
                   [--failureEmails FAILUREEMAILS]
                   [--successEmailsOverride SUCCESSEMAILSOVERRIDE]
                   [--failureEmailsOverride FAILUREEMAILSOVERRIDE]
                   [--notifyFailureFirst NOTIFYFAILUREFIRST]
                   [--notifyFailureLast NOTIFYFAILURELAST]
                   [--failureAction FAILUREACTION]
                   [--concurrentOption CONCURRENTOPTION] [--returnExecid]
eboshi exec: error: argument --url is required
```
```
eboshi exec --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --flow azkaban_flow --flowOverride k1=v1 k2=v2 --disabled '["aaa","bbb"]'
```

* get schedule azkaban job
```
$ eboshi getSchedule
usage: eboshi getSchedule [-h] --url URL --username USERNAME --password
                          PASSWORD --project PROJECT --flow FLOW
eboshi getSchedule: error: argument --url is required
```
```
eboshi getSchedule --url http://localhost:8081 --username azkaban --password azkaban --project azkaban_project --flow azkaban_flow
```

* get most recent next exec time
```
$ eboshi getMostRecentNextExecTime
usage: eboshi getMostRecentNextExecTime [-h] --url URL --username USERNAME
                                        --password PASSWORD
eboshi getMostRecentNextExecTime: error: argument --url is required
```
```
eboshi getMostRecentNextExecTime --url http://localhost:8081 --username azkaban --password azkaban
```

* fetch flow azkaban job
```
$ eboshi fetchFlow
usage: eboshi fetchFlow [-h] --url URL --username USERNAME --password PASSWORD
                        --execid EXECID
eboshi fetchFlow: error: argument --url is required
```
```
eboshi fetchFlow --url http://localhost:8081 --username azkaban --password azkaban --execid 100
```
