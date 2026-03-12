# Global list to store contacts
contacts = []

# ===== TIME COMPLEXITY ANALYSIS =====
# add_contact()     : O(n)   - Linear search for duplicates
# remove_contact()  : O(n)   - Linear search to find contact
# edit_contact()    : O(n)   - Linear search to find contact
# linear_search()   : O(n)   - Must check every contact
# binary_search()   : O(log n) - Only works on sorted list by phone
# bubble_sort()     : O(n²)  - Two nested loops
# merge_sort()      : O(n log n) - Divide and conquer
# quick_sort()      : O(n log n) avg, O(n²) worst case
# load_from_file()  : O(n)   - Read n contacts from file
# save_to_file()    : O(n)   - Write n contacts to file

def add_contact(name, phone, silent=False):
    """Add a new contact. Time Complexity: O(n)"""
    if not name or not phone:
        if not silent:
            print("Error: Name and phone cannot be empty.")
        return False
    
    name = name.strip()
    phone = phone.strip()
    
    # Linear Search for duplicates - O(n)
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            if not silent:
                print(f"Error: Contact '{name}' already exists.")
            return False
    
    contacts.append({'name': name, 'phone': phone})
    if not silent:
        print(f"Contact '{name}' added successfully.")
    return True

def remove_contact(name):
    """Remove a contact by name. Time Complexity: O(n)"""
    name = name.strip()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name.lower():
            contacts.pop(i)
            print(f"Contact '{name}' removed successfully.")
            return True
    print(f"Contact '{name}' not found.")
    return False

def edit_contact(name, new_phone):
    """Edit a contact's phone number. Time Complexity: O(n)"""
    name = name.strip()
    new_phone = new_phone.strip()
    for contact in contacts:
        if contact['name'].lower() == name.lower():
            contact['phone'] = new_phone
            print(f"Contact '{name}' updated successfully.")
            return True
    print(f"Contact '{name}' not found.")
    return False

def linear_search(search_name):
    """Linear search for contacts by name. Time Complexity: O(n)"""
    search_name = search_name.lower()
    results = []
    for contact in contacts:
        if search_name in contact['name'].lower():
            results.append(contact)
    return results

def binary_search(phone):
    """Binary search for contact by phone. Time Complexity: O(log n)
    Note: Requires contacts to be sorted by phone number."""
    left, right = 0, len(contacts) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_phone = contacts[mid]['phone']
        
        if mid_phone == phone:
            return contacts[mid]
        elif mid_phone < phone:
            left = mid + 1
        else:
            right = mid - 1
    
    return None

def insert_bst_node(root, contact):
    """Insert contact into Binary Search Tree using dictionary. Time Complexity: O(log n) avg"""
    if root is None:
        return {'contact': contact, 'left': None, 'right': None}
    
    if contact['name'].lower() < root['contact']['name'].lower():
        root['left'] = insert_bst_node(root['left'], contact)
    else:
        root['right'] = insert_bst_node(root['right'], contact)
    
    return root

def search_bst_node(root, name):
    """Search in Binary Search Tree using dictionary. Time Complexity: O(log n) avg, O(n) worst"""
    if root is None:
        return None
    
    if root['contact']['name'].lower() == name.lower():
        return root['contact']
    elif name.lower() < root['contact']['name'].lower():
        return search_bst_node(root['left'], name)
    else:
        return search_bst_node(root['right'], name)

def quick_sort():
    """Sort contacts by name using quick sort. Time Complexity: O(n log n) avg, O(n²) worst"""
    if len(contacts) <= 1:
        return
    
    def partition(arr, low, high):
        pivot = arr[high]['name'].lower()
        i = low - 1
        
        for j in range(low, high):
            if arr[j]['name'].lower() < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    def quick_sort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi - 1)
            quick_sort_helper(arr, pi + 1, high)
    
    quick_sort_helper(contacts, 0, len(contacts) - 1)
    print("Contacts sorted by name (Quick Sort).")

def merge_sort():
    """Sort contacts by name using merge sort. Time Complexity: O(n log n)"""
    if len(contacts) <= 1:
        return
    
    def merge(arr, left, mid, right):
        left_part = arr[left:mid + 1]
        right_part = arr[mid + 1:right + 1]
        i = j = 0
        k = left
        
        while i < len(left_part) and j < len(right_part):
            if left_part[i]['name'].lower() <= right_part[j]['name'].lower():
                arr[k] = left_part[i]
                i += 1
            else:
                arr[k] = right_part[j]
                j += 1
            k += 1
        
        while i < len(left_part):
            arr[k] = left_part[i]
            i += 1
            k += 1
        
        while j < len(right_part):
            arr[k] = right_part[j]
            j += 1
            k += 1
    
    def merge_sort_helper(arr, left, right):
        if left < right:
            mid = (left + right) // 2
            merge_sort_helper(arr, left, mid)
            merge_sort_helper(arr, mid + 1, right)
            merge(arr, left, mid, right)
    
    merge_sort_helper(contacts, 0, len(contacts) - 1)
    print("Contacts sorted by name (Merge Sort).")

def bubble_sort():
    """Sort contacts by name using bubble sort. Time Complexity: O(n²)"""
    n = len(contacts)
    for i in range(n):
        for j in range(0, n - i - 1):
            if contacts[j]['name'].lower() > contacts[j + 1]['name'].lower():
                contacts[j], contacts[j + 1] = contacts[j + 1], contacts[j]
    print("Contacts sorted by name (Bubble Sort).")

def selection_sort():
    """Sort contacts by name using selection sort. Time Complexity: O(n²)"""
    n = len(contacts)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if contacts[j]['name'].lower() < contacts[min_idx]['name'].lower():
                min_idx = j
        contacts[i], contacts[min_idx] = contacts[min_idx], contacts[i]
    print("Contacts sorted by name (Selection Sort).")

def load_from_file(filename="PhoneBookDataset.csv"):
    """Load contacts from CSV file. Time Complexity: O(n)"""
    try:
        import csv
        import os
        
        if not os.path.exists(filename):
            print(f"Note: {filename} does not exist yet. Starting with empty phonebook.")
            return False
        
        # Try multiple encodings to handle different file formats
        encodings = ['utf-8', 'windows-1252', 'latin-1', 'cp1252']
        
        for encoding in encodings:
            try:
                with open(filename, 'r', encoding=encoding) as f:
                    reader = csv.DictReader(f)
                    if reader is None or reader.fieldnames is None:
                        print(f"{filename} is empty or invalid.")
                        return False
                    
                    count = 0
                    for row in reader:
                        # Handle both lowercase and capitalized column names
                        name = row.get('name') or row.get('Name')
                        phone = row.get('phone') or row.get('Phone')
                        
                        if name and phone:
                            add_contact(name, phone, silent=True)
                            count += 1
                    
                    if count > 0:
                        print(f"Successfully loaded {count} contact(s) from {filename}\n")
                    return True
            except (UnicodeDecodeError, UnicodeError):
                continue
        
        print(f"Error: Could not read {filename} with any supported encoding.")
        return False
    except PermissionError:
        print(f"Permission denied: Cannot read {filename}. Check file permissions.")
        return False
    except Exception as e:
        print(f"Error loading file: {e}")
        return False

def save_to_file(filename="PhoneBookDataset.csv"):
    """Save contacts to CSV file. Time Complexity: O(n)"""
    try:
        import csv
        import os
        
        # Ensure the directory exists
        directory = os.path.dirname(filename)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'phone'])
            writer.writeheader()
            writer.writerows(contacts)
        
        print(f"Contacts saved successfully to {filename}.")
        return True
    except PermissionError:
        print(f"Permission denied: Cannot write to {filename}. Check file permissions.")
        return False
    except Exception as e:
        print(f"Error saving file: {e}")
        return False

def display_all():
    """Display all contacts. Time Complexity: O(n)"""
    if not contacts:
        print("No contacts in the phonebook.")
        return
    print("\n" + "="*50)
    print("         CONTACTS LIST")
    print("="*50)
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']:<30} | {contact['phone']}")
    print("="*50)
    print(f"Total contacts: {len(contacts)}")
    print("="*50)

def search_by_phone_linear(phone):
    """Linear search for contact by phone. Time Complexity: O(n)"""
    phone = phone.strip()
    for contact in contacts:
        if contact['phone'] == phone:
            return contact
    return None

def display_contact_details(contact):
    """Display detailed information about a contact."""
    if contact:
        print("\n" + "="*50)
        print("         CONTACT DETAILS")
        print("="*50)
        print(f"Name:  {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print("="*50)
    else:
        print("Contact not found.")

def display_statistics():
    """Display phonebook statistics."""
    print("\n" + "="*50)
    print("      PHONEBOOK STATISTICS")
    print("="*50)
    print(f"Total Contacts: {len(contacts)}")
    if contacts:
        names = [c['name'] for c in contacts]
        print(f"First Contact: {names[0]}")
        print(f"Last Contact: {names[-1]}")
        print(f"Sorted: No")
    else:
        print("No contacts in the phonebook.")
    print("="*50)

def compare_search_algorithms():
    """Compare all search algorithms with time complexity analysis."""
    if not contacts:
        print("No contacts to search. Please add contacts first.")
        return
    
    print("\n" + "="*70)
    print("       SEARCH ALGORITHMS COMPARISON")
    print("="*70)
    
    search_term = input("Enter a name to search for: ").strip()
    
    print("\n" + "-"*70)
    print("1. LINEAR SEARCH (by Name)")
    print("-"*70)
    print("   Time Complexity: O(n) - Must check every contact")
    print("   Space Complexity: O(n) - Uses array storage")
    print("   Best Case: O(1) - Found at first position")
    print("   Worst Case: O(n) - Found at last position or not found")
    results = linear_search(search_term)
    print(f"   Result: Found {len(results)} contact(s)")
    if results:
        for r in results:
            print(f"     - {r['name']}: {r['phone']}")
    
    print("\n" + "-"*70)
    print("2. LINEAR SEARCH (by Phone)")
    print("-"*70)
    print("   Time Complexity: O(n) - Must check every contact")
    phone = input("Enter a phone number to search for: ").strip()
    result = search_by_phone_linear(phone)
    print(f"   Result: {'Found' if result else 'Not found'}")
    if result:
        print(f"     - {result['name']}: {result['phone']}")
    
    print("\n" + "-"*70)
    print("3. BINARY SEARCH (by Phone - requires sorted data)")
    print("-"*70)
    print("   Time Complexity: O(log n) - Divide and conquer")
    print("   Space Complexity: O(1) - Only indexes")
    print("   Requires: Data to be sorted")
    print("   Note: Much faster for large datasets")
    result = binary_search(phone)
    print(f"   Result: {'Found' if result else 'Not found'}")
    if result:
        print(f"     - {result['name']}: {result['phone']}")
    
    print("\n" + "-"*70)
    print("4. BINARY SEARCH TREE (by Name)")
    print("-"*70)
    print("   Time Complexity: O(log n) avg, O(n) worst")
    print("   Space Complexity: O(n) - Tree structure")
    print("   Advantage: Hierarchical organization")
    print("   Building tree...")
    bst_root = None
    for contact in contacts:
        bst_root = insert_bst_node(bst_root, contact)
    result = search_bst_node(bst_root, search_term)
    print(f"   Result: {'Found' if result else 'Not found'}")
    if result:
        print(f"     - {result['name']}: {result['phone']}")
    
    print("\n" + "="*70)
    print("SUMMARY:")
    print("  • Use LINEAR SEARCH for unsorted small datasets")
    print("  • Use BINARY SEARCH for sorted large datasets (fastest)")
    print("  • Use BST for dynamic insertion/deletion with quick lookups")
    print("="*70)

def compare_sort_algorithms():
    """Compare all sorting algorithms with time complexity analysis."""
    if not contacts:
        print("No contacts to sort. Please add contacts first.")
        return
    
    import copy
    
    print("\n" + "="*70)
    print("       SORTING ALGORITHMS COMPARISON")
    print("="*70)
    
    print("\n" + "-"*70)
    print("1. BUBBLE SORT")
    print("-"*70)
    print("   Time Complexity: O(n²) always")
    print("   Space Complexity: O(1) - In-place sorting")
    print("   Best Case: O(n) - Already sorted")
    print("   Worst Case: O(n²) - Reverse sorted")
    print("   Method: Compare adjacent elements, swap if needed")
    print("   Status: Simplest but slowest")
    test_contacts = copy.deepcopy(contacts)
    contacts[:] = test_contacts
    bubble_sort()
    display_all()
    
    print("-"*70)
    print("2. SELECTION SORT")
    print("-"*70)
    print("   Time Complexity: O(n²) always")
    print("   Space Complexity: O(1) - In-place sorting")
    print("   Best Case: O(n²) - Finds minimum every time")
    print("   Worst Case: O(n²) - Same as best case")
    print("   Method: Select minimum, place at beginning")
    print("   Status: Predictable performance, equal for best/worst")
    test_contacts = copy.deepcopy(contacts)
    contacts[:] = test_contacts
    selection_sort()
    display_all()
    
    print("-"*70)
    print("3. MERGE SORT")
    print("-"*70)
    print("   Time Complexity: O(n log n) always")
    print("   Space Complexity: O(n) - Extra space needed")
    print("   Best Case: O(n log n) - Divide and conquer")
    print("   Worst Case: O(n log n) - Guaranteed performance")
    print("   Method: Divide into halves, merge sorted halves")
    print("   Status: Great for large datasets, stable sort")
    test_contacts = copy.deepcopy(contacts)
    contacts[:] = test_contacts
    merge_sort()
    display_all()
    
    print("-"*70)
    print("4. QUICK SORT")
    print("-"*70)
    print("   Time Complexity: O(n log n) avg, O(n²) worst")
    print("   Space Complexity: O(log n) - Recursive calls")
    print("   Best Case: O(n log n) - Good pivot selection")
    print("   Worst Case: O(n²) - Bad pivot (rare)")
    print("   Method: Partition by pivot, sort recursively")
    print("   Status: Fastest in practice, most used")
    test_contacts = copy.deepcopy(contacts)
    contacts[:] = test_contacts
    quick_sort()
    display_all()
    
    print("="*70)
    print("COMPARISON SUMMARY:")
    print("-"*70)
    print("Algorithm       | Time (Avg)  | Time (Worst) | Space | Stable")
    print("-"*70)
    print("Bubble Sort     | O(n²)       | O(n²)        | O(1)  | Yes")
    print("Selection Sort  | O(n²)       | O(n²)        | O(1)  | No")
    print("Merge Sort      | O(n log n)  | O(n log n)   | O(n)  | Yes")
    print("Quick Sort      | O(n log n)  | O(n²)        | O(log n) | No")
    print("-"*70)
    print("RECOMMENDATION:")
    print("  • For SMALL arrays: Bubble or Selection (simple)")
    print("  • For LARGE arrays: Merge or Quick (efficient)")
    print("  • For STABILITY: Merge Sort (maintains order)")
    print("  • For PRACTICE: Quick Sort (most interview question)")
    print("="*70)

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("         PHONEBOOK APPLICATION")
    print("="*50)
    print("1.  Add Contact")
    print("2.  Remove Contact")
    print("3.  Edit Contact")
    print("4.  View All Contacts")
    print("5.  Search by Name (Linear Search - O(n))")
    print("6.  Search by Phone - Linear (O(n))")
    print("7.  Search by Phone - Binary (O(log n))")
    print("8.  Sort Contacts")
    print("9.  Search using Binary Search Tree (O(log n))")
    print("10. Display Statistics")
    print("11. Compare ALL Search Algorithms")
    print("12. Compare ALL Sort Algorithms")
    print("13. Save to File")
    print("14. Load from File")
    print("15. Exit")
    print("="*50)

def display_sort_menu():
    """Display the sort options menu."""
    print("\n--- Sort Options ---")
    print("1. Merge Sort (O(n log n))")
    print("2. Quick Sort (O(n log n))")
    print("3. Bubble Sort (O(n²))")
    print("-------------------")

def menu_add_contact():
    """Menu option to add a contact."""
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    add_contact(name, phone)
    input("\nPress Enter to continue...")

def menu_remove_contact():
    """Menu option to remove a contact."""
    display_all()
    name = input("Enter contact name to remove: ").strip()
    remove_contact(name)
    input("\nPress Enter to continue...")

def menu_edit_contact():
    """Menu option to edit a contact."""
    display_all()
    name = input("Enter contact name to edit: ").strip()
    new_phone = input("Enter new phone number: ").strip()
    edit_contact(name, new_phone)
    input("\nPress Enter to continue...")

def menu_linear_search():
    """Menu option for linear search by name."""
    search_term = input("Enter name to search for: ").strip()
    results = linear_search(search_term)
    
    if results:
        print(f"\nFound {len(results)} contact(s):")
        for contact in results:
            print(f"  - {contact['name']}: {contact['phone']}")
    else:
        print(f"No contacts found with '{search_term}'")
    
    input("\nPress Enter to continue...")

def menu_search_phone_linear():
    """Menu option for linear search by phone."""
    phone = input("Enter phone number to search for: ").strip()
    contact = search_by_phone_linear(phone)
    
    if contact:
        display_contact_details(contact)
    else:
        print(f"\nNo contact found with phone '{phone}'")
    
    input("\nPress Enter to continue...")

def menu_binary_search():
    """Menu option for binary search by phone."""
    phone = input("Enter phone number to search for: ").strip()
    contact = binary_search(phone)
    
    if contact:
        display_contact_details(contact)
    else:
        print(f"\nNo contact found with phone '{phone}'")
    
    input("\nPress Enter to continue...")

def menu_bst_search():
    """Menu option to search using Binary Search Tree."""
    if not contacts:
        print("No contacts to search. Please add contacts first.")
        input("\nPress Enter to continue...")
        return
    
    print("Building Binary Search Tree...")
    bst_root = None
    for contact in contacts:
        bst_root = insert_bst_node(bst_root, contact)
    
    name = input("Enter contact name to search using BST: ").strip()
    result = search_bst_node(bst_root, name)
    
    if result:
        print(f"\nFound: {result['name']}: {result['phone']}")
    else:
        print(f"Contact '{name}' not found in BST")
    
    input("\nPress Enter to continue...")

def menu_compare_searches():
    """Menu option to compare all search algorithms."""
    if not contacts:
        print("No contacts to search. Please add contacts first.")
        input("\nPress Enter to continue...")
        return
    
    compare_search_algorithms()
    input("\nPress Enter to continue...")

def menu_compare_sorts():
    """Menu option to compare all sort algorithms."""
    if not contacts:
        print("No contacts to sort. Please add contacts first.")
        input("\nPress Enter to continue...")
        return
    
    compare_sort_algorithms()
    input("\nPress Enter to continue...")

def menu_sort():
    """Menu option to sort contacts."""
    if not contacts:
        print("No contacts to sort. Please add contacts first.")
        input("\nPress Enter to continue...")
        return
    
    while True:
        display_sort_menu()
        choice = input("Select sort algorithm: ").strip()
        
        if choice == '1':
            merge_sort()
            print("Contacts sorted successfully!")
            display_all()
            break
        elif choice == '2':
            quick_sort()
            print("Contacts sorted successfully!")
            display_all()
            break
        elif choice == '3':
            bubble_sort()
            print("Contacts sorted successfully!")
            display_all()
            break
        else:
            print("Invalid choice. Please try again.")
    
    input("\nPress Enter to continue...")

def run_application():
    """Run the phonebook application."""
    print("\n" + "="*50)
    print("*** Welcome to Phonebook Application ***")
    print("="*50)
    print("Loading data from file...")
    load_from_file("PhoneBookDataset.csv")
    
    while True:
        display_menu()
        choice = input("Select an option (1-15): ").strip()
        
        if choice == '1':
            menu_add_contact()
        elif choice == '2':
            menu_remove_contact()
        elif choice == '3':
            menu_edit_contact()
        elif choice == '4':
            display_all()
            input("\nPress Enter to continue...")
        elif choice == '5':
            menu_linear_search()
        elif choice == '6':
            menu_search_phone_linear()
        elif choice == '7':
            menu_binary_search()
        elif choice == '8':
            menu_sort()
        elif choice == '9':
            menu_bst_search()
        elif choice == '10':
            display_statistics()
            input("\nPress Enter to continue...")
        elif choice == '11':
            menu_compare_searches()
        elif choice == '12':
            menu_compare_sorts()
        elif choice == '13':
            save_to_file("PhoneBookDataset.csv")
            input("\nPress Enter to continue...")
        elif choice == '14':
            contacts.clear()
            load_from_file("PhoneBookDataset.csv")
            input("\nPress Enter to continue...")
        elif choice == '15':
            print("\n" + "="*50)
            print("Saving contacts before exit...")
            save_to_file("PhoneBookDataset.csv")
            print("Thank you for using Phonebook Application!")
            print("="*50)
            break
        else:
            print("Invalid choice. Please select a valid option (1-15).")
            input("\nPress Enter to continue...")

# Main entry point
if __name__ == "__main__":
    run_application()
