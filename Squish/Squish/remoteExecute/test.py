import os
 
def main():
    stdout, exit_code = os_capture("mycommand")
    test.compare(exit_code, 0, "Expected exit code: 0")
    test.verify(stdout.find("some expected substring") != -1, "Expected to find: 'some expected substring'")
 
def os_capture(args, cwd=None):
    if cwd is None:
        cwd = os.getcwd()
    proc = subprocess.Popen(
        args=args,
        cwd=cwd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT)
    stdout = proc.communicate()[0]
  
    return stdout, proc.returncode

	