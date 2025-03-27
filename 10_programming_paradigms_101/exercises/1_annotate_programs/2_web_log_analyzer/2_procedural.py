#!/usr/bin/env python3


def parse_log_entries(filename):
    log_entries = []
    with open(filename, "r") as log_file:
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
    return log_entries


def count_server_errors(log_entries):
    return sum(1 for entry in log_entries if entry["status_code"].startswith("5"))


def analyze_traffic(log_entries):
    traffic_by_endpoint = {}
    for entry in log_entries:
        endpoint = entry["endpoint"]
        traffic_by_endpoint[endpoint] = traffic_by_endpoint.get(endpoint, 0) + 1
    return traffic_by_endpoint


def calculate_response_times(log_entries):
    response_time_totals = {}
    for entry in log_entries:
        endpoint = entry["endpoint"]
        response_time = entry["response_time"]

        if endpoint not in response_time_totals:
            response_time_totals[endpoint] = {"total_time": response_time, "count": 1}
        else:
            response_time_totals[endpoint]["total_time"] += response_time
            response_time_totals[endpoint]["count"] += 1

    return response_time_totals


def print_analysis(log_entries, error_count, traffic, response_times):
    print("\nLog Analysis Summary:")
    print(f"Total Log Entries: {len(log_entries)}")
    print(f"Total Server Errors: {error_count}")

    print("\nTraffic by Endpoint:")
    for endpoint, count in sorted(traffic.items(), key=lambda x: x[1], reverse=True):
        print(f"{endpoint}: {count} requests")

    print("\nAverage Response Times:")
    for endpoint, data in response_times.items():
        avg_response_time = data["total_time"] / data["count"]
        print(f"{endpoint}: {avg_response_time:.2f} ms")


def main():
    print("\nSimple Web Log Analyzer\n")

    log_entries = parse_log_entries("server.log")
    error_count = count_server_errors(log_entries)
    traffic_by_endpoint = analyze_traffic(log_entries)
    response_time_totals = calculate_response_times(log_entries)

    print_analysis(log_entries, error_count, traffic_by_endpoint, response_time_totals)


main()
