from search import search_jobs

def main():
    print("=" * 50)
    print("AI Job Agent")
    print("=" * 50)

    jobs = search_jobs()

    for job in jobs:
        print()
        print("-" * 40)
        print(f"Company : {job.company}")
        print(f"Role    : {job.title}")
        print(f"Location: {job.location}")
        print(f"URL     : {job.url}")

    print()
    print(f"Total jobs found: {len(jobs)}")


if __name__ == "__main__":
    main()