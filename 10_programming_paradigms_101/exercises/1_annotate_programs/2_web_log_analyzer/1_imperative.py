#!/usr/bin/env python3

print("\nSimple Web Log Analyzer\n")

log_entries = []
error_count = 0
traffic_by_endpoint = {}
response_time_totals = {}

with open("server.log", "r") as log_file:
    for line in log_file:
        parts = line.strip().split("|")
        if len(parts) == 4:
            timestamp, endpoint, status_code, response_time = parts

            log_entries.append(
                {
                    "timestamp": timestamp,
                    "endpoint": endpoint,
                    "status_code": status_code,
                    "response_time": float(response_time),
                }
            )

            if status_code.startswith("5"):
                error_count += 1

            traffic_by_endpoint[endpoint] = traffic_by_endpoint.get(endpoint, 0) + 1

            if endpoint not in response_time_totals:
                response_time_totals[endpoint] = {
                    "total_time": float(response_time),
                    "count": 1,
                }
            else:
                response_time_totals[endpoint]["total_time"] += float(response_time)
                response_time_totals[endpoint]["count"] += 1

print("\nLog Analysis Summary:")
print(f"Total Log Entries: {len(log_entries)}")
print(f"Total Server Errors: {error_count}")
print("\nTraffic by Endpoint:")
for endpoint, count in sorted(
    traffic_by_endpoint.items(), key=lambda x: x[1], reverse=True
):
    print(f"{endpoint}: {count} requests")

print("\nAverage Response Times:")
for endpoint, data in response_time_totals.items():
    avg_response_time = data["total_time"] / data["count"]
    print(f"{endpoint}: {avg_response_time:.2f} ms")
