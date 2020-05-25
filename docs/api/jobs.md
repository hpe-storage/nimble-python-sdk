
# nimbleclient.v1.api.jobs


## Job
```python
Job(self, id, attrs=None, client=None, collection=None)
```
Jobs are operations in progress in the system.

__Parameters__

- __completion_time           __: Completion time of the job.
- __creation_time             __: Time when this job was created.
- __current_phase             __: Phase number of the job in progress.
- __current_phase_description __: Description of the current phase of the job.
- __description               __: Description of the job.
- __id                        __: Identifier for job.
- __name                      __: Name of the job.
- __last_modified             __: Time of the last update from the job.
- __object_id                 __: Identifier for object being acted upon.
- __op_type                   __: Type of operation.
- __type                      __: Job type.
- __parent_job_id             __: Identifier of parent job.
- __percent_complete          __: Progress of the job as a percentage.
- __request                   __: Original request that the job is responsible for.
- __response                  __: Response from the operation as the job executes.
- __state                     __: Status of the job.
- __result                    __: Result of the job.
- __total_phases              __: Total number of phases of the job.


## JobList
```python
JobList(self, client=None)
```

