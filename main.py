# main.py
# Compare hash table performance with different 
# number of items
from hash_table import HashTable
from random import randint
from time import perf_counter_ns

def draw_hash_table_performance_charts(get_times, table_sizes):
    import matplotlib.pyplot as plt
    
    # Convert nanoseconds to microseconds for better readability
    get_times_us = [time / 1000 for time in get_times]
    
    plt.figure(figsize=(10, 6))
    plt.plot(table_sizes, get_times_us, marker='o', label='Hash Table Get', linewidth=2, markersize=6)
    plt.title("Hash Table Retrieval Performance")
    plt.xlabel("Number of Items in Hash Table")
    plt.ylabel("Average Retrieval Time (microseconds)")
    plt.ylim(bottom=0)  # Start y-axis at 0
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()


def experiment_hash_table(num_items, num_trials, num_lookups):
    """
    Test hash table performance with a given number of items.
    
    Args:
        num_items: Number of items to insert into the hash table
        num_trials: Number of trials to run for averaging
        num_lookups: Number of lookup operations per trial
    
    Returns:
        Average time per lookup operation in nanoseconds
    """
    total_time = 0
    
    for trial in range(num_trials):
        # Create hash table and populate it
        ht = HashTable()
        keys = []
        
        # Insert items with random keys and values
        for i in range(num_items):
            key = randint(1, num_items * 2)  # Some overlap possible
            value = f"value_{key}"
            ht.insert(key, value)
            keys.append(key)
        
        # Add some extra keys that might not be in the table (for misses)
        test_keys = keys[:num_lookups//2] + [randint(num_items * 2 + 1, num_items * 3) for _ in range(num_lookups//2)]
        
        # Time the lookup operations
        start_time = perf_counter_ns()
        for key in test_keys:
            ht.get(key)  # This might be a hit or miss
        end_time = perf_counter_ns()
        
        total_time += (end_time - start_time)
    
    # Return average time per lookup operation
    return total_time / (num_trials * num_lookups)

def main():
    print("Running hash table performance trials...")
    
    # Test with different numbers of items in the hash table
    table_sizes = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000, 12000, 13000, 14000, 15000]
    get_times = []
    num_trials = 10
    num_lookups = 1000  # Number of lookup operations to test per trial
    
    for size in table_sizes:
        print(f"Testing hash table with {size} items...")
        avg_time = experiment_hash_table(size, num_trials, num_lookups)
        get_times.append(avg_time)
    
    print("\nHash Table Performance Results:")
    print("Items\tAvg Retrieval Time (ns)")
    print("-" * 35)
    for i in range(len(table_sizes)):
        print(f"{table_sizes[i]}\t{get_times[i]:.2f}")
    
    # Draw the performance chart
    draw_hash_table_performance_charts(get_times, table_sizes)

if __name__ == '__main__':
    main()