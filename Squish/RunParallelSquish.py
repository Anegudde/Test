import codecs
import datetime
import os
import os.path
import subprocess
import sys
import time
 
def print_usage():
    print "USAGE:"
    print
    print "  " + sys.argv[0] + " <runner_count> <server_count> <first_server_port> [<squishrunner_arguments>"
    print
    print "Output is written to..."
    print
    print "  squishserver_<timestamp>-#n.txt"
    print "  squishrunner_<timestamp>-#n.txt"
    print
    print "...respectively, where n is the number of the instance."
    print
 
def exec_async( command, output_filename=None ):
    stdout = subprocess.PIPE
    if output_filename is not None:
        stdout = file( output_filename, "wb" )
 
    p = subprocess.Popen( 
        args=command,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=stdout,
        stderr=subprocess.STDOUT )
    return p
 
def main():
    argv = sys.argv[1:]
 
    if len( argv ) < 5:
        print_usage()
        sys.exit( 1 )
 
    start_time = datetime.datetime.now()
 
    timestamp = datetime.datetime.strftime( datetime.datetime.now(), "%Y%m%d-%H%M%S" )
 
    squishrunner_count = int( argv[0] )
    argv = argv[1:]
 
    squishserver_count = int( argv[0] )
    argv = argv[1:]
 
    squishserver_first_port = int( argv[0] )
    argv = argv[1:]
 
    squishserver_cmd = os.path.join( "bin", "squishserver.exe" )
    if not os.path.exists( squishserver_cmd ):
        print "ERROR: squishserver not found:", squishserver_cmd
        sys.exit( 1 )
 
    squishservers_ports = start_squishservers( squishserver_cmd, squishserver_count, timestamp, squishserver_first_port )
 
    squishrunner_args = " ".join( argv )
    squishrunners = start_squishrunners( 
        squishserver_first_port,
        squishserver_count,
        squishrunner_args,
        squishrunner_count,
        timestamp )
 
    wait_for_squishrunners( squishrunners )
 
    stop_squishservers( squishserver_cmd, squishservers_ports )
 
    td = datetime.datetime.now() - start_time
    time_required = td.microseconds / 1000000.0 + td.seconds + td.days * 24.0 * 3600.0
    print "Time required:", time_required, "seconds"
 
def start_squishservers( squishserver_cmd, squishserver_count, timestamp, squishserver_first_port ):
    squishserver_output_filename_part = "squishserver_" + timestamp
    port = squishserver_first_port
    squishservers_port = []
    for i in range( squishserver_count ):
        i += 1
        print "\rStarting squishserver #" + str( i ),
        fn = squishserver_output_filename_part + "-#" + str( i ) + ".txt"
 
        proc = exec_async( squishserver_cmd + " --verbose --port " + str( port ), fn )
        squishservers_port.append( ( proc, port ) )
 
        port += 1
    print
    return squishservers_port
 
def stop_squishservers( squishserver_cmd, squishservers_ports ):
    i = 0
    for proc, port in squishservers_ports:
        i += 1
        print "\r" + "Waiting for squishserver on port " + str( port ) + " #" + str( i ) + "..." + 10 * " ",
        p = exec_async( squishserver_cmd + " --stop --port " + str( port ) )
        p.wait()
        if proc is not None:
            proc.wait()
        print "\r" + "Waiting for squishserver on port " + str( port ) + " #" + str( i ) + "...done",
    print
 
def wait_for_squishrunners( squishrunners ):
    for i, proc in enumerate( squishrunners ):
        i += 1
        print "\r" + "Waiting for squishrunner #" + str( i ) + "..." + 10 * " ",
        if proc is not None:
            proc.wait()
        print "\r" + "Waiting for squishrunner #" + str( i ) + "...done",
    print
 
def start_squishrunners( squishserver_first_port, squishserver_count, squishrunner_args, squishrunner_count, timestamp ):
    squishrunner_output_filename_part = "squishrunner_" + timestamp
    squishrunner_cmd = os.path.join( "bin", "squishrunner" )
    squishrunners = []
 
    port = squishserver_first_port
    port_max = squishserver_first_port + squishserver_count - 1
    for i in range( squishrunner_count ):
        i += 1
        print "\rStarting squishrunner on port " + str( port ) + " #" + str( i ),
        fn = squishrunner_output_filename_part + "-#" + str( i ) + ".txt"
        cmd = squishrunner_cmd + " --port " + str( port ) + " " + squishrunner_args
        proc = exec_async( cmd, fn )
        squishrunners.append( proc )
 
        port += 1
        if port > port_max:
            port = squishserver_first_port
        time.sleep( 1 )
    print
    return squishrunners
 
if __name__ == "__main__":
    main()