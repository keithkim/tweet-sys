#!/bin/sh
# kFreeBSD do not accept scripts as interpreters, using #!/bin/sh and sourcing.
if [ true != "$INIT_D_SCRIPT_SOURCED" ] ; then
    set "$0" "$@"; INIT_D_SCRIPT_SOURCED=true . /lib/init/init-d-script
fi
### BEGIN INIT INFO
# Provides:          tweet-sys
# Required-Start:    $network $syslog
# Required-Stop:     $network $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Log START, SHUTDOWN to syslog and twitter
### END INIT INFO

# Author: Keith kim <keithkim@gmail.com>

case "$1" in
    start)
        /opt/tweet-sys/tweet-sys.py start
        ;;
    stop)
        /opt/tweet-sys/tweet-sys.py shutdown
        ;;
esac

exit 0
