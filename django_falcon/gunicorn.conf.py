import multiprocessing

workers = 2 * multiprocessing.cpu_count() * 1
forwarded_allow_ips = '*'
log_level = 'debug'
proc_name = 'django'
timeout = 600
max_requests = 100
graceful_timeout = 30

accesslog = '-'
