# Resource usage

## Resource Requests

All of our containers include predefined resource request values. By default we
have not put resource limits into place. But we recommend users set limits, particularly
on memory if they are running on nodes without a lot of excess memory capacity.
(You want to avoid running out of memory on any of your Kubernetes nodes, as the
Kernel memory killer may end essential Kube processes)

In order to come up with our default request values, we run the application, and
come up with a way to generate various levels of load for each service. We monitor the
service, and make a call on what we think is the best default value.

We will measure:

- **Idle Load** - No default should be below these values, but an idle process
isn't useful, so typically we will not set a default based on this value.

- **Minimal Load** - The values required to do the most basic useful amount of work.
Typically, for cpu, this will be used as the default, but memory requests come with
the risk of the Kernel reaping processes, so we will avoid using this as a memory default.

- **Average Loads** - What is considered *average* is highly dependant on the installation,
for our defaults we will attempt to take a few measurements at a few of what we
consider reasonable loads. (we will list the loads used). If the service has a pod
autoscaler, we will typically try to set the scaling target value based on these.
And also the default memory requests.

- **Stressful Task** - Measure the usage of the most stressful task the service
should perform. (Not necessary under load). When applying resource limits, try and
set the limit above this and the average load values.

- **Heavy Load** - Try and come up with a stress test for the service, then measure
the resource usage required to do it. We currently don't use these  values for any
defaults, but users will likely want to set resource limits somewhere between the
average loads/stress task and this value.

### Unicorn

Load was tested using https://gitlab.com/andrewn/gitlab-load-kit each test over
a period of 5 minutes, on the first 100 urls crawlable by the root user. Values
are per pod.

- **Idle values**
  * 0 concurrent user, 2 pods
  - cpu: 0
  - memory: 850M


- **Minimal Load**
  * 1 concurrent user, 2 pods
    - cpu: 300m
    - memory: 1.2G


- **Average Loads**
   * 5 concurrent users, 3 pods
     - cpu: 1
     - memory: 1.2G
   * 20 concurrent users, 3 pods
     - cpu: 1.4
     - memory: 1.2G


- **Stressful Task**
  * Loading large MR diff (gitlab-ce master to 10-0-stable)
    - cpu: 400m
    - memory: 1.4G


- **Heavy Load**
  * 100 concurrent users, 5 pods
    - cpu: 1.5
    - memory: 1.2G


- **Default Requests**
  * cpu: 300m (from minimal load)
  * memory: 1.2G (from average loads)
  * target cpu average: 1 (from average loads)


- **Recommended Limits**
  * cpu: > 1.4 (greater than average load)
  * memory: > 1.4G (greater than stress task)


### Sidekiq

- **Idle values**
  * 0 tasks, 1 pods
    - cpu: 0
    - memory: 450M


- **Minimal Load**
  * ~20 tasks (create pipeline), 1 pods
    - cpu: 50m
    - memory: 550M


- **Average Loads**
   * x concurrent users, x pods
     - cpu: x
     - memory: x
   * x concurrent users, x pods
     - cpu: x
     - memory: x


- **Stressful Task**
  * x
    - cpu: x
    - memory: x


- **Heavy Load**
  * x concurrent users, x pods
    - cpu: x
    - memory: x


- **Default Requests**
  * cpu: x (from minimal load)
  * memory: x (from average loads)
  * target cpu average: x (from average loads)


- **Recommended Limits**
  * cpu: > x (greater than average load)
  * memory: > x (greater than stress task)
