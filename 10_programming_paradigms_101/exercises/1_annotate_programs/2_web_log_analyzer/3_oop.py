#!/usr/bin/env python3


class WebLogAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.log_entries = []
        self.error_count = 0
        self.traffic_by_endpoint = {}
        self.response_time_totals = {}

    def parse_log_entries(self):
        with open(self.filename, "r") as log_file:
            for line in log_file:
                parts = line.strip().split("|")
                if len(parts) == 4:
                    timestamp, endpoint, status_code, response_time = parts
                    entry = {
                        "timestamp": timestamp,
                        "endpoint": endpoint,
                        "status_code": status_code,
                        "response_time": float(response_time),
                    }
                    self.log_entries.append(entry)

    def count_server_errors(self):
        self.error_count = sum(
            1 for entry in self.log_entries if entry["status_code"].startswith("5")
        )

    def analyze_traffic(self):
        for entry in self.log_entries:
            endpoint = entry["endpoint"]
            self.traffic_by_endpoint[endpoint] = (
                self.traffic_by_endpoint.get(endpoint, 0) + 1
            )

    def calculate_response_times(self):
        for entry in self.log_entries:
            endpoint = entry["endpoint"]
            response_time = entry["response_time"]

            if endpoint not in self.response_time_totals:
                self.response_time_totals[endpoint] = {
                    "total_time": response_time,
                    "count": 1,
                }
            else:
                self.response_time_totals[endpoint]["total_time"] += response_time
                self.response_time_totals[endpoint]["count"] += 1

    def print_analysis(self):
        print("\nLog Analysis Summary:")
        print(f"Total Log Entries: {len(self.log_entries)}")
        print(f"Total Server Errors: {self.error_count}")

        print("\nTraffic by Endpoint:")
        for endpoint, count in sorted(
            self.traffic_by_endpoint.items(), key=lambda x: x[1], reverse=True
        ):
            print(f"{endpoint}: {count} requests")

        print("\nAverage Response Times:")
        for endpoint, data in self.response_time_totals.items():
            avg_response_time = data["total_time"] / data["count"]
            print(f"{endpoint}: {avg_response_time:.2f} ms")

    def analyze(self):
        print("\nSimple Web Log Analyzer\n")

        self.parse_log_entries()
        self.count_server_errors()
        self.analyze_traffic()
        self.calculate_response_times()
        self.print_analysis()


# Usage
log_analyzer = WebLogAnalyzer("server.log")
log_analyzer.analyze()
