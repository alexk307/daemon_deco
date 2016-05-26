# daemon_deco
Daemonize your Python scripts with a decorator

# Example

```python
@daemonize(log_file='customlog.log')
def daemon_test():
    for i in range(10):
        print 'hello from daemon'
```

Creates a logfile named `customlog.log`, redirects all output from `print` to your logfile, and runs it in it's separate process.
