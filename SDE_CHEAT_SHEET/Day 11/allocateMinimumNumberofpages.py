
def allocate_minimum_number_of_pages(books, k):

    def is_possible_to_allocate(barrier):
        allocated_students, pages = 1, 0
        for book in books:
            if pages + book > barrier:
                allocated_students += 1
                pages = book
            else:
                pages += book

        if allocated_students > k:
            return False

        return True

    low, high = max(books), sum(books)
    ans = -1
    while low <= high:
        mid = low + (high - low) // 2

        if is_possible_to_allocate(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


print(allocate_minimum_number_of_pages([12, 34, 67, 90], 2))
