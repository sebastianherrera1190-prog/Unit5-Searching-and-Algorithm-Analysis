"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

POKEMON POKEDEX SEARCH SYSTEM

This program demonstrates linear search and binary search
using Pokemon Pokedex numbers.

The program compares both algorithms using small and large
datasets and demonstrates different edge cases.
"""


def linear_search(lst, target):
    """
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Linear search has O(n) time complexity because it
      may need to examine every element in the list.
    """

    for index in range(len(lst)):

        # Check each Pokemon Pokedex number individually.
        if lst[index] == target:
            return index

    # Return -1 if the Pokemon number does not exist.
    return -1


def binary_search(lst, target):
    """
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Binary search has O(log n) time complexity because
      each iteration eliminates approximately half of
      the remaining search area.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find the middle position of the search area.
        middle = (left + right) // 2

        if lst[middle] == target:
            return middle

        elif lst[middle] < target:

            # Target must be in the right half.
            # Eliminate the middle element and everything left.
            left = middle + 1

        else:

            # Target must be in the left half.
            # Eliminate the middle element and everything right.
            right = middle - 1

    # Return -1 if the target cannot be found.
    return -1


def main():

    print("========================================")
    print("      POKEMON POKEDEX SEARCH SYSTEM")
    print("========================================")

    # Pokemon dictionary containing Pokedex numbers
    # and their corresponding Pokemon names.

    pokemon_names = {
        1: "Bulbasaur",
        4: "Charmander",
        7: "Squirtle",
        25: "Pikachu",
        39: "Jigglypuff",
        52: "Meowth",
        133: "Eevee",
        143: "Snorlax",
        150: "Mewtwo",
        151: "Mew"
    }

    # ===============================
    # SMALL DATASET
    # ===============================
    #
    # Create a small sorted dataset containing 10 Pokemon.
    # Each number represents a National Pokedex ID.
    #
    # Both search algorithms will search for the same
    # Pokemon numbers so their results can be compared.

    print("\n=== SMALL DATASET TEST ===")

    small_dataset = sorted(pokemon_names.keys())

    print("\nPokemon Pokedex:")

    for number in small_dataset:
        print(f"#{number}: {pokemon_names[number]}")

    # Test a Pokemon that exists.

    target = 25

    linear_result = linear_search(small_dataset, target)
    binary_result = binary_search(small_dataset, target)

    print("\nSearching for Pokemon #25:")

    if linear_result != -1:
        print("Pokemon Found:", pokemon_names[target])
    else:
        print("Pokemon Not Found")

    print("Linear Search Index:", linear_result)
    print("Binary Search Index:", binary_result)

    # Both algorithms should find Pikachu at index 3.

    # Test a Pokemon that does not exist.

    target = 999

    linear_result = linear_search(small_dataset, target)
    binary_result = binary_search(small_dataset, target)

    print("\nSearching for Pokemon #999:")

    if linear_result == -1:
        print("Pokemon Not Found")

    print("Linear Search Index:", linear_result)
    print("Binary Search Index:", binary_result)

    # Both algorithms return -1 because Pokemon #999
    # does not exist in our small dataset.

    # ===============================
    # LARGE DATASET
    # ===============================
    #
    # Create a larger sorted dataset containing 1,000
    # numerical Pokemon records.
    #
    # This demonstrates how the algorithms perform
    # when searching through a much larger dataset.

    print("\n=== LARGE DATASET TEST ===")

    large_dataset = list(range(1, 1001))

    print("Total Pokemon Records:", len(large_dataset))

    target = 875

    # Measure the number of comparisons for linear search.

    linear_count = 0

    for number in large_dataset:

        linear_count += 1

        if number == target:
            break

    # Measure the number of comparisons for binary search.

    binary_count = 0

    left = 0
    right = len(large_dataset) - 1

    while left <= right:

        binary_count += 1

        middle = (left + right) // 2

        if large_dataset[middle] == target:
            break

        elif large_dataset[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    print("\nSearching for Pokemon #875:")

    print("Linear Search Comparisons:", linear_count)
    print("Binary Search Comparisons:", binary_count)

    # Linear search checks each number until it finds #875.
    # Binary search repeatedly eliminates half of the
    # remaining search area.
    #
    # Binary search only needs 3 comparisons in this example
    # because the target is found near the middle of the
    # search range after the first few divisions.

    print("\nWhy Binary Search Is More Efficient:")
    print("Binary search eliminates half of the remaining")
    print("search area with each iteration.")
    print("This makes it much faster when searching large")
    print("sorted datasets compared to linear search.")
    print("Linear search has O(n) time complexity.")
    print("Binary search has O(log n) time complexity.")

    # ===============================
    # EDGE CASES
    # ===============================
    #
    # Demonstrate different situations that can occur
    # when searching through a dataset.

    print("\n=== EDGE CASE TESTS ===")

    # EDGE CASE 1: Empty list.

    empty_dataset = []

    print("\n1. Empty Dataset:")

    print("Linear Search:", linear_search(empty_dataset, 25))
    print("Binary Search:", binary_search(empty_dataset, 25))

    # Both algorithms return -1 because there are no
    # Pokemon records available to search.

    # EDGE CASE 2: Single-element list.

    single_dataset = [25]

    print("\n2. Single Pokemon Dataset:")
    print("Dataset: [25 - Pikachu]")

    print("Searching for Pokemon #25:")

    print("Linear Search:", linear_search(single_dataset, 25))
    print("Binary Search:", binary_search(single_dataset, 25))

    # Both algorithms successfully find Pikachu at index 0.

    # EDGE CASE 3: Search for the first element.

    print("\n3. Searching for the First Pokemon (#1):")

    print("Pokemon:", pokemon_names[1])

    print("Linear Search:", linear_search(small_dataset, 1))
    print("Binary Search:", binary_search(small_dataset, 1))

    # Both algorithms find Bulbasaur at index 0.

    # EDGE CASE 4: Search for the last element.

    print("\n4. Searching for the Last Pokemon (#151):")

    print("Pokemon:", pokemon_names[151])

    print("Linear Search:", linear_search(small_dataset, 151))
    print("Binary Search:", binary_search(small_dataset, 151))

    # Both algorithms find Mew at index 9.

    # EDGE CASE 5: Search for a missing Pokemon.

    print("\n5. Searching for Missing Pokemon (#500):")

    print("Pokemon Not Found")

    print("Linear Search:", linear_search(small_dataset, 500))
    print("Binary Search:", binary_search(small_dataset, 500))

    # Both algorithms return -1 because Pokemon #500
    # is not included in our small dataset.

    # ===============================
    # FINAL SUMMARY
    # ===============================

    print("\n========================================")
    print("       SEARCH TESTING COMPLETED")
    print("========================================")

    print("\nFinal Comparison:")
    print("Linear Search: O(n)")
    print("Binary Search: O(log n)")
    print("\nBinary search is more efficient for large")
    print("sorted datasets because it reduces the")
    print("search area with every iteration.")


if __name__ == "__main__":
    main()
