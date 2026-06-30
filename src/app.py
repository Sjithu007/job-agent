from ai import ask_ai


def main():

    print("=" * 40)
    print("CareerPilot AI")
    print("=" * 40)

    print("\nTesting AI...\n")

    answer = ask_ai("Introduce yourself in one sentence.")

    print(answer)


if __name__ == "__main__":
    main()