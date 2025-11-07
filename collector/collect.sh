#!/bin/bash
OUTDIR="./collected/$(date +%Y%m%d_%H%M%S)"; mkdir -p $OUTDIR

# 1) docker events (container lifecycle)
docker events --since 0 > $OUTDIR/docker_events.log &
pid_events=$!

# 2) docker logs (for model_server container)
docker logs -f model_server > $OUTDIR/docker_logs_model_server.log &
pid_logs=$!

# 3) tcpdump (host network, filter by port 8080)
sudo tcpdump -i any -w $OUTDIR/tcpdump.pcap port 8080 &
pid_tcp=$!

# 4) optional: strace attach to container process (find PID then trace syscalls)
CID=$(docker ps -qf "name=model_server")
PID=$(docker inspect --format '{{.State.Pid}}' $CID)
sudo strace -f -tt -o $OUTDIR/strace_model_server.log -p $PID &
pid_strace=$!

echo "Collectors started. PIDs: $pid_events $pid_logs $pid_tcp $pid_strace"
echo "Press ENTER to stop..."
read
sudo kill $pid_tcp || true
kill $pid_logs $pid_events $pid_strace || true
echo "Stopped."