import subprocess
import time
from data_generator import generate_data

def run_pinpoint_for_python():
    command = [
        "./pinpoint/build/pinpoint", "--", "python3",
        "code/merge_sort.py",
        "-data", "data/data_test_1mil.txt",
        "-output", "merge_sort_python.txt"
    ]
    
    output_file = "pinpoint_output_python.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
        
    print(f"Output saved to {output_file}")

def run_pinpoint_for_c():
    # Execute the compiled program
    command = [
        "./pinpoint/build/pinpoint", "--", "./merge_sort",
        "data/data_test_1mil.txt",
        "merge_sort_c.txt"
    ]
    
    output_file = "pinpoint_output_c.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
        
    print(f"Output saved to {output_file}")

def run_pinpoint_for_haskell():
    # Execute the compiled program
    command = [
        "./pinpoint/build/pinpoint", "--", "./merge_sort_haskell",
        "data/data_test_1mil.txt",
        "merge_sort_haskell.txt"
    ]
    
    # Output file for pinpoint results
    output_file = "pinpoint_output_haskell.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
    
    print(f"Output saved to {output_file}")


def run_pinpoint_for_java():
    # Execute the compiled program
    command = [
        "./pinpoint/build/pinpoint", "--","java", "-cp", "code", "MergeSort",
        "data/data_test_1mil.txt",
        "merge_sort_java.txt"
    ]
    
    # Output file for pinpoint results
    output_file = "pinpoint_output_java.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
    
    print(f"Output saved to {output_file}")


def run_pinpoint_for_javascript():
    command = [
        "./pinpoint/build/pinpoint", "--", "node",
        "code/merge_sort_js.js",
        "data/data_test_1mil.txt",
        "merge_sort_javascript.txt"
    ]
    
    # Output file for pinpoint results
    output_file = "pinpoint_output_javascript.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
    
    print(f"Output saved to {output_file}")


def compare_energy_usage():
    energy_usage = {"Python": 0, "C": 0, "Haskell": 0, "Java": 0, "JavaScript": 0}
    
    for lang, file in [("Python", "pinpoint_output_python.txt"), 
                       ("C", "pinpoint_output_c.txt"),
                       ("Haskell", "pinpoint_output_haskell.txt"),
                       ("Java", "pinpoint_output_java.txt"),                   
                       ("JavaScript", "pinpoint_output_javascript.txt")]:
        try:
            with open(file, "r") as f:
                for line in f:
                    # Comparing the energy consumption of the whole package
                    if "J rapl:pkg" in line:
                        energy_usage[lang] = float(line.split()[0])
        except FileNotFoundError:
            print(f"Warning: {file} not found. Skipping {lang}.")

    print("\nEnergy Usage Comparison:")
    langs = []
    for lang, energy in energy_usage.items():
        langs.append((lang, energy))
    sorted_langs = sorted(langs, key=lambda x: x[1])
    for lang in sorted_langs:
        print(f"{lang[0]}: {lang[1]}")

def write_data_to_file(file_path, arr):
    with open(file_path, 'w') as file:
        for item in arr:
            file.write(f"{item}\n")

if __name__ == "__main__":
    # Compile the Haskell program
    compile_command = [
        "ghc", "-o", "merge_sort_haskell", "code/merge_sort_haskell.hs"
    ]
    compile_process = subprocess.run(compile_command, check=True)
    if compile_process.returncode != 0:
        print("Haskell compilation failed:")
        print(compile_process.stderr)

    # Compile the C program
    compile_command = [
        "gcc", "code/merge_sort.c", "-o", "merge_sort"
    ]
    
    compile_process = subprocess.run(compile_command, check=True)
    if compile_process.returncode != 0:
        print("C compilation failed:")
        print(compile_process.stderr)

    # Compile the Java program
    compile_command = ["javac", "code/MergeSort.java"]
    compile_process = subprocess.run(compile_command, capture_output=True, text=True)

    if compile_process.returncode != 0:
        print("Java compilation failed:")
        print(compile_process.stderr)
    
    langs = [run_pinpoint_for_python, run_pinpoint_for_c,
             run_pinpoint_for_haskell, run_pinpoint_for_java,
             run_pinpoint_for_javascript]
    num_values = 1000000
    output_file = "data/data_test_1mil.txt"
    value_range = (1, 10000000)
    for lang in langs:
        # generate new data for each execution
        generate_data(output_file, num_values=num_values, value_range=value_range)
        # allocate some time for the machine to rest
        time.sleep(100)
        lang()

    compare_energy_usage()
