import subprocess

def run_pinpoint_for_python():
    command = [
        "./pinpoint/build/pinpoint", "--", "python3",
        "code/merge_sort.py",
        "-data", "data/data_test_50k.txt",
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
        "data/data_test_50k.txt",
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
        "data/data_test_50k.txt",
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
        "data/data_test_50k.txt",
        "merge_sort_java.txt"
    ]
    
    # Output file for pinpoint results
    output_file = "pinpoint_output_java.txt"
    
    with open(output_file, "w") as f:
        process = subprocess.run(command, stdout=f, stderr=f, text=True)
    
    print(f"Output saved to {output_file}")


def run_pinpoint_for_javascript():
    # Execute the compiled program
    command = [
        "./pinpoint/build/pinpoint", "--", "node",
        "code/merge_sort_js.js",
        "data/data_test_50k.txt",
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
                    if "J rapl:psys" in line:
                        energy_usage[lang] = float(line.split()[0])
        except FileNotFoundError:
            print(f"Warning: {file} not found. Skipping {lang}.")

    print("\nEnergy Usage Comparison:")
    for lang, energy in energy_usage.items():
        print(f"{lang}: {energy} J")

    min_energy = min(energy_usage, key=energy_usage.get)
    print(f"{min_energy} is the most energy-efficient.")

if __name__ == "__main__":
    # Compile the Haskell program
    compile_command = [
        "ghc", "-o", "merge_sort_haskell", "code/merge_sort_haskell.hs"
    ]
    subprocess.run(compile_command, check=True)

    # Compile the C program
    compile_command = [
        "gcc", "code/merge_sort.c", "-o", "merge_sort"
    ]
    
    subprocess.run(compile_command, check=True)
    
    run_pinpoint_for_python()
    run_pinpoint_for_c()
    run_pinpoint_for_haskell()


    # Compile the Java program
    compile_command = ["javac", "code/MergeSort.java"]
    compile_process = subprocess.run(compile_command, capture_output=True, text=True)

    if compile_process.returncode != 0:
        print("Java compilation failed:")
        print(compile_process.stderr)
    
    run_pinpoint_for_java()
    run_pinpoint_for_javascript()
    compare_energy_usage()
