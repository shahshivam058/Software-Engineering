- process = process is nothing but program in execution which allocates memory space execution and system context  
- each process has unique id named pid or process id , Unique ID Assigned to each process for tracking and managment 
- TWO Process cant have same PID ,
- each process has different states within execution , 
- even pid of first process running is nothing but 1 as systemd or terminal already learning 
- knowing process state is important allows to help why its stuck not responding 
- running : when application is in running state means actively using cpu 
- sleeping : process waiting for event disk or network 
- stop : process is suspended and genrally stopped by used
- zombie : completed execution but not yet clean up , also defunct process 
    - Zombies themselves don’t consume CPU or memory, but many zombies can exhaust the process table, blocking new processes from being created.
    - For an SRE, this could mean:
    - Failed deployments (new worker processes can’t start)
    - Web/API downtime (because new connections can’t be served)
    - Alerts from monitoring systems


- each process start as child of another process , Each process has parent process bhaving tree like organiztion 
- first process which start in linux is nothing but init process or systemd in many os,
- all other process branch out from them and we call it process tree.

- pstree : shows process in tree mode from root process to child branching and all 

- ps : returning process which are running 
- ps aux :
- top : real time process  


- process managment is one of the critical aspect in Linux or any OS system admin directly impect :
    - System Perfomance : can be help us for system performance and optimized the same 
    - Security Posture : sometime marlware runs as process , identify unexpected process , consuming much network amd memory 
    - overall reliability : Server is healthy , Running fine , without any crash 

- When you are accessing each program in Linux even terminal it will create a new process 
- process control block :
    when a process is created an os creates a process control block to store all information about process
    - Ragister value 
    - Memory Allocation detail 
    - file discriptor
    - scheduling information 
    - Kernal creates a process control block for each process 

- process creation model :
    - fork : creates a new process by duplicating the parent process also known as child process . Resources and memory are different
    - exec : Replace child process memory image with new process , Child running different different PID 
    - Result : flexible process creation while maintaining security boundry 

- Process States :
    - Running : Process is executing IN CPU or waiting in queue for cpu time 
    - Sleeping , Interupttable : Waiting for CPU or event can be awaked by signal  
    - Sleeping , UNInterupttable : Process waiting for I/O can not be awakened by or inturrpted by signal , even if we kill wait for input 
    - Stopped : Suspended By Signal (SINGTERM , SINGKILL) , Remained in memory 
    - Zombie : Completed execution and waiting parenent to read exit status , Also known as ghost process 


excercise : 

Start Long Runnable process and Look at different steps 

- sleep 300 & : Creates A process which is in sleep state  & : Running In backgroud with any command we can do & in last 

- ps -p 3347 -o pid,stat,comm : Shows the status of Process with pid and also stat and command  -o means output 

- kill -STOP 3347 : Will Kill process with explicit PID 

- kill -CONT 3347 : Sends Continue signal for running process 


- ps -eo pid,ppid,comm,stat | grep 'z' : List out all process with PID , PPID , Command name and stat and filter out zombie process

- exit 0 : Process exited grecefully 

- ps aux : shows all process with detailed user orianted format 

- ps -ef : shows all process in formatted with parent child relation ship 

- ps -eo pid,ppid,comm,stat,%cpu,%mem,user : shows all process in formatted with parent child relation ship 

- ps -u username : display all process related to spasefic user , process spawned by spasefic user 

- ps --forest : shows the process hierarchy in tree format 



- ps aux | head 10 : list out first 10 process 

- ps aux | tail 10 : list out last 10 process

- stress-ng --cpu 2 --timeout 30s & : During the same it will take 100 percent of cpu
    - --cpu 2 : Uses 2 cpu worker 
    - Timeout within 30s 
    - & Running In Background 


- ps aux | grep 'stress' : to get pid of stress command 


- ps :
    
Column	Meaning
PID	Process ID – the unique identifier for the process.
PPID	Parent Process ID – the PID of the process that started this one.
UID	User ID number of the process owner.
USER	Username of the process owner.
EUID	Effective User ID (what the process runs as, may differ due to sudo/setuid).
RUID	Real User ID (actual user who started the process).
TTY	Terminal controlling the process (or ? if none).
STAT	Process status code(s):
- R = Running
- S = Sleeping
- D = Uninterruptible sleep (I/O wait)
- T = Stopped (job control)
- Z = Zombie
Plus modifiers like < (high priority), N (low priority/niced), L (locked in memory), s (session leader), + (foreground).
COMMAND / COMM	The command name (COMM is just the executable name; COMMAND shows the whole command line if available).
CMD	Like COMMAND, but often truncated.
ARGS	The command with all arguments (like COMMAND).
PRI	Priority of the process (kernel scheduling priority).
NI	Nice value (affects scheduling priority; range -20 [high priority] to +19 [low priority]).
VSZ	Virtual memory size (in KB).
RSS	Resident Set Size – actual physical memory used (in KB).
%MEM	Percentage of system memory the process uses.
%CPU	Percentage of CPU usage.
TIME	Total CPU time the process has consumed.
ELAPSED	Time since the process started.
START	When the process started (date/time or time of day).
C	CPU utilization (in terms of scheduling).
WCHAN	What kernel function the process is waiting in (if sleeping).




Real Life scenario :


Get process overview :

- ps aux --sort=-%cpu | head -10 : List out 10 process with higher cpu consumpsion 
- ps aux --sort=-%mem | head -10 : List out 10 process with higher memory consumpsion 

- ps -u $USER -o pid,ppid,cmd,%cpu,%mem,etime


-  ps --forest -eo  pid,ppid,cmd : list out all process in tree hierarchy format 





TOP Command :

- ps : Nothing but snapshot of process state 

In devsecops required real time situation :

- Top : This command gives us continous update about linux system performance 
- top is an interactive command-line utility in Linux/Unix that provides a dynamic, real-time view of system processes.
- It helps diagnose CPU, memory, and process usage — essential for debugging performance issues in production.

It may help us monitoring :

- System Process 
- CPU Usage 
- Memory Consumpsion 
- System Load average 
As an SRE, you’re often on-call to troubleshoot:

- High CPU usage alerts
- Memory leaks or OOM (Out Of Memory) kills
- Hung or resource-starved applications
- Investigating load before scaling decisions
- top gives a fast, low-overhead snapshot of what’s happening on the server right now.

- ps = provides you static snapshot 
- top = constantly refreshing 
- lscpu : returns system spasefication have all information about cors 
- nproc = returns no of cpu cores 

- process dashboard update every few secounds show real time cpu and memory usage by process
- Load Avarage Represent number of process waiting for cpu 
- cpu valueable resource for us 
- if it > core count means system overloaded 


- Load Average: (1 min, 5 min, 15 min).
    - As an SRE, compare it with number of CPU cores.
    - If load avg > #cores consistently → system is overloaded.
- Tasks: Running vs sleeping processes → too many running tasks = CPU contention.
- System load ≠ CPU usage. It means number of processes waiting for CPU or I/O.
- Compare it to # of CPU cores:
- If you have 4 cores and load avg = 1.12 → system is fine (25–30% busy).
- If load avg consistently > cores → CPU or I/O contention.


- if system is using swap then system is under the memory load . if system using swap then system will slowdown 
- hard disk not faster as cpu 
- if system using slow memory its obvious it will be slowdown 


Example:
Tasks: 231 total,   1 running, 230 sleeping,   0 stopped,   0 zombie

Interpretation:
- 231 total processes exist on the system.
- 1 process is actively running or waiting to run on a CPU.
- 230 processes are sleeping (waiting for events like I/O or network).
- 0 processes are stopped by signals.
- 0 processes are zombies waiting to be reaped.

----------------------------------------------------

Process States Explained

1. Running
What it is:
Processes currently executing on a CPU or waiting in the run queue (ready to run but waiting for a CPU core).

SRE Perspective:
- Healthy: running ≤ number_of_cores.
- If running > number_of_cores consistently → system is CPU-bound.
- During incidents, a spike in running tasks means CPU-heavy operations are happening (e.g., bad query, runaway thread).

----------------------------------------------------

2. Sleeping
What it is:
Processes waiting for an event (I/O, network, timers). This is the most common state.

SRE Perspective:
- High sleeping count is normal (web servers, daemons, cron jobs often sleep).
- Key detail: what they are sleeping on.
  top doesn’t show this directly.
  Use tools like pidstat, strace, or perf for deeper inspection.

----------------------------------------------------

3. Stopped
What it is:
Processes paused by signals (e.g., SIGSTOP) or by pressing Ctrl+Z in a shell.

SRE Perspective:
- Rare in production.
- Common causes:
  - Admin debugging a process.
  - Process trapped in a debugger.
- Requires manual intervention: either resume (SIGCONT) or terminate.

----------------------------------------------------

4. Zombie
What it is:
Processes that have finished execution but remain in the process table because their parent has not reaped their exit status.

SRE Perspective:
- A few zombies (<5) are harmless (they take negligible resources).
- A growing zombie count = bug in parent process (not calling wait()).
- Risks: Exhaustion of process IDs (PIDs), preventing new processes.

Action Items:
1. Identify parent process (ps -o ppid= -p <zombie_pid>).
2. Restart or fix the parent.
3. Killing the zombie itself won’t work — it’s already dead.

----------------------------------------------------

Quick SRE Checklist for Tasks
- Running > cores? → CPU-bound.
- Many sleepers? → Normal; investigate only if latency or blocking observed.
- Stopped? → Likely admin/debugger; verify.
- Zombies increasing? → Bug in parent process, restart/patch required.




- us → % CPU in user space (apps, services). High → app code is CPU-intensive.
- sy → % CPU in system/kernel space (syscalls, interrupts). High → kernel overhead, maybe networking or filesystem.
- ni → % CPU for processes with nice priority (rarely critical).
- id → % CPU idle (free).
- wa → % CPU waiting on I/O (disk/network). High → I/O bottleneck.
- hi → % CPU handling hardware interrupts. High → bad drivers or hardware storm.
- si → % CPU handling software interrupts (network packets, softirqs). High → heavy network load.
- st → % CPU stolen by hypervisor (VMs only). High → noisy neighbor in shared environment.

- us (user) & sy (system): High us means the application itself is busy (e.g., running business logic). High sy can mean the OS is busy with system calls (e.g., context switching, network handling). A very high sy might indicate a kernel-level issue.

- wa (I/O wait): This is a critical metric. A high wa (e.g., > 10%) means the CPUs are idle, waiting for disk or network I/O. This immediately points the investigation towards storage performance (disk latency) or network issues. The system isn't CPU-bound; it's I/O-bound.

- st (steal time): Crucial in virtualized/cloud environments. This is time the hypervisor took away from this VM to service other VMs. A consistently high st means you have a "noisy neighbor" and your underlying host is oversubscribed. This is a common cause of mysterious performance degradation in the cloud.



- The I/O Bottleneck

    - Observation: load average is high, but running tasks is low. %wa (I/O wait) in the CPU line is high.
    - Hidden Clue: Many of the sleeping processes are actually in D state (Uninterruptible Sleep). You can see this in the process list (S column).
    - Diagnosis: The system is waiting on slow disk or network I/O. Processes are blocked, unable to do work.

----------------------------------------------------

- The Zombie Apocalypse
    - Observation: zombie count is 25 and slowly increasing. New service instances fail to start, reporting "no more processes."
    - Diagnosis: A buggy application is forking child processes but not waiting for them to exit properly.
    - Action: Use ps aux | grep 'Z' to find zombie processes and their parent PIDs. Restart the faulty parent service. Escalate to developers with the evidence.

----------------------------------------------------

- The CPU Saturation
    - Observation: running tasks is consistently 8 on a 4-core system. Load average is >4. User CPU (%us) is very high.
    - Diagnosis: The system has more work than it can handle. Requests are queuing, leading to high latency.
    - Action: Scale up (more CPU) or scale out (more instances). Optimize the CPU-heavy application code.
"""




👉 SRE Interpretation:

- High us → app CPU-bound → profile or scale horizontally.
- High sy → system/kernel issue → maybe syscalls, packet floods.
- High wa → storage or DB slowness.
- High st in cloud → open a ticket with provider (oversubscribed VM).



The Anatomy of Linux Memory

MiB Mem :  15927.4 total,    512.8 free,   8192.6 used,   7221.9 buff/cache
MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.  14829.4 avail Mem

SRE Interpretation:
- I have ~16GB of RAM.
- Only 512MB is completely idle.
- 8GB is actively used by applications.
- 7GB is being used by the kernel for caching (to make things faster).
- I have 2GB of swap, but it is unused.
- Crucially, about 14.5GB of memory is available for new applications without causing problems.

------------------------------------------------------
1. total
- What it is: Physical RAM installed.
- SRE Perspective: Establishes the baseline. Is this system appropriately sized for its workload?
  - Example: A database needing 64GB but running on 8GB is a fundamental problem.

------------------------------------------------------
2. free (The Misleading Metric)
- What it is: Memory that is completely unused and not serving any purpose.
- SRE Perspective: A low free memory is NORMAL and GOOD on Linux.
  - The kernel uses free memory for caches to speed up the system.
  - If you have a lot of free memory, you may have over-provisioned hardware.
  - Do not panic about low free memory.

------------------------------------------------------
3. used
- What it is: Memory currently allocated to applications and the kernel.
- SRE Perspective: This includes buff/cache. A high "used" number alone does not indicate a problem.

------------------------------------------------------
4. buff/cache (The Performance Booster)
- What it is: Memory used by the kernel for disk caching (cache) and buffer I/O (buff).
- SRE Perspective: This is reclaimable memory. If applications need more RAM, the kernel can free it instantly.
  - High buff/cache typically means:
    - The system is doing a lot of disk I/O (good for a database or file server).
    - The system has been running for a while and optimized itself.

------------------------------------------------------
5. avail Mem (The Most Important Metric)
- What it is: An estimate of how much memory is available for starting new applications without forcing the system to swap.
- SRE Perspective: This is the number you should watch. Calculated as: free + most of the buff/cache.
  - Green Zone: avail Mem > 20% of total RAM → System is healthy.
  - Yellow Zone: avail Mem < 10% of total RAM → Monitor closely (system under memory pressure).
  - Red Zone: avail Mem very low AND Swap is being used → Critical situation.

------------------------------------------------------
6. Swap (The Emergency Valve)
- What it is: Disk space used as "overflow" RAM.
- SRE Perspective: Swap is a safety net but extremely slow compared to RAM.
  - used > 0 → RAM is exhausted, paging to disk has begun (indicator of memory pressure).
  - High si/so (swap in/out) → System is thrashing (moving data between RAM and swap instead of doing useful work). This kills performance.


------------------------------------------------------
The "Memory Leak" Incident
- Observation: avail Mem is steadily decreasing over hours/days. used is going up, but buff/cache is stable or shrinking. Eventually, Swap used starts increasing.
- Diagnosis: An application is allocating memory and not releasing it.
- Action: 
  - Use top's process list, sort by %MEM (press M).
  - Find the process whose RES (resident memory) is constantly growing.
  - Restart that service and file a bug with the development team.

------------------------------------------------------
The "Noisy Neighbor" Problem
- Observation: avail Mem is low on one VM, but the main application doesn't seem to be using that much memory (RES).
- Diagnosis: Another process on the same machine (maybe another tenant in a multi-tenant system) is consuming RAM.
- Action:
  - In top, look at the RES column for all processes to find the memory hog.




- top -u username : List out all process created by user 
- top -d secounds : at what process should refreshed . now its refreshed every 3 secounds  keep it more we want to see long term process patterns 
- top -p pid : monitor spasefic process 
- top -b -n1 : Batch mode for single snapshot , Interactive control gose away . Snapshot of particular minutes 

- Interactive commands :

- M, P , T : Sort all the process sorted by CPU Usage memory usage and running time 
- k : kill the process prompt for pid 
- q : quit
- 1 : Shows Core wise cpu and memory usage 
- r : renice the process change the priority 
- f : add or remove column 
- W : write configration to top command c file 