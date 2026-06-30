from models import Job
from search.base import JobProvider


class GreenhouseProvider(JobProvider):

    def fetch_jobs(self):

        jobs = [
            Job(
                title="Senior DevOps Engineer",
                company="Demo Company",
                location="Kochi",
                url="https://example.com"
            )
        ]

        return jobs