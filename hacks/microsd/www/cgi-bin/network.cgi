#!/bin/sh

echo "Content-type: text/html"
echo "Pragma: no-cache"
echo "Cache-Control: max-age=0, no-store, no-cache"
echo ""
source ./func.cgi
PATH="/bin:/sbin:/usr/bin:/usr/sbin"

cat << EOF
Information:
<pre>Interfaces:<br/>$(ifconfig; iwconfig)</pre>
<pre>Routes:<br/>$(route)</pre>
<pre>DNS:<br/>$(cat /etc/resolv.conf)</pre>
</body>
</html>
EOF


