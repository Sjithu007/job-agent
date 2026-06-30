from models import Job


def search_jobs():
    jobs = [
        Job(
            title="DevOps Engineer",
            company="IBM",
            location="Kochi",
            url="https://example.com/1"
        ),
        Job(
            title="Platform Engineer",
            company="UST",
            location="Kochi",
            url="https://example.com/2"
        ),
        Job(
            title="Cloud Engineer",
            company="TCS",
            location="Bangalore",
            url="https://example.com/3"
        ),
    ]

    return jobs