from duplicate_finder import find_duplicates


def main():
    print("\n===== DUPLICATE FILE FINDER =====")
    folder_path = input("Enter folder path to scan: ").strip().strip('"')

    try:
        duplicate_groups = find_duplicates(folder_path)

        if not duplicate_groups:
            print("\nNo duplicate files found.")
            return

        print(f"\nFound {len(duplicate_groups)} duplicate group(s).\n")

        for number, group in enumerate(duplicate_groups, start=1):
            print(f"Group {number}:")
            for file_path in group:
                print(f"  {file_path}")
            print()

    except (ValueError, OSError) as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()