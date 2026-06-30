from search.greenhouse import GreenhouseProvider


class JobAggregator:

    def __init__(self):
        self.providers = [
            GreenhouseProvider()
        ]

    def fetch_all_jobs(self):
        jobs = []
        for provider in self.providers:
            jobs.extend(provider.fetch_jobs())
        return jobs