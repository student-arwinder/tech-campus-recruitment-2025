## Discussion.md

### Approaches Considered

1. **Reading the File Line by Line**
   - This method reads the log file sequentially, checking each line for the required date.
   - **Pros:** Simple and memory efficient.
   - **Cons:** Extremely slow for a 1TB file.

2. **Dividing the File into Chunks with Multiprocessing** *(Final Choice)*
   - The file is processed in **1MB chunks** using multiple CPU cores.
   - Each chunk is processed independently to filter out relevant log entries.
   - **Pros:** Efficient use of CPU, avoids loading the entire file into memory, scalable.
   - **Cons:** Requires careful chunking to avoid splitting log entries across chunks.

3. **Using Memory-Mapped Files (`mmap`) with Parallel Processing**
   - Treating the file as a memory object, ensuring efficient access.
   - Aligning chunks with newline characters to maintain complete log entries.
   - **Pros:** Fast, efficient in memory usage, and scalable.
   - **Cons:** Slightly complex implementation, can be inefficient for very large files.

### Why We Chose This Approach

We selected **chunk-based processing with multiprocessing** because it provides a balance between **speed, memory efficiency, and simplicity**:
- Reads the file in **small 1MB chunks**, reducing memory usage.
- Uses **multiple CPU cores** to process chunks in parallel.
- Ensures **only relevant log entries** are written to the output file.

This approach avoids the complexity of memory-mapping while being **fast, scalable, and efficient** for a **1TB file**.

### How to Use the Script

1. **Check if Python is Installed:**
   ```sh
   python --version
   ```
   If not installed, download it from [python.org](https://www.python.org/).

2. **Run the Script:**
   ```sh
   python extract_logs.py <log_file_path> YYYY-MM-DD
   ```
   Example:
   ```sh
   python extract_logs.py /path/to/logfile.log 2024-12-01
   ```

3. **Find the Output:**
   - The extracted logs will be saved in the `output/` folder:
     ```sh
     output/output_2024-12-01.txt
     ```
