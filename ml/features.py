import json, datetime
def parse_docker_logs(path):
    # very naive example: count lines with certain keywords per window
    with open(path) as f:
        for line in f:
            yield line

def build_windows(logfiles, window_seconds=5, out="windows.jsonl"):
    # read combined timestamps from logs, bucket into windows, compute features
    # feature examples: request_count, avg_latency, suspicious_keyword_count, syscalls_per_window
    # For brevity, implement simple counting of suspicious substrings.
    pass