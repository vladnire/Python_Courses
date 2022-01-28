""" log parser
    The file is a linux-like log file
    from a system you are debugging.  Mixed in among the various statements are
    messages indicating the state of the device.  They look like:
        Jul 11 16:11:51:490 [139681125603136] dut: Device State: ON
    The device state message has many possible values, but this program only
    cares about three: ON, OFF, and ERR.
    Your program will parse the given log file and print out a report giving
    how long the device was ON, and the time stamp of any ERR conditions.
"""
from dateutil import parser


def log_parser(log_file):
    log_list = []
    with open(log_file) as f:
        for line in f:
            if "dut: Device State: " in line:
                log_list.append(line)
    
    output = []
    errors_timestamps = []
    on_time = 0

    # from this "Jul 11 16:11:51:490 [139681125603136] dut: Revision : 64180"
    # to this "Jul 11 16:11:51"

    for e in log_list:
        if "ON" in e:
            start_time = parser.parse(e.split(" [")[0][:-4])
        elif 'OFF' in e:
            end_time = parser.parse(e.split(" [")[0][:-4])
            on_time += int((end_time - start_time).total_seconds())
        elif "ERR" in e:
            errors_timestamps.append(e.split(" [")[0])
    
    output.append(f"Device was on for {on_time} seconds")
    output.append("Timestamps of error events:")
    output.extend(errors_timestamps)

    return output


log_parser("test.log")